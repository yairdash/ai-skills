# H3 and FAL Contract

Invoke `$h3-prompt-writing`. Base field order is `integrated_multimodal_description`, `overall_soundscape`, `non_diegetic_music`. Full-reference order is `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music`. Dialogue requires stable speaker IDs and `<d>[Language]…</d>`. Do not use TTS-only pause notation.

Verified 2026-08-12, but refresh immediately before use:

- `minimax/h3/text-to-video`
- `minimax/h3/image-to-video`
- `minimax/h3/reference-to-video`
- observed price `$0.26` per generated second

Observed reference limit: 12 total, at most 9 images, 3 videos, and 3 audio; audio cannot be the sole reference. Treat this as a dated cache.

Before submission display exact endpoint, duration, resolution, aspect ratio, expansion, reference provenance, price timestamp and estimate, frame inputs, and disclosure status. Keep `approval_status: pending` until the user approves those exact values.

Never assume `enable_prompt_expansion` exists. Compare the payload with the freshly returned endpoint schema. If the field is absent, omit it and disclose prompt expansion as provider-managed. An old schema snapshot never overrides the live connector.

## Connector submission route

When a FAL connector/plugin is callable:

1. Refresh the exact model schema and price.
2. Compile only fields exposed by that schema.
3. Upload references and verify remote byte length or hash when possible.
4. Show the full cost gate and obtain explicit approval.
5. Submit exactly one job and persist its request ID immediately.
6. Poll or recover that same request ID until terminal status.
7. Fetch the result and verify the downloaded file.

The offline script remains deliberately unable to submit. Connector availability is separate from script capability.

Persist a successful request ID immediately. If status is unclear, recover or poll it. A changed payload is a new billable job and needs separate approval.

Do not automatically retry a failed input, upload, or generation. A replacement job requires a new explicit cost approval. A truncated reference upload is an input-integrity failure; repair and verify the asset before requesting replacement approval.
