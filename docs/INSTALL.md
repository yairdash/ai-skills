# Install and use a skill

Use an agent with network access, file access and the required tools. Node.js/npm is needed for the Skills CLI. See the [upstream CLI documentation](https://github.com/vercel-labs/skills).

## Choose a catalog entry

Read `catalog.json`. Check its requirements, source, review status and compatibility evidence. Do not install every skill just to solve one task.

For a hosted entry, install from the `skills/<name>` URL in its record. For an external entry, use its `source.url`. For either, first inspect the available skills:

```sh
npx skills add <source-url> --list
```

Then install the selected frontmatter name to the current project, for example:

```sh
npx skills add <source-url> --skill <frontmatter-name> --agent codex --copy
```

Replace `codex` with a supported target agent such as `claude-code` or `cursor`. Project-local is the default; add `--global` only when the user requests a user-wide install. Use `--copy` to avoid symlink limitations on Windows. Do not run the command with literal angle-bracket placeholders.

External catalog entries point to reviewed commit revisions. Use the complete URL from the catalog, including its commit SHA. Hosted entries track this repository's main branch; resolve and record its current commit before installation when reproducibility is needed. For example, this installs the original historical prose critique skill:

```sh
npx skills add https://github.com/haowjy/creative-writing-skills/tree/5b12a118445619be5ef4591440a47baf6cacc662/skills/prose-critique --skill prose-critique --agent codex --copy
```

This exact pinned source was installed successfully in an isolated Codex project. Installation checks verify files; they do not verify every runtime feature. The library contains both hosted skills and external links; give the library URL to an agent to select an entry, then install from that entry's source URL.

## Hosted model and video-post skills

Choose `seedance-director-2` for creative direction, or `fal-seedance-2-5` for fal-specific request construction and reference syntax. They can complement each other; the live fal schema controls technical execution. `grok-imagine-filmmaking` and `wan-3-filmmaking` target their respective providers. `x-video-packaging` drafts post copy from an inspected clip or a clearly labeled description.

For example, install only the directing skill:

```sh
npx skills add https://github.com/yairdash/ai-skills --skill seedance-director-2 --agent codex --copy
```

The complete folder includes the referenced documents and provenance. Media APIs, image tools and account access are not installed by this command. See [model skill notes](MODEL-SKILLS.he.md).

If a required sibling skill or shared runtime is missing, install the documented dependency or use the source project's installation instructions. Some catalogs contain recipes for a whole application rather than independently runnable skills.

## Hosted H3 workflow

Install `develop-h3-parody-shorts` from this repository, then install its companion `h3-prompt-writing` using the pinned external URL in the catalog. The public workflow includes its Python validator and tests; it does not include private production observations or media. Resolve `scripts/` relative to the installed skill folder. No media generation is needed to run the validators.

## Private sources

Use the same flow while signed in through an authorized Git credential helper or GitHub CLI. Never paste tokens into chat, command URLs, catalog entries or committed files. An authenticated GitHub connector does not necessarily authenticate local Git or the browser.

## Manual fallback

Download the complete skill folder, including references, scripts and assets, into the target agent's documented skill directory. Do not download only SKILL.md when it references other files. Preserve the prior installation before replacing anything.

## Chat-only use

An agent able to fetch the URL may read the instructions and necessary references for this conversation. That does not install a persistent skill, grant missing tools or make desktop scripts work in the cloud. Check `docs/WORK.he.md`.

## After installation

Check the installed files, ask the target agent to use the skill on a small example and record source revision and outcome. Confirm that real runtime dependencies work before labeling a skill tested.
