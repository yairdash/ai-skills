# Verification — 2026-10-16, Windows x64

- Node 24.19.0; FFmpeg and ffprobe 8.1.2.
- Herk 2.0.0: all 11 upstream tests passed.
- Herk check-kit: 700 distribution files, 2 styles, 406 cards, both skill trees;
  0 errors. Core fixtures and linked card resources are included.
- Herk media smoke: synthesized eight-second H.264/AAC source; silence pass
  expected 3.96s / encoded 3.96s; reviewed-cut pass expected 3.66s / encoded
  3.673s. Word text and retimed transcript checks passed; A/V lengths within
  the upstream test's 0.12s tolerance.
- HyperFrames 0.7.109: neutral demo lint returned 0 errors / 0 warnings;
  encoded 8s, 1920x1080, 30fps MP4. Decoded mid-frame visually inspected:
  headline and all three cards readable, no visible layout overflow.
- Remotion 4.0.536: separate neutral starter installed with npm ci; rendered
  60 frames / 2s, 1080x1080, 30fps H.264. Decoded frame visually inspected:
  Hebrew RTL line, title and animated progress bar displayed correctly.
- Codex skill-creator quick_validate passed for the root skill.
- Both MP4s decoded completely with FFmpeg without errors; ffprobe confirmed
  expected duration, dimensions, H.264 codec and 30fps.
- Portable ZIP extracted into a different path containing spaces: all 1,048
  payload hashes matched; the 11 upstream tests passed from the relocated copy.
- Transcript normalizer preserved Hebrew text and word times, and rejected
  segment-only timestamps, words past media duration, and unordered words.

The 1,048-file relocation test above describes the original portable package.
Public adaptation: newer HyperFrames entry documents renamed REFERENCE.md;
public-facing documentation and provenance added; no runtime code changed.
Public catalog and package checks are performed separately before publication.
No private machine paths, logs, footage or transcripts are part of this report.

Limits: Windows was exercised; macOS/Linux installation has not been executed.
These are synthetic smoke tests, not proof of production quality for every
card, language, codec or project. No Hebrew speech-recognition or speaker
diarization test was performed. No cloud APIs or paid generation were called.
The reference videos are silent; the Herk media test includes synthetic audio.

HyperFrames doctor also reports optional whisper-cpp, Kokoro, MusicGen and
Docker as absent, and advertises 0.8.164 as newer. The kit intentionally retains
Herk's pinned 0.7.109 for the verified integration. These optional components
are not required for the local renders that succeeded. Latest upstream skill
references may describe features beyond the pinned CLI.

Chrome Headless Shell is configured locally; the portable ZIP excludes the
browser, FFmpeg, dependencies, fonts, models, local paths and credentials.
On a new machine use the documented setup/browser commands. Local sandbox
restrictions required approved escalated npm downloads and Chrome rendering.
