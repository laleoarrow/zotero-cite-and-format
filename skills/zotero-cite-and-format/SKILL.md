---
name: zotero-cite-and-format
description: Use when Word-facing manuscripts need Zotero live-field repair or verification, bibliography refresh/export, review-vs-research formatting routing, table and supplement formatting (Excel/Word), or final package QA.
---

Related skills: `zotero:Zotero` for library search/import/full text; `academic-editing` for broad prose restructuring. This skill owns Word implementation, live-field safety, export routing, and package QA.

# Zotero Cite + Format / Zotero 引文与格式

## Scope
Use this skill for Word-facing manuscript work where Zotero field integrity, DOCX formatting, table/supplement aesthetics (including SCI-standard Excel supplementary tables), and submission safety interact.

Do not use it as the primary Zotero library-search or full-text workflow. Route those tasks to `zotero:Zotero` and return here when the manuscript file itself needs work.

## Core Contract
- Primary job: keep the manuscript Word-safe, Zotero-live, and journal-ready.
- Canonical live source is `name_zotero.docx`.
- Create `name.docx` only when the journal or submission system requires or recommends a static copy, or when the user explicitly asks for one.
- Leave at most two user-facing manuscript DOCX files and delete temporary or throwaway variants before finishing.
- Never fake citations, never unlink the canonical live source, and never treat `ADDIN ZOTERO_ITEM` counts alone as proof of correctness.
- Every Word-facing output must pass the SCI typography rules in `references/sci-formatting.md`: statistical italic `P`, true Word superscript/subscript, scientific notation, real symbols, and no Markdown/code markup leaks.
- The SCI typography pass is blocking. After the last save, refresh, or export, run it on every delivered DOCX, including the Zotero-live source and any static submission copy. Do not report completion unless unresolved candidates are zero or every remaining candidate is reported with exact file and location.
- Keep a visible TODO on multi-step work; append new issues before continuing.

## Hard Rules
- Verify official journal instructions before claiming static-copy policy or journal-specific formatting rules.
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
- `zotero-cite-and-format` owns Word live fields, bibliography rendering, static-export routing, manuscript-type formatting, table and supplement formatting, and package-level QA.

## Route First
1. Ask only for missing routing facts: target journal and whether the journal or submission path requires a static manuscript.
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
5. Always load `references/sci-formatting.md` before creating, editing, exporting, or verifying a Word-facing manuscript file.
6. If the journal is unknown or silent, keep only `name_zotero.docx`.
7. Export `name.docx` only from a verified live source.

## Zotero Field Integrity Gate
Run this gate whenever you insert, repair, clone, or rewrite any live Zotero citation or bibliography field.

1. Structural scan:
```bash
python3 scripts/check_zotero_fields.py /path/to/file.docx
```
- This must pass with `OK: all Zotero live fields have begin/instr/separate/text/end structure`.
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
- Zotero-editable source file
- static submission file, if any
- whether static submission is required, recommended, or silent/not found, with official-source basis and date checked
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
