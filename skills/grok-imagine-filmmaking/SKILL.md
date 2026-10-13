---
name: grok-imagine-filmmaking
description: Plan, prompt, troubleshoot, and hand off AI-film image and video work in Grok Imagine. Use when the user asks to work in Grok Imagine, Imagine Agent/Canvas, or needs Grok-specific help with reference images, recurring-character or prop continuity, voice continuity, image editing, image-to-video, multi-shot sequences, extensions, or external post-production.
---

# Grok Imagine Filmmaking

Build dependable short-form AI-film work by separating **what must remain fixed** from **what the current shot changes**. Treat references as visual evidence, not as magic character tokens.

## Start here

1. Identify the working surface: consumer UI, API/Playground, or an exported clip. Do not assume that an API feature has the same label or availability in the consumer UI.
2. Determine whether the request is a one-off still/clip, a new shot with continuity, a true continuation, an edit, or a multi-shot plan.
3. Read only the relevant reference file below, then produce the requested prompts or plan.
4. For a multi-shot scene, lock the project brief and the continuity bible before writing individual shot prompts.

## Reference routing

| Need | Read |
| --- | --- |
| Set up a project, asset list, naming, a character/prop/location bible, or reference hierarchy | [production-foundations.md](references/production-foundations.md) |
| Generate a still, create an animation keyframe, composite references, or make a precise image edit | [image-workflows.md](references/image-workflows.md) |
| Generate a video, choose text/image/reference-to-video, direct camera and action, or write spoken dialogue | [video-workflows.md](references/video-workflows.md) |
| Preserve identity across shots, extend action, edit a clip, recover from drift, or assemble coverage | [continuity-and-sequences.md](references/continuity-and-sequences.md) |
| Run a full Canvas / Agent Mode session: plan, board, generate, iterate, organize, and assemble a scene | [canvas-agent-workflow.md](references/canvas-agent-workflow.md) |
| Plan a multi-shot workspace/project or decide what belongs in an NLE | [project-assembly.md](references/project-assembly.md) |
| Diagnose a bad result, select takes, hand off an edit, or run final continuity QC | [finishing-qc-and-troubleshooting.md](references/finishing-qc-and-troubleshooting.md) |
| Confirm current capabilities, limits, model names, or voice-reference availability before relying on them | [capabilities-and-version-check.md](references/capabilities-and-version-check.md) |

## Operating rules

- Ask only for material missing inputs: target format/length, available references, spoken text, or desired outcome. Make a reasoned recommendation when the user leaves the mode undecided.
- Prefer a strong, approved start image when the first frame or production design matters. Use visual references for a new angle or action that needs to retain identity or a hero asset.
- Write prompts in chronological, shot-readable language: subject/action → camera → setting/light → dialogue/audio → continuity constraints. Keep one principal beat and one primary camera move per generated clip unless the user asks for a deliberately complex experiment.
- Use extension only for continuous time from the final frame. For a new angle, new coverage, or a recovery from drift, start a fresh generation with the approved reference set.
- State the role of each reference explicitly when more than one is attached: identity, wardrobe, prop, location, style, or start frame. Do not attach redundant images merely because a mode permits them.
- Keep an approved frame after every successful generation. Promote it to the current reference set only when it actually improves continuity.
- Use Canvas / Agent Mode as a full production workspace when the user asks for it. Use the controls confirmed in the user's current interface; do not invent an unavailable template, lock, or stitch command.
- Do not assume an undocumented saved character ID, permanent reference lock, or voice-cloning entitlement. Treat the user's live Grok interface as authoritative.
- Use only likeness, voice, and assets the user has a right to use.

## Default deliverable

Unless the user asks for something else, give the recommended mode and reference package, a compact production-ready prompt, a short continuity block where useful, and an explicit next step or recovery option.

For a scene, provide a concise coverage plan first, then one prompt per shot. Keep prompts neutral enough for the Grok UI unless the user specifically asks for API syntax.

## Accuracy gate

Read `references/capabilities-and-version-check.md` before asserting a current product limit, model name, interface control, reference-audio workflow, or account-specific feature. Product UI changes quickly; do not turn a temporary interface observation into a general instruction.

## Execution scope

Prompt writing and planning do not authorize media generation. Generate only when requested, using available tools and the host agent's cost policy; do not add automatic proofs, batches or retries. Never claim a render, saved file or account capability without evidence.
