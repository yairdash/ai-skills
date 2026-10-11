---
name: develop-h3-parody-shorts
description: Research, benchmark, develop, prompt, generate, and review original MiniMax H3 parody and crossover shorts using famous fictional character engines. Use when evaluating H3 native character knowledge, maintaining evidence, building character bibles or concept cards, writing micro-gags and storyboards, compiling official H3 prompts, preparing or submitting approved FAL payloads, estimating cost, or scoring outputs. Never submit a paid FAL job without explicit user approval.
---

# Develop H3 Parody Shorts

Use research evidence before creative confidence. Treat recognizable characters as behavioral engines placed in new worlds with new conflicts, not as a license to copy dialogue, plots, or beat structures.

Read [references/empirical-findings.md](references/empirical-findings.md) before choosing a property. Keep project-demonstrated results, repeated community reports, isolated claims, and predictions visibly separate.

When researching a property, also consult [references/lora-derived-knowledge.md](references/lora-derived-knowledge.md). LoRA listings can contribute attributed descriptive hypotheses, never proof that the FAL API can reproduce a character or world.

## Required Gate Order

1. Research and collect evidence.
2. Benchmark character and world knowledge.
3. Build a sourced character bible and transformation analysis.
4. Develop original concepts.
5. Write the script and storyboard.
6. Compile the prompt with `$h3-prompt-writing`.
7. Refresh the live FAL schema and price, validate the payload, show cost, and obtain explicit approval.
8. Score the output, revise, and conduct publication review.

Do not skip a gate whose output is required downstream. Stop before Gate 7 submission unless the user clearly approves the exact endpoint, duration, resolution, references, and estimated cost shown in the current turn.

## Route by Task

- For research, evidence classification, and uncertainty ranking, read [references/research-and-evidence.md](references/research-and-evidence.md). When applicable, read [references/lora-derived-knowledge.md](references/lora-derived-knowledge.md) before the character-bible stage.
- For benchmarks, classification thresholds, scoring, and rerun decisions, read [references/benchmark-and-qa.md](references/benchmark-and-qa.md).
- For the current property map and production lessons, read [references/empirical-findings.md](references/empirical-findings.md).
- For character bibles, concept cards, voice, scenes, and storyboards, read [references/creative-development.md](references/creative-development.md).
- For H3 field order, FAL endpoints, reference constraints, manifests, cost gates, and retry safety, read [references/h3-fal-contract.md](references/h3-fal-contract.md), then invoke `$h3-prompt-writing`.
- For synthetic-media disclosure, actor audio, endorsement, and publication review, read [references/rights-and-publication.md](references/rights-and-publication.md).
- For source provenance and upstream revisions, read [references/sources.md](references/sources.md).

## Deterministic Checks

Run `scripts/h3_workflow.py` before accepting prompts or manifests:

```powershell
python scripts/h3_workflow.py lint-prompt --mode base --duration 5 --prompt-file prompt.txt --forbidden-dialogue-file forbidden-dialogue.txt
python scripts/h3_workflow.py validate-case --file benchmark-case.yaml
python scripts/h3_workflow.py validate-manifest --file generation-manifest.json
python scripts/h3_workflow.py validate-lora-observations --file research/lora-observations.jsonl
python scripts/h3_workflow.py estimate-cost --duration 5 --runs 6 --price-per-second 0.26
```

The script only validates and prepares data. It contains no FAL submission operation. If a callable FAL connector or plugin is available, use it only after the live-schema and cost gate in [references/h3-fal-contract.md](references/h3-fal-contract.md).

## Core Rules

- Record claims before relying on them. Community reports are leads, not ground truth.
- Keep adapter observations in `research/lora-observations.jsonl`, separate from native-H3 evidence. Never download weights or automatically paste LoRA trigger words into an API prompt.
- Label each character-bible, concept-card, storyboard, and prompt ingredient as `project-demonstrated`, `official`, `community-reported`, `LoRA-derived`, or `inferred`.
- Reject unsupported numeric accuracy claims from the uploaded guide.
- Preserve exact prompts, payloads, schema timestamps, references, request IDs, outputs, and scores.
- Prefer one visible speaking face at a time. Give every silent listener a distinct appearance, fixed screen position, and explicit closed-mouth instruction.
- Treat a successful five-second identity probe as a lead, not proof that a ten-second comedy scene will preserve behavior, voice, staging, and timing.
- Use stable speaker IDs and `<d>[Language]…</d>` for every spoken line.
- Use H3-native vocal resemblance only. Never attach cloned actor audio without documented consent or licensing.
- Avoid catchphrases, quoted dialogue, recreated scenes, borrowed shot sequences, and an “official” presentation.
- Default creative form after benchmark acceptance: 8–15 seconds, 9:16, frame-one hook, one escalating conflict, reaction payoff.
- Prepare payloads freely; spending is always opt-in.

## Done Criteria

A research or benchmark phase is complete only when evidence is sourced, uncertainties are ranked, artifacts validate, and the next paid test is both necessary and costed. A creative phase is complete only when the concept passes the originality check, its prompt passes linting, and publication risks are disclosed.
