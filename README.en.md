# word-zotero

### Word + Zotero Citation Repair

**English** | **[中文](README.md)**

`word-zotero` is a small skill for repairing Word manuscripts that rely on Zotero. It is meant for documents where citation integrity matters more than prose: broken live citations, corrupted bibliographies, style initialization problems, and safe export from a live Zotero source to a static submission file.

The point is not to make a file *look* right. The point is to know whether the document still contains real Zotero fields and whether it can survive another refresh or journal submission step.

## What the Skill Covers

- restoring active Zotero citations in `.docx`
- rebuilding a broken Zotero bibliography
- checking whether a manuscript is live or already flattened
- initializing or switching citation styles
- creating a static submission file from a live Zotero source
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
Decide what the file should be
    live source or static submission copy
                ↓
Inspect the DOCX package
    document.xml / custom props / customXml
                ↓
Repair citations or bibliography if needed
                ↓
Refresh in Word with Zotero
                ↓
Export the submission copy
                ↓
Verify that the export is actually clean
```

## A Failure Mode Worth Knowing

The most important export bug is easy to miss because the document may still open normally.

In some Zotero-generated bibliographies, reference `1` is rendered in the same paragraph as the bibliography field anchor. If a static export routine strips that anchor paragraph incorrectly, the manuscript can lose the first reference while leaving the rest of the bibliography behind.

What you see in Word is usually:
- a large blank-looking gap under `References`
- a bibliography that starts from `2.`
- a heading that looks detached from the list

That is not just spacing. It is a damaged export.

## Minimum Checks After Static Export

For any submission file exported from a live Zotero source, verify:

1. `ZOTERO_ITEM = 0`
2. `ZOTERO_BIBL = 0`
3. `References` is followed immediately by reference `1`
4. the references run consecutively
5. the body text still matches the vetted live/source manuscript

## When to Use It

Use `word-zotero` for requests like:
- “Zotero no longer recognizes these citations”
- “Please rebuild this bibliography”
- “Export a submission-ready Word file from the Zotero version”
- “Word opens the manuscript, but Zotero refresh is broken”

Do not use it for ordinary text polishing or generic reference formatting that does not involve live Zotero behavior.

## Related Skills

| Skill | Purpose |
|-------|---------|
| `doc` | Structured DOCX editing and layout checks |
| `academic-editing` | Manuscript revision and content consistency |
| `bioinfo-autopilot` | Evidence-chain checks for data-heavy papers |

## License

MIT License
