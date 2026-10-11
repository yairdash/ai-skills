#!/usr/bin/env python3
"""Offline linting and validation for the H3 parody-short workflow.

This module intentionally has no network or submission operation.
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


ENDPOINTS = {
    "minimax/h3/text-to-video",
    "minimax/h3/image-to-video",
    "minimax/h3/reference-to-video",
}
RESOLUTIONS = {"768P", "2K", "4K"}
T2V_RATIOS = {"21:9", "16:9", "4:3", "1:1", "3:4", "9:16"}
REF_RATIOS = T2V_RATIOS | {"adaptive"}
BASE_FIELDS = ["integrated_multimodal_description", "overall_soundscape", "non_diegetic_music"]
REF_FIELDS = ["subject_definitions", "summary", "retention_analysis", "detailed_description", "overall_soundscape", "non_diegetic_music"]
REQUIRED_CASE_FIELDS = {
    "id", "character", "canonical_show_or_film", "expected_visual_traits",
    "behavioral_traits", "voice_traits", "set_anchors", "prompt_variant",
    "endpoint", "expansion_setting", "duration", "aspect_ratio", "hypothesis", "prompt",
}
MAX_SCHEMA_AGE = dt.timedelta(hours=24)
LORA_COMPATIBILITY = {
    "h3-direct",
    "h3-local-only",
    "peer-transfer-hypothesis",
    "image-only-reference",
}
REQUIRED_LORA_FIELDS = {
    "id", "property_or_character", "source_model", "adapter_type", "compatibility",
    "source_url", "source_kind", "source_date", "creator_claim", "short_terms",
    "visual_anchors", "set_anchors", "costume_or_era", "motion_performance_cues",
    "negative_or_failure_notes", "license_or_restriction_note", "evidence_quality",
    "confidence", "verification_status",
}


def load_data(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    if path.suffix.lower() in {".yaml", ".yml"}:
        return yaml.safe_load(text) if yaml is not None else _simple_yaml_load(text)
    raise ValueError(f"Unsupported data file: {path}")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at line {line_number}: {exc.msg}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"JSONL line {line_number} must be an object")
        records.append(value)
    return records


def _yaml_scalar(raw: str) -> Any:
    value = raw.strip()
    if value in {"true", "false"}:
        return value == "true"
    if value in {"null", "~"}:
        return None
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        return [] if not body else [_yaml_scalar(part.strip()) for part in body.split(",")]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def _simple_yaml_load(text: str) -> Any:
    """Parse the controlled YAML subset used by this skill, without dependencies."""
    lines = text.splitlines()

    def indent_of(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def next_content(index: int) -> int:
        while index < len(lines) and not lines[index].strip():
            index += 1
        return index

    def parse_mapping(index: int, indent: int, initial: tuple[str, Any] | None = None):
        result: dict[str, Any] = {}
        if initial:
            result[initial[0]] = initial[1]
        while index < len(lines):
            if not lines[index].strip():
                index += 1
                continue
            current_indent = indent_of(lines[index])
            if current_indent < indent or current_indent != indent or lines[index].lstrip().startswith("- "):
                break
            content = lines[index].strip()
            if ":" not in content:
                raise ValueError(f"Invalid YAML mapping line {index + 1}")
            key, raw = content.split(":", 1)
            raw = raw.strip()
            if raw in {"|", "|-"}:
                index += 1
                block: list[str] = []
                block_indent = indent + 2
                while index < len(lines):
                    line = lines[index]
                    if line.strip() and indent_of(line) <= indent:
                        break
                    block.append(line[block_indent:] if len(line) >= block_indent else "")
                    index += 1
                result[key] = "\n".join(block).rstrip("\n")
                continue
            if raw:
                result[key] = _yaml_scalar(raw)
                index += 1
                continue
            child_index = next_content(index + 1)
            if child_index >= len(lines) or indent_of(lines[child_index]) <= indent:
                result[key] = None
                index += 1
                continue
            result[key], index = parse_block(child_index, indent_of(lines[child_index]))
        return result, index

    def parse_list(index: int, indent: int):
        result = []
        while index < len(lines):
            index = next_content(index)
            if index >= len(lines) or indent_of(lines[index]) != indent or not lines[index].lstrip().startswith("- "):
                break
            item = lines[index].strip()[2:].strip()
            if ":" in item:
                key, raw = item.split(":", 1)
                index += 1
                mapping, index = parse_mapping(index, indent + 2, (key, _yaml_scalar(raw.strip())))
                result.append(mapping)
            else:
                result.append(_yaml_scalar(item))
                index += 1
        return result, index

    def parse_block(index: int, indent: int):
        if lines[index].lstrip().startswith("- "):
            return parse_list(index, indent)
        return parse_mapping(index, indent)

    start = next_content(0)
    if start >= len(lines):
        return None
    value, _ = parse_block(start, indent_of(lines[start]))
    return value


def calculate_cost(duration: int, runs: int, price: Decimal) -> Decimal:
    return (Decimal(duration) * Decimal(runs) * price).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _field_order_errors(prompt: str, fields: list[str]) -> list[str]:
    positions = [prompt.find(f"{name}:") for name in fields]
    missing = [fields[i] for i, pos in enumerate(positions) if pos < 0]
    errors = [f"missing required field: {name}" for name in missing]
    present_positions = [p for p in positions if p >= 0]
    if present_positions != sorted(present_positions):
        errors.append("required fields are in the wrong order")
    return errors


def lint_prompt(prompt: str, mode: str, duration: int, forbidden_phrases: list[str] | None = None) -> list[str]:
    errors = _field_order_errors(prompt, BASE_FIELDS if mode == "base" else REF_FIELDS)
    if re.search(r"<#\s*\d+(?:\.\d+)?\s*#>", prompt):
        errors.append("unsupported TTS-only pause syntax")

    blocks = list(re.finditer(r"<d>\[([^\]]+)\](.*?)</d>", prompt, flags=re.DOTALL))
    if "<d>" in prompt and not blocks:
        errors.append("malformed <d>[Language]…</d> dialogue wrapper")
    for block in blocks:
        prefix = prompt[max(0, block.start() - 240):block.start()]
        if not re.search(r"\(S\d+(?:,S\d+)*\)", prefix):
            errors.append("dialogue block lacks a nearby stable speaker ID")
        if not block.group(2).strip():
            errors.append("empty dialogue block")

    outside = re.sub(r"<d>.*?</d>", "", prompt, flags=re.DOTALL)
    if re.search(r"\b(?:says?|asks?|replies?|shouts?|whispers?|exclaims?)\b[^\n]{0,80}[\"“][^\"”]+[\"”]", outside, flags=re.IGNORECASE):
        errors.append("spoken dialogue appears outside a <d> wrapper")

    speaker_ids = re.findall(r"\(S(\d+)\)", prompt)
    if speaker_ids:
        unique = sorted({int(x) for x in speaker_ids})
        if unique != list(range(1, max(unique) + 1)):
            errors.append("speaker IDs are not contiguous from S1")

    times = []
    for minute, second, millis in re.findall(r"At\s+(\d{2}):(\d{2})\.(\d{3})", prompt):
        value = int(minute) * 60 + int(second) + int(millis) / 1000
        times.append(value)
        if value >= duration:
            errors.append(f"shot timestamp {value:.3f}s is outside {duration}s duration")
    if times != sorted(times) or len(times) != len(set(times)):
        errors.append("shot timestamps are not strictly increasing")

    if mode == "reference":
        labels = re.findall(r"<([A-Za-z]+)\s+(\d+)>", prompt)
        allowed = {"Subject", "Picture", "Video", "Audio"}
        invalid = sorted({kind for kind, _ in labels if kind not in allowed})
        if invalid:
            errors.append(f"invalid reference label types: {', '.join(invalid)}")
    normalized = prompt.casefold()
    leaked = [phrase for phrase in (forbidden_phrases or []) if phrase.strip() and phrase.casefold() in normalized]
    if leaked:
        errors.append("copied-dialogue leakage: " + ", ".join(sorted(leaked)))
    return sorted(set(errors))


def validate_payload(endpoint: str, payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if endpoint not in ENDPOINTS:
        return [f"unsupported endpoint: {endpoint}"]
    if not isinstance(payload.get("prompt"), str) or not payload["prompt"].strip():
        errors.append("payload.prompt must be a non-empty string")
    duration = payload.get("duration", 5)
    if not isinstance(duration, int) or isinstance(duration, bool) or not 5 <= duration <= 15:
        errors.append("duration must be an integer from 5 through 15")
    if payload.get("resolution", "2K") not in RESOLUTIONS:
        errors.append("resolution must be 768P, 2K, or 4K")
    for flag in ("enable_prompt_expansion", "enable_safety_checker"):
        if flag in payload and not isinstance(payload[flag], bool):
            errors.append(f"{flag} must be boolean")

    common = {"prompt", "resolution", "duration", "enable_prompt_expansion", "enable_safety_checker"}
    if endpoint.endswith("text-to-video"):
        allowed = common | {"aspect_ratio"}
        if payload.get("aspect_ratio", "16:9") not in T2V_RATIOS:
            errors.append("invalid text-to-video aspect_ratio")
    elif endpoint.endswith("image-to-video"):
        allowed = common | {"image_url", "end_image_url"}
        if payload.get("end_image_url") and not payload.get("image_url"):
            errors.append("end_image_url requires image_url")
        if "aspect_ratio" in payload:
            errors.append("image-to-video follows the image ratio and does not accept aspect_ratio")
    else:
        allowed = common | {"aspect_ratio", "reference_image_urls", "reference_video_urls", "reference_audio_urls"}
        if payload.get("aspect_ratio", "adaptive") not in REF_RATIOS:
            errors.append("invalid reference-to-video aspect_ratio")
        images = payload.get("reference_image_urls", [])
        videos = payload.get("reference_video_urls", [])
        audios = payload.get("reference_audio_urls", [])
        if not all(isinstance(x, list) for x in (images, videos, audios)):
            errors.append("reference URL fields must be arrays")
        else:
            if len(images) > 9 or len(videos) > 3 or len(audios) > 3:
                errors.append("reference modality limit exceeded")
            if len(images) + len(videos) + len(audios) > 12:
                errors.append("total reference limit of 12 exceeded")
            if audios and not (images or videos):
                errors.append("audio cannot be the only reference input")
            prompt = str(payload.get("prompt", ""))
            for label, count in (("Image", len(images)), ("Video", len(videos)), ("Audio", len(audios))):
                for idx in map(int, re.findall(rf"\b{label}\s+(\d+)\b", prompt)):
                    if idx < 1 or idx > count:
                        errors.append(f"{label} {idx} has no matching payload reference")

    unknown = sorted(set(payload) - allowed)
    if unknown:
        errors.append(f"unsupported payload fields for endpoint: {', '.join(unknown)}")
    return sorted(set(errors))


def validate_case(data: dict[str, Any]) -> list[str]:
    errors = [f"missing benchmark field: {x}" for x in sorted(REQUIRED_CASE_FIELDS - set(data))]
    endpoint = data.get("endpoint")
    payload = {
        "prompt": data.get("prompt"), "duration": data.get("duration"),
        "resolution": data.get("resolution", "2K"),
        "enable_prompt_expansion": data.get("expansion_setting"),
    }
    if endpoint == "minimax/h3/text-to-video":
        payload["aspect_ratio"] = data.get("aspect_ratio")
    errors.extend(validate_payload(endpoint, payload))
    if isinstance(data.get("prompt"), str) and isinstance(data.get("duration"), int):
        errors.extend(lint_prompt(data["prompt"], "base", data["duration"], data.get("forbidden_dialogue", [])))
    return sorted(set(errors))


def validate_lora_observation(data: dict[str, Any]) -> list[str]:
    errors = [f"missing LoRA observation field: {x}" for x in sorted(REQUIRED_LORA_FIELDS - set(data))]
    if data.get("compatibility") not in LORA_COMPATIBILITY:
        errors.append("compatibility must be h3-direct, h3-local-only, peer-transfer-hypothesis, or image-only-reference")
    if not isinstance(data.get("source_url"), str) or not re.match(r"https://", data.get("source_url", "")):
        errors.append("source_url must be an https URL")
    try:
        dt.date.fromisoformat(str(data.get("source_date")))
    except ValueError:
        errors.append("source_date must be YYYY-MM-DD")
    for field in ("short_terms", "visual_anchors", "set_anchors", "costume_or_era", "motion_performance_cues", "negative_or_failure_notes"):
        value = data.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{field} must be an array of non-empty strings")
    terms = data.get("short_terms")
    if isinstance(terms, list):
        if len(terms) > 12:
            errors.append("short_terms may contain at most 12 retained terms")
        if any(len(term) > 120 for term in terms if isinstance(term, str)):
            errors.append("short_terms entries must be 120 characters or fewer")
    if data.get("evidence_quality") not in {"low", "medium", "high"}:
        errors.append("evidence_quality must be low, medium, or high")
    if data.get("confidence") not in {"low", "medium", "high"}:
        errors.append("confidence must be low, medium, or high")
    return sorted(set(errors))


def validate_lora_observations(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, record in enumerate(records, start=1):
        record_id = record.get("id", f"line-{index}")
        if record_id in seen:
            errors.append(f"duplicate LoRA observation id: {record_id}")
        seen.add(record_id)
        errors.extend(f"{record_id}: {error}" for error in validate_lora_observation(record))
    return errors


def _parse_timestamp(value: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=dt.timezone.utc)


def validate_manifest(data: dict[str, Any], now: dt.datetime | None = None) -> list[str]:
    required = {"endpoint", "payload", "schema_timestamp", "pricing_timestamp", "price_per_second_usd", "cost_estimate_usd", "approval_status", "reference_provenance", "request_id", "output_url_or_path", "disclosure_status"}
    errors = [f"missing manifest field: {x}" for x in sorted(required - set(data))]
    if errors:
        return errors
    errors.extend(validate_payload(data["endpoint"], data["payload"]))
    current = now or dt.datetime.now(dt.timezone.utc)
    for field in ("schema_timestamp", "pricing_timestamp"):
        try:
            age = current - _parse_timestamp(data[field]).astimezone(dt.timezone.utc)
            if age < dt.timedelta(0) or age > MAX_SCHEMA_AGE:
                errors.append(f"{field} must be refreshed within 24 hours")
        except (TypeError, ValueError):
            errors.append(f"{field} must be an ISO-8601 timestamp")
    try:
        expected = calculate_cost(int(data["payload"].get("duration", 5)), 1, Decimal(str(data["price_per_second_usd"])))
        actual = Decimal(str(data["cost_estimate_usd"])).quantize(Decimal("0.01"))
        if expected != actual:
            errors.append(f"cost_estimate_usd must equal {expected}")
    except Exception:
        errors.append("invalid price or cost value")
    if data["approval_status"] not in {"pending", "approved", "rejected"}:
        errors.append("approval_status must be pending, approved, or rejected")
    if data["approval_status"] == "approved" and not data.get("approval_evidence"):
        errors.append("approved manifest requires approval_evidence")
    if data.get("request_id") and data["approval_status"] != "approved":
        errors.append("request_id cannot exist without approval")
    return sorted(set(errors))


def load_manifest_for_validation(path: Path) -> dict[str, Any]:
    """Load a manifest and materialize a local prompt_file for offline validation."""
    data = load_data(path)
    if not isinstance(data, dict):
        raise ValueError("manifest must be a JSON object")
    payload = data.get("payload")
    if isinstance(payload, dict) and "prompt_file" in payload:
        prompt_path = path.parent / str(payload["prompt_file"])
        materialized = dict(payload)
        materialized["prompt"] = prompt_path.read_text(encoding="utf-8")
        materialized.pop("prompt_file", None)
        data = dict(data)
        data["payload"] = materialized
    return data


def _print_result(errors: list[str]) -> int:
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 1 if errors else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    lint = sub.add_parser("lint-prompt")
    lint.add_argument("--mode", choices=("base", "reference"), required=True)
    lint.add_argument("--duration", type=int, required=True)
    lint.add_argument("--prompt-file", type=Path, required=True)
    lint.add_argument("--forbidden-dialogue-file", type=Path)
    case = sub.add_parser("validate-case")
    case.add_argument("--file", type=Path, required=True)
    suite = sub.add_parser("validate-suite")
    suite.add_argument("--file", type=Path, required=True)
    manifest = sub.add_parser("validate-manifest")
    manifest.add_argument("--file", type=Path, required=True)
    lora = sub.add_parser("validate-lora-observations")
    lora.add_argument("--file", type=Path, required=True)
    cost = sub.add_parser("estimate-cost")
    cost.add_argument("--duration", type=int, required=True)
    cost.add_argument("--runs", type=int, default=1)
    cost.add_argument("--price-per-second", type=Decimal, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "lint-prompt":
        forbidden = []
        if args.forbidden_dialogue_file:
            forbidden = [line.strip() for line in args.forbidden_dialogue_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        return _print_result(lint_prompt(args.prompt_file.read_text(encoding="utf-8"), args.mode, args.duration, forbidden))
    if args.command == "validate-case":
        return _print_result(validate_case(load_data(args.file)))
    if args.command == "validate-suite":
        data = load_data(args.file)
        if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
            return _print_result(["suite must contain a cases array"])
        errors = []
        seen = set()
        for index, case_data in enumerate(data["cases"]):
            case_id = case_data.get("id", f"index-{index}") if isinstance(case_data, dict) else f"index-{index}"
            if case_id in seen:
                errors.append(f"duplicate case id: {case_id}")
            seen.add(case_id)
            if not isinstance(case_data, dict):
                errors.append(f"{case_id}: case must be an object")
                continue
            errors.extend(f"{case_id}: {error}" for error in validate_case(case_data))
        return _print_result(errors)
    if args.command == "validate-manifest":
        return _print_result(validate_manifest(load_manifest_for_validation(args.file)))
    if args.command == "validate-lora-observations":
        return _print_result(validate_lora_observations(load_jsonl(args.file)))
    cost = calculate_cost(args.duration, args.runs, args.price_per_second)
    print(json.dumps({"duration": args.duration, "runs": args.runs, "price_per_second_usd": str(args.price_per_second), "estimated_cost_usd": str(cost)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
