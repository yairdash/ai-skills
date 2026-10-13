# 04 — Reference Roles, Technical Checks and Advanced Workflows

## Contents
- Technical status and verification
- Core modular formula
- Reference roles and selection
- Audio and negative instructions
- Timing and stages
- Conditional extension and editing workflows

## Technical status and verification
The original skill contained a supplied Seedance 2.5 specification whose official provenance was not independently verified. Do not treat those inherited figures or claimed capabilities as current facts. This revision retains its useful directing workflows but removes reliance on unverified numeric limits, Ultra Long claims, resolution tables, file-format limits and universal 2.0 inheritance.

Before advising on duration, resolution, reference count, file size, editing, extension, audio-only input or model availability, check the exact model and platform’s current official documentation or interface. Cite sources for technical answers. Distinguish user-tested practices from verified specifications. If unavailable, state what remains unknown; still write a useful creative prompt when possible. Do not transfer a 2.5 capability to 2 without evidence.

## Core modular formula
For simple image-to-video use camera direction, character, action plus manner, followed by optional dialogue in quotation marks, environment changes, motion style and sound. Choose editing structure using doc 01; add `One continuous shot` only when that mode was deliberately selected, or use `CUT TO:` for planned edits. Avoid describing an already visible still. For multiple references, prepend role mapping. Use a longer prompt only for necessary control, not as a quality ritual. Keep UI generation settings outside prompt text.

## Reference roles for multiple materials

For multi-reference work, state what each supplied material contributes. Use actual interface identifiers; @Image 1, @Video 1 and @Audio 1 below are illustrative. Add exclusions when a specific unwanted attribute could leak in. Never rely on text labels inside images; never make the model infer which material maps to what.

> @Image 1 defines `<subject>`'s `<appearance, clothing, structure, or material>`. Do not use `<the image background / the people in the image / the composition>`.
> @Video 1 defines `<motion, camera movement, or pacing>`. Do not use the person's identity, clothing, or scene from the video.
> @Audio 1 defines `<character or sound type>`'s `<voice, dialogue, ambience, or music>`.

Rules:
- **Map one-to-one.** Never write "@Images 1 through 4 define four characters respectively" — state which image is which character.
- **Multiple views of one subject:** say so explicitly ("@Image 1 defines the front view of the same folding desk lamp... All four images define one lamp. The output must contain only one lamp throughout.").
- **Single-instance continuity:** clearly identify one subject across views and preserve appearance and part-count as needed; this is an instruction, not a guaranteed fix.
- **When a reference video already defines motion accurately**, state only which attributes to inherit — restating every action can conflict with the reference. A blockout video provides motion and spatial structure only; the prompt must still define subjects, scene, action, and style.
- **Grid overlay exclusion (this GPT's standard):** when the reference is an annotated pose grid, assign motion phases and optionally identity as intended; the role line and excludes grid layout, panels, arrows, trails, annotations, numbers, and text (see doc `03`).

### Many materials — the full discipline
The goal is to help the model pick the right material per scene, not to make everything appear at once. Order of operations: define each material's role → map subjects one-to-one → group by type ([Characters] / [Props] / [Scenes] / [Motion and Audio]) → create a **subject profile** for important recurring subjects → select references per scene.

Subject profile pattern:
> [Subject Profile: `<name>`]
> Appearance and clothing: @Image 1. Fixed prop: `<prop>` from @Image 5. Locations: `<scene A>`, `<scene B>`. Motion references: `<motion>` from @Video 1. Do not use: other characters' clothing. Do not give this character `<other subject's prop>`.

Per-scene selection pattern:
> Scene 1 | `<title>` — Use: `<subjects, props, scene, motion refs>`. Event: `<one event>`. End state: `<visible state>`.

## Audio and negative instructions
Use ordinary language and exact dialogue in quotation marks. Specify speaker and the language or delivery where helpful. Preserve the user’s dialogue. Distinguish a voice-identity sample from a recording whose actual words and performance should drive the shot; clarify only if the intended role is unclear. Include the words the character says even when audio is supplied.

For a simple opening-image shot with a separately bound voice sample, omit tags when the actual interface does not require them. The attachment steps belong outside the prompt. For complex multi-reference audio, map the intended speaker to the correct material.

Simple opening-image work generally needs no negative prompts unless a demonstrated failure warrants them. Advanced video-reference work may use targeted exclusions to separate motion from identity, scenery or annotations. Avoid generic negative lists and automatic no-music/no-subtitle clauses. Role exclusions are negative instructions too, not a guaranteed separate mechanism. Do not generalize their effectiveness to all image-only reference work.

## Timing and stages
Use natural causal progression for ordinary action. When needed, use consecutive time ranges, a critical time point, or relative timing. These guide pacing rather than guarantee frame-accurate cuts. Ensure dialogue and actions fit the allotted time. Do not force timestamps or stages into a simple shot.

Optional complex-sequence structure:
> [Generation Goal] <intended scene or event>
> [Stage 1] <primary event, camera and acting; initial/end state only if needed>
> [Stage 2] <next event with necessary continuity>
> [Maintain Consistency] <only attributes at risk of changing>

## 7. Video extension — align the boundary frame first

**Extension after the source, if supported:** the extension's first frame continues the source's **last frame**. First describe the continuous state of that last frame (subject pose/orientation, prop positions, background, camera, lighting, motion direction), then describe the new content, then state what stays continuous throughout (identity, clothing, key props, layout, axis of action).

> @Video 1 is the source video to extend after its end.
> Continue after the end of @Video 1. The first frame of the extended segment directly continues from the last frame of @Video 1. Maintain continuity in `<boundary-frame state>`.
> Then, `<new action, event, camera treatment, or audio>`.
> Throughout the extension, maintain continuity in `<identity and clothing>`, `<key props>`, `<background layout>`, and `<axis of action>`.

**Extension before the source, if supported:** describe what happens before the source begins, then define the source's **first frame as the explicit end state** of the extended segment. Writing only "then connect to the source video" can introduce later elements too early or let the image drift after reaching the target state.

**With additional materials:** define every added material's role first, then state that the source video controls the extension boundary — new materials may supplement characters, props, or audio but must not override the source's boundary-frame control. After generation, inspect the boundary frame *and* whether characters, props, background, and events in the extension are correct.

## 8. Video editing — master video, scope, preserve

Define the source as the **sole editing master**, then the edit target, scope, target material, and content to preserve:

> [Edit Goal] Edit @Video 1. Within `<entire video / time range>`, `<add / remove / replace / adjust>` `<object, region, or audio category>`.
> [Source Video Role] @Video 1 is the sole editing master. It defines `<characters, scene, actions, composition, camera movement, occlusion relationships, audio, event order>`.
> [Target Material Role] @Image 1 or @Audio 1 defines `<specified attributes of the target>`. Do not use `<irrelevant background, people, or composition>`.
> [Edit Scope] Modify only `<object, region, time range, or audio category>`. The video contains `<N>` target object(s). Do not modify `<content to preserve>`.
> [Timeline Inheritance] `<Target>` inherits every appearance, motion, occlusion, and exit of `<original>`, including timing, duration, path, and speed changes.
> Except for the object or area explicitly modified above, keep all other people, props, scene content, camera movements, cuts, and event order from @Video 1 unchanged.

Named patterns: **subject replacement** (replace one object; keep exactly one instance; inherit its full timeline), **background replacement** (modify only outside the subject's silhouette; keep identity, position, size, motion; allow natural lighting response on the subject), **audio editing** (section 4), **time-ranged edits** ("Only from 4–7 seconds, change...").


Verify that these extension or editing modes exist in the selected model and platform before presenting them as executable workflows. For first/last-frame generation, describe the connecting action, preserve compatible composition and aspect ratio, and state the destination only when it matters.
