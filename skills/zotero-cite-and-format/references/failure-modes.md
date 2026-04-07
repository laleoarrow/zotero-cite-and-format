# Common Failure Modes / 常见失败模式

This is a catalog of real failure modes observed in Zotero + Word manuscript workflows. Load this file when diagnosing a problem or when verification reveals an unexpected symptom.

## Citation & Field Failures
- **Numbers visible but not live**: the document only contains rendered text
- **Broken bibliography**: a field exists, but stale rendered references were left behind
- **Style dialog blocks automation**: document preferences were not initialized for the new file
- **False-green refresh**: the macro returned successfully, but the rendered bibliography or citations did not actually update
- **Minimal field payload not refreshable**: rebuilt citations have `id + uri` but lack the `itemData` that Zotero practically needs to refresh reliably
- **Wrong numbering after refresh**: Zotero renumbered by true first appearance; this may be expected
- **Metadata gap in a Zotero item**: bibliography renders but one entry is incomplete; fix the Zotero library item itself
- **False bibliography alarm**: the reference list looks like ordinary text in Word, but this may simply be the rendered result of a real `ZOTERO_BIBL` field rather than a broken bibliography

## Export & Static-File Failures
- **Dropped first reference during static export**: the exporter mishandled the bibliography anchor paragraph and deleted reference `1`
- **Fake blank gap under `References`**: often a symptom of the same bibliography-anchor bug rather than true paragraph spacing
- **Second live manuscript left behind**: an internal rebuild checkpoint was treated as a deliverable instead of being kept under `agents/` or a temporary path
- **Supplement numbering drift**: the manuscript cites `Supplementary Table S3` or `S4`, but the actual submission package does not yet contain the corresponding `S1/S2/...` deliverables

## Document Integrity Failures
- **Collateral content loss**: citation repair or XML editing accidentally deleted existing manuscript text, tables, legends, or other non-target content
- **DOCX integrity damage**: the file technically exists after editing, but Word opens it with repair prompts, corruption symptoms, or visibly broken layout
- **Gray brackets around headings or paragraph ends**: often caused by visible bookmark/navigation anchors from pandoc or Word display settings rather than real manuscript punctuation; inspect bookmark nodes before rewriting content
- **Duplicated first-page title**: often caused by combining YAML/title metadata with a separate `Title Page` heading and `Title:` line in the same DOCX build path

## Formatting Failures
- **Unicode fake superscripts/subscripts**: the document looks acceptable at a glance but uses pasted glyphs instead of Word formatting, making later editing and consistency checks brittle
- **Markdown syntax leakage**: the Word manuscript still shows source notation such as `10^-6^` or backticks instead of true Word formatting
- **Text extraction looks flat after correct superscripting**: XML or PDF text extraction may show `10-3`; verify the rendered page before treating this as a formatting failure

## Prose & Content Failures
- **Code-like methods prose in narrative sections**: function calls, argument syntax, workspace or authentication details, or monospace fragments can survive from Markdown or script-derived drafting; translate them into methodological prose unless the journal explicitly requires that notation, while allowing only genuinely informative identifiers in Methods
- **Current-study limitation leakage into the Introduction**: evidence-lock or reviewer-defense wording about non-independence, nested releases, or hierarchy rules drifted into the Introduction and made it read like Methods or Discussion instead of background-gap-aim narrative; this does not mean prior-literature limitations should be removed from the Introduction
- **Mechanical citation-parity chasing**: Introduction and Discussion were padded or trimmed just to make citation counts look similar, instead of fixing the real issue of overreviewing in the Introduction or under-contextualized claims in the Discussion
- **Citation stacking in background claims**: disease-burden or mechanism sentences in the Introduction accumulated 4 to 6 references where 2 to 3 authoritative citations would usually carry the claim more cleanly
- **Methods package-version clutter**: the manuscript lists document-building or workflow-support packages that were useful locally but are not necessary for the reader to understand or reproduce the scientific analysis
- **Data Availability mismatch**: references may be technically valid, but the journal-facing submission copy may read better with explicit URLs unless author instructions require citation-style formatting
- **Metadata-only Zotero curation**: cited items exist in Zotero but most lack child attachments or child links, so the manuscript workflow is not truly source-complete
- **Local-workflow prose leakage**: Data Availability or related sections mention the current workspace, local machine paths, or agent-generated process wording
