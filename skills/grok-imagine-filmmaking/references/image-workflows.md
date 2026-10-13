# Image workflows

Use Grok Imagine still generation to make identity sheets, wardrobe/prop masters, location masters, and start images for video. Use image editing when a successful frame needs one constrained correction rather than a complete reinvention.

## Generate a master still

Order the prompt by importance:

```text
[subject and pose]
[environment and essential objects]
[lighting and atmosphere]
[framing / lens / viewpoint]
[material, style, or finish]
[constraints]
```

Example:

```text
NOA stands on the wet abandoned metro platform holding the matte-black ORBITAL case, looking back toward camera.
Green tiled columns, cool fluorescent practicals, faint haze, wet reflections.
Shoulder-height medium shot, 50mm feeling, restrained cinematic realism.
The case has one centred white ORBITAL logo; no extra bags or people.
```

## Build reference-ready images

For identity, use a clear face, simple expression, even light, and unobtrusive background. For wardrobe, include enough of the body to record silhouette and key details. For a hero prop, use a clean, readable angle. Avoid trying to make a highly dramatic still do every job.

## Edit a still

Make one major correction at a time. Start with the base image, list critical invariants, then state the single edit.

```text
Use the attached image as the base.

PRESERVE EXACTLY: NOA's facial identity, dark shoulder-length curls, charcoal bomber jacket, black ORBITAL case, camera angle, and existing lighting direction.

CHANGE ONLY: replace the background with the established green-tile metro platform at night. Keep the character's pose and expression unchanged.
```

For a multi-reference composite, assign roles explicitly:

```text
Use <IMAGE_0> for exact facial identity, <IMAGE_1> for the charcoal bomber wardrobe, and <IMAGE_2> for the ORBITAL case. Create a shoulder-height medium shot on the metro platform. Preserve each named reference only in its assigned role.
```

## Quality check before video

- Is the face clear enough to use as identity evidence?
- Are wardrobe silhouette and prop geometry unambiguous?
- Does the keyframe already contain the desired production design and first composition?
- Is there any accidental extra object, unreadable text, or hand error that will amplify in video?

If not, make the smallest viable edit before animating. Repeated heavy edits may soften or drift the frame; start from the strongest clean master rather than repeatedly editing an already compromised output.
