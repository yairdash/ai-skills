# Wan 3.0 capability map

Original notes: 2026-09-03; core modes and media limits rechecked against the linked Alibaba guide on 2026-10-13. Not all examples or model-performance claims have been independently tested. This file uses Alibaba Cloud Model Studio’s Wan 3.0 documentation as the source of truth. A third-party Wan interface can expose fewer controls, different pricing, or a different model version.

## Bottom line: comparable to the H3 comic workflow?

**Yes, in feature coverage.** Wan 3.0 can make a reference-led audiovisual clip, accept images, video and audio together, use a first or first/last frame, edit a supplied video, and extend it. It also supports native dialogue/audio and up to 30 seconds, so it is a strong candidate for a comic-page-to-animated-sequence workflow.

**But the critical comic trick is not verified as automatic.** Alibaba documents image references and native dialogue, but does not document a feature that reliably reads a graphic-novel page’s speech bubbles, removes them from the output, and performs their wording. Use the page as visual/staging reference and repeat the exact dialogue in the prompt. Test one short panel first; see `storyboard-and-comic-to-video.md`.

## Documented Model Studio capability matrix

| Goal | Wan 3.0 route | Key documented control |
| --- | --- | --- |
| New clip | Text-to-video | Prompt only; 2–30 sec, 480P/720P/1080P, 30 fps |
| Animate a designed still | First-frame image-to-video | `first_frame`; adaptive ratio recommended |
| Bridge two locked designs | First/last-frame video | `first_frame` + `last_frame` |
| Recurring characters, props, style, shot/motion, voice/music | All-in-one multimodal reference | Up to 10 reference images, 5 videos, 5 audios; 20 total reference assets |
| Video-to-video edit | Reference video + explicit edit intent | Add/remove/replace, style/lighting, dialogue, reference-driven edits |
| Continue a shot | Reference video + explicit extension intent | Forward, backward, or bidirectional extension; input + output total ≤30 sec |
| Turn a brief/deck/article into a video | One file or one public web link | Files/web link are a separate reference type; public link must not require login |
| Spoken performance | Native audiovisual output; optional audio reference | Dialogue, ambience, BGM and effects can be generated; source audio can guide sync/tone |

The Model Studio guide says to refer to media by type-specific index: the first `reference_image` is `Image 1`, the first `reference_video` is `Video 1`, and the first `reference_audio` is `Audio 1`. Their indices do not collide.

## Mode-selection rule

| If the creative intention is… | Use… | Do not use… |
| --- | --- | --- |
| “Bring this exact designed image to life.” | first-frame I2V | a loose style reference as a substitute for the first frame |
| “Move visibly from this composition to that composition.” | first/last-frame I2V | an extension; it continues a clip, not a new endpoint plan |
| “Same hero/prop, new camera/setting/action.” | multimodal reference-to-video | an edit, unless you want to preserve an existing clip’s timing/action |
| “Keep this video; change a specific thing.” | video editing | a generic reference-led generation |
| “Continue immediately before/after this shot.” | video extension | a new reference-led shot with a new viewpoint |
| “Borrow the camera move or choreography only.” | reference video with a narrow role statement | a source edit without saying what should change |

## Strengths

- **One model, broad asset grammar.** It can combine character, prop, location/style, action/camera and audio references in the same generation.
- **Longer native unit.** A 2–30 second shot with 30 fps and native sound is useful for a whole dialogue beat or a short multi-shot micro-scene.
- **Directed audiovisual storytelling.** Official docs specifically describe time-coded multi-shot prompts, native dialogue, music and effects.
- **Practical finishing tools.** Instructional video edit and forward/backward/bidirectional extension make it possible to repair or continue a successful take instead of restarting every time.
- **Useful non-media input.** A single PDF/PPT/etc. or public webpage can serve as a creative brief/reference, useful for concept films or product work.

## Limits and risk controls

| Risk | Working response |
| --- | --- |
| Very new model / limited independent field evidence | Treat claims of “perfect” identity, text, physics or lip sync as hypotheses. Suggest a short 5–8 second proof before a long generation; execute it only if the user authorized it. |
| Provider mismatch | Identify the UI/API. The published Model Studio limits and modes may not appear in another Wan surface. |
| Reference overload | Assign one role per asset and label it. Start with 1 character + 1 scene/style + 1 motion/audio asset; add only when a control is missing. |
| Exact speech wording or multilingual delivery | Attribute short quoted lines to the speaker, keep the face visible, listen and transcribe the render. Plan a post-dub/re-edit fallback for critical copy. |
| Comic page text/borders appear in output | Use clean cropped art/first frame if possible; treat page as reference; say no panels/gutters/bubbles/captions/subtitles/visible text; include a transcript separately. |
| Long multi-shot drift | Use 4–6 sec beats, repeat identity/wardrobe/prop anchors at every beat, and split into separate shots if one beat must be exact. |
| “Edit” turns into a rewrite | Name the target, edit action, and preservation boundary: “Change only X. Keep performance, timing, camera, background and audio unchanged.” |
| More than 30 sec | Generate/extend in coherent sections, save best end frames and use a continuity packet for the next section. |

## Sources

- [Alibaba Cloud: Wan3.0 Video Generation guide](https://help.aliyun.com/en/model-studio/wan3-video-generation-guide) — authoritative capability, media-limit, prompt, editing and extension documentation.
- [Alibaba Cloud: Video generation and editing model comparison](https://help.aliyun.com/en/model-studio/video-generate-edit-model/) — model routes and output specifications.
- [Alibaba Cloud: model pricing](https://help.aliyun.com/en/model-studio/model-pricing) — current regional availability/pricing context; check before production because it changes.
