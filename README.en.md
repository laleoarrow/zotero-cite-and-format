# zotero-cite-and-format

### Zotero Cite + Format

**English** | **[中文](README.md)**

`zotero-cite-and-format` is a skill for Word manuscripts where citation integrity and journal-facing formatting both matter. Zotero repair is one part of it, not the whole. It covers broken live citations, corrupted bibliographies, style initialization problems, journal-specific formatting cleanup, and controlled export from a verified Zotero-editable source document to a static submission file.

The point is not to make a file *look* right. The point is to know whether the document still contains real Zotero fields and whether it can survive another refresh or journal submission step.

By default, it should not export a static submission file immediately. Start with two questions:
- What is the target journal?
- Does that journal, or its submission system, explicitly require a static manuscript with field codes removed?

If the journal has not been chosen yet, or if no such requirement has been confirmed, maintain the Zotero-editable source document only.

The intended order is strict:
1. repair or confirm the Zotero-editable source document first
2. treat that source document as the canonical manuscript
3. derive a static submission file from that source only if it is actually needed

## What the Skill Covers

- restoring active Zotero citations in `.docx`
- rebuilding a broken Zotero bibliography
- checking whether a manuscript is live or already flattened
- initializing or switching citation styles
- applying journal-directed Word formatting cleanup without damaging semantic formatting or live citations
- creating a static submission file from a Zotero-editable source document
- verifying that the static export did not silently damage the reference list

## Working Assumption

If a Word manuscript contains numeric citations, that tells you almost nothing by itself.

What matters is:
- whether the document still contains `ADDIN ZOTERO_ITEM` fields
- whether the bibliography is still a real Zotero bibliography field
- whether the document preferences still point to a valid Zotero style
- whether the cited items can still be resolved in the local Zotero library

## Source Discipline

This skill should be used with the same standard you would apply to a submission-critical methods note.

Operational claims should be checked against official sources when they affect the outcome:
- Zotero field behavior: Zotero knowledge base
- Word integration details: Zotero integration repositories
- submission rules: the journal's official author instructions

That matters because journal-specific rules can override convenient assumptions. A file that is acceptable for local editing may still be the wrong file to upload.

## Typical Workflow

```text
Ask for the journal
and whether a static manuscript is required
                ↓
Decide what the file should be
    verified editable source first / then a separate static copy if needed
                ↓
Inspect the DOCX package
    document.xml / custom props / customXml
                ↓
Repair citations or bibliography if needed
                ↓
Refresh in Word with Zotero
                ↓
Export the submission copy from the verified Zotero source
                ↓
Verify that the export is actually clean
```

## How to Validate the Skill

At the moment this is a documentation-first skill, not a packaged automation tool with bundled scripts. So the right validation target is not "does a test runner pass?" but "does the skill lead the operator to the right decisions and checks?"

The minimum validation standard is:

1. It separates a `Zotero-editable source document` from a `static submission file`.
2. It points the operator to official Zotero and journal sources before making submission-critical claims.
3. It catches the failure modes that matter in real manuscripts.

That is why the repo includes a `references/` directory:
- `references/official-sources.md`
  - official Zotero KB pages, integration repositories, and journal-instruction examples
- `references/validation-cases.md`
  - real failure cases from actual manuscript repair work, including the dropped-reference-1 export bug

If the skill later grows a bundled export or verification script, then a `scripts/` directory and executable tests would make sense. Right now, `references/` is the more useful scaffolding.

## A Failure Mode Worth Knowing

The most important export bug is easy to miss because the document may still open normally.

In some Zotero-generated bibliographies, reference `1` is rendered in the same paragraph as the bibliography field anchor. If a static export routine strips that anchor paragraph incorrectly, the manuscript can lose the first reference while leaving the rest of the bibliography behind.

What you see in Word is usually:
- a large blank-looking gap under `References`
- a bibliography that starts from `2.`
- a heading that looks detached from the list

That is not just spacing. It is a damaged export.

## SCI Formatting Hygiene

Unless the target journal says otherwise, a final Word manuscript should keep semantic formatting as real Word formatting rather than as pasted look-alike characters.

In practice, that means:
- use true superscript formatting for exponents in scientific notation
- prefer `1.54 × 10` with superscript `-3`, not `1.54 × 10⁻3`
- use real italics for text that genuinely requires italics
- do not blindly normalize hyphen, minus, en dash, and em dash into one symbol
- verify the rendered page, because plain-text extraction may flatten correct superscripts into `10-3`

## Minimum Checks After Static Export

For any submission file exported from a Zotero-editable source document, verify:

1. `ZOTERO_ITEM = 0`
2. `ZOTERO_BIBL = 0`
3. `References` is followed immediately by reference `1`
4. the references run consecutively
5. the body text still matches the vetted live/source manuscript

## Installation

### CC Switch

```bash
git clone https://github.com/laleoarrow/zotero-cite-and-format.git ~/agents/zotero-cite-and-format
mkdir -p ~/.cc-switch/skills
ln -s ~/agents/zotero-cite-and-format/skills/zotero-cite-and-format ~/.cc-switch/skills/zotero-cite-and-format
```

### Claude Code

```bash
git clone https://github.com/laleoarrow/zotero-cite-and-format.git ~/agents/zotero-cite-and-format
ln -s ~/agents/zotero-cite-and-format/skills/zotero-cite-and-format ~/.claude/skills/zotero-cite-and-format
```

### Codex CLI

```bash
git clone https://github.com/laleoarrow/zotero-cite-and-format.git ~/agents/zotero-cite-and-format
ln -s ~/agents/zotero-cite-and-format/skills/zotero-cite-and-format ~/.codex/skills/zotero-cite-and-format
```

Always point the host to `skills/zotero-cite-and-format`, which is the canonical skill root containing both `SKILL.md` and `references/`.

## When to Use It

Use `zotero-cite-and-format` for requests like:
- “Zotero can no longer recognize, edit, or refresh these citations”
- “Please rebuild this bibliography”
- “Export a submission-ready Word file from the Zotero version”
- “Word opens the manuscript, but Zotero refresh is broken”
- “Adjust this Word file to the target journal's citation and formatting requirements”

Do not use it for ordinary text polishing or generic reference formatting that does not involve live Zotero behavior.

## Related Skills

| Skill | Purpose |
|-------|---------|
| `doc` | Structured DOCX editing and layout checks |
| `academic-editing` | Manuscript revision and content consistency |
| `bioinfo-autopilot` | Evidence-chain checks for data-heavy papers |

## License

MIT License
