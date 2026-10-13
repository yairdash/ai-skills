---
name: wan-3-filmmaking
description: Plan, prompt, troubleshoot, and hand off Wan 3.0 video work. Use for Wan 3.0 text-to-video, image/first-last-frame video, multimodal image-video-audio references, video-to-video editing, extension, native dialogue, storyboards, comic pages, recurring character/prop continuity, or a Wan 3.0 capability comparison.
---

# Wan 3 Filmmaking

Use this skill to turn a creative brief or supplied assets into a **Wan 3.0-ready production plan**, not merely a long generic prompt. State which facts are documented for Alibaba Model Studio and which depend on the user's Wan provider/UI.

## Start with the production decision

Ask only if the answer changes the plan:

- Which surface is being used: Alibaba Model Studio / wan.video / another hosted UI / API?
- Is the goal a new shot, animation of a locked first frame, an end-frame transition, reference-led creation, a video edit, or an extension?
- Is native spoken dialogue essential, and in which language?

If no answer is available, make a provider-neutral plan and label exact upload limits or UI controls as **Model Studio-specific**. Do not claim that every Wan-branded provider exposes the complete Wan 3.0 Omni workflow.

## Route to the right reference

| Need | Read |
| --- | --- |
| What Wan 3.0 can actually do; mode choice; strengths and limits | `references/capability-map.md` |
| Prompt structure; image/video/audio/document/web references; native audio | `references/prompting-and-references.md` |
| Video-to-video editing, motion/camera reference, extension, continuity | `references/video-editing-and-continuity.md` |
| Storyboards, graphic-novel/comic pages, dialogue bubbles, shot maps | `references/storyboard-and-comic-to-video.md` |

Read only the relevant files, but always use the capability map before making a precise capability claim.

## Default working method

1. **Choose one job for the generation.** New scene, first-frame animation, first/last-frame bridge, reference-led new shot, edit, or extension are different modes. Do not blur them together.
2. **Build a labelled asset pack.** Give every image/video/audio item one role: character, prop, location, visual style, camera/action, source video, or voice/music. Keep a small asset set unless there is a clear reason to add more.
3. **Bind roles in the prompt.** In Model Studio, refer to uploaded assets by the documented labels `Image 1`, `Video 1`, and `Audio 1` in their type-specific upload order. In other UIs, use their own labelling conventions or describe the roles explicitly.
4. **Write in shot language.** Lead with shot/framing, subjects, action, camera movement, scene/lighting, then audio. For multi-shot work, timestamp 4–6-second beats rather than putting a whole film into one sentence.
5. **Separate hard constraints from taste.** State what must persist (identity, wardrobe, prop, setting, intended words, no visible text) before aesthetic refinements.
6. **Review like an editor.** Check identity, action, camera, audio/dialogue, lip sync, unwanted text/bubbles, continuity, and whether the requested edit was local rather than a full rewrite. Make the next pass change one main failure.

## Non-negotiable rules

- `reference_video` can mean three different things: a **motion/camera inspiration**, a **source to edit**, or a **clip to extend**. Use explicit verbs such as “use Video 1 only for the orbiting camera move,” “edit Video 1,” or “extend Video 1 backward.”
- Treat a comic page as a **staging/style reference**, not a promise that the model will OCR, hide, and perform its bubbles correctly. Supply a clean dialogue transcript and explicit output exclusions.
- If exact wording matters, use a short, attributed line in quotation marks, keep the speaking face readable, and plan an audio/post fallback. Do not silently replace required dialogue with captions.
- Do not use “8K”, “pixel-perfect”, or other unsupported output claims as a quality instruction. Wan 3.0’s documented API outputs top out at 1080P.
- Preserve assets and generated URLs promptly. Model Studio documents that result URLs expire after 24 hours.

## Deliverable format

For a practical request, return:

1. chosen mode and why;
2. asset/upload list with roles and ordering;
3. settings to choose if the UI exposes them;
4. one copy-ready prompt;
5. a short QC checklist and the most appropriate fallback.

For a storyboard or comic, include a panel/shot map before the prompt. For a request comparing Wan 3.0 with another model, distinguish documented feature coverage from quality expectations that require a user test.

## Execution scope

Planning or writing prompts does not authorize generation. Use available tools only when the user requests execution; respect the host agent's authorization and cost policy. Do not start an automatic proof, batch, retry or final render. Check the current provider schema, save request IDs and report actual results honestly.
