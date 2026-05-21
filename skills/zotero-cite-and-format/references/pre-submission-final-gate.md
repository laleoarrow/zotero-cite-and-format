# Pre-Submission Final Gate

Use this reference only for final journal-package checks or after repeated formatting/correctness failures. The goal is to make the last pass deterministic enough that citation, number, table, figure, and style errors are found before the user sees the files.

## Required TODO

Keep a visible TODO list and mark each item as completed, failed, or blocked. If the user raises a new issue mid-task, add it to the TODO before continuing.

1. Lock the authoritative inputs: canonical manuscript, title page text, author list, funding text, author contributions, abstract source, main tables, figures, supplementary figures, supplementary tables, journal name, and journal author-instruction URLs.
2. Enforce a single-writer state: close or avoid stale Word sessions before package-level DOCX edits; reopen from disk after edits.
3. Verify target-journal rules from official sources for manuscript font, abstract length, title page, line numbering, table placement, figure legends, figure file delivery, supplementary files, and whether static/unlinked citations are required. If not found, report "official instructions silent/not found."
4. Establish a task-specific style anchor before formatting. When a corrected package, prior approved table, journal template, or user-designated reference file exists for the current manuscript, inspect the real DOCX/XLSX formatting and clone that concrete style instead of applying mechanical text rules. Record the selected anchor files in the TODO for that task. Do not bake a previous project's files, paths, journal, or visual preferences into the general skill.
5. Verify Zotero integrity: live citation and bibliography fields exist where expected; document preferences exist; field result text matches stored Zotero citation text; bibliography is one continuous Zotero-managed block; no orphaned or duplicate reference blocks remain.
6. Verify citation semantics: for each cited item or a risk-based complete set in large manuscripts, check local Zotero metadata and attachment/abstract/full text where available. Confirm the cited article actually supports the manuscript claim; flag indirect or weak matches. If the title/abstract appears inconsistent with the cited claim, inspect the full text before clearing the citation. If the citation set is too large for the current pass and the user permits delegation, use a bounded subagent review for citation-claim screening.
7. Check abstract parity: the abstract in the main manuscript and any standalone abstract file must match exactly unless the journal requires different forms; word count must satisfy the target journal. Do not leave a shortened placeholder abstract if a fuller approved abstract exists. Verify the official abstract word limit for the target journal and do not underfill by replacing a complete approved abstract with a much shorter draft.
8. Check numeric consistency and asset citation completeness: every numerical result stated in the abstract, Results, Discussion, tables, figures, supplementary figures, and supplementary tables must agree with the authoritative table/figure/supplement source. Every cited table/figure/supplement must exist, every intended main or supplementary asset must be cited or intentionally uncited, and panel labels in text/legends must match the actual figure panels; do not write A/B panel language when the figure has no A/B panels. When the manuscript, legend, or style anchor implies a combined multi-panel figure, verify that the delivered figure asset is actually merged into the expected file rather than left as separate pieces. Record any intentional rounding convention.
9. Check Word typography, grammar, symbols, and spacing: target font/style, direct-format drift, label-only bolding, statistical italic `P`, non-italic author initials such as `P.Y.`, SCI symbols from `references/sci-formatting.md`, plural/count agreement such as participants vs participant, section spacing, blank lines between major sections when journal instructions are silent and the user's reference style uses them, abstract page break/standalone placement, and line numbering scope.
10. Check title page and statement blocks: title, authors, affiliations, correspondence, funding, author contributions, acknowledgments, and disclosures must match the authoritative user/source text exactly where specified. Their font and paragraph style must match the target manuscript style; do not leave the whole body of a label-plus-text paragraph bold merely because the label is bold.
11. Check main Word tables: journal-appropriate three-line style, no vertical borders unless required, top and bottom rules heavier than internal rules when following common SCI three-line tables, no table line numbers unless the journal requires them, and footnotes outside the bordered table body when that is the chosen format. If the journal is silent, first follow the task-specific style anchor; only if no usable anchor exists and the user has stated a preferred default should that default be applied, such as 1.5 pt top/bottom rules and 0.75 pt internal/header separator rules. Verify footnote marker typography against the journal or reference table style; if the marker scheme is changed from alphabetic labels to symbol footnotes, convert the entire sequence consistently and update every corresponding in-table marker and footnote label. Do not leave a partially converted scheme such as early notes changed to `*`, `†`, `‡` while a later note remains `g. Each ...`.
12. Check Excel supplementary tables: hidden gridlines, no colored table themes or filters unless required, clear title/caption, stable column widths, expected wrap behavior for title and footnote cells based on the journal or the style anchor, three-line borders excluding footnotes, correct footnote symbols, and no accidental line numbering. If the journal is silent, first follow the task-specific style anchor; only if no usable anchor exists and the user has stated a preferred default should that default be applied, such as 1.5 pt top/bottom rules and 0.75 pt internal/header separator rules. If the footnote marker scheme is converted, convert the whole sequence consistently rather than leaving mixed alphabetic and symbol markers within the same table.
    For supplementary Excel tables, treat each actual table body or panel body as its own three-line entity. By default:
    - the caption/title row is outside the bordered table body
    - an optional blank spacer row below the title is outside the bordered table body
    - panel-heading rows such as `A.` / `B.` labels are outside the bordered table body unless the style anchor shows them inside
    - the header row carries the top rule and the header-underlining rule
    - the final data row of that body carries the closing bottom rule
    - `Footnote:` separator rows and footnote text rows are outside the bordered table body and should not receive the closing bottom border
    - do not force wrap in title rows, spacer rows, or short footnote-label rows just because cells were merged narrowly; use widths/merges that let the caption and footnote block read naturally
    - long footnote sentences may wrap naturally within a wide merged text row, but the wrap should come from readable layout rather than a cramped title/footnote box
13. Check figure package: file existence, order, panel labels, legend/callout consistency, multi-panel merge state, and internal text scan. Do not edit figure internals unless explicitly authorized; report exact figure/panel text that needs user action.
14. Check language only to the requested depth. If the user asks for "list only" language polishing, list concise candidate edits without applying them; otherwise, fix clear grammar errors in the manuscript when the current task authorizes manuscript editing.
15. Final report must state what passed, what was changed, what official sources were checked, and every unresolved blocker by file and location.

## Failure Behavior

- A missing official journal rule is not permission to invent one.
- A field count without rendered-result and metadata checks is not Zotero verification.
- A Word XML property check without Word-native or rendered visual confirmation is not enough for disputed formatting.
- A figure text problem is not permission to edit figure artwork.
- Do not create extra static DOCX, backup, or duplicate deliverables unless the journal or user explicitly requires them.

## Optional Codex Hooks

Use hooks only as deterministic local gates when the project trusts the hook command. Project-local hooks should live in Codex-supported hook config such as `.codex/hooks.json` or `.codex/config.toml`, and only run after the project `.codex/` layer is trusted. Hooks should fail fast with actionable messages and must not auto-edit manuscripts, fetch web pages, or make semantic citation judgments.

Preferred Codex hook placement:
- `PostToolUse` after DOCX/XLSX edits for deterministic file scans
- `Stop` as a final-answer blocker when a required gate item is still unverified

For `Stop`, emit valid JSON or the Codex-supported blocking exit pattern; do not rely on transcript parsing as a stable API.

Good hook candidates:
- after DOCX/XLSX edits, scan for Zotero field counts and stored/result mismatches
- scan edited DOCX runs for non-target fonts, accidental whole-paragraph bold/italic, and missing italic statistical `P`
- compare abstract text and word count across main and standalone abstract files
- scan main/supplementary tables for borders, wrapText, gridline visibility, footnote borders, and line-number contamination
- scan figure PDFs/images for known forbidden phrases and panel-label inconsistencies, then report only

Do not assume hooks are installed. If useful, offer to add a project-local hook configuration and a deterministic check script; otherwise run the checks manually and report the outputs.
