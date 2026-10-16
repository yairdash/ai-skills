# Remotion production

Prefer the official installed Remotion plugin and its create/markup/render/
captions skills. Official upstream: https://github.com/remotion-dev/skills.
The source snapshot has no LICENSE file; it is preserved in the repository
archive but not redistributed in this kit. On another computer install the
official plugin. The following original recipe works without that plugin.

The neutral starter in templates/remotion pins all Remotion packages to
4.0.536. `node KIT/kit.mjs setup-remotion` installs it under runtime/remotion.
`node KIT/kit.mjs remotion studio --no-open` opens an editable composition.
`node KIT/kit.mjs remotion render src/index.tsx KitSmoke out/smoke.mp4`
exports the two-second smoke composition. This is a runtime test, not a design
template or a copy of the user's earlier project.

Animate from useCurrentFrame(), interpolate(), spring() and useVideoConfig();
avoid CSS animations, random values and wall-clock timing. Each named scene
gets its own component; register the full composition and useful scene views.
Keep fps, durationInFrames and dimensions explicit. Use local media and fonts
with redistribution rights. For bundled media use staticFile().

Start Studio early and verify the actual preview. Render when the user asks
for an export or finished video. Inspect rendered frames and decode the MP4.
Use supported Chrome Headless Shell; `remotion browser ensure` installs it.
Do not diagnose Edge-launch failure as an animation-code error.
Keep Remotion, @remotion/cli and other @remotion/* packages on one version.

The engine has its own terms: https://www.remotion.dev/license.
The portable kit includes original sample source and dependency lockfiles,
not a license to third-party fonts, footage, or the Remotion engine itself.
