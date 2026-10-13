# Prompting and reference workflows

## Asset roles before prompt writing

Create a short asset manifest first. Do not make the model infer why an asset exists.

| Asset | Give it one job | Prompt label in Model Studio |
| --- | --- | --- |
| Designed keyframe | Lock opening composition | `first_frame` (not a general reference) |
| End-state keyframe | Lock final composition | `last_frame` |
| Character turnaround/portrait | Identity, costume, hair | `Image 1` |
| Hero prop/product | Shape, material, color | `Image 2` |
| Location/style frame | Palette, atmosphere, production design | `Image 3` |
| Motion/camera clip | Camera path or choreography only | `Video 1` |
| Source clip | Preserve it except named edit or extension | `Video 1` |
| Voice/music/room-tone clip | Cadence, voice character, beat or sonic world | `Audio 1` |
| PDF/PPT/public page | Content brief; not exact final visual layout | `file` or `link` |

When a UI lets you arrange uploads, use a stable order and write it down. In Model Studio, image/video/audio numbering is separate, so `Image 1`, `Video 1`, and `Audio 1` can all exist in the same prompt.

## Prompt grammar

Use this order for a one-shot generation:

```text
[MODE AND GOAL]
[REFERENCE ROLES]
[SHOT / FRAMING]
[SUBJECTS AND NON-NEGOTIABLE APPEARANCE]
[SINGLE CLEAR ACTION]
[CAMERA MOVEMENT]
[LOCATION, LIGHT, ATMOSPHERE]
[AUDIO: dialogue, ambience, effects, music]
[PRESERVATION / EXCLUSION RULES]
```

Prefer concrete film language: `wide establishing shot`, `medium two-shot`, `tight close-up`, `slow dolly-in`, `locked tripod`, `gentle handheld`, `lateral tracking`, `orbit`, `rack focus`. Name one primary camera move per beat.

## Copy-ready prompt templates

### 1. First-frame image-to-video

```text
Animate the supplied first frame. Preserve the character’s face, costume, key prop, composition and visual style from the first frame.

Shot: [framing]. Action: [one physical or emotional beat]. Camera: [one camera movement]. Environment: [specific light, weather, background movement].

Audio: [no dialogue / Speaker name says: "short exact line"]. [ambient sound]. [one or two sound effects]. [music cue or no music].

Do not introduce extra characters, logos, captions, subtitles, visible text or an unexplained cut.
```

### 2. Multimodal reference-to-video: new scene

```text
Create a new [duration]-second cinematic scene. Image 1 is the character identity and wardrobe reference; Image 2 is the hero prop reference; Image 3 is the location/style reference. Video 1 supplies only the [camera move / action choreography]; Audio 1 supplies only the [voice tone / music texture].

Shot: [framing]. [Character] performs [one clear action] with [prop] in [location]. Preserve [the exact recurring features]. Camera [movement] while [background detail]. Lighting and palette: [specific choices].

Audio: [Speaker] says: "[short exact line]." [ambience]. [effects]. [music].

No visible text, captions, subtitles, logos, UI, borders, or unintended extra people. Do not copy the literal setting/identity from Video 1 unless stated above.
```

### 3. Multi-shot, native 12–24 second scene

Use this only when the intermediate shots may be interpretive. Make each beat 4–6 seconds and repeat anchors.

```text
Create a 16-second audiovisual sequence. Across every shot, preserve Character A: [identity/wardrobe], and the [hero prop] from Image 2. The scene is [location and visual style].

0:00–0:04 — Wide establishing shot. [action and camera].
0:04–0:08 — Medium shot. [next beat]. Character A says: "[short line]."
0:08–0:12 — Close-up. [reaction/prop beat].
0:12–0:16 — Medium/wide resolution. [ending composition].

Audio: [speaker attribution], [ambience], [effects], [music]. No on-screen subtitles, captions, logos, or visible text.
```

### 4. Reference audio as performance guide

```text
Image 1 is the speaker’s identity. Audio 1 is a voice-performance reference only: use its calm, low, intimate cadence, not any unintended background content.

Tight medium close-up. The speaker looks just off camera, takes a small breath, then says: "[exact short line]." Natural blink, small head movement and restrained expression. Camera makes a very slow push-in. Warm lamp light, rain against the window.

No subtitles, no visible written words, no music over the line; keep the face clearly readable during speech.
```

## Native dialogue rules

- Attribute each line to a named speaker and quote it. Keep dialogue brief enough for the chosen duration.
- Put the speaking face in a readable medium-close/close shot; do not ask for a whip-pan or cut during a critical line.
- Describe voice mood and sound layers separately. Example: `Audio: Maya speaks quietly but clearly; distant traffic; one soft kettle click; no music.`
- Native dialogue is a valuable generation target, not a contract for exact spelling, accent, timing or lip sync. For material where every word is legally/editorially fixed, reserve post dubbing or an edit pass.

## Files and public webpages

Use one document or one public, no-login webpage only for high-level content/reference. Give it a film brief that says what to extract and what not to reproduce literally.

```text
Using the supplied presentation only as the factual source, create a 20-second product-film concept. Extract [three facts]; do not reproduce slide layouts, logos, small text, tables or charts literally. Build a visual story with [visual direction] and [voiceover text].
```

Never use a private / login-gated link as if the model can access it.
