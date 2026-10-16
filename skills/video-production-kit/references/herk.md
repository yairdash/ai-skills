# Herk editing

Version: 2.0.0; exact upstream commit and archive hash: ../sources.lock.json.
Read ../vendor/herk/AGENTS.md and ../vendor/herk/docs/WORKFLOW.md.
Run `node KIT/kit.mjs setup` once, then work in KIT/runtime/herk.
`node KIT/kit.mjs herk scripts/new-video.mjs project-slug` creates a project.
Herk itself pins HyperFrames 0.7.109 and GSAP 3.14.2.

Load only the needed module from ../vendor/herk/.agents/skills/:
- edit-video: full workflow.
- short-form-edit: reels and Shorts, source-mapped captions and scene plan.
- cut-silences: transcript-based gaps; preserve natural speech rhythm.
- cut-mistakes: candidate generation, contextual review, applied cut decisions.
- video-storytelling: narrative arc and visual callbacks.
- hyperframes-video-beats: transcript-anchored overlays.
- motion-showreel: rhythm and visual motifs, optional external asset services.
- style-library: 406 draft cards; adapt typography, brand and placeholder data.
- make-a-video: new graphic video from a brief.
- website-to-hyperframes: website-inspired compositions.
- hyperframes, hyperframes-cli, hyperframes-registry, gsap: framework helpers.
- short-form-video: historical example workflow; referenced May projects are
  intentionally NOT bundled, so prefer short-form-edit for new work.

Silence pass outputs become BOTH the next video AND next transcript. Never
apply source-time captions to an edited video. Preserve EDLs through each pass.
Speech or factual edits need contextual judgment; detectors are candidates.

Verification commands:
```
node KIT/kit.mjs npm test
node KIT/kit.mjs herk scripts/smoke-media.mjs
node KIT/kit.mjs herk scripts/preflight.mjs video-projects/project-slug
```
The smoke exercise uses synthetic media, requires no API key, and checks the
encoded lengths against retimed transcripts. It does not test Hebrew ASR.
Transcription: use supplied word timestamps, an already configured local
Whisper, or the user's chosen provider. ElevenLabs is optional, not installed
or authorized merely by this kit. See vendor/herk/docs/TOOLS-AND-API-KEYS.md.

AIS brand assets and published source projects are excluded. Some teaching
references therefore point to the upstream repository rather than local files.
The core test fixtures, card dependencies and starter composition are included.
