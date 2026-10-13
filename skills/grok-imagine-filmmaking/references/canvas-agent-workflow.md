# Canvas / Agent Mode workflow

Use Canvas / Agent Mode as the main workspace for a multi-shot scene, recurring-character project, or cinematic sketch. It is not merely a prompt box: make it the place where the brief, reference set, storyboards, generated clips, and decisions remain visible together.

## Set up the canvas

Start a project/canvas and establish four clear working groups:

| Group | Contains |
| --- | --- |
| Locked references | identity, wardrobe, hero prop, location/style masters, approved voice decision |
| Plan | brief, script excerpt, shot list, continuity notes |
| Boards | static keyframes or storyboard panels, one per intended shot |
| Selects | approved animated clips, alternate takes, and assembly order |

Use labels, positions, colours, or names provided by the current UI to make these groups legible. Do not rely on spatial organization as the only record of an important decision; write the key invariant on the relevant card/note too.

## Start with a staged instruction

Give the agent the goal, the reference roles, and an approval gate before any heavy generation:

```text
Create a 30-second cinematic scene from the attached character, wardrobe, red-handbag, and location references.

First make a four-shot plan as text cards. Identify the exact role of every reference and state the continuity invariants.
Then create one still storyboard panel per shot. Do not animate anything until I approve the boards.
Keep the character's face, wardrobe, red handbag, location design, and visual treatment consistent throughout.
```

For a user who already has a shot plan, tell the agent to use it rather than asking it to invent a second plan.

## Full production path

1. Add or create the project brief and continuity bible.
2. Attach and label the identity, wardrobe, prop, location, and optional voice references.
3. Ask for a concise shot list before generating images. Keep a simple scene to two to four coverage setups.
4. Ask for static boards/keyframes. Correct continuity, wardrobe, composition, and screen direction here.
5. Approve only the boards worth animating; do not animate every panel by default.
6. Animate each approved panel with one principal action and one camera move. Use a new reference-guided generation for a new angle; use an extension only for continuous time in the same setup.
7. Review clips beside their corresponding boards. Promote the strongest result to Selects and retain alternatives only when they solve a different editorial problem.
8. Create an in-canvas draft assembly only if the current controls make it useful; otherwise export selects and cut externally.

## Reference instruction

At the start, state both the roles and the change boundary:

```text
Use the attached portrait as the character identity reference, the full-body image as the exact wardrobe reference, the close-up as the red handbag reference, and the environment image as the location and lighting master.

Across every board and clip, preserve the actress's identity, hairstyle, wardrobe, the handbag's colour/shape/handles, and the location's basic design. Change only action, performance, camera position, and shot-specific framing.
```

Re-state the relevant invariants whenever the agent begins a new shot or appears to drift. A Canvas project is organizational support, not evidence that the model has permanently trained on the references.

## Direct work at the right level

Use broad instructions for planning and targeted instructions for corrections.

| Goal | Good Canvas instruction |
| --- | --- |
| Tighten the scene | "Revise only the shot list: reduce it to three setups while retaining the discovery, line, and reaction." |
| Fix one board | "Regenerate only Board 2 as a tighter reverse medium close-up. Preserve all references and the scene's screen direction." |
| Animate selectively | "Animate Boards 1 and 3 only. Keep Board 2 as a still reaction insert." |
| Keep a good take | "Keep the selected clip unchanged; create one alternate take with a slower push-in and no other changes." |
| Recover a bad result | "Discard this variant from Selects. Rebuild the board from the identity, wardrobe, prop, and location masters; do not use the drifted clip as a reference." |

Change one major variable per revision: composition, performance, camera, prop, or lighting—not all at once.

## Canvas prompt templates

### Fiction scene

```text
Build a [length]-second [tone] scene from these references. Start with [brief event].
Create [number] storyboard panels with this coverage: [setup 1], [setup 2], [setup 3].
Use the continuity package already on the canvas. Keep [invariants].
Wait for approval after the storyboard stage, then animate only the approved panels.
```

### Fast social sketch

```text
Plan a [length]-second vertical sketch around [comic premise].
Create five compact boards, then identify the strongest three to animate.
Keep the avatar/recurring character, setting, and visual style consistent. Use simple cuts; do not attempt a long continuous story in one clip.
```

## Assemble and hand off

Use Canvas for visual planning, asset continuity, and rough sequencing. Use a non-linear editor for final timing, titles, music, sound replacement, subtitles, or any critical audio performance. Preserve the final board, selected clip, and prompt/continuity note for each shot so a later correction can be regenerated without rebuilding the project from memory.
