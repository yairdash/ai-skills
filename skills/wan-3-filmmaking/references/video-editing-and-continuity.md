# Video-to-video, extension, and continuity

Wan 3.0’s all-in-one reference mechanism can use `Video 1` as a motion reference, a source video to edit, or a source video to extend. The verbs and preservation boundary decide the job.

## 1. Instructional video edit

Use when the source clip’s timing, performance and camera are mostly valuable.

```text
Edit Video 1. Replace only the red canvas backpack with the olive-green leather satchel from Image 1. Keep the actor’s identity, body performance, hand positions, timing, camera movement, background, lighting and existing audio unchanged. The satchel must remain physically attached to the actor’s shoulder throughout; no cutout edge or geometry changes.
```

Useful edit verbs: `edit Video 1`, `remove`, `replace`, `change to`, `add`. Name **what changes**, then list **what must remain**.

### Common repairs

| Problem | Better instruction |
| --- | --- |
| It reimagines the whole shot | “Change only [target]. Everything else in Video 1 remains unchanged.” |
| Added object floats/does not interact | Specify contact point, hand/body interaction, occlusion, light direction and persistence. |
| Character changes | Include a character identity reference and say “preserve the performer in Video 1.” |
| Dialogue change fails | Request the visual edit separately first, then a dedicated dialogue-edit pass / post dub. |

## 2. Motion or camera reference—not an edit

Use when a clip gives useful rhythm/choreography but the resulting scene is new.

```text
Create a new scene with Character A from Image 1 in the alleyway from Image 2. Use Video 1 only as a reference for the slow 180-degree orbiting camera move and the timing of the turn. Do not copy Video 1’s person, wardrobe, setting, colour palette, or visible objects.
```

This is the safer choice for a new shot or a new angle. Do not write “edit Video 1” if you want a different scene.

## 3. Video extension

Use when the desired next beat begins at the existing first/last frame. Model Studio documents forward, backward and bidirectional extension; the input plus output must total no more than 30 seconds.

```text
Extend Video 1 with 6 seconds of preceding content, ending exactly on its original first frame (called forward extension in the checked Model Studio guide). Maintain the existing lens, camera height, lighting, character identity, wardrobe, location and ambient sound. Before the supplied clip begins, the character finishes folding the map, places it into the same satchel, looks toward the approaching train light, then turns into the exact opening posture of Video 1. No new characters or cuts.
```

The checked Model Studio guide calls preceding content `forward` and subsequent content `backward`; other providers may use the opposite labels. Always state before/after explicitly and identify whether the new segment ends on the original first frame or starts from the original last frame. Verify the current provider wording before execution. The guide describes target output duration as the final combined clip; check its current duration constraints rather than adding source duration twice.

### Do not use extension when

- you need a new camera angle;
- the next shot must move to a different location/time;
- the visible end frame does not contain the character/prop that needs to carry over;
- you need an exact, separately art-directed end composition.

Use reference-to-video or first/last-frame instead and reattach identity/location/prop references.

## Continuity packet for multi-clip work

Keep this text with the project and repeat the relevant pieces in every prompt:

```text
CHARACTER A — [face/hair/age range], [wardrobe], [distinguishing mark], [emotional state].
HERO PROP — [shape/material/colour/condition]; held [where/how].
LOCATION — [place], [time of day], [weather], [lighting], [palette].
CAMERA / LENS FEEL — [shot size, movement, handheld/tripod].
AUDIO WORLD — [language/voice mood], [room tone], [recurring music/SFX rule].
PREVIOUS TAKE END — [final pose, screen direction, object state].
NEXT TAKE GOAL — [one action and ending image].
```

Suggest a low-cost proof when useful and run it only if authorized; save any authorized output and still frames before moving to a separately authorized longer/higher-resolution job. Do not depend on a previous job URL alone—save a local copy before the documented URL expiry.
