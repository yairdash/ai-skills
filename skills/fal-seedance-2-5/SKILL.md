---
name: fal-seedance-2-5
description: Create, rewrite, audit, or run ByteDance Dreamina Seedance 2.5 video prompts on fal.ai. Use for text-to-video, start/end-frame image-to-video, multimodal reference-to-video, ordered image/video/audio mapping, 4–30 second staged narratives, native dialogue and sound, identity continuity, video editing, subject replacement, forward extension, storyboards, blockouts, and fal request validation.
---

# Create Seedance 2.5 videos on fal.ai

Turn the user's concept and media into one clear Seedance 2.5 prompt and, only when requested, one valid fal.ai job. Treat references as control signals, stages as visible state changes, and every stage's end state as the continuity contract for the next stage.

This is a self-contained fal-specific skill. Do not look for companion files.

## Follow the authority rules

- Use this skill only for Seedance 2.5 on fal.ai.
- Inspect the live endpoint schema before execution. The live schema overrides static limits or fields in this file.
- Never silently substitute Seedance 2.0 or another model.
- When the user asks to write, format, rewrite, or audit a prompt, do not run a model.
- When the user explicitly asks to generate or render, submit one job. Do not start batches, preview-plus-final pairs, or automatic retries without authorization.
- Follow the host agent's authorization and cost policy for paid execution.
- Ask a question only when a missing fact would change subject identity, reference order, the edit target, extension direction, or story outcome. Infer harmless defaults.

## Select the endpoint

| Intent | Endpoint | Inputs |
| --- | --- | --- |
| Text only | `bytedance/seedance-2.5/text-to-video` | `prompt` plus generation settings |
| One start frame, optionally one end frame | `bytedance/seedance-2.5/image-to-video` | `image_url`, optional `end_image_url`, `prompt` |
| Multiple references, editing, replacement, or extension | `bytedance/seedance-2.5/reference-to-video` | `image_urls`, `video_urls`, `audio_urls`, `prompt` |

Use image-to-video for a true first-frame or first-and-last-frame transition. Do not place those boundary images into a reference array merely to imitate the dedicated fields.

Use reference-to-video when a source video is the editing master, when several inputs have distinct roles, or when extending a source video.

## Use fal's exact reference dialect

For reference-to-video, use these case-sensitive, one-based prompt tokens:

```text
@Image1  @Image2
@Video1  @Video2
@Audio1  @Audio2
```

Do not use lowercase Dreamina UI tokens such as `@image1`, space-separated labels such as `Image 1`, bare labels such as `Image1`, or square-bracket labels such as `[Image1]`.

Each media type has its own index. `@Image1` is the first item in `image_urls`; `@Video1` is the first item in `video_urls`; `@Audio1` is the first item in `audio_urls`. Preserve array order from registry through submission.

## Respect the current fal request contract

Verify these values against the live schema before a run:

- Resolution: `480p`, `720p`, or `1080p`; default `720p` (documentation checked 2026-10-13).
- Duration: `"auto"` or a string from `"4"` through `"30"`.
- Text-to-video and reference-to-video aspect ratio: `"auto"`, `"21:9"`, `"16:9"`, `"4:3"`, `"1:1"`, `"3:4"`, or `"9:16"`.
- Image-to-video aspect ratio: always `"auto"`, inherited from the start image.
- `generate_audio`: defaults to `true` and controls synchronized dialogue, ambience, and effects.
- `end_user_id`: pass it only when the user's fal environment requires it; never fabricate one.
- The reference-to-video input schema exposes optional integer `seed`. The checked text-to-video and image-to-video schemas return a seed but do not expose it as an input. Send it only when the exact live route accepts it; reproducibility is not guaranteed.
- On reference-to-video set `task` explicitly: `reference`, `editing`, or `extension`. Editing coerces duration and aspect ratio to `auto`; extension coerces aspect ratio to `auto`. Do not rely on prompt wording alone to select the API operation.
- Optional `draft`, `bitrate_mode`, and `codec` exist in the checked schemas. Read their live contract when needed; a draft followed by completion is a separate workflow and must be authorized, not an automatic extra job.
- Do not promise 4K or more than 30 seconds on fal unless a newer live schema explicitly exposes it.

Reference-to-video currently accepts up to 50 files total:

- `image_urls`: up to 30 images; JPG, PNG, WebP, BMP, TIFF, GIF, HEIC, or HEIF; no more than 30 MB each.
- `video_urls`: up to 10 MP4 or MOV files; each 1.8–30.2 seconds and no more than 200 MB; combined duration no more than 30.2 seconds; 300–6,000 pixels per side; aspect ratio 0.4–2.5; 24–60 FPS.
- `audio_urls`: up to 10 MP3 or WAV files; each 1.8–30.2 seconds and no more than 15 MB; combined duration no more than 30.2 seconds.
- When audio is supplied, include at least one image or video reference.

Use more references only when they remove uncertainty. Trim reference video and audio to the relevant segment. Prefer separate views over one dense collage for an important subject.

## Classify the creative task

Choose one contract before writing:

- **Simple generation:** one subject, action, and scene.
- **Reference-to-video:** one or more references define subjects, props, scene, motion, camera, voice, or sound.
- **Staged narrative:** two or more consecutive visible changes.
- **Timed narrative:** a critical entrance, exit, handoff, transition, or sound cue needs a time budget.
- **Video edit or replacement:** modify a source video while preserving everything outside the exact scope.
- **Forward extension:** continue from the last frame of a source video.
- **First/last frame:** transition between dedicated start and end images.
- **Storyboard/blockout:** inherit declared composition, staging, motion, camera, cuts, or lighting evidence.

Do not promise backward extension unless the current fal documentation explicitly supports it. A prompt describing preceding action is not proof that the endpoint provides a backward-extension operation.

## Build the reference registry

Before composing, record for every input:

1. Exact array and slot.
2. fal prompt token.
3. Named subject or production role.
4. Attributes to inherit.
5. Incidental attributes to exclude.

Use explicit role statements:

```text
@Image1 defines <subject>'s <face, clothing, structure, material, or color>. Do not use <background, people, composition, or incidental content>.
@Video1 defines only <motion path, camera movement, pacing, action timing, or transition>. Do not use <person, scene, materials, or style>.
@Audio1 defines <speaker>'s <voice, accent, delivery, or exact dialogue performance>.
```

Never rely on “respectively.” Map every character, prop, environment, motion source, and voice independently.

When several images show one entity, declare the relationship:

```text
@Image1 defines the front of the same folding lamp.
@Image2 defines the left-side structure of the same folding lamp.
@Image3 defines the rear structure of the same folding lamp.
All three images define one continuous folding lamp. Keep exactly one lamp throughout.
```

For more than four references, group the map under `[Characters]`, `[Props]`, `[Scenes]`, `[Motion and Camera]`, and `[Audio]`. Use only the relevant references in each scene; do not force every input to appear at once.

## Choose the lightest time structure

- Use natural chronological prose for one simple event in one shot.
- Use named stages for two or more events and ordinary 10–30 second narratives.
- Give every stage one primary state change and an observable end state.
- Use time ranges only to allocate pacing or control important entrances, exits, handoffs, transitions, or sound cues.
- Use an exact time point for at most one key event.
- Keep ranges consecutive, non-overlapping, achievable, and within the requested duration.
- Treat ranges as pacing budgets, not frame-accurate edit points.

## Compose in production order

Use the smallest useful subset of this structure:

```text
[Reference Map]
<Character A> corresponds to @Image1. Use only <identity traits>. Do not use <incidental content>.
<Prop A> corresponds to @Image2. Use only <structure, material, color, or wear>.
<Scene A> references @Image3. Use only <layout, architecture, lighting, or atmosphere>. Do not use <people or foreground objects>.
@Video1 defines only <motion, camera movement, action timing, or pacing>. Do not use <person, scene, or style>.
@Audio1 defines <Character A>'s <voice, accent, and delivery>.

[Generation Goal]
Generate a <video type>. <One-sentence story>.

[Global Direction]
<Environment, visual treatment, camera language, and sound bed>.

[Stage 1 | Name]
Initial state: <what is visibly true at the start>.
Primary event: <one main action or state change>.
Camera: <shot size, angle, movement, focus, or transition>.
Audio: <speaker and quoted dialogue, ambience, effects, or music>.
End state: <positions, prop ownership, object count, screen direction, and visible result>.

[Stage 2 | Name]
Continue from Stage 1: <visible inherited state>.
Primary event: <one main action or state change>.
Camera: <shot and movement>.
Audio: <sound direction>.
End state: <visible result>.

[Maintain Consistency]
Keep <identity, clothing, prop ownership, object count, spatial layout, screen direction, camera axis, and voice> consistent.

[Negative Constraints]
Do not use <specific incidental reference content or likely failure>.
```

Omit empty sections. Do not add decorative adjectives or a generic negative-prompt dump. Prefer observable constraints: write `the florist still holds the bouquet in the left hand`, not `keep continuity perfect`.

## Direct dialogue, sound, and text plainly

- Put exact spoken dialogue in double quotes.
- Name the speaker, language or regional accent when relevant, and delivery before the quote.
- Describe music, ambience, and sound effects in plain prose.
- Describe on-screen text explicitly and quote the exact text.
- Do not rely on Dreamina-only punctuation conventions for dialogue, music, effects, or subtitles.

Example:

```text
Dialogue language: natural conversational American English. The presenter says calmly, "Let's begin."
Quiet ventilation continues underneath. A brass latch clicks once as the case opens. No music or subtitles.
```

## Apply the mode clause

### Edit or replace

Name `@Video1` as the sole editing master. State the exact target, time range, replacement reference, and preserved content. For a moving replacement, require the new subject or object to inherit every appearance, path, speed change, occlusion, interaction, and exit of the original. Keep the requested instance count explicit.

```text
[Edit Goal]
Edit @Video1. Replace only <original> with <target> from @Image1.

[Source Video Role]
@Video1 is the sole editing master for scene, action, timing, camera, cuts, occlusions, audio, and event order.

[Target Reference Role]
@Image1 defines only <target appearance, structure, and material>. Do not use its background or composition.

[Content to Preserve]
Except for the replacement, keep all people, props, environment, camera, cuts, dialogue, ambience, effects, timing, and event order from @Video1 unchanged.
```

### Forward extension

Make the first generated frame inherit the source video's last frame before describing new action. Lock pose and orientation, prop position and state, background relationships, camera and composition, lighting, and motion direction. Keep every subject as the same single instance; do not duplicate, split, or change part count.

### First and last frames

Use `image_url` for the start and `end_image_url` for the finish. State that the output begins exactly from the start image's observable composition and ends naturally at the end image's observable composition. Describe the intervening action without contradicting either boundary. Keep identity, object count, screen direction, and lighting logic compatible.

### Storyboard

State the panel reading order and that panels are consecutive shots, not simultaneous quadrants. Map subject identity separately from panel composition when different inputs control those roles. Preserve composition, screen direction, and action order; do not inherit storyboard line art unless requested.

### Blockout

Inherit only declared camera routes, timing, motion paths, subject positions, light changes, cuts, or edit rhythm. Replace primitive geometry, colors, low-detail materials, and labels explicitly. Define final subjects, environment, materials, lighting, and style.

## Execute carefully on fal

When execution is requested:

1. Search for the exact endpoint and inspect its current schema and pricing.
2. Upload local inputs and build ordered URL arrays from the registry.
3. Validate every prompt token against its array index.
4. Put duration, resolution, aspect ratio, `generate_audio` and, for reference-to-video, `task` in API fields. Respect task-specific coercion. Keep settings out of prompt prose unless they change the story structure.
5. Prefer queued execution for long outputs and jobs containing reference video.
6. Preserve the request ID. If polling times out, check the same job later; do not resubmit automatically.
7. Never fabricate a status, seed, result URL, or downloaded file.

A short 480p proof may reduce iteration cost, but suggest it rather than running it unless the user authorized a proof render.

## Validate before returning or submitting

Confirm all of the following:

- The endpoint matches the task.
- Every reference token uses exact fal syntax and points to an existing array slot.
- Array order, per-modality limits, combined durations, file constraints, and the 50-file total are valid.
- Every token maps to one named job with targeted leakage exclusions where needed.
- Identities, clothing, props, counts, ownership, camera axis, and voice cannot swap.
- Every stage has one primary change and a visible inheritable end state.
- Time ranges are consecutive, non-overlapping, achievable, and fit the API duration.
- Dialogue uses a named speaker and double quotes when exact speech matters.
- Editing names one source master, exact scope, timeline inheritance, and preserved content.
- Extension fully defines the last-frame-to-first-frame seam.
- No instruction contradicts a reference's assigned role.
- API-only settings are not buried in prompt prose.
- The live schema, not memory, determined execution fields and limits.

## Return the result

For prompt creation, return:

1. A short `Reference map` when two or more references are used.
2. One final prompt in a single plain-text code block.
3. Proposed fal endpoint and request settings.
4. A short `Assumptions` or `Watch-outs` note only when useful.

For an audit, return the corrected prompt plus a concise list of material fixes.

For execution, return the exact endpoint, submitted settings, request ID, output URL or file, returned seed, and submitted prompt.

Do not return competing variants unless requested. Do not expose private reasoning or a lengthy explanation of the formatting process.

## Primary sources and freshness

Technical snapshot checked 2026-10-13. Read the exact route's current schema and pricing before execution:

- [Text-to-video](https://fal.ai/models/bytedance/seedance-2.5/text-to-video/api)
- [Image-to-video](https://fal.ai/models/bytedance/seedance-2.5/image-to-video/api)
- [Reference, editing and extension](https://fal.ai/models/bytedance/seedance-2.5/reference-to-video/api)

These checks establish documented request fields, not measured quality or a guarantee of reference fidelity.
