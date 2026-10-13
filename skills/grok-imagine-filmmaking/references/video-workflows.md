# Video workflows

Select the mode by the continuity problem, not by which button happens to be visible first. Confirm current UI/API availability in `capabilities-and-version-check.md` when a specific limit matters.

## Mode choice

| Need | Preferred approach |
| --- | --- |
| Explore a new idea quickly | Text-to-video |
| Preserve an exact first composition | Image-to-video from an approved start image |
| Keep a person, outfit, prop, or style while changing action/angle | Reference-to-video |
| Modify a finished short clip | Video edit |
| Continue the same shot in time | Video extension |

Reference images alone guide the result without locking the first frame. On the documented 1.5 API, combine references with the dedicated pinned-frame fields when needed; verify availability in the actual UI before recommending that route.

## Prompt structure

Write compact, chronological prose:

```text
[who / what] [does one clear action].
[single camera position and move].
[environment, lighting, and pace].
[spoken line or key sound, if any].
[continuity block].
```

Example:

```text
NOA walks left to right across the established metro platform, holding the ORBITAL case. At the end of the walk she looks once over her right shoulder.
Slow handheld tracking shot at shoulder height; restrained motion, 50mm feeling.
Cool fluorescent practical light, wet reflections, faint haze.
Preserve her exact identity, charcoal bomber jacket, the matte-black case, and the existing station design. Change only the blocking and camera position.
```

Keep a generated clip to one principal beat. A short reaction after a line is normally safer than a second unrelated action.

## Dialogue and voice

Use native dialogue only when the specific workflow supports it. Tie the speaking person and selected voice reference together explicitly:

```text
The person from <IMAGE_0> addresses camera using <AUDIO_0>.
She says: "You weren't supposed to find this place."
After the line, hold on a silent, wary reaction.
```

For recurring speakers, keep the same selected voice and writing register across clips. For a highly critical performance, plan an external final dialogue pass as a contingency. Do not imply that a user-supplied audio clip is available as a general voice reference unless the user's account/workflow has confirmed it.

## Camera language

Use one unambiguous primary instruction: `locked-off medium shot`, `slow push-in`, `slow pull-back`, `handheld tracking`, or `slow orbit`. Add only one framing term and one move. Do not ask for rapid cuts inside a single generation; generate coverage as separate clips.

## Initial troubleshooting

| Failure | First correction |
| --- | --- |
| Face/wardrobe drift | Reduce to role-specific reference images; make invariants explicit |
| Weak action | Put the action in the first sentence and remove competing beats |
| Camera ignores direction | Reduce the action to one beat and name only one camera move |
| Opening frame is wrong | Use image-to-video from an approved start image |
| Dialogue is present but unclear | Shorten the line, simplify staging, and leave a short reaction hold |
