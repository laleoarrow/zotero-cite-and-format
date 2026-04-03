---
name: zotero-cite-and-format
description: Use when Word .docx manuscripts need journal-specific citation or formatting cleanup, Zotero live-field repair, bibliography regeneration, or controlled export between Zotero-editable source documents and submission-ready static files.
---

# Zotero Cite + Format / Zotero 引文与格式

## Overview / 概览
This skill handles **Word manuscript citation and formatting work** when journal requirements, Zotero editability, and submission safety interact. It can repair or rebuild **real Zotero live citations**, preserve or export them appropriately, and fix formatting details that must remain semantically correct in Word rather than only looking correct on screen.

**Final objective:** first produce a clean **Zotero-editable source document** that can still refresh in Word and remains suitable for further drafting. Only after that, and only if the journal or user actually needs it, derive a clean **static submission file** that no longer depends on Zotero and matches the target journal's operational formatting requirements.

Do not confuse the two.

**User-facing output limit:** at most **two** manuscript DOCX files should be left as final deliverables for the same paper:
- `name_zotero.docx` -> editable Zotero manuscript
- `name.docx` -> optional static submission copy

Do not leave extra variants such as `revised`, `final`, `submission_static`, `v2`, or similar names in the deliverable folder.

## Accuracy Rule / 准确性规则
This skill is technical but still evidence-sensitive. Do not claim Word, Zotero, or journal-submission behavior from memory alone when the point is operationally important.

Before asserting a rule about:
- Zotero field behavior
- broken-citation recovery
- bibliography regeneration
- field-code visibility
- scientific-notation or run-level formatting behavior in Word
- whether a target journal accepts or forbids reference-manager field codes

verify it against official sources first.

Preferred source order:
1. Zotero official knowledge base
2. Zotero official integration repositories when implementation detail matters
3. the target journal's official author instructions

At minimum, the operator should know these official Zotero support pages exist and use them when relevant:
- `word_processor_plugin_usage`
- `word_processor_integration`
- `word_processor_plugin_troubleshooting`
- `preferences/cite`
- `dev/client_coding/connector_http_server`
- `kb/moving_documents_between_word_processors`
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

## Source-First Gate / 先修 Zotero 源稿
The default workflow is mandatory unless the user explicitly says the file is already a vetted static-only deliverable:

1. repair or confirm the **Zotero-editable source document** first
2. verify that Word + Zotero refresh works on that source document
3. treat that verified Zotero version as the canonical manuscript
4. only then derive a static submission file if the journal or user actually needs one

Do not start from a broken static manuscript and push formatting changes straight into a submission copy while the Zotero source remains unresolved.

## Content Preservation Rule / 内容保全规则
Word editing in this skill is preservation-first.

Unless the user explicitly asks to delete, rewrite, or replace content:
- do not let citation repair, bibliography repair, XML surgery, unlink/export, or formatting cleanup remove existing manuscript content
- do not damage the DOCX package so that Word opens with loss, repair prompts, or broken layout
- preserve non-target content such as headings, paragraphs, tables, figure legends, footnotes, comments, and reference text outside the intended edit scope

If a proposed edit path is likely to drop content, choose a narrower or safer path.

## Manuscript Prose Rule / 稿件叙述规则
For journal-facing manuscript prose, prefer scientific narrative over implementation syntax.

Rules:
- Override order for manuscript prose is: target-journal requirement first, then explicit user instruction for the current manuscript scope, then the default anti-code-tone rule. Neither journal silence nor generic reproducibility preference is enough to justify code-style narrative in abstract, Results, Discussion, or Conclusions.
- Do not leave literal function calls, wrapper names, argument strings, or code-style tokens in the abstract, Results, Discussion, or Conclusions unless the target journal explicitly requires them.
- Treat "no code-tone in manuscript narrative" as an explicit default rule, not a stylistic preference. Journal-facing prose should not read like pasted scripts, package calls, or pipeline logs.
- In Methods, translate implementation into what the analysis did and why it matters. Thresholds, models, endpoint identifiers, software names, and selected identifiers such as dataset codes or outcome labels may remain only when they materially clarify the methodological operation, reproducibility, or source mapping. Raw function calls, `package::function` syntax, argument strings, authentication details, workspace paths, and command fragments should not remain in the main text when a prose translation would convey the method just as well.
- Avoid monospace/code formatting in running manuscript prose for package names, file paths, function names, or parameter settings unless the target journal explicitly requires it in the main text. If the user wants reproducibility-heavy detail, place that notation in an appendix, supplement, or separate methods artifact rather than in the main narrative by default.
- If a literal identifier must remain, make the surrounding sentence explain the methodological meaning rather than presenting the identifier as if the function name itself were the method.
- Even in Methods, do not let code-like details create visibly different typography from the surrounding text unless the journal explicitly requires a distinct format for such material.
- When target-journal guidance is silent, default to the journal's conventional published prose style rather than to implementation-level notation.

## Output Naming Policy / 输出命名规则
The user-facing manuscript outputs should be named by one stable stem only.

- Editable Zotero manuscript: `name_zotero.docx`
- Static submission manuscript: `name.docx`

Rules:
- The two files, when both exist, should differ only in Zotero editability and any journal-required submission-safe cleanup directly tied to static export.
- Do not create additional user-facing DOCX variants such as `name_revised.docx`, `name_submission_static.docx`, `name_final.docx`, or `name_v2.docx`.
- Internal backups, rebuild checkpoints, and scratch DOCX files belong outside the deliverable folder, for example under `agents/` or another process-artifact location.
- If the journal does not explicitly require or recommend a static submission file, or if the user explicitly prefers Zotero-only output, generate only `name_zotero.docx`.
- Rare exception: if the task is explicitly a vetted static-only deliverable and no Zotero-editable source is requested or in scope, the final deliverable may be `name.docx` only. State that exception explicitly when reporting completion.

## When to Use / 适用场景
- A user says Zotero refresh fails, bibliography is broken, or Word throws document-preferences errors.
- A manuscript has static numeric citations but must be converted back to Zotero live citations.
- A document needs a journal style change and bibliography regeneration while preserving editability.
- A Word manuscript needs journal-specific formatting cleanup that must not break citation fields or semantic Word formatting.
- A project needs both a Zotero-editable source and a separate submission-ready static file.

## Quick Reference / 快速参考
| Situation | Action |
|---|---|
| User only needs a final submission file | If a working Zotero source exists, verify that source first and export `name.docx` from `name_zotero.docx`; skip Zotero repair only when the deliverable is truly static-only. |
| User wants to keep editing with Zotero | Rebuild real Word fields and refresh in Word. |
| Word shows numbers but Zotero cannot detect citations | Treat them as static text until proven otherwise. |
| First refresh opens a style dialog | Select the correct style once, then rerun refresh. |
| Rebuilt document has live-looking fields but `Refresh` does nothing | Run `ZoteroAddEditCitation`, accept `Document Preferences`, and only then rerun `ZoteroRefresh`; a no-op refresh is not proof of success. |
| User wants citation or formatting cleanup without collateral damage | Back up first, apply the narrowest edit possible, and verify that no previously existing content was deleted or broken. |
| Word manuscript will remain Zotero-editable | Store citations as `Fields` unless real Word/LibreOffice interoperability requires `Bookmarks`. |
| User needs a static submission copy | Duplicate the verified `name_zotero.docx` source and create `name.docx` on the copy only. |
| User asks for formatting-only cleanup | Fix Word run/style formatting without rewriting prose or disturbing Zotero unless required. If code-like narrative is already present, limit formatting-only work to typographic cleanup unless the user widens scope to manuscript editing. |
| DOCX shows gray square brackets around headings or paragraph ends | Suspect pandoc/bookmark display artifacts first; inspect `w:bookmarkStart` / `w:bookmarkEnd` and remove nonessential bookmarks from the submission copy. |
| First page repeats the manuscript title | Treat duplicated title blocks as a document-template problem, not a journal requirement, unless the target journal explicitly requires both a manuscript title and a separate title-page title line in the same file. |
| Data Availability reads like citation-only prose but the journal usually shows direct links | Verify the journal's published style or author instructions; if no contrary rule is found, prefer human-readable resource names plus explicit URLs in the submission copy. |
| Methods prose contains code calls such as `foo(arg = 1)` | Replace the implementation syntax with journal-style methodological prose unless the target journal explicitly requires software-notation detail in the main text. Endpoint IDs or model labels may stay when they aid source mapping, but they should remain typographically consistent with the surrounding prose. |

## Non-Negotiable Rule / 不可协商规则
Never fake Zotero by inserting plain text that merely looks like a citation.

Real Zotero citations in Word require:
1. Word field codes in `word/document.xml`
2. valid Zotero document preferences in `docProps/custom.xml`
3. resolvable Zotero library items, ideally with both `itemID` and `uri`
4. a real Zotero bibliography field if bibliography regeneration is required

If any of these are missing, the file is not truly Zotero-live.

Operational repair rule:
- a minimally valid field shape is not automatically refreshable
- for rebuilt citations, treat `citationItems[].itemData` as standard repair payload, not optional decoration

## Editable vs Static Split / 可编辑稿与静态稿分流
Always decide which of these the user needs before editing:

- **Zotero-editable source document / Zotero 可编辑稿**
  - must support Word Zotero refresh
  - citations and bibliography are field-backed
  - default Word storage mode is `Fields`
  - do not run `Unlink Citations` here
  - use this for ongoing drafting

- **Static submission file / 静态提交稿**
  - may keep plain rendered citations and references
  - safer for journal submission
  - derive it by duplicating the verified `_zotero` source first
  - do not continue Zotero editing here

If the user needs both, maintain two files explicitly.

Default policy:
- journal not chosen yet -> maintain only `name_zotero.docx`
- journal chosen but static requirement unknown -> check official instructions first, and still default to `name_zotero.docx` only until a static need is confirmed
- static manuscript explicitly required or recommended -> export `name.docx` in addition to `name_zotero.docx`
- user explicitly wants Zotero-only output -> maintain only `name_zotero.docx`

Operational rule:
- the Zotero-editable source document is the canonical working manuscript
- the static submission file is a derived artifact, not the primary editing target
- `Unlink Citations` belongs only on the final submission copy, never on the Zotero-editable source
- user-facing deliverables should therefore be either:
  - one file: `name_zotero.docx`
  - or two files: `name_zotero.docx` plus `name.docx`
  - or, only for an explicit vetted static-only exception, one file: `name.docx`

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
- whether any field parser reconstructs long `w:instrText` payloads across multiple XML runs instead of assuming one node per field code

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

For rebuilt citation payloads, standardize `citationItems[].itemData` from the local Zotero API rather than relying on `id + uri` alone.

## Local API Repair / 本地 API 修复
When a rebuild needs authoritative item metadata for `citationItems[].itemData`, use the local Zotero API against `127.0.0.1:23119`:

- `http://127.0.0.1:23119/api/users/0/items/<itemKey>`
- `http://127.0.0.1:23119/api/users/0/items/<itemKey>?format=csljson`

Use `?format=csljson` as the standard repair path for rebuilding `itemData`.

Operational notes:
- prefer non-browser local requests to the local API over browser-origin fetches, which can fail because webpages often cannot read responses from the integrated Zotero HTTP server
- use the API output to repair Zotero field payloads, not as a substitute for official Zotero policy guidance

## Style Initialization / 样式初始化
Verify the target CSL style locally before writing it into the document.

Typical local paths on macOS:
- `~/Zotero/styles/*.csl`
- Zotero app Cite preferences for installed style availability

The corresponding style id belongs in `docProps/custom.xml` under `ZOTERO_PREF_*`.

A rebuilt document may need explicit citation-side initialization before `ZoteroRefresh` does anything useful.

Use this order:
1. run `ZoteroAddEditCitation`
2. accept or initialize the `Document Preferences` window
3. confirm the intended style and `Store Citations as: Fields` unless actual Word/LibreOffice collaboration requires `Bookmarks`
4. run `ZoteroRefresh`

Treat this as first-time initialization, not immediate failure. `ZoteroRefresh` alone can return successfully while still doing nothing.

## Preferred Repair Procedure / 首选修复流程
1. Identify or create the Zotero-editable source document that will serve as the canonical manuscript.
2. Back up the original file before editing.
3. Inspect package parts, count existing Zotero fields, and record the visible manuscript content that must survive unchanged.
4. If converting static text back to live citations:
   - map each cited reference to a real Zotero library item
   - rebuild citation fields with real `itemID + uri + itemData`
   - obtain `itemData` from the local Zotero API using `?format=csljson`
   - replace the static reference list with a real Zotero bibliography field
   - write valid Zotero document preferences for the intended style
5. Open the document in Word and, if the file is rebuilt or newly live-looking, run `ZoteroAddEditCitation` first.
6. In `Document Preferences`, confirm the target style and `Fields` storage mode unless interoperability explicitly requires `Bookmarks`.
7. Run `ZoteroRefresh`.
8. If needed, use `ZoteroAddEditBibliography` only after the citation-side initialization and refresh path is working.
9. Save and close the Zotero-editable source document.
10. Reopen the document in Word or re-inspect the package to confirm the refresh actually happened and no non-target content disappeared.
11. Compare against the backup or pre-edit baseline to confirm there was no unintended deletion, truncation, or layout-breaking corruption.
12. Only after the source document is verified, decide whether a separate static submission file is required.

## Static Export Procedure / 静态提交稿导出流程
Only run this procedure after the Zotero-editable source document has already been repaired or verified and confirmed as the canonical manuscript. When exporting a static submission file from that source document, do not treat bibliography fields as generic inline fields.

Use this order:
1. Start from `name_zotero.docx`, duplicate it, and export only the duplicate as `name.docx`.
2. Prefer a Word-side unlink/export path when available, and use `Unlink Citations` only on the duplicated submission copy.
3. If the manuscript was generated from Markdown or pandoc, inspect for nonessential heading bookmarks before export; strip them from the submission copy if they create visible gray brackets or navigation artifacts in Word/LibreOffice.
4. If an XML-level unlink is required, unlink only Zotero citation/bibliography fields. Preserve unrelated Word fields such as `PAGE`, `NUMPAGES`, and other non-Zotero document mechanics unless the user explicitly asks to flatten them.
5. Special-case the Zotero bibliography field.
6. Re-check the rendered reference block and the rest of the manuscript immediately after export.

Never unlink the canonical Zotero-editable source document.
Never leave the duplicated static file under a third name such as `submission_static` or `revised`.

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
7. nonessential bookmarks or pandoc navigation anchors do not render as visible gray brackets in the submission file
8. no duplicated title block remains unless the journal explicitly requires it
9. unrelated Word fields such as page numbering still behave correctly after export

## SCI Formatting Hygiene / SCI 通用格式卫生
Unless the target journal says otherwise, treat these as general Word-manuscript rules for English SCI submissions:

1. Use real Word character formatting for superscript, subscript, italic, bold, and small caps. Do not fake these with Unicode look-alike glyphs.
2. For scientific notation, prefer `a × 10^n` with a real multiplication sign `×` and a truly superscripted exponent. In Word terms, the exponent should be plain text in its own run with superscript formatting applied, not a pasted Unicode form such as `10⁻3`.
3. Do not normalize hyphen, minus, en dash, and em dash blindly. Preserve one role per symbol and keep the manuscript's convention consistent unless the target journal explicitly wants a different style.
4. Use true italic formatting for material that field convention marks as italic, such as Latin species names or other biologic labels that genuinely require italics. Do not replace italics with styled Unicode characters.
5. Use real symbol characters when the symbol itself carries meaning, such as Greek letters, `≤`, `≥`, `±`, and `×`. Do not silently downgrade them to plain-text approximations unless the journal or submission system requires it.
6. If the user asks for formatting-only cleanup, keep the change at run level whenever possible. Do not rewrite prose, renumber citations, or refresh Zotero unless explicitly requested. The only exception is normalizing the typography of identifiers that are already intentionally retained in the prose.
7. If verification uses XML extraction, `pdftotext`, or similar text-only views, remember that correctly superscripted text may flatten during extraction. Judge the final formatting from Word or rendered PDF output, not from plain extracted text alone.
8. Do not let code-style monospace or inline backticks leak into narrative manuscript sections merely because the source text came from Markdown, notebooks, or scripts. Journal-facing prose should read like prose unless the target journal explicitly requires a software or reproducibility notation in the main text. User preference for reproducibility detail should normally be satisfied in Methods supplements, appendices, or separate technical artifacts rather than by making the main narrative read like code.

## Mac Word Automation / macOS 上的 Word 自动化
On macOS, Word Zotero integration can be triggered through Word macros such as:
- `ZoteroRefresh`
- `ZoteroAddEditBibliography`
- `ZoteroAddEditCitation`

If using AppleScript automation:
- on macOS Word, use `run VB macro macro name "ZoteroRefresh"` style syntax rather than `run VB macro "ZoteroRefresh"`
- prefer opening the document in Word, running the macro, saving, and closing
- do not assume UI automation is available
- if a modal dialog appears and automation cannot click it, narrow the blocker and ask the user for that one click

## Verification Checklist / 验证清单
Before claiming success, verify all of the following:

- the Zotero-editable source document exists and is the canonical manuscript for any later static export
- the edited `.docx` still opens normally in Word and does not trigger document-repair symptoms attributable to the edit
- `docProps/custom.xml` contains the intended Zotero style id and document-preference payload
- the file contains the expected number of `ADDIN ZOTERO_ITEM` fields, but field counts are not treated as sufficient proof
- the bibliography placeholder has been replaced by a rendered bibliography
- no stale placeholders remain:
  - `{Citation}`
  - `{Bibliography}`
  - duplicated old reference lists
- no previously existing non-target content was accidentally deleted, truncated, or reordered
- headings, body paragraphs, tables, figure legends, and other untouched manuscript regions still match the pre-edit document except for explicitly requested changes
- rendered citations and bibliography text change as expected after refresh
- verification is based on Word-visible output or a rendered export, not only XML inspection or field counts
- macro/process success messages alone are not accepted as evidence that refresh happened
- scientific-notation exponents, if present, use true Word superscript formatting rather than pasted Unicode superscript glyphs
- the Zotero-editable source document and any static submission copy have no unintended body-text drift
- the regenerated bibliography count matches the intended unique references
- any style-driven renumbering is explained to the user
- any journal-specific submission rule that matters for the chosen output file has been checked against official author instructions

For realistic coverage checks, compare the current task against the cases in `references/validation-cases.md`.

## Smoke Test / 烟测
- "Zotero can no longer recognize or refresh these citations." -> inspect package parts first; do not trust the visible numbers
- "Please make this Word manuscript refreshable in Zotero again." -> rebuild real citation fields, then refresh in Word
- "The refresh macro returned successfully, but the bibliography still didn't appear." -> treat this as a false green; initialize with `Add/Edit Citation`, confirm `Document Preferences`, and verify rendered output
- "Please export a submission-ready copy for AJO." -> verify journal policy first, make sure the Zotero source document is working, then export a separate static file
- "The references now start from 2 after export." -> check the bibliography anchor paragraph before touching spacing

This skill is considered working when it consistently routes these cases to the correct path and the verification checklist can be satisfied on the output files.

## Common Failure Modes / 常见失败模式
- **Numbers visible but not live**: the document only contains rendered text
- **Broken bibliography**: a field exists, but stale rendered references were left behind
- **Style dialog blocks automation**: document preferences were not initialized for the new file
- **False-green refresh**: the macro returned successfully, but the rendered bibliography or citations did not actually update
- **Minimal field payload not refreshable**: rebuilt citations have `id + uri` but lack the `itemData` that Zotero practically needs to refresh reliably
- **Collateral content loss**: citation repair or XML editing accidentally deleted existing manuscript text, tables, legends, or other non-target content
- **DOCX integrity damage**: the file technically exists after editing, but Word opens it with repair prompts, corruption symptoms, or visibly broken layout
- **Wrong numbering after refresh**: Zotero renumbered by true first appearance; this may be expected
- **Metadata gap in a Zotero item**: bibliography renders but one entry is incomplete; fix the Zotero library item itself
- **Dropped first reference during static export**: the exporter mishandled the bibliography anchor paragraph and deleted reference `1`
- **Fake blank gap under `References`**: often a symptom of the same bibliography-anchor bug rather than true paragraph spacing
- **Gray brackets around headings or paragraph ends**: often caused by visible bookmark/navigation anchors from pandoc or Word display settings rather than real manuscript punctuation; inspect bookmark nodes before rewriting content
- **Duplicated first-page title**: often caused by combining YAML/title metadata with a separate `Title Page` heading and `Title:` line in the same DOCX build path
- **Data Availability mismatch**: references may be technically valid, but the journal-facing submission copy may read better with explicit URLs unless author instructions require citation-style formatting
- **Code-like methods prose in narrative sections**: function calls, argument syntax, workspace or authentication details, or monospace fragments can survive from Markdown or script-derived drafting; translate them into methodological prose unless the journal explicitly requires that notation, while allowing only genuinely informative identifiers in Methods
- **Unicode fake superscripts/subscripts**: the document looks acceptable at a glance but uses pasted glyphs instead of Word formatting, making later editing and consistency checks brittle
- **Text extraction looks flat after correct superscripting**: XML or PDF text extraction may show `10-3`; verify the rendered page before treating this as a formatting failure

## Output Contract / 输出约定
When you finish, report:
- which file is the Zotero-editable source document
- which file is the static submission file, if one exists
- which journal-facing formatting adjustments were made, if any
- whether refresh completed successfully
- how many live citation fields and unique Zotero items were verified
- whether document integrity was checked and whether any non-target content changed
- any remaining user-only blocker, narrowed to a single concrete action

When delivering files, prefer wording like:
- `name_zotero.docx` only
- or `name_zotero.docx` + `name.docx`
- or, only for an explicit vetted static-only exception, `name.docx` only
