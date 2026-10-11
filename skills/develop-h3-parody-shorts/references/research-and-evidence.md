# Research and Evidence

Use exactly one `source_class`: `official`, `community-repeated`, `community-single`, `project-empirical`, or `disproved-or-stale`. Confidence is `low`, `medium`, or `high` and describes support, not desirability. Community repetition is informative, but only official or project evidence can establish production guidance.

## Procedure

1. Start with current MiniMax and FAL primary sources.
2. Map prompt format, endpoint schema, price, references, and examples.
3. Research successes and failures across identity, behavior, voice, world recall, aspect ratio, and reference rescue.
4. Extract atomic claims into `research/evidence-record.jsonl`.
5. Record conflicts; do not silently choose the more exciting claim.
6. Rank uncertainties by production impact and cheapest discriminating test.

Treat unofficial technical guides as hypothesis sources. Reject unsupported numeric accuracy claims. Current official prompt rules and live provider schemas override it.

Keep sourced canon, community observations, project tests, creative proposals, and rejected ideas separate. Add new dated records when claims change; mark old records stale instead of erasing history.

## LoRA-derived observation boundary

Store adapter-marketplace and local-workflow claims in `research/lora-observations.jsonl`, not in `evidence-record.jsonl`. Classify an adapter as `h3-direct`, `h3-local-only`, `peer-transfer-hypothesis`, or `image-only-reference`. A peer-model LoRA may suggest useful costume, set, movement, or framing vocabulary, but it does not establish H3 native recall or FAL compatibility. Preserve only short, attributable production terms; do not retain weights, datasets, source media, long prompt templates, or actor-audio material.
