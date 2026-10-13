# Storyboards and comic/graphic-novel pages to video

## The safe claim

Wan 3.0 is documented to accept image references and native dialogue, and its official guide supports a multi-shot storyboard format with 4–6 second timestamped shots. This makes a comic/storyboard workflow practical.

It is **not** documented to automatically perform this exact conversion: read speech bubbles → omit them visually → speak their exact contents. Treat that as a testable interpretation workflow, not a one-click guarantee.

## Best-practice asset pack

| Asset | Preferred role | Why |
| --- | --- | --- |
| Cropped panel with the visual art intact | `Image 1`: composition/staging/style | Lets the model understand the intended moment without asking it to animate the whole page layout. |
| Same panel, cleaned of balloons/captions if possible | `first_frame` or `Image 2` | Prevents bubble/panel graphics from leaking into the result. |
| Character design/turnaround | `Image 3` | Protects face, costume and recurring visual signatures. |
| Prop/location reference | `Image 4` / `Image 5` | Protects the details most likely to drift. |
| Exact written dialogue as prompt text | Transcript, not image-only | Gives the audio system an explicit, reviewable source of truth. |
| Optional voice/motion reference | `Audio 1` / `Video 1` | Add only a narrow role: voice cadence, camera move, or choreography. |

If all you have is a single comic page, use it as `Image 1` and explicitly say “interpret as staging, not a literal page or frame.” For a dense page, crop the panels and make one shot per panel or one 2–3 panel sequence. This is a recommended reliability strategy, not a documented input limit.

## Panel-to-shot map before prompting

Make the model’s reading order explicit. Example:

| Panel | Visual beat | Screen treatment | Spoken line | Duration |
| --- | --- | --- | --- | --- |
| 1 | Mara sees the train lights | Wide, locked establishing shot | — | 0–4 sec |
| 2 | She grips the satchel | Medium close-up; slow push-in | Mara: “It’s early.” | 4–8 sec |
| 3 | The train enters frame | Reverse wide; slight handheld | Voice off-screen: “Then run.” | 8–12 sec |

The panel map prevents an attractive but incoherent montage. It also separates a speaker’s bubble from the exact spoken line.

## Production prompt: comic page → animated dialogue scene

```text
Create a 12-second audiovisual cinematic sequence inspired by the staging, colour palette and character design in Image 1. Interpret Image 1 as a storyboard/comic reference only, not as a literal page or visible frame. Image 2 is the clean character/wardrobe reference; Image 3 is the olive-green satchel reference.

0:00–0:04 — Wide static establishing shot. At a rain-dark rural station at dusk, Mara stands under the platform light holding the olive-green satchel. Train lights appear in the distance. Damp concrete, wind moves the coat hem.
0:04–0:08 — Medium close-up, very slow push-in. Preserve Mara’s face and coat from Image 2. She tightens her grip on the satchel, looks toward the approaching train and says quietly: "It’s early."
0:08–0:12 — Reverse medium-wide shot. The train rolls into frame; an unseen companion answers from behind camera: "Then run." Mara turns toward the sound.

Audio: rain and a distant train, low natural room tone, no music under the dialogue. Keep speakers distinguishable and lips natural when Mara speaks.

Output must contain no comic panels, gutters, page texture, panel numbers, speech bubbles, captions, subtitles, written dialogue, logos, UI, or other visible text. Do not reproduce Image 1 literally; turn its story beat into live cinematic space.
```

## One-panel proof prompt

Use this first when dialogue accuracy matters:

```text
Animate one 6-second cinematic shot from Image 1. Use Image 1 only for the character, staging and lighting; do not show the comic page itself. Tight medium close-up: [speaker] pauses, then says exactly: "[short line]." Keep the face visible and lips readable.

No speech bubbles, captions, subtitles, written words, panel borders, gutters, page texture, logos or UI. Natural [ambience]; no music.
```

## Iteration ladder

1. **Proof the visual interpretation** — 5–8 sec, no dialogue. Confirm it rejects panels/bubbles and keeps the character/prop.
2. **Proof one spoken line** — keep camera still or slow; listen for exact words and lip readability.
3. **Build panel/shot sequence** — use 4–6 sec beats. If one shot needs exact timing, generate it separately.
4. **Repair instead of restarting** — use video edit for an unwanted item/style/line, or extension only for the immediate adjacent beat.
5. **Post fallback** — if picture succeeds but dialogue fails, retain the picture and replace dialogue in editorial/audio post rather than throwing away the shot.

## QC checklist

- Does it read as cinematic space rather than a page being animated?
- Are gutters, panel borders, captions, balloons and unintended text absent?
- Is the correct speaker performing each exact line, with intelligible speech and reasonable lip sync?
- Did the actual visual beat, screen direction, prop and character identity survive?
- Does every cut/beat have one dominant action and one camera intention?
- If it is part of a sequence, do costume, prop condition, eyeline, screen direction, lighting and audio world match the prior shot?
