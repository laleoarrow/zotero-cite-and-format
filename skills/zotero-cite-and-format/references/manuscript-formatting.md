# Manuscript Formatting

Use this reference for title page edits, prose cleanup, tables, figures, supplementary workbooks, symbols, spacing, and visual Word fidelity.

This file is the **common formatting base**. It is not the complete rule set for every manuscript type.

- For reviews, also load `review-manuscripts.md`.
- For original research manuscripts, also load `research-manuscripts.md`.
- Do not assume this common file alone defines review-section or research-section writing requirements.

## Style Anchor First
- If the journal is silent, use the current task's corrected file, approved table, workbook, or user-designated reference as the style anchor.
- Do not import formatting habits from another journal or another project.

## DOCX Fidelity
- For existing formatted blocks, do not replace the whole paragraph or cell text.
- Clone the nearest correct paragraph, cell, or row and replace only the text payload.
- Preserve run properties, paragraph spacing, alignment, font family, and East Asia font settings.
- If the user says formatting is still wrong twice, stop micro-edits and reconstruct from a known-good template block.

## Abstract Block
- Verify the target journal's official abstract word limit before editing length.
- Use the user-approved or authoritative abstract source; do not replace it with a much shorter placeholder.
- Keep the abstract in the main manuscript and any standalone abstract file identical unless the journal explicitly requires different versions.
- Check abstract heading, paragraph style, font, spacing, and page/section placement against the journal or current style anchor.
- Re-check every numerical result in the abstract against the authoritative tables, figures, and supplements.
- If the journal wants structured headings, preserve the exact required labels and order.

## Title Page Block
- Verify the target journal's title-page requirements before changing order or content.
- Source-lock the title page to the user-designated authoritative text.
- Check title, authors, equal-contribution notes, affiliations, corresponding author, address, emails, telephone, funding, disclosures, acknowledgments, and author contributions when present.
- Do not pull title-page metadata, funding ids, or contribution text from older drafts, templates, or temporary intermediate files.
- Preserve the title-page font, paragraph style, line spacing, and page/section breaks from the journal or current style anchor.
- Keep only intended labels bold or italic; do not let the whole statement body inherit label formatting.
- After editing the title page, run a style-drift check on the whole block, not only on the changed sentence.

## Identity Blocks
Source-lock these fields to the user-designated authoritative text:
- title
- author list
- affiliations
- corresponding author block
- funding and grant ids
- disclosures
- acknowledgments
- author contributions

Formatting rules:
- keep only the intended label emphasized
- do not let the whole paragraph inherit bold or italic from the label

## Prose Rules
- Prefer scientific prose over code-style narrative.
- Do not leave function calls, argument strings, workspace paths, or command fragments in abstract, Results, Discussion, or Conclusions unless the journal explicitly requires them.
- In Methods, keep only software and identifiers that materially clarify the analysis.
- Do not introduce unsupported sociology-of-the-field claims.
- Do not pad Discussion citations just to match Introduction counts.
- If abbreviations remain, define them at first use unless already defined earlier.

## Table and Figure Placement
When a target journal is known, verify official instructions for:
- main table placement
- figure legend placement
- figure file delivery format
- supplementary file packaging

If the journal is silent:
- default to main tables in the manuscript body
- default to consolidated figure legends after References
- default to separate uploaded figure files

## Tables
For Main Word Tables and Supplementary Excel Tables formatting rules, see `table-formatting.md`.

## Figures
- Verify file existence, order, legends, callouts, and panel labels.
- If the manuscript implies a combined multi-panel figure, verify that the delivered asset is actually merged.
- Figure-internal text is report-only unless the user authorizes figure editing.
- Do not write A/B panel language in the manuscript if the figure has no A/B panels.

## Formatting Hygiene
- Italicize statistical `P` when journal policy is silent or expects conventional SCI style.
- Do not italicize initials such as `P.Y.`.
- Use true superscript/subscript formatting rather than pasted Unicode look-alikes.
- Keep scientific symbols as real symbols when they carry meaning.
- Preserve section spacing and blank-line behavior from the journal or style anchor.

## Visual Verification
Do not accept XML-only proof for formatting disputes.

Verify visually in Word or another Word-native rendering path:
- title page
- edited body paragraphs
- tables
- supplementary workbooks
- figure legends
