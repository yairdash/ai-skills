# HyperFrames motion graphics

Use the Herk-locked runtime through `node KIT/kit.mjs hyperframes ...` from the
composition folder. Load vendor/herk/.agents/skills/hyperframes/SKILL.md and
the relevant GSAP and CLI modules first. The current upstream references in
references/hyperframes/skills are also saved with their Apache-2.0 license;
they can describe newer features. Check installed CLI `--help` before using
new commands. Do not silently upgrade a working project's lockfile.

Create a neutral starter: `node KIT/kit.mjs herk scripts/new-video.mjs my-video`.
Then change directory to KIT/runtime/herk/video-projects/my-video:
```
node KIT/kit.mjs hyperframes lint
node KIT/kit.mjs hyperframes preview
node KIT/kit.mjs hyperframes render --quality draft --output renders/draft.mp4
```
Read the reported preview URL; inspect it before a production render. A setup
smoke render is already authorized by a request to verify the installation.

Root visible div: id, data-composition-id, data-start, data-duration,
data-width, data-height. Timed clips have data-start, data-duration and
data-track-index. Avoid same-track overlap. Register a synchronous paused,
finite GSAP timeline at window.__timelines[compositionId]. Let HyperFrames
own media playback; mute visual video and mix its sibling audio once.
Use local assets and fonts for reproducible timing. Carry their licenses.

Browser: `node KIT/kit.mjs hyperframes browser ensure` downloads the supported
Chrome Headless Shell when absent. An existing supported binary can be set
with `configure browser ABSOLUTE_EXECUTABLE_PATH`; do not assume Edge works.
Docker is optional for the local renderer. doctor --json may exit zero while
reporting failed checks; read its checks, distinguishing optional services.
Sandbox loopback/Chrome restrictions may require an approved escalated render;
they do not prove that a composition or GPU is broken.
