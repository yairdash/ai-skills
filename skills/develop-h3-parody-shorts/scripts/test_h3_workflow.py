import datetime as dt
import json
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

import h3_workflow as h3


BASE_PROMPT = """integrated_multimodal_description: [Shot 1] Live-action. A tense man (S1) says: <d>[English] This queue has rules.</d>

overall_soundscape: Quiet room tone.

non_diegetic_music: N/A"""


class WorkflowTests(unittest.TestCase):
    def test_exact_cost(self):
        self.assertEqual(h3.calculate_cost(5, 6, Decimal("0.26")), Decimal("7.80"))

    def test_prompt_order_and_dialogue(self):
        self.assertEqual(h3.lint_prompt(BASE_PROMPT, "base", 5), [])
        bad = BASE_PROMPT.replace("<d>[English] This queue has rules.</d>", '"This queue has rules."')
        self.assertIn("spoken dialogue appears outside a <d> wrapper", h3.lint_prompt(bad, "base", 5))

    def test_timing_and_pause_lint(self):
        bad = BASE_PROMPT.replace("Quiet room tone.", "At 00:05.000, cut. <#1#>")
        errors = h3.lint_prompt(bad, "base", 5)
        self.assertTrue(any("outside" in e for e in errors))
        self.assertIn("unsupported TTS-only pause syntax", errors)

    def test_forbidden_dialogue_leakage(self):
        errors = h3.lint_prompt(BASE_PROMPT, "base", 5, ["This queue has rules."])
        self.assertTrue(any("copied-dialogue leakage" in error for error in errors))

    def test_all_endpoint_payloads_and_frames(self):
        common = {"prompt": BASE_PROMPT, "duration": 5, "resolution": "2K", "enable_prompt_expansion": False}
        self.assertEqual(h3.validate_payload("minimax/h3/text-to-video", common | {"aspect_ratio": "16:9"}), [])
        self.assertEqual(h3.validate_payload("minimax/h3/image-to-video", common | {"image_url": "https://x/a.png", "end_image_url": "https://x/b.png"}), [])
        ref = common | {"aspect_ratio": "adaptive", "prompt": "Image 1 and Video 1", "reference_image_urls": ["https://x/a.png"], "reference_video_urls": ["https://x/a.mp4"], "reference_audio_urls": []}
        self.assertEqual(h3.validate_payload("minimax/h3/reference-to-video", ref), [])

    def test_reference_limits_and_audio_only(self):
        payload = {"prompt": "Audio 1", "duration": 5, "reference_audio_urls": ["https://x/a.wav"]}
        self.assertIn("audio cannot be the only reference input", h3.validate_payload("minimax/h3/reference-to-video", payload))
        payload["reference_image_urls"] = [f"https://x/{i}.png" for i in range(10)]
        self.assertIn("reference modality limit exceeded", h3.validate_payload("minimax/h3/reference-to-video", payload))

    def test_duration_aspect_and_endpoint_fields(self):
        payload = {"prompt": BASE_PROMPT, "duration": 4, "aspect_ratio": "adaptive"}
        errors = h3.validate_payload("minimax/h3/text-to-video", payload)
        self.assertTrue(any("duration" in e for e in errors))
        self.assertIn("invalid text-to-video aspect_ratio", errors)
        image_errors = h3.validate_payload("minimax/h3/image-to-video", {"prompt": BASE_PROMPT, "duration": 5, "end_image_url": "https://x/end.png"})
        self.assertIn("end_image_url requires image_url", image_errors)

    def test_schema_refresh_and_approval(self):
        now = dt.datetime(2026, 8, 12, 12, tzinfo=dt.timezone.utc)
        manifest = {
            "endpoint": "minimax/h3/text-to-video",
            "payload": {"prompt": BASE_PROMPT, "duration": 5, "aspect_ratio": "16:9"},
            "schema_timestamp": "2026-08-10T00:00:00Z",
            "pricing_timestamp": "2026-08-12T11:00:00Z",
            "price_per_second_usd": 0.26,
            "cost_estimate_usd": 1.30,
            "approval_status": "pending",
            "reference_provenance": [], "request_id": None,
            "output_url_or_path": None, "disclosure_status": "not-applicable-benchmark",
        }
        self.assertIn("schema_timestamp must be refreshed within 24 hours", h3.validate_manifest(manifest, now))
        manifest["schema_timestamp"] = "2026-08-12T11:00:00Z"
        manifest["approval_status"] = "approved"
        self.assertIn("approved manifest requires approval_evidence", h3.validate_manifest(manifest, now))

    def test_no_submission_command_exists(self):
        parser = h3.build_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["submit"])

    def test_manifest_prompt_file_is_materialized(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "h3-prompt.txt").write_text(BASE_PROMPT, encoding="utf-8")
            manifest = {
                "endpoint": "minimax/h3/text-to-video",
                "payload": {"prompt_file": "h3-prompt.txt", "duration": 5, "aspect_ratio": "16:9"},
            }
            path = root / "generation-manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            loaded = h3.load_manifest_for_validation(path)
            self.assertEqual(loaded["payload"]["prompt"], BASE_PROMPT)
            self.assertNotIn("prompt_file", loaded["payload"])

    def test_benchmark_case_contract(self):
        case = {
            "id": "probe", "character": "George Costanza", "canonical_show_or_film": "Seinfeld",
            "expected_visual_traits": ["balding", "glasses"], "behavioral_traits": ["status anxiety"],
            "voice_traits": ["agitated cadence"], "set_anchors": ["diner booth"],
            "prompt_variant": "minimal-anchor", "endpoint": "minimax/h3/text-to-video",
            "expansion_setting": False, "duration": 5, "aspect_ratio": "16:9",
            "hypothesis": "Native recall is recognizable.", "prompt": BASE_PROMPT,
        }
        self.assertEqual(h3.validate_case(case), [])

    def test_lora_observation_contract(self):
        record = {
            "id": "lora-test", "property_or_character": "Test property", "source_model": "MiniMax H3",
            "adapter_type": "style LoRA", "compatibility": "h3-local-only", "source_url": "https://example.test/lora",
            "source_kind": "community", "source_date": "2026-08-14", "creator_claim": "A short claim.",
            "short_terms": ["controlled reaction"], "visual_anchors": ["close-medium framing"], "set_anchors": [],
            "costume_or_era": [], "motion_performance_cues": ["small hand gesture"], "negative_or_failure_notes": ["not API compatible"],
            "license_or_restriction_note": "Not reviewed.", "evidence_quality": "low", "confidence": "low", "verification_status": "research-only",
        }
        self.assertEqual(h3.validate_lora_observation(record), [])
        record["compatibility"] = "API-ready"
        self.assertTrue(any("compatibility" in error for error in h3.validate_lora_observation(record)))


if __name__ == "__main__":
    unittest.main()
