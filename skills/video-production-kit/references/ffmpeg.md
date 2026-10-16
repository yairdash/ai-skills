# FFmpeg operations

Use `node KIT/kit.mjs ffmpeg ...` and `... ffprobe ...` so configured paths are
available without changing machine-wide PATH. Standard binaries on PATH also
work. The wrapper inherits the caller's working directory; quote paths with spaces.

Inspect before editing:
```
ffprobe -v error -show_format -show_streams -of json input.mp4
```
Check audio presence, SAR, rotation, duration, frame rate and variable-rate
timestamps. Normalize to a chosen frame rate for deterministic composition.

Accurate re-encoded excerpt (10 seconds starting at 3):
```
ffmpeg -n -ss 3 -i input.mp4 -t 10 -map 0:v:0 -map 0:a:0? -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -movflags +faststart excerpt.mp4
```
Do not promise frame-accurate stream-copy cuts: keyframes constrain them.
For arbitrary EDLs prefer trim/atrim with setpts/asetpts and concat, using the
same boundaries for audio and video. Use Herk's tested retiming helpers for
word transcripts. Avoid applying loudnorm to every tiny segment separately.

Audio: use two-pass loudnorm for a delivery loudness requirement. Measure the
whole program first, then apply its measured values; LUFS target and channel
layout depend on the requested outlet. Inspect clipping and listen to cut joins.
Do not invent missing audio or duplicate streams to mask a duration mismatch.

Final container check and decode:
```
ffprobe -v error -show_format -show_streams -of json final.mp4
ffmpeg -v error -i final.mp4 -f null -
```
Inspect decoded frames at transitions and title holds. FFmpeg success alone
does not prove text readability, visual quality or an editorially good cut.
Sources: https://ffmpeg.org/ffmpeg.html and https://ffmpeg.org/ffmpeg-filters.html.
