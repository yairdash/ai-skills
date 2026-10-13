# Capability check — 13 October 2026

These are dated API notes. Check the exact current model and surface before execution or a technical recommendation; consumer UI controls and account access can differ.

| Route | Checked documentation |
| --- | --- |
| Image generation/editing | `grok-imagine-image-2.0`; 1K/2K; up to 5 source images for multi-image editing |
| General video | `grok-imagine-video-1.5`; text/image input, native audio, up to 15 seconds; up to 1080p depending on route |
| Reference-to-video | On 1.5: up to 14 reference images, 3 preset voices, up to 15 seconds and 720p. The older `grok-imagine-video` route has different limits. |
| Pinned frames with references | On 1.5, `image` supplies a first frame alongside references; `last_frame` and up to 4 `keyframes` can constrain later frames. Use the documented fields rather than treating a reference image as a first-frame lock. |
| Voice selection | Preset `voice_id` references; prompt tags `<AUDIO_0>` etc. User audio-file voice references are documented for trusted partners on request, not universal access. |
| Video editing | Checked route is `grok-imagine-video`; source up to 8.7 seconds, same duration/aspect ratio, capped at 720p. Do not assume the general 1.5 generation route accepts editing. |
| Extension | Checked route is `grok-imagine-video`; source 2–15 seconds, new portion 2–10 seconds; output inherits source aspect ratio/resolution capped at 720p. |
| Canvas / Agent workspace | Use only controls actually exposed in the user's live interface. This skill does not establish account access, permanent reference locks, saved-character tokens, stitching or specific templates. |

## Primary sources

- [Imagine overview and image editing](https://docs.x.ai/developers/model-capabilities/imagine)
- [Reference-to-video, voices and pinned frames](https://docs.x.ai/developers/model-capabilities/video/reference-to-video)
- [Video editing](https://docs.x.ai/developers/model-capabilities/video/editing)
- [Video extension](https://docs.x.ai/developers/model-capabilities/video/extension)

Product capabilities and pricing can change. These checks establish documented features, not measured identity, motion, dialogue or continuity performance.
