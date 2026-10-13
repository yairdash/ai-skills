# Production foundations

Use this file at the start of a project or whenever continuity repeatedly fails.

## Project brief

Keep the brief compact enough to use while prompting:

```text
TITLE:
LOGLINE / PURPOSE:
FORMAT: aspect ratio, target duration, delivery platform
TONE AND VISUAL TREATMENT:
CAST: recurring characters and who speaks
PERSISTENT ASSETS: wardrobe, props, locations, graphic elements
SHOT CONSTRAINTS: e.g. two people maximum, no cuts inside a generation
AUDIO: native dialogue, generated ambience, or external post
```

## Continuity bible

Create a short record for every recurring item. Use stable visual descriptions, approved files, and roles—not an invented platform character token.

```text
CHARACTER: NOA — protagonist
IDENTITY REF: NOA_identity_v03 (clean 3/4 portrait)
WARDROBE REF: NOA_jacket_v02 (full body)
FIXED APPEARANCE: dark shoulder-length curls, charcoal bomber, silver chain
HERO PROP: ORBITAL case — matte black, white logo centred on lid
LOCATION: Metro Platform A — green tiles, wet floor, cool fluorescent practicals
VOICE: chosen built-in voice / separately produced voice; confirm availability
```

Use one dedicated reference per role where possible. A clean face reference and a separate full-body wardrobe reference normally give the model clearer instructions than several near-identical portraits.

## Reference package by task

| Task | Minimum useful package |
| --- | --- |
| First appearance | identity + wardrobe + optional location/style master |
| New angle of the same character | identity + wardrobe + hero prop if visible |
| Product/hero object shot | object master + location or style reference |
| Exact opening composition | approved start image |
| Dialogue performance | identity reference + chosen voice option, if available |

## Naming and selection

Use a simple, chronological naming pattern: `project_character_asset_or_shot_v##`.

Examples: `noa_identity_v03`, `orbital_case_v02`, `metro_platform_master_v01`, `noa_sh03_mcu_v04`.

Promote a new output into the reference package only after checking face, wardrobe, prop design, and lighting treatment. Keep the former approved version available; a new frame can be better for pose but worse for identity.

## Continuity block

Use this block after the shot action. Replace the bracketed items; do not list irrelevant assets.

```text
REFERENCE ROLES
<IMAGE_0> is [NAME]'s identity reference.
<IMAGE_1> is the exact [wardrobe / hero prop / location] reference.

PRESERVE
Keep [identity details], [wardrobe details], [prop design], and the established [location / visual treatment].

CHANGE ONLY
Change only [blocking, expression, action, camera position]. Do not redesign the identity, outfit, prop, or location.
```

Keep the block short. Its purpose is to establish invariants, not to restate the whole project bible in every prompt.

## Rights check

Use a person's likeness or voice only with the necessary permission. Preserve source records and any consent documentation outside the prompt workflow; platform availability does not itself create permission.
