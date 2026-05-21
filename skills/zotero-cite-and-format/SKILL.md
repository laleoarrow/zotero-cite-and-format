---
name: zotero-cite-and-format
description: Use when Word-facing manuscripts need Zotero live-field repair or verification, bibliography refresh/export, review-vs-research formatting routing, or final package QA after citation and formatting edits.
---

Related skills: `zotero:Zotero` for library search/import/full text; `academic-editing` for broad prose restructuring. This skill owns Word implementation, live-field safety, export routing, and package QA.

# Zotero Cite + Format / Zotero 引文与格式

## Scope
Use this skill for Word-facing manuscript work where Zotero field integrity, DOCX formatting, and submission safety interact.

Do not use it as the primary Zotero library-search or full-text workflow. Route those tasks to `zotero:Zotero` and return here when the manuscript file itself needs work.

## Core Contract
- Primary job: keep the manuscript Word-safe, Zotero-live, and journal-ready.
- Canonical live source is `name_zotero.docx`.
- Create `name.docx` only when the journal or submission system requires or recommends a static copy, or when the user explicitly asks for one.
- Leave at most two user-facing manuscript DOCX files and delete temporary or throwaway variants before finishing.
- Never fake citations, never unlink the canonical live source, and never treat `ADDIN ZOTERO_ITEM` counts alone as proof of correctness.
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
- If footnote markers are converted to symbols, convert the entire sequence consistently.
- If Word starts throwing unreadable-content or repeated open/save failures, stop patching the live file, rebuild from a verified source or clean Word-saved copy, reopen-test from disk, and then remove temporary recovery files.

## Division of Labor
- `zotero:Zotero` owns library search, item lookup, import, full-text retrieval, BibTeX export, and local Zotero API work.
- `academic-editing` owns broad prose restructuring and manuscript voice.
- `zotero-cite-and-format` owns Word live fields, bibliography rendering, static-export routing, manuscript-type formatting, and package-level QA.

## Route First
1. Ask only for missing routing facts: target journal and whether the journal or submission path requires a static manuscript.
2. Choose one active branch:
- `Library / Citation Discovery` -> route to `zotero:Zotero`
- `Live Field / Bibliography` -> read `references/word-zotero-workflow.md`
- `Review Manuscript Formatting` -> read `references/manuscript-formatting.md` + `references/review-manuscripts.md`
- `Research Manuscript Formatting` -> read `references/manuscript-formatting.md` + `references/research-manuscripts.md`
- `Package Final Gate` -> read `references/pre-submission-final-gate.md`
3. Keep only one manuscript-type branch active unless the task truly spans review and research formats.
4. Load auxiliaries only when triggered:
- `references/official-sources.md` for journal policy or Zotero behavior claims
- `references/sci-formatting.md` for symbols, italics, superscripts, and run-level hygiene
- `references/validation-cases.md` for regression comparison
- `references/failure-modes.md` for abnormal failures or repeated DOCX/Word breakage
5. If the journal is unknown or silent, keep only `name_zotero.docx`.
6. Export `name.docx` only from a verified live source.

## Final Gate
Trigger this gate if:
- the user says final, submit, submission, 投稿, 投稿前, 最终, 全文核对, 检查, or names a target journal
- the task follows any citation, table, figure, supplement, title page, funding, author-contribution, abstract, or formatting edit
- the package has already had repeated correctness or formatting failures

Action:
- read `references/pre-submission-final-gate.md`
- do not claim completion until it passes or every remaining issue is reported as a named blocker with exact file and location

## Report Back
Always report:
- Zotero-editable source file
- static submission file, if any
- whether static submission is required, recommended, or silent/not found, with official-source basis and date checked
- journal-facing formatting changes made
- whether refresh completed successfully, if refresh was part of the task
- whether the Mandatory Pre-Submission Final Gate passed, if triggered
- what temporary files or extra variants were removed
- any remaining blocker narrowed to one concrete action

For citation-repair or Zotero-verification tasks also report:
- live citation field count and unique Zotero item count verified
- resolution counts by direct match, DOI, PMID/PMCID, stable URL, and title-author-year fallback
- whether cited items were checked for collection membership and attachment or link completeness
- whether duplicate or near-duplicate Zotero items had to be merged or remapped
