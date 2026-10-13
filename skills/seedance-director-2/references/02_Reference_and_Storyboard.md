# 02 — Reference & Storyboard

This stage runs only when the user did **not** provide a reference (Axis A = "generate one"). When actual image creation is requested and the tool is available, output a **rendered image**; honor explicit text-only requests. Use the structures below internally to drive the image generation, then render the actual image.

**Execution rule:** render an image only when the user requested image creation. Story approval alone does not authorize a render. Honor text-only requests. When rendering an action grid, check that the requested motion annotations appear; if they do not, explain the defect and make at most one corrective retry within the authorized scope. If a tool is unavailable or fails, provide the complete image prompt and report the limitation. Never imply an image was created when it was not.

Pick the reference type by the job:
- **9-pose action grid** — for a single, continuous, choreographed action where body mechanics and phase-by-phase motion must be locked. Treat this as a working choreography-reference method; do not present format support as an independently verified model guarantee.
- **Start frame** — for a scene built from an idea, where the video is directed from an opening image rather than a motion sequence.

Editing (continuous vs multi-shot) is decided separately in doc `03`. Either reference type can feed either editing mode.

---

## A. 9-Pose Action Grid

Internal prompt structure:

> create 9 poses of `<the action>` with a unique and stylized character `<attach/preserve the character image if provided>` in a grid. **Overlay clear motion-direction annotations directly on the poses: arrows for movement and force direction, motion trails, weight-shift indicators, contact points, balance line, spin/rotation axis, and short timing/performance notes.** in a 1x1 aspect ratio.

Rules:
- When actual image creation was requested, render using the structure above internally; for a text-only request return the complete image prompt.
- **9 distinct poses**, each a different phase of the action — not minor variations of the same pose.
- If the user gave only an action, invent a strong, unique stylized character that fits it.
- If the user gave a character image, preserve identity, costume logic, body type, attitude, and visual style as much as possible.
- **Motion annotations are mandatory, not optional.** Every action grid must render visible on-image guidance — arrows, movement trails, body-mechanics notes, timing cues, force direction, weight shift, contact point, balance line, spin/rotation axis, performance instruction. For a **dynamic continuous action**, a grid with poses but no annotations is a defective output — follow the bounded corrective retry rule above. The board must read like a coached choreography sheet, not a plain pose gallery.
- Square, **1:1** aspect ratio.
- The result should read like a professional action-reference board for animation, choreography, cinematic blocking, or video generation.

**Important:** these overlays (arrows, trails, numbers, notes) are for the reference only. In the video prompt, the grid gets an `@Image` role line that limits it to the pose sequence and explicitly excludes the grid layout and all annotations — the focused reference-role exclusion pattern in doc `04`. The role line is itself a targeted exclusion, not a separate guaranteed mechanism. Inspect results for overlay leakage. Assign identity to the grid only if intended; otherwise use the separate character reference.

### Fallback — if image generation fails
Image generation sometimes fails in this environment. If a render doesn't succeed after a retry, do **not** stay silent or pretend an image was made. Instead:
1. Tell the user plainly that the image generation isn't going through right now.
2. Give a **complete, self-contained image prompt in English** that the user can paste into any other image generator (Midjourney, another GPT, etc.) to produce the grid themselves.

This fallback prompt is different from the short internal prompt above — it must stand on its own with no prior context, spelling out: the 9 distinct action phases, the character (full identity/costume/style, or the invented one), the **motion annotations as explicit written instructions** (arrows for movement and force direction, motion trails, weight-shift, contact points, balance line, spin axis, timing notes), and `1:1 aspect ratio`. State clearly that it's a prompt for an **image** generator (not video), and that the annotations should be drawn on the poses.

---

## B. Start Frame (scene from an idea)

When there is no action grid and no user image — the job is a directed scene from a concept — create a single cinematic **opening frame** only when the user requests image creation; otherwise supply an opening-image prompt that establishes subject, environment, light, and mood. This frame becomes the start image the video prompt in doc `03` directs from.

Rules:
- For authorized image creation, render one strong cinematic frame (not a grid).
- Match aspect ratio to the intended video; default 16:9 unless the user specifies otherwise. (Verify the selected platform’s aspect-ratio behavior where needed; compose the frame for the intended output.)
- Establish clear motion potential: posture, spatial depth, tension, light direction — so the requested action can begin naturally.
- No overlays, arrows, or notes on a start frame.

---

## User-provided reference sets
When the user brings their own materials — character images, multiple views of a product, a motion video, audio — this doc's generation stage is skipped, but the materials still need discipline: map multi-reference materials one-to-one per doc 04. Add exclusions only for a concrete risk of leakage. Simple opening-image and separately bound voice-sample prompts remain clean without tags. Use distinct views when useful without assuming a numeric threshold.

## Missing information
If something essential is missing (exact action, character type/identity, character style, or scene concept), ask for a preference. If there's enough to proceed, make a strong creative choice and continue — don't over-ask.
