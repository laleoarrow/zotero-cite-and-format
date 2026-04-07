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

Journal-policy response rule:
- If the user has named a target journal, you must explicitly tell the user which of the following is supported by official sources:
  - the journal **requires** a static submission manuscript
  - the journal **recommends** a static submission manuscript
  - no explicit requirement or recommendation was found in the official instructions checked
- Do not leave this implicit.
- If the official instructions are silent or ambiguous, say so explicitly and report the date checked plus the official sources consulted.
- For the operational decision of whether to generate a static submission manuscript, treat the **target journal and its submission system** as the authority.
- If the target journal or submission system does **not explicitly require or recommend** a static submission manuscript, do **not** generate one by default.
- General Zotero guidance about unlinking citations before submission may be reported as background, but it does not by itself justify generating `name.docx` when the journal is silent.

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

Note: the Section-Role Rule in `academic-editing` also governs Introduction/Methods/Discussion structure. If both skills are loaded, this skill's prose rules apply specifically to citation-and-formatting work; for broader manuscript-level rewriting, defer to `academic-editing`.
- Override order for manuscript prose is: target-journal requirement first, then explicit user instruction for the current manuscript scope, then the default anti-code-tone rule. Neither journal silence nor generic reproducibility preference is enough to justify code-style narrative in abstract, Results, Discussion, or Conclusions.
- Do not leave literal function calls, wrapper names, argument strings, or code-style tokens in the abstract, Results, Discussion, or Conclusions unless the target journal explicitly requires them.
- Treat "no code-tone in manuscript narrative" as an explicit default rule, not a stylistic preference. Journal-facing prose should not read like pasted scripts, package calls, or pipeline logs.
- Respect section role as well as sentence style. Introduction paragraphs should usually frame background, prior-literature gap, rationale, and aim; they may discuss limitations of previous studies when that defines the gap, but they should not open by defending limitations of the current study, nested-dataset dependence, or replication caveats unless the target journal explicitly requires that structure.
- Do not introduce unsupported field-wide generalizations into journal-facing prose, such as claims about how large public resources are "often" used, unless the statement is backed by a source and materially needed. When support is absent, rewrite the sentence as a concrete scientific gap or study rationale.
- Do not enforce numeric parity between Introduction and Discussion citations as a manuscript-quality rule. Mainstream guidance evaluates whether citations are balanced, relevant, and useful for the role of each section, not whether the raw counts are similar.
- In Methods, translate implementation into what the analysis did and why it matters. Thresholds, models, endpoint identifiers, software names, and selected identifiers such as dataset codes or outcome labels may remain only when they materially clarify the methodological operation, reproducibility, or source mapping. Raw function calls, `package::function` syntax, argument strings, authentication details, workspace paths, and command fragments should not remain in the main text when a prose translation would convey the method just as well.
- In Methods, report only analysis-relevant software detail. Keep software names or versions only when they materially support reproducibility of the scientific analysis itself. Do not pad the manuscript with agent-side document-building libraries, local asset-generation dependencies, or package inventories that were useful for drafting but are not part of the research method the reader needs to understand or reproduce.
- When supplementary tables are delivered as Excel workbooks, format them as journal-style three-line tables rather than leaving raw spreadsheet defaults. That means: keep a clear in-sheet caption/title, hide worksheet gridlines, avoid colored Excel themes and filter widgets unless the journal explicitly wants them, omit vertical borders, place a rule above and below the header row, and place a closing bottom rule at the end of the table. The workbook should read like a submission-ready table artifact, not like an analysis dump.
- Do not let a Methods cleanup create a catch-all bucket such as "Software, Reporting, and Ethics" unless the target journal explicitly prefers that structure. Put ethics and reporting scope in Study Design or the relevant data-source subsection, and place software details near the analytic step they support.
- If non-independence, nested-cohort dependence, or hierarchy rules must be introduced before Methods, compress them into brief study-rationale language and reserve the full caveat or defense for Methods or Discussion.
- Internal endpoint codes, portal-specific variable names, or study-export labels that do not help an informed reader understand the method should be moved out of the main narrative and, if still needed, into a supplement, note, or reproducibility artifact.
- Avoid monospace/code formatting in running manuscript prose for package names, file paths, function names, or parameter settings unless the target journal explicitly requires it in the main text. If the user wants reproducibility-heavy detail, place that notation in an appendix, supplement, or separate methods artifact rather than in the main narrative by default.
- If a literal identifier must remain, make the surrounding sentence explain the methodological meaning rather than presenting the identifier as if the function name itself were the method.
- Even in Methods, do not let code-like details create visibly different typography from the surrounding text unless the journal explicitly requires a distinct format for such material.
- When target-journal guidance is silent, default to the journal's conventional published prose style rather than to implementation-level notation.
- Citation-balance heuristic: the Introduction should cite enough key background and gap-defining studies without turning into a literature review, whereas the Discussion should cite enough prior work to compare findings, explain agreement or disagreement, and place the results in context. If Discussion is interpretive but sparsely cited, add targeted comparison citations. Only when the Discussion is already adequately supported for its interpretive claims should rebalancing default to trimming Introduction citation stacking rather than padding Discussion just to match counts. This is most useful for disease-burden or mechanism/background claim clusters in the Introduction.
- Discussion-depth heuristic: when the Discussion feels thin, do not solve it by adding generic review citations at random. First diagnose which of the following is missing, then add targeted references accordingly: 1) comparison citations that show where the current findings agree, extend, or diverge from prior cataract or adjacent-disease evidence; 2) clinical-relevance citations that justify why the prioritized panel matters for risk stratification, prevention, or follow-up; 3) translation-boundary citations that explain why the manuscript still stops short of immediate clinical deployment; and 4) mechanism-boundary citations that support plausible biological interpretation without overstating metabolite-specific causality. If these functions require it, increasing the total reference count is appropriate.
- For citation-trimming decisions, define a claim cluster narrowly as one discrete factual assertion, or one tightly linked pair of assertions in the same sentence or adjacent clause that genuinely rely on the same support base. Do not merge several distinct claims into one trimming unit.
- "Most authoritative" does not mean "largest number of reviews." Keep the sources that best support the exact claim being made, usually favoring claim-appropriate primary studies plus at most one major review, guideline, or global-burden source when that broader source is what the sentence actually needs.

Examples:
- Bad abstract/methods carryover: "variants were harmonized with `harmonise_data(action = 2)`"
- Better manuscript prose: "variants underwent allele-frequency-aware strand harmonization, retaining resolvable palindromic variants and excluding unresolved ambiguities"
- Bad workflow wording: "instruments were extracted using JWT-authenticated queries"
- Better manuscript prose: "instruments were obtained through the OpenGWAS interface"
- Bad Introduction carryover: "However, the earlier 120k release is nested within the later 500k release, so cross-release concordance cannot be interpreted as independent replication."
- Better Introduction-level rationale: "We therefore used a prespecified hierarchical triangulation framework to distinguish the primary observational layer from supporting analyses."
- Bad unsupported gap claim: "Large public metabolomics resources are often used descriptively rather than within a prespecified triangulation framework."
- Better evidence-grounded gap: "Existing observational and genetic findings do not yet show which metabolite signals remain prioritized when causal inference and age-stratified population support are considered together."
- Bad mixed-bucket heading: "## Software, Reporting, and Ethics"
- Better Methods placement: put ethics and reporting scope in Study Design, and place software details in the analytic subsection that used them.
- Bad citation-ratio heuristic: "Discussion should have about the same number of citations as the Introduction."
- Better section-role heuristic: "Introduction and Discussion should each have the citations needed for their own job; add or trim references based on background-vs-interpretation needs, not to equalize raw counts."
- Better trimming heuristic: "For dense background claims in the Introduction, once the Discussion is already adequately supported, keep the 2 to 3 most claim-appropriate citations per narrowly defined claim cluster unless the journal or field convention clearly needs more."
- Better Discussion upgrade heuristic: "If Discussion lacks clinical relevance or depth, add the missing comparison, clinical, translation, or mechanism-boundary citations rather than padding with loosely related reviews."

## Output Naming Policy / 输出命名规则
The user-facing manuscript outputs should be named by one stable stem only.

- Editable Zotero manuscript: `name_zotero.docx`
- Static submission manuscript: `name.docx`

Rules:
- The two files, when both exist, should differ only in Zotero editability and any journal-required submission-safe cleanup directly tied to static export.
- Do not create additional user-facing DOCX variants such as `name_revised.docx`, `name_submission_static.docx`, `name_final.docx`, or `name_v2.docx`.
- Internal backups, rebuild checkpoints, and scratch DOCX files belong outside the deliverable folder, for example under `agents/` or another process-artifact location.
- If the journal does not explicitly require or recommend a static submission file, or if the user explicitly prefers Zotero-only output, generate only `name_zotero.docx`.
- Do not let general reference-manager advice override a silent journal. If the journal and submission system do not explicitly require or recommend a static submission file, keep only `name_zotero.docx`.
- Rare exception: if the task is explicitly a vetted static-only deliverable and no Zotero-editable source is requested or in scope, the final deliverable may be `name.docx` only. State that exception explicitly when reporting completion.
- Do not leave a second live Zotero manuscript under another user-facing name or in another deliverable directory. If an internal checkpoint is needed during rebuild, keep it under `agents/` or a temporary path and report only the final `name_zotero.docx`.

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
| A second live DOCX appears during rebuild | Keep only `name_zotero.docx` as the user-facing live manuscript; move internal checkpoints to `agents/` or a temporary path and do not leave a duplicate live deliverable. |
| Cited items exist in Zotero but lack attachment or link children | Add or import a PDF/link child automatically when possible; if automatic attachment fails, ask the user for the missing source before claiming the workflow is complete. |
| DOCX shows gray square brackets around headings or paragraph ends | Suspect pandoc/bookmark display artifacts first; inspect `w:bookmarkStart` / `w:bookmarkEnd` and remove nonessential bookmarks from the submission copy. |
| First page repeats the manuscript title | Treat duplicated title blocks as a document-template problem, not a journal requirement, unless the target journal explicitly requires both a manuscript title and a separate title-page title line in the same file. |
| Data Availability reads like citation-only prose but the journal usually shows direct links | Verify the journal's published style or author instructions; if no contrary rule is found, prefer human-readable resource names plus explicit URLs in the submission copy. |
| Methods prose contains code calls such as `foo(arg = 1)` | Replace the implementation syntax with journal-style methodological prose unless the target journal explicitly requires software-notation detail in the main text. Endpoint IDs or model labels may stay when they aid source mapping, but they should remain typographically consistent with the surrounding prose. |
| Introduction opens with current-study non-independence caveats or defensive hierarchy language | Keep prior-study limitations in the Introduction if they define the gap, but move the full caveat about the current study to Methods or Discussion and keep only concise study-rationale wording in the Introduction unless the journal explicitly wants the caveat there. |
| Introduction contains an unsupported sentence about what researchers usually do with a public resource | Remove the sociology-of-the-field claim unless it is sourced; restate the gap in terms of unanswered scientific or analytical questions. |
| User asks whether Discussion citations should roughly equal Introduction citations | Do not enforce count matching. Check whether the Introduction is balanced and non-review-like, and whether the Discussion has enough citations to compare findings with prior studies and support interpretive claims. If the Discussion is already adequately supported, trim dense Introduction citation stacks before adding new Discussion references just to narrow the gap; otherwise add the missing Discussion citations first. |
| Main-text supplement numbering looks out of order | Check the full supplement package, not only the first visible file. Supplementary numbering should match the actual deliverable set cited in the manuscript. If only one supplement is truly in scope, it should usually be S1; if S1/S2/S4 already exist as deliverables, S3 is not inherently wrong. |
| Methods ends with a leftover `Software, Reporting, and Ethics` bucket | Redistribute ethics/reporting language to Study Design or the relevant source subsection and move software names to the analytic sections that used them, unless the journal explicitly requires a separate heading. |
| STROBE-MR covers only one component of a mixed-design paper | State that the MR component was reported with reference to STROBE-MR where applicable; do not imply that the whole paper fully conforms to the checklist if that is not true. |
| Word manuscript contains markdown-style superscript such as `10^-6^` | Replace it with true Word run-level superscript formatting before treating the file as manuscript-ready. |
| Data Availability says "current workspace", local file paths, or agent-process narration | Rewrite it into manuscript-ready repository or availability language; do not leak local workflow narration into a journal-facing document. |
| References appear as plain text under a `References` heading even though body citations are Zotero-live | This is expected Word behavior when field codes are not being displayed. Verify the presence of the `ADDIN ZOTERO_BIBL` field in the DOCX package or through Word field-code display before concluding that the bibliography is disconnected. |
| User wants supplementary tables as Excel rather than Word/PDF | Export each supplementary table as its own `.xlsx` with journal-style three-line formatting, keep numbering consistent with the main-text citations, and do not leave default spreadsheet gridlines or colored table themes in the deliverable. |
| Main tables were placed only in a supplementary Excel file | Move them back into the main manuscript body unless the target journal explicitly permits main-table-only supplement placement. |
| Figure legends appear scattered throughout the body text | Consolidate all figure legends into a single Figure Legends section after References (or before figures if the journal attaches figures to that section), unless the journal explicitly requires in-text legend placement. |
| Figure image files are embedded inline in the DOCX | Confirm whether the journal requires embedded or separately uploaded figures; for most SCI journals, figures are uploaded as separate high-resolution files and the DOCX body contains only brief callouts plus a consolidated Legends section. |
| Supplementary figure legends are mixed with main-text figure legends | Separate them: main-text legends belong in the main manuscript Legends section; supplementary figure legends belong in the supplementary file alongside those figures. |

## Table and Figure Placement Rule / 表格与图片放置规则（强制执行）

This rule is **mandatory** and must be checked before finalizing any submission package. Placement requirements vary by journal — do not apply any default layout without first checking the target journal's official author instructions.

### Step 0: Journal Policy Lookup (Mandatory) / 期刊政策查询（必须在前）

**When a target journal is known, look up its official author instructions before making any placement decision.**

Required lookups:
- Where must main tables appear? (in-body vs. supplement-permitted vs. end-of-manuscript)
- Where must figure legends appear? (after References, end-of-manuscript, attached to figures, or in-text)
- How must figure files be submitted? (embedded in DOCX vs. separate high-resolution uploads vs. both)
- Are supplementary tables/figures submitted separately or within the same file?

If the journal's author instructions are silent on a specific point, state that explicitly and apply the most conservative default (main tables in body; legends consolidated after References; figures as separate uploads).

Do not apply a prior journal's requirements to a new submission. Each journal must be checked independently.

### Tables / 表格

After confirming journal policy:
- Place main tables (Table 1, Table 2, …) wherever the journal requires — most journals require them in the manuscript body, but some allow or prefer end-of-text placement or separate files.
- Supplementary tables (Supplementary Table S1, S2, …) go in whichever supplementary format the journal specifies (Excel, Word, or within the main file).
- If the user's current placement violates what the journal actually requires, flag it:
  > `[Placement Error] Table X placement does not match [Journal]'s author instructions: [journal requirement]. Current placement: [what the file has].`
- Do not silently leave tables in the wrong location. Do not move tables without verifying journal policy.
- When supplementary tables are delivered as Excel, apply journal-style three-line table formatting: clear caption, hidden gridlines, no colored themes or filter widgets, rules above/below header and at table bottom, no vertical borders.

### Figures / 图片

After confirming journal policy:
- Place figure legends in whatever location the journal specifies. Common variants:
  - Consolidated **Figure Legends** section after References (e.g., IOVS, many ophthalmology/clinical journals)
  - Legends embedded immediately after corresponding figures (some methods/data journals)
  - Legends in a separate legends document
- Figure files: follow the journal's specification (separate high-resolution uploads vs. embedded in DOCX vs. end-of-manuscript).
- The DOCX body should usually contain only figure callouts (e.g., `Figure 1.`) and not full legends or embedded images unless the journal explicitly requires otherwise.
- Supplementary figure legends stay in the supplementary file alongside those figures.
- If the current file's figure legend placement or figure file format violates journal requirements, flag it:
  > `[Placement Error] Figure legends are [current state] but [Journal] requires [journal requirement].`

### Enforcement Actions / 执行动作
Before claiming the submission package is ready:
1. Confirm that journal author instructions were checked for table placement, figure legend placement, and figure file delivery format.
2. Verify that every main table, every figure legend, and every figure are placed/delivered in the journal-required location or format.
3. If any placement violates journal policy, report a `[Placement Error]` block with the specific journal requirement and the current file state, and resolve it before export.
4. If the journal is unknown or instructions are silent, state what default was applied and why.
5. Do not silently produce a noncompliant submission package.

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
- journal chosen but static requirement unknown -> check official instructions first, and still default to `name_zotero.docx` only until a static need is explicitly confirmed by the journal or submission system
- static manuscript explicitly required or recommended -> export `name.docx` in addition to `name_zotero.docx`
- user explicitly wants Zotero-only output -> maintain only `name_zotero.docx`

Interpretation rule:
- target journal or submission system explicitly requires or recommends static manuscript -> generate `name.docx`
- target journal or submission system does not explicitly require or recommend static manuscript -> do **not** generate `name.docx`
- do not elevate general Zotero submission advice into a journal requirement

Communication rule:
- when a target journal is known, completion reports must explicitly say whether that journal requires, recommends, or does not explicitly mention a static submission copy
- if no explicit journal rule was found, state that the working policy is **not to generate a static manuscript** and to keep only the Zotero-editable source document until journal-side evidence says otherwise

Operational rule:
- the Zotero-editable source document is the canonical working manuscript
- the static submission file is a derived artifact, not the primary editing target
- `Unlink Citations` belongs only on the final submission copy, never on the Zotero-editable source
- user-facing deliverables should therefore be either:
  - one file: `name_zotero.docx`
  - or two files: `name_zotero.docx` plus `name.docx`
  - or, only for an explicit vetted static-only exception, one file: `name.docx`
- if no static file is in scope, do not leave any second live manuscript in `manuscript/`, `output/`, or another deliverable directory

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

## Project Collection and Attachment Gate / 项目 collection 与附件闸门
For manuscript workflows, citation validity is not just "the item exists in Zotero."

Required checks:
- Every cited reference must resolve to an existing local Zotero item.
- If a project-specific Zotero collection exists or the user identifies a target collection, every cited item should belong to that collection before completion unless the user explicitly opts out.
- Every cited item should have at least one child attachment or child link when a PDF, DOI landing page, publisher URL, or stable web source can reasonably be attached.

Operational rule:
- If DOI or URL metadata allows automatic attachment, attempt the import or linked attachment first.
- If automatic attachment is not possible or fails, ask the user for the missing PDF or URL before claiming the citation workflow is complete.
- Do not describe a citation set as "fully curated" when most cited items remain metadata-only.
- Best-effort degradation: if the user cannot provide a PDF for a paywalled article, record the gap in the completion report ("item X: metadata-only, no open-access PDF found") rather than blocking the entire workflow.

## Local API Repair / 本地 API 修复
When a rebuild needs authoritative item metadata for `citationItems[].itemData`, use the local Zotero API against `127.0.0.1:23119`:

- `http://127.0.0.1:23119/api/users/0/items/<itemKey>`
- `http://127.0.0.1:23119/api/users/0/items/<itemKey>?format=csljson`

Use `?format=csljson` as the standard repair path for rebuilding `itemData`.

Operational notes:
- prefer non-browser local requests to the local API over browser-origin fetches, which can fail because webpages often cannot read responses from the integrated Zotero HTTP server
- use the API output to repair Zotero field payloads, not as a substitute for official Zotero policy guidance
- if Zotero is not running or the API is unreachable, tell the user to open Zotero first; do not silently skip metadata repair and produce incomplete field payloads
- if Better BibTeX is expected but not installed, note the gap and fall back to the standard Zotero API

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
13. Verify that cited Zotero items satisfy the project collection and attachment gate when that policy is in scope for the project.

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
Unless the target journal says otherwise, treat these as general Word-manuscript rules for English SCI submissions.

Read: `references/sci-formatting.md`.

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
Before claiming success, verify all applicable items for the chosen workflow path:

- the edited `.docx` still opens normally in Word and does not trigger document-repair symptoms attributable to the edit
- the bibliography placeholder has been replaced by a rendered bibliography
- no stale placeholders remain:
  - `{Citation}`
  - `{Bibliography}`
  - duplicated old reference lists
- no previously existing non-target content was accidentally deleted, truncated, or reordered
- headings, body paragraphs, tables, figure legends, and other untouched manuscript regions still match the pre-edit document except for explicitly requested changes
- any retained code-adjacent identifier in Methods still uses the same body-text typography as the surrounding paragraph rather than monospace, backticks, or visually mismatched styling
- verification is based on Word-visible output or a rendered export, not only XML inspection or field counts
- scientific-notation exponents, if present, use true Word superscript formatting rather than pasted Unicode superscript glyphs
- the Zotero-editable source document and any static submission copy have no unintended body-text drift
- the regenerated bibliography count matches the intended unique references
- any style-driven renumbering is explained to the user
- any journal-specific submission rule that matters for the chosen output file has been checked against official author instructions
- citation distribution across Introduction and Discussion has been checked for section-role fit, and no edit was made merely to force similar raw citation counts
- if Introduction citation stacks were trimmed for balance, the edit first confirmed that Discussion interpretive claims were already adequately supported, and then retained the most claim-appropriate 2 to 3 citations for each narrowly defined claim cluster unless the field or journal clearly justified a denser cluster
- if a target journal is known, the user has been explicitly told whether the journal requires, recommends, or does not explicitly mention a static submission manuscript
- no second user-facing live manuscript remains outside `name_zotero.docx` when a static copy is not in scope
- project-collection membership and attachment/link completeness of cited items have been checked when the project policy requires them
- all main tables (Table 1–N) are present in the main manuscript DOCX body and not only in a supplementary file
- all figure legends are consolidated in a single Legends section after References, not scattered in body text, unless the target journal explicitly requires otherwise
- figure image files are confirmed as separate upload assets; if they are embedded inline in the DOCX, journal policy on figure delivery has been checked and confirmed

If a Zotero-editable source document is in scope, also verify:
- the Zotero-editable source document exists and is the canonical manuscript for any later static export
- `docProps/custom.xml` contains the intended Zotero style id and document-preference payload
- the file contains the expected number of `ADDIN ZOTERO_ITEM` fields, but field counts are not treated as sufficient proof
- rendered citations and bibliography text change as expected after refresh
- macro/process success messages alone are not accepted as evidence that refresh happened

If the task is the explicit vetted static-only exception, also verify:
- the completion report explicitly states that no Zotero-editable source document was requested or maintained in scope
- the static submission file satisfies the separate submission-file verification checklist for rendered references, body-text integrity, and field-removal status where applicable

For realistic coverage checks, compare the current task against the cases in `references/validation-cases.md`.

## Smoke Test / 烟测
- "Zotero can no longer recognize or refresh these citations." -> inspect package parts first; do not trust the visible numbers
- "Please make this Word manuscript refreshable in Zotero again." -> rebuild real citation fields, then refresh in Word
- "The refresh macro returned successfully, but the bibliography still didn't appear." -> treat this as a false green; initialize with `Add/Edit Citation`, confirm `Document Preferences`, and verify rendered output
- "Please export a submission-ready copy for AJO." -> verify journal policy first, make sure the Zotero source document is working, then export a separate static file
- "The references now start from 2 after export." -> check the bibliography anchor paragraph before touching spacing

This skill is considered working when it consistently routes these cases to the correct path and the verification checklist can be satisfied on the output files.

## Common Failure Modes / 常见失败模式
Load when diagnosing an unexpected symptom or verifying that the current task's failure is covered.

Read: `references/failure-modes.md`.

## Context Management / 上下文管理
This skill file is large. Follow these rules to manage context:
- Core sections (Accuracy Rule, Source-First Gate, Non-Negotiable Rule, Editable vs Static Split, Preferred Repair Procedure, Verification Checklist) are always needed.
- Reference files should be loaded on demand:
  - `references/official-sources.md` — when verifying Zotero or journal policy
  - `references/validation-cases.md` — when checking failure coverage
  - `references/failure-modes.md` — when diagnosing an unexpected symptom
  - `references/sci-formatting.md` — when doing formatting cleanup
- The Manuscript Prose Rule section overlaps with `academic-editing`'s Section-Role Rule. If both are loaded, this skill governs citation/formatting scope; `academic-editing` governs broader prose structure.

## Output Contract / 输出约定
When you finish, report:
- which file is the Zotero-editable source document
- which file is the static submission file, if one exists
- if a target journal was provided, whether that journal requires, recommends, or does not explicitly mention a static submission copy, with the official source basis and date checked
- which journal-facing formatting adjustments were made, if any
- whether refresh completed successfully
- how many live citation fields and unique Zotero items were verified
- whether cited Zotero items were checked for project-collection membership and how many lacked attachment/link children
- whether document integrity was checked and whether any non-target content changed
- any remaining user-only blocker, narrowed to a single concrete action

When delivering files, prefer wording like:
- `name_zotero.docx` only
- or `name_zotero.docx` + `name.docx`
- or, only for an explicit vetted static-only exception, `name.docx` only
