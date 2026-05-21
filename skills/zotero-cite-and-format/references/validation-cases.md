# Validation Cases

These are not synthetic examples. They come from the actual failure modes encountered while rebuilding a Word + Zotero manuscript.

Use them to decide whether the skill really covers the current task.

## Section Index
- Cases 1-3: live-field recovery, style initialization, static export failure
- Cases 4-5: when static submission is or is not needed
- Cases 6-8: false-green refresh, content loss, manual bibliography pressure
- Case 9: IOVS regression case for repeated formatting/correctness failures

## Case 1: Recover live citations from a flattened AJO manuscript

### Input
- Word `.docx` with citation-like numbers in the body
- broken or missing Zotero live fields
- valid Zotero library items available locally

### Expected handling
- identify the file as a Zotero-recovery task, not a prose task
- rebuild citation fields with real `itemID + uri + itemData`
- obtain `itemData` from the local Zotero API using `?format=csljson`
- reinitialize document preferences for the target style
- refresh in Word and regenerate the bibliography

### Success criteria
- citation fields exist again
- bibliography field exists again
- Word Zotero refresh completes

## Case 2: First refresh triggers the style dialog

### Input
- rebuilt Word manuscript with correct field structure
- Zotero document preferences not yet accepted by Word/Zotero

### Expected handling
- recognize this as first-time style initialization, not immediate document corruption
- run `ZoteroAddEditCitation` before trusting `ZoteroRefresh`
- choose the correct journal style and confirm `Store Citations as: Fields` unless interoperability requires `Bookmarks`
- rerun refresh after confirmation

### Success criteria
- bibliography is rendered
- no placeholder bibliography remains
- rendered citations or bibliography visibly change, rather than only the macro returning success

## Case 3: Static export silently drops reference 1

### Input
- live Zotero manuscript with a bibliography field
- naive XML-level field stripping during static export

### Observed failure
- `References` heading followed by a large blank-looking gap
- bibliography starts from `2.`

### Root cause
- reference `1` was rendered inside the same paragraph as the Zotero bibliography field anchor
- export logic removed the anchor paragraph instead of preserving its rendered result runs

### Success criteria
- `ZOTERO_ITEM = 0`
- `ZOTERO_BIBL = 0`
- `References` is followed immediately by `1.`

## Case 4: Journal policy requires static submission

### Input
- working Zotero-editable source document
- target journal author instructions explicitly require field codes to be removed before submission

### Expected handling
- keep the Zotero-editable source as the working document
- export a separate static submission copy
- do not overwrite the Zotero-editable source document with the flattened version

### Success criteria
- two files exist with different roles
- the submission copy is field-free
- the Zotero source remains refreshable

## Case 5: Journal not yet chosen

### Input
- manuscript still under active editing
- no confirmed target journal

### Expected handling
- ask whether a static submission file is actually needed
- if not confirmed, maintain only the Zotero-editable source

### Success criteria
- no unnecessary static export
- no duplicate maintenance burden introduced by habit

## Case 6: Refresh looks successful but is operationally a no-op

### Input
- rebuilt manuscript with live-looking Zotero field counts
- `ZoteroRefresh` or automation returns successfully
- bibliography placeholder remains missing or stale, or citations do not visibly update

### Expected handling
- do not accept macro success or field counts as sufficient evidence
- rerun the workflow as `ZoteroAddEditCitation -> Document Preferences -> ZoteroRefresh`
- verify the style id in `docProps/custom.xml`
- verify the rendered bibliography and citations in Word-visible output

### Success criteria
- bibliography placeholder is gone
- rendered bibliography block exists
- rendered citations and bibliography reflect the intended style and metadata

## Case 8: Citation repair succeeds but the manuscript loses existing content

### Input
- Word manuscript with valid non-reference content already present
- an edit path that touches XML, fields, or bibliography structure
- risk that a targeted repair accidentally deletes unrelated paragraphs, headings, tables, or legends

### Expected handling
- do not create user-facing backup variants unless the user explicitly asks; if a high-risk temporary checkpoint is needed, keep it outside the deliverable set and remove it before final reporting
- define the intended edit scope narrowly
- compare the edited document against the pre-edit baseline in Word-visible output, not just by field counts
- reject the result as failed if non-target content disappears or the document opens with corruption symptoms

### Success criteria
- the edited document opens normally in Word
- all non-target manuscript content remains present unless the user explicitly requested its removal
- only the intended citation, bibliography, or formatting regions changed

## Case 7: User wants to keep editing but also asks for manual bibliography tweaks

### Input
- Zotero-editable Word source document
- user asks for a manual bibliography tweak or field removal while still planning to keep editing with Zotero

### Expected handling
- keep the editable source untouched as the canonical manuscript
- explain that manual bibliography editing belongs only in a duplicated final submission copy after `Unlink Citations`
- if a static deliverable is needed, derive it from the verified source rather than unlinking the source itself

### Success criteria
- the Zotero-editable source remains refreshable
- any unlink or manual bibliography edits occur only in the duplicated submission copy

## Case 9: IOVS final package after repeated formatting and correctness failures

This is a regression case from one manuscript package, not a global rule source. Use it to recognize the failure pattern; do not copy IOVS-specific paths, preferences, or requirements to other journals.

### Input
- target journal is IOVS
- user reports mismatched abstract versions, underfilled abstract, incorrect title page or author contributions, stale funding text, inconsistent numbers between prose and tables/figures/supplements, uncited supplementary assets, figure panel labels in text that do not exist in the figure, figure-internal text concerns, malformed three-line tables, footnote rows included inside table borders, ugly title/footnote wrapping in supplementary tables, line numbers inside tables, font drift, bold labels/body drift, non-italic statistical `P`, SCI symbol drift, grammar/count-noun errors, and citation semantics needing Zotero verification
- user reports mismatched abstract versions, underfilled abstract, incorrect title page or author contributions, stale funding text, inconsistent numbers between prose and tables/figures/supplements, uncited supplementary assets, figure panel labels in text that do not exist in the figure, figure-internal text concerns, malformed three-line tables, partially converted footnote-marker sequences such as `a, b, c ... g` becoming mixed `*, †, ‡ ... g`, footnote rows included inside table borders, ugly title/footnote wrapping in supplementary tables, line numbers inside tables, font drift, bold labels/body drift, non-italic statistical `P`, SCI symbol drift, grammar/count-noun errors, and citation semantics needing Zotero verification

### Expected handling
- trigger the Mandatory Pre-Submission Final Gate and maintain a visible TODO list
- if the user raises new problems during the pass, append them to the TODO immediately before continuing
- verify official IOVS instructions before asserting abstract length, font, line numbering, table/figure placement, static/unlinked citation needs, or supplementary file requirements
- use the corrected files from the current manuscript package as style anchors for journal-silent formatting details; inspect and clone their actual formatting instead of applying mechanical replacements from memory
- keep only the Zotero-editable source unless IOVS or the user explicitly requires a static copy
- preserve live Zotero fields and verify stored citation data against rendered text and local Zotero metadata
- when Zotero metadata title/abstract appears mismatched to the citation claim, inspect the full text before clearing that reference
- check every manuscript number against the authoritative table, figure, supplementary figure, or supplementary table source
- check every table/figure/supplement citation against existing assets, including whether panel labels such as A/B actually exist
- when the manuscript implies one combined figure, verify that the file package actually contains the merged figure rather than unmerged component pieces
- repair Word and Excel formatting at run/table-border level without rewriting unrelated content
- format main and supplementary tables as true three-line tables; do not include title rows, spacer rows, `Footnote:` rows, or footnote text rows inside the three-line body; treat each panel body as its own three-line entity when the sheet contains multiple panels; follow official journal rules or the task-specific style anchor when the journal is silent
- report figure-internal text problems without editing artwork unless the user authorizes figure editing
- list language polish candidates only when the user asks for review-only language suggestions

### Success criteria
- final report states the canonical file, journal sources checked, abstract word count and parity, Zotero field/metadata status, numeric consistency status, table/supplement formatting status, figure report-only issues, and all unresolved blockers
- no extra backup, duplicate static, or stale intermediate deliverables are left in the user-facing submission folder
