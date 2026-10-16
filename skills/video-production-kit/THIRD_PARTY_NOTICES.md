# Provenance and exclusions

- Herk: https://github.com/nateherkai/herk-edit-kit. MIT with brand exceptions;
  pipeline material retains its own explicit use permission. All license files
  are retained under vendor/herk/LICENSE and vendor/herk/licenses; also read
  vendor/herk/THIRD_PARTY_NOTICES.md. The original bytes of included files are
  preserved. Excluded: AIS assets, brand example DESIGN file, published projects,
  showcase videos and assistant configuration. Historical references may point
  at those excluded examples; retrieve upstream if needed for study, not reuse.
- HyperFrames reference skill documentation: https://github.com/heygen-com/hyperframes,
  Apache-2.0; retained at references/hyperframes/LICENSE. Runtime installed via
  Herk's locked npm dependencies. Only Markdown and the license are packaged
  from the newer snapshot; its helper code and auxiliary media are excluded.
  Use the complete Herk modules for execution. Some newer references may exceed locked CLI.
- GSAP: downloaded by npm, not included in the portable source ZIP. Its own
  license applies: https://gsap.com/community/standard-license/.
- Remotion engine: downloaded by npm, subject to https://www.remotion.dev/license.
  The official Remotion skills snapshot has no license file; its source is not
  redistributed here. Install the official Codex plugin on the destination.
- FFmpeg: no binaries bundled. Use a local or official linked build and its
  corresponding license: https://ffmpeg.org/download.html.
- No user footage, transcripts, models, API credentials, Windows fonts,
  node_modules, browser executables or machine-specific config is packaged.

sources.lock.json records upstream commits and original archive SHA-256 hashes.
PROVENANCE.json records the public adaptation and hashes of published files.
The public package excludes original archive locations and local configuration.
Newer HyperFrames SKILL.md entry files are named REFERENCE.md here so they
remain documentation rather than incomplete automatically discovered skills.
