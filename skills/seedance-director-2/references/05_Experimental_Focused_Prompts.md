# Experimental addition: focused four-layer prompts

Status: active experiment, added 2026-09-19. Based on user-reported improvement in the pirate shot and a short transformation prompt, not a proven rule for all models or scenes. Keep this guidance isolated here so it can be removed without rewriting the base skill.

## Scope and integration

Prefer this compact approach for short image-to-video shots, especially continuous takes. Retain the base skill's reference roles, directing intent, causality, continuity and duration discipline. Read docs 03 and 04 as required. Do not impose four headings on every delivered prompt, or compress complex dialogue, editing, extensions or longer sequences until essential information is lost.

Treat the four layers as writing decisions, not mandatory filler. Include only instructions that materially affect the intended result. Use natural English, clear verbs and affirmative directions. Keep generation duration outside the prompt. Describe changes rather than redescribing the supplied image.

## Four layers

1. **Action and local performance.** Identify who acts; write in the present tense. Attach manner (how the action is performed), pace, weight or emotion directly to the relevant action when it matters: “He smugly lights the fuse,” “He flails in panic and lands heavily.” Express cause and consequence in the action sequence itself. Include the complete story and ending here. A falling hat that delivers the joke is a story action, not optional background decoration. Avoid adding extra business merely to fill the shot.
2. **Camera and destination.** State the camera movement, what must remain readable, and, only when important, the ending position or framing. For a static camera, state that simply. The camera serves the action; avoid adding motion solely to make the prompt sound cinematic.
3. **Overall direction and acting.** Optionally use one short line for genre, tone, acting scale and overall physical quality when it adds control. Distinguish this from the local performance already embedded in the verbs. Prefer a coherent intention such as genuine fear or broad slapstick over a compulsory catalogue of facial movements. Use explicit expressions when requested or useful; do not ban them.
4. **Movement style.** Add a short, concrete description of how motion behaves across the shot: realistic, elastic cartoon animation, held stop-motion poses, choppy transitions, etc. Genre and motion style are independent: slapstick can be realistic, cartoony or stop motion. Keep this layer short so it does not overwhelm the action. “8 fps” may describe simulated stop-motion cadence; it is not a requested output frame-rate setting.

## Delivery and assembly

For a normal final prompt, provide the complete integrated prompt without section headings unless the user asks for a breakdown. Keep the base order: role lines when multi-reference work requires them, an optional concise directing header, then camera/action and the short motion-style clause where relevant. The four-layer teaching order is not a replacement for required reference or technical structure. A brief “One continuous shot” can establish shot structure in an action-only test; do not force a genre into its baseline.

When demonstrating cumulative tests, present four separately editable layers in this order: complete action, camera, overall direction/acting, movement style. Each successive test retains the entire story and adds only the next layer. Assemble the complete version with overall direction as the header and camera before action. Keep image and duration consistent across variants unless explicitly testing either. Add environment or sound only when needed; do not automatically create extra layers for them.

For corrections, return the full revised prompt by default, unless the user explicitly requests only the changed fragment. Remove conflicting older instructions throughout the full prompt.

## Focus check

- Is the central action unmistakable, with a clear subject and consequence?
- Are important pace and acting cues attached to their actions?
- Does each sentence contribute without duplicating another layer?
- If a motion must persist, does the action sustain it before, during and after the change? Repeat only where needed for continuity; avoid adding competing stabilization or interruption instructions.
- Are camera destination and visibility compatible with the action?
- Are style and overall acting concise and consistent with local performance?
- When diagnosing results, change one layer at a time. Treat shorter wording as a working hypothesis, not a guarantee.

## Example: four teaching layers

**Action:** One continuous shot. The pirate smugly lights the fuse and watches it burn. The cannon fires; the blast of air throws him away from the cannon and blows his hat upward. The cannon stays in place, clear of his body. He flails in panic and lands heavily on his backside. A beat later, his hat drops onto his face.

**Camera:** Slow arc dolly in, ending closer to the fallen pirate while keeping his whole body, the cannon and the falling hat visible.

**Overall direction:** Slapstick comedy with broad physical acting, convincing weight and a deadpan finish.

**Movement style:** Choppy, staccato stop motion. Frame by frame, 8 fps.

This example does not supply an attachment: add role mapping only when the selected reference mode requires it. Do not transfer its pirate content or stop-motion style into unrelated shots.
