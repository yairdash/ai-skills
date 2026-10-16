---
name: video-production-kit
description: Edit social videos and spoken recordings with Herk and FFmpeg, or build motion graphics with HyperFrames and Remotion using this portable local toolkit. Use for these production workflows and their local setup; preserve the user's chosen editor or framework.
---

# Portable video production

This folder is KIT. Its setup instructions are in [README.he.md](README.he.md).
Run `node KIT/kit.mjs doctor` to inspect this computer. Machine-specific paths
belong in `local.config.json`, never in portable sources. Preserve original footage.

Choose the smallest applicable workflow:

| Request | Read |
| --- | --- |
| Complete talking-head edit, Shorts/Reels, silence or mistake cuts | [Herk workflow](references/herk.md) |
| Trim, join, convert, audio leveling, final encode or media QA | [FFmpeg](references/ffmpeg.md) |
| HTML/GSAP motion graphics and infographics | [HyperFrames](references/hyperframes.md) |
| React-based animation or a requested Remotion project | [Remotion](references/remotion.md) |
| Hebrew text/captions or final delivery | [Delivery checks](references/delivery.md) |

Use the available creative-development/writing skills when the user requests
them; a graphics library does not replace a script. Keep the brief, script,
scene timing, and chosen output format with the project. For an existing edit,
inspect the media and reuse verified transcripts before choosing transcription.

Herk's bundled skill folders are supporting resources, not separate global
installations. Resolve its workspace-relative scripts/docs against
`runtime/herk`, created by `node KIT/kit.mjs setup`. Read the corresponding
source under `vendor/herk` when no runtime exists. Do not copy only a SKILL.md:
its sibling skills, scripts, references and style library are dependencies.

This wrapper's routing preserves explicit framework choices. Upstream
HyperFrames-first defaults apply within a HyperFrames project only. No cloud
uploads, paid generation, publication, or messages are implied by local editing.
CapCut projects require a separate native-project workflow; neither an HTML
timeline nor React source is a verified CapCut project.

Deliver an MP4 when requested, plus editable source, assets with licenses,
an EDL and retimed transcript where applicable, and honest verification notes.
Automation proposes editorial cuts; review meaning, natural breaths and joins.
