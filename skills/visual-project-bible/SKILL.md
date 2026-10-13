---
name: visual-project-bible
description: Build or audit a visual project bible and decide which foundation reference images to create for characters, wardrobe, locations, props and visual style. Use before storyboards and shot opening frames, or when an existing reference collection needs gaps, priorities and approval criteria. Works across image and video providers.
---

# Visual Project Bible

Turn a premise, script or existing reference collection into a small, justified foundation image package. The outcome is an agreed visual design system and an ordered asset plan that another creator or agent can use without redesigning the project.

## Scope and inputs

Default to **planning and image prompts**, not image generation. A request to build a bible does not itself authorize renders, paid jobs, uploads or publication. If the user also requests image creation, use available tools within that request and cost constraints; do not run an automatic sample-plus-final pipeline. Never claim an image was inspected or generated without doing so.

This stage establishes reusable design references. Do not drift into a shot list, storyboard, motion prompt or shot opening frame unless requested. A location master establishes a space; it is not automatically the opening composition of a future shot. This is a visual bible, not a replacement for a full story/series bible, production schedule or narrative-development process.

Use the supplied context before asking questions. Clarify only uncertainties that materially alter the image package: the project premise/use, recurring subjects, visual medium, approved references, or production constraints. Do not require a full script or a chosen provider to start. With an early idea, state provisional assumptions and offer a compact first pass. Preserve established creative choices; ask before replacing a user-approved design. Respond in the user's language; use their requested prompt language, otherwise English for reusable image prompts.

## Workflow

1. **Extract design commitments.** Identify the project's visual intent, recurring characters, wardrobe states, locations, story-critical props and visual transformations. Mark each commitment as supplied, observed, proposed or unresolved. Do not invent a cast, extra location or costume change just to fill a template.
2. **Audit what already exists.** Inspect accessible references and record their actual filenames/links, intended roles and known approval status. A supplied image is not automatically approved. If images cannot be viewed, record their descriptions as unverified and continue planning without claiming a visual audit. Separate useful design evidence from unsuitable backgrounds, poses or styles that must not carry over.
3. **Choose the smallest useful package.** Read [asset selection](references/asset-selection.md). For each proposed image, name the design question it answers and the future use that needs it. Reuse adequate images; add views, expressions, variants or spatial diagrams only for a specific visibility, interaction, continuity or provider requirement. Distinguish indispensable assets, conditional assets and deferred ideas. Do not prescribe a fixed number of images per character or project.
4. **Build the bible and image register.** Use [bible template](assets/visual-bible-template.md) and [image register](assets/image-register-template.md), trimming unused sections. Keep stable entity IDs separate from image IDs. Each required visual decision needs an existing reference or a planned image, or an explicit reason that text alone is enough. Record invariants, permitted changes, approval criteria and dependencies.
5. **Order creation by dependency.** Resolve visual direction before expanding style variants; establish character identity before dependent wardrobe or expression variants; establish location layout before dependent alternate views. Existing approved inputs can satisfy those dependencies. Explain what can proceed independently; do not enforce a universal sequence when a hero product or designed setting is the project's starting point. When budget is unknown, provide a lean first wave and a conditional second wave, with image counts and reasons but no invented prices.
6. **Write requested image prompts.** For each first-wave asset, state its purpose, inherited references, visible design constraints, useful framing/background and acceptance criteria. Use [prompt and review guidance](references/prompts-and-review.md). Prompts establish reusable references, not dramatic shot action. Do not invent attachment IDs, provider syntax, reference capacity or supported output sizes. If the user only asks for a plan, keep full prompts optional.
7. **Check coverage and hand off.** Verify that every required entity/state has a usable reference or a named gap; no image duplicates another's job without a reason; dependencies are satisfied or scheduled first; and conflicting references are resolved or flagged. Distinguish proposed plans from approved designs. End with the next actionable wave and remaining decisions, not a request to approve every minor choice.

## Deliverable

For a new project, provide:

- A concise visual bible with design intent and stable character/location/prop definitions.
- An image register: what exists, what is needed, why, priority, dependency, prompt readiness and approval criteria.
- An ordered first wave, conditional additions and deliberate omissions. Count existing reusable assets separately from new images to create. Where no budget was set, avoid treating an initial count as a spending commitment.
- Copy-ready first-wave image prompts when requested, or a clear offer of that next step when only planning was requested.
- A short handoff describing which approved images control identity, wardrobe, environment, prop or style. Later directing skills determine shot composition and motion; their exact provider schemas control technical reference binding.

For an audit or small revision, return only the affected bible entries, register changes, conflicts and next wave. Do not rebuild approved work unnecessarily.

Use the asset templates inline for chat-only work. When the user asks for a saved bible or an existing project workflow requires files, save a trimmed copy in that project's chosen location; do not write into the installed skill's own assets. Preserve previous approved versions and record which dependent assets become stale when a design changes. Refer to approval as a recorded user/team decision, not a status the agent grants itself.

## Boundaries and maintenance

- A beautiful image can be a poor reference: judge recognizability, readable design, geometry, visibility and consistency for its assigned task.
- Do not promise perfect identity, exact text, identical lighting or reliable multi-view geometry from a prompt. Treat untested workflows as proposals.
- Provider-specific references, transparency, sizes, formats and costs require checking the exact current tool contract when relevant. Planning itself needs no model account or companion skill.
- Keep source and usage notes for external references; permission to use an image as inspiration does not establish permission to redistribute it. Do not copy private source images or account links into a public bible by default.
- When the user later requests shots, freeze the applicable design version and pass only relevant approved references to the next stage. A new pose or attractive shot does not silently replace the canonical identity image.
