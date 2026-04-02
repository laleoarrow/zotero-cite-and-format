---
name: word-zotero
description: Use when Word .docx files with Zotero citations need live-field repair, bibliography regeneration, style initialization, or conversion between static submission files and Zotero-editable source documents.
---

# Word + Zotero Citation Repair / Word + Zotero 引文修复

## Overview / 概览
This skill repairs or rebuilds **real Zotero live citations** in Word `.docx` files. It is for fragile situations where the document must remain Zotero-refreshable, not merely display citation-like text.

**Final objective:** produce either:
- a clean **Zotero-editable source document** that can still refresh in Word, or
- a clean **static submission file** that no longer depends on Zotero.

Do not confuse the two.

## Accuracy Rule / 准确性规则
This skill is technical but still evidence-sensitive. Do not claim Word, Zotero, or journal-submission behavior from memory alone when the point is operationally important.

Before asserting a rule about:
- Zotero field behavior
- broken-citation recovery
- bibliography regeneration
- field-code visibility
- whether a target journal accepts or forbids reference-manager field codes

verify it against official sources first.

Preferred source order:
1. Zotero official knowledge base
2. Zotero official integration repositories when implementation detail matters
3. the target journal's official author instructions

At minimum, the operator should know these Zotero KB pages exist and use them when relevant:
- `word_field_codes`
- `existing_citations_not_detected`
- `debugging_broken_documents`
- `citations_not_updating`

Read:
- `references/official-sources.md` when the task depends on Zotero or journal policy details
- `references/validation-cases.md` when checking whether the skill actually covers the current failure mode

## Intake Rule / 起始询问规则
At the start, ask only the minimum needed to choose the right document path:

1. What is the target journal?
2. Does that journal, or its submission system, require a static manuscript with field codes removed?

If the user does not yet have a target journal, or if no static-submission requirement has been confirmed, default to maintaining only the **Zotero-editable source document**.

Do not export a static submission file just for ceremony.

## When to Use / 适用场景
- A user says Zotero refresh fails, bibliography is broken, or Word throws document-preferences errors.
- A manuscript has static numeric citations but must be converted back to Zotero live citations.
- A document needs a journal style change and bibliography regeneration while preserving editability.
- A project needs both a Zotero-editable source and a separate submission-ready static file.

## Quick Reference / 快速参考
| Situation | Action |
|---|---|
| User only needs a final submission file | Keep it static; do not force Zotero back in. |
| User wants to keep editing with Zotero | Rebuild real Word fields and refresh in Word. |
| Word shows numbers but Zotero cannot detect citations | Treat them as static text until proven otherwise. |
| First refresh opens a style dialog | Select the correct style once, then rerun refresh. |

## Non-Negotiable Rule / 不可协商规则
Never fake Zotero by inserting plain text that merely looks like a citation.

Real Zotero citations in Word require:
1. Word field codes in `word/document.xml`
2. valid Zotero document preferences in `docProps/custom.xml`
3. resolvable Zotero library items, ideally with both `itemID` and `uri`
4. a real Zotero bibliography field if bibliography regeneration is required

If any of these are missing, the file is not truly Zotero-live.

## Editable vs Static Split / 可编辑稿与静态稿分流
Always decide which of these the user needs before editing:

- **Zotero-editable source document / Zotero 可编辑稿**
  - must support Word Zotero refresh
  - citations and bibliography are field-backed
  - use this for ongoing drafting

- **Static submission file / 静态提交稿**
  - may keep plain rendered citations and references
  - safer for journal submission
  - do not continue Zotero editing here

If the user needs both, maintain two files explicitly.

Default policy:
- journal not chosen yet -> maintain the Zotero-editable source only
- journal chosen but static requirement unknown -> check official instructions first
- static manuscript explicitly required -> export a separate submission copy

## Document Package Inspection / 文档包检查
Before editing, inspect the DOCX package and verify the following parts:

- `word/document.xml`
- `docProps/custom.xml`
- `customXml/item1.xml`
- `customXml/itemProps1.xml`
- `customXml/_rels/item1.xml.rels`

At minimum, check:
- whether `ADDIN ZOTERO_ITEM CSL_CITATION` exists
- whether `ADDIN ZOTERO_BIBL` exists
- whether `ZOTERO_PREF_*` is present and has the intended style id
- whether placeholders like `{Citation}`, `{Bibliography}`, or duplicated static lists remain
- whether the target file is truly `.docx` rather than a format that would flatten fields in the current workflow

## Field Shapes / 字段形状
The critical field signatures are:

- Citation field:
  - `ADDIN ZOTERO_ITEM CSL_CITATION {json}`
- Bibliography field:
  - `ADDIN ZOTERO_BIBL {"uncited":[],"omitted":[],"custom":[]} CSL_BIBLIOGRAPHY`

For rebuilt citations, prefer real Zotero-linked citation items using:
- `id`: local Zotero `itemID`
- `uris`: `http://zotero.org/users/<user>/items/<key>`

Do not invent item keys. Check the local Zotero library first.

## Style Initialization / 样式初始化
Verify the target CSL style locally before writing it into the document.

Typical local path on macOS:
- `~/Zotero/styles/*.csl`

The corresponding style id belongs in `docProps/custom.xml` under `ZOTERO_PREF_*`.

If the first refresh opens the Zotero document-preferences dialog:
1. choose the intended journal style
2. click `OK`
3. rerun `ZoteroRefresh`

Treat this as first-time initialization, not immediate failure.

## Preferred Repair Procedure / 首选修复流程
1. Determine whether the target file should be live or static.
2. Back up the original file before editing.
3. Inspect package parts and count existing Zotero fields.
4. If converting static text back to live citations:
   - map each cited reference to a real Zotero library item
   - rebuild citation fields with real `itemID + uri`
   - replace the static reference list with a real Zotero bibliography field
   - write valid Zotero document preferences for the intended style
5. Open the document in Word and run `ZoteroRefresh`.
6. If needed, use `ZoteroAddEditBibliography` only after style initialization is complete.
7. Save and close the document.
8. Reopen or re-inspect the package to confirm the refresh actually happened.

## Static Export Procedure / 静态提交稿导出流程
When exporting a static submission file from a Zotero-editable source document, do not treat bibliography fields as generic inline fields.

Use this order:
1. Duplicate the Zotero-editable source document and export on the copy only.
2. Prefer a Word-side unlink/export path when available.
3. If an XML-level unlink is required, special-case the Zotero bibliography field.
4. Re-check the rendered reference block immediately after export.

### Bibliography Anchor Gotcha / 参考文献锚段陷阱
The first rendered reference entry may live in the **same paragraph** as the `ADDIN ZOTERO_BIBL` field container.

That means:
- a naive "strip all field code runs and keep later bibliography paragraphs" strategy can silently delete reference `1`
- the result may look like a large blank gap under `References`
- the heading may appear visually detached from the list even though the XML looks superficially valid

If the bibliography field is unlinked at XML level:
- preserve the rendered result runs inside the bibliography anchor paragraph
- do not replace that paragraph with a placeholder or a single blank run
- explicitly verify that reference `1` survives the export

## Submission-File Verification / 投稿静态稿验证
For any static submission file derived from a Zotero-editable source document, verify all of the following before claiming success:

1. `ZOTERO_ITEM = 0`
2. `ZOTERO_BIBL = 0`
3. `References` is followed immediately by reference `1`, not by a blank block
4. references run consecutively without a missing first entry
5. the `References` heading is not orphaned from the first bibliography paragraph
6. the body text still matches the vetted live/source version

## SCI Formatting Hygiene / SCI 通用格式卫生
Unless the target journal says otherwise, treat these as general Word-manuscript rules for English SCI submissions:

1. Use real Word character formatting for superscript, subscript, italic, bold, and small caps. Do not fake these with Unicode look-alike glyphs.
2. For scientific notation, prefer `a × 10^n` with a real multiplication sign `×` and a truly superscripted exponent. In Word terms, the exponent should be plain text in its own run with superscript formatting applied, not a pasted Unicode form such as `10⁻3`.
3. Do not normalize hyphen, minus, en dash, and em dash blindly. Preserve one role per symbol and keep the manuscript's convention consistent unless the target journal explicitly wants a different style.
4. Use true italic formatting for material that field convention marks as italic, such as Latin species names or other biologic labels that genuinely require italics. Do not replace italics with styled Unicode characters.
5. Use real symbol characters when the symbol itself carries meaning, such as Greek letters, `≤`, `≥`, `±`, and `×`. Do not silently downgrade them to plain-text approximations unless the journal or submission system requires it.
6. If the user asks for formatting-only cleanup, keep the change at run level whenever possible. Do not rewrite prose, renumber citations, or refresh Zotero unless explicitly requested.
7. If verification uses XML extraction, `pdftotext`, or similar text-only views, remember that correctly superscripted text may flatten during extraction. Judge the final formatting from Word or rendered PDF output, not from plain extracted text alone.

## Mac Word Automation / macOS 上的 Word 自动化
On macOS, Word Zotero integration can be triggered through Word macros such as:
- `ZoteroRefresh`
- `ZoteroAddEditBibliography`
- `ZoteroAddEditCitation`

If using AppleScript automation:
- prefer opening the document in Word, running the macro, saving, and closing
- do not assume UI automation is available
- if a modal dialog appears and automation cannot click it, narrow the blocker and ask the user for that one click

## Verification Checklist / 验证清单
Before claiming success, verify all of the following:

- the file contains the expected number of `ADDIN ZOTERO_ITEM` fields
- the bibliography placeholder has been replaced by a rendered bibliography
- no stale placeholders remain:
  - `{Citation}`
  - `{Bibliography}`
  - duplicated old reference lists
- scientific-notation exponents, if present, use true Word superscript formatting rather than pasted Unicode superscript glyphs
- the Zotero-editable source document and the static正文版 have no unintended body-text drift
- the regenerated bibliography count matches the intended unique references
- any style-driven renumbering is explained to the user
- any journal-specific submission rule that matters for the chosen output file has been checked against official author instructions

For realistic coverage checks, compare the current task against the cases in `references/validation-cases.md`.

## Smoke Test / 烟测
- "Zotero says these are not active citations anymore." -> inspect package parts first; do not trust the visible numbers
- "Please make this Word manuscript refreshable in Zotero again." -> rebuild real citation fields, then refresh in Word
- "Please export a submission-ready copy for AJO." -> verify journal policy first, then export a separate static file
- "The references now start from 2 after export." -> check the bibliography anchor paragraph before touching spacing

This skill is considered working when it consistently routes these cases to the correct path and the verification checklist can be satisfied on the output files.

## Common Failure Modes / 常见失败模式
- **Numbers visible but not live**: the document only contains rendered text
- **Broken bibliography**: a field exists, but stale rendered references were left behind
- **Style dialog blocks automation**: document preferences were not initialized for the new file
- **Wrong numbering after refresh**: Zotero renumbered by true first appearance; this may be expected
- **Metadata gap in a Zotero item**: bibliography renders but one entry is incomplete; fix the Zotero library item itself
- **Dropped first reference during static export**: the exporter mishandled the bibliography anchor paragraph and deleted reference `1`
- **Fake blank gap under `References`**: often a symptom of the same bibliography-anchor bug rather than true paragraph spacing
- **Unicode fake superscripts/subscripts**: the document looks acceptable at a glance but uses pasted glyphs instead of Word formatting, making later editing and consistency checks brittle
- **Text extraction looks flat after correct superscripting**: XML or PDF text extraction may show `10-3`; verify the rendered page before treating this as a formatting failure

## Output Contract / 输出约定
When you finish, report:
- which file is the Zotero-editable source document
- which file is the static submission file, if one exists
- whether refresh completed successfully
- how many live citation fields and unique Zotero items were verified
- any remaining user-only blocker, narrowed to a single concrete action
