---
name: zotero-cite-and-format
description: Use when Word-facing manuscripts need Zotero live-field creation, repair, or verification; dynamic bibliography refresh; review-vs-research formatting routing; table and supplement formatting (Excel/Word); or final package QA. Require every citation-bearing DOCX deliverable to retain dynamic Zotero citation and bibliography fields.
---

Related skills: `zotero:Zotero` for library search/import/full text; `academic-editing` for broad prose restructuring. This skill owns Word implementation, dynamic-field safety, and package QA.

# Zotero Cite + Format / Zotero 引文与格式

## Scope
Use this skill for Word-facing manuscript work where Zotero field integrity, DOCX formatting, table/supplement aesthetics (including SCI-standard Excel supplementary tables), and submission safety interact.

Do not use it as the primary Zotero library-search or full-text workflow. Route those tasks to `zotero:Zotero` and return here when the manuscript file itself needs work.

## Core Contract
- Primary job: keep the manuscript Word-safe, Zotero-live, and journal-ready.
- Treat every citation-bearing DOCX as a Zotero-live source regardless of filename. Respect the requested filename; do not require a `_zotero` suffix.
- Deliver one user-facing manuscript DOCX by default. If the user explicitly requests additional Word variants, retain dynamic Zotero citation and bibliography fields in every variant.
- Delete temporary or throwaway variants before finishing.
- Never fake citations, unlink or flatten Zotero fields, deliver a static citation copy, or replace Zotero fields with typed citation numbers or a static reference list.
- Require an active `ADDIN ZOTERO_ITEM` field for every visible manuscript citation and an active `ADDIN ZOTERO_BIBL` field for every visible Zotero-managed reference list.
- Never treat field counts alone as proof of correctness.
- Every Word-facing output must pass the SCI typography rules in `references/sci-formatting.md`: statistical italic `P`, true Word superscript/subscript, scientific notation, real symbols, and no Markdown/code markup leaks.
- The SCI typography pass is blocking. After the last save or refresh, run it on every delivered DOCX. Do not report completion unless unresolved candidates are zero or every remaining candidate is reported with exact file and location.
- Keep a visible TODO on multi-step work; append new issues before continuing.

## Hard Rules
- Verify official journal instructions before claiming journal-specific formatting rules.
- Do not ask whether a static or unlinked manuscript is required; citation storage is fixed to dynamic Zotero fields under this skill.
- If official journal instructions or a submission system require removal of field codes or reject live fields, report the exact incompatibility as a blocker. Do not create an unlinked or flattened copy.
- If the journal is silent, use the current task's style anchor, not memory or another project.
- Verify abstract parity and target-journal word limit.
- If a manuscript claim does not fit a citation title or abstract, inspect the full text before clearing that citation.
- Figure-internal text is report-only unless the user explicitly authorizes figure editing.
- For existing formatted Word blocks, clone the block or row and replace only the text payload; do not overwrite whole paragraphs or cells with `paragraph.text = ...` or `cell.text = ...`.
- Preserve label-only emphasis; do not leave whole label-plus-body paragraphs accidentally bold or italic.
- Format statistical `P` correctly and never italicize initials such as `P.Y.`.
- Format scientific notation and exponents with real Word runs: use `×` and true superscript for powers, never Unicode fake superscripts or Markdown exponent syntax.
- When editing or inserting Zotero live fields, do not rely on `python-docx` paragraph text, visible `ADDIN ZOTERO_ITEM` counts, or XML payload presence alone as proof that the field still renders correctly in Word. A field can still leak raw `instrText` into the page if `begin/separate/end` structure is broken.
- Prefer cloning a known-good Zotero field cluster from the same document or fully rebuilding the affected citation cluster. Do not partially splice citation runs by guessed indices without a structural validation pass.
- Before reporting completion for any DOCX edit or DOCX creation, run a deterministic SCI typography scan plus rendered/Word-native visual verification. The scan must cover body text, Word tables, headers, footers, footnotes/endnotes, accessible text boxes, and bibliography/reference blocks, not only the edited pages.
- Verification must inspect Word run properties, not only extracted text or visual appearance: statistical `P` must be italic at run level, and scientific exponents must be true superscript runs.
- If footnote markers are converted to symbols, convert the entire sequence consistently.
- If Word starts throwing unreadable-content or repeated open/save failures, stop patching the live file, rebuild from a verified source or clean Word-saved copy, reopen-test from disk, and then remove temporary recovery files.

## Division of Labor
- `zotero:Zotero` owns library search, item lookup, import, full-text retrieval, BibTeX export, and local Zotero API work.
- `academic-editing` owns broad prose restructuring and manuscript voice.
- `zotero-cite-and-format` owns Word live fields, bibliography rendering, manuscript-type formatting, table and supplement formatting, and package-level QA.

## Route First
1. Ask only for missing routing facts needed for formatting, such as the target journal. Do not create a citation-storage decision branch: all citation-bearing DOCX outputs remain Zotero-live.
2. Choose one active branch:
- `Library / Citation Discovery` -> route to `zotero:Zotero`
- `Live Field / Bibliography` -> read `references/word-zotero-workflow.md`
- `Table / Supplement Formatting` -> read `references/table-formatting.md`
- `Review Manuscript Formatting` -> read `references/manuscript-formatting.md` + `references/review-manuscripts.md`
- `Research Manuscript Formatting` -> read `references/manuscript-formatting.md` + `references/research-manuscripts.md`
- `Package Final Gate` -> read `references/pre-submission-final-gate.md`
3. Keep only one manuscript-type branch active unless the task truly spans review and research formats.
4. Load auxiliaries only when triggered:
- `references/official-sources.md` for journal policy or Zotero behavior claims
- `references/validation-cases.md` for regression comparison
- `references/failure-modes.md` for abnormal failures or repeated DOCX/Word breakage
5. Always load `references/sci-formatting.md` before creating, editing, refreshing, or verifying a Word-facing manuscript file.
6. Keep one user-facing DOCX by default and use the filename requested by the user.
7. Never export or unlink a static citation copy. If an external submission path cannot accept live fields, stop at a named blocker while preserving the verified dynamic manuscript.

## Zotero Field Integrity Gate
Run this gate whenever you insert, repair, clone, or rewrite any live Zotero citation or bibliography field.

1. Structural scan:
```bash
python3 scripts/check_zotero_fields.py /path/to/file.docx
```
- This must pass with a nonzero Zotero citation-field count, exactly one Zotero bibliography field, and `begin/instr/separate/text/end` structure for every citation field.
- `NO_ZOTERO_CITATION_FIELDS`, `NO_ZOTERO_BIBLIOGRAPHY_FIELD`, or `MULTIPLE_ZOTERO_BIBLIOGRAPHY_FIELDS` is a hard failure for a citation-bearing manuscript.
- A nonzero exit means the field cluster is broken even if the DOCX still opens.

2. Rendered-text leak scan:
```bash
soffice -env:UserInstallation=file:///tmp/lo_profile_$$ --headless --convert-to pdf --outdir /tmp/docx_check /path/to/file.docx
pdftotext /tmp/docx_check/$(basename /path/to/file.docx .docx).pdf /tmp/docx_check/out.txt
rg -n 'ADDIN ZOTERO_ITEM|CSL_CITATION|http://zotero.org/groups/|\"citationItems\":|\"formattedCitation\":' /tmp/docx_check/out.txt
```
- Any match is a hard failure. It means Word-visible field code leaked into the rendered document.

3. Run-level formatting scan for edited statistics:
- Check each edited `P` value at run level: statistical `P` must be italic.
- Check each edited scientific notation exponent at run level: the exponent must be true superscript.
- If the edited paragraph contains both live fields and scientific notation, verify both the field gate and the run-format gate before delivery.

4. Visual gate:
- Re-render the affected page(s) and inspect them. Do not stop at XML success.
- If a rendered page still shows raw field code or unformatted exponents, rebuild the affected field cluster from a known-good source and rerun the full gate.

## Final Gate
Trigger this gate if:
- the user says final, submit, submission, 投稿, 投稿前, 最终, 全文核对, 检查, or names a target journal
- the task follows any citation, table, figure, supplement, title page, funding, author-contribution, abstract, or formatting edit
- the package has already had repeated correctness or formatting failures

Action:
- read `references/pre-submission-final-gate.md`
- do not claim completion until it passes or every remaining issue is reported as a named blocker with exact file and location
- if the task touched live Zotero fields, the Zotero Field Integrity Gate above is also mandatory

## Report Back
Always report:
- each delivered Zotero-live DOCX file
- confirmation that every delivered citation-bearing DOCX retains dynamic citation and bibliography fields and that no static or unlinked copy was created
- any verified journal or submission-system conflict with live fields as a named blocker, with official-source basis and date checked
- journal-facing formatting changes made
- SCI typography checks completed, including statistical italic `P`, scientific notation superscripts, real symbols, Markdown/code-markup leaks, and visual/rendered verification
- whether the Zotero Field Integrity Gate passed, including structural scan, rendered-text leak scan, and page-level visual verification, if live fields were touched
- whether refresh completed successfully, if refresh was part of the task
- whether the Mandatory Pre-Submission Final Gate passed, if triggered
- what temporary files or extra variants were removed
- any remaining blocker narrowed to one concrete action

For citation-repair or Zotero-verification tasks also report:
- live citation field count and unique Zotero item count verified
- resolution counts by direct match, DOI, PMID/PMCID, stable URL, and title-author-year fallback
- whether cited items were checked for collection membership and attachment or link completeness
- whether duplicate or near-duplicate Zotero items had to be merged or remapped
