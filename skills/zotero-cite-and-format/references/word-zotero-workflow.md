# Word + Zotero Workflow

Use this reference for live-field repair, bibliography rebuilds, static export, or Word/Zotero refresh failures.

## Section Index
- Canonical source and single-writer safety
- Minimum live-Zotero shape and package inspection
- Citation repair and local Zotero access
- Style initialization and repair sequence
- Bibliography span and static export
- Static-file verification
- Modified-citation prompt handling
- Collection/attachment gate and automation notes

## Canonical Source
- Repair or verify the live Zotero source first.
- Treat `name_zotero.docx` as canonical.
- Never unlink the canonical source.
- Export `name.docx` only from the verified live source.

## Single-Writer Rule
- Before package-level edits, check whether the DOCX is open in Word.
- Do not let a stale Word window save over an externally repaired file.
- After XML/package edits, reopen the document from disk before Word/Zotero actions.

## Minimum Live-Zotero Shape
- citation fields exist in `word/document.xml`
- bibliography field exists when bibliography regeneration is required
- Zotero document preferences exist in `docProps/custom.xml`
- citation items resolve to real local Zotero items

Field signatures:
- citation: `ADDIN ZOTERO_ITEM CSL_CITATION {json}`
- bibliography: `ADDIN ZOTERO_BIBL ... CSL_BIBLIOGRAPHY`

## Package Inspection
Inspect:
- `word/document.xml`
- `docProps/custom.xml`
- `customXml/item1.xml`
- `customXml/itemProps1.xml`
- `customXml/_rels/item1.xml.rels`

Check:
- `ADDIN ZOTERO_ITEM` and `ADDIN ZOTERO_BIBL`
- style id and Zotero preferences
- placeholder remnants such as `{Citation}` or `{Bibliography}`
- duplicated static reference lists
- long `w:instrText` payloads reconstructed across runs

## Citation Repair Rules
- Resolve citations in this order: existing item key -> DOI -> PMID/PMCID -> arXiv/repository id -> stable URL -> title/author/year fallback.
- Standardize rebuilt `citationItems[].itemData` from the local Zotero API with `?format=csljson`.
- If two Zotero items share the same DOI or PMID, treat them as duplicates unless there is clear contrary evidence.
- Do not mark a citation fully verified when it only survived title/author/year fallback.

## Local Zotero Access
Use the local API:
- `http://127.0.0.1:23119/api/users/0/items/<itemKey>`
- `http://127.0.0.1:23119/api/users/0/items/<itemKey>?format=csljson`

If Zotero is unavailable:
1. try the local MCP path
2. check whether Zotero.app is already running
3. if not running, launch Zotero
4. wait for `127.0.0.1:23119`
5. retry before asking the user to intervene

## Style Initialization
Before trusting `ZoteroRefresh`:
1. run `ZoteroAddEditCitation`
2. accept or initialize `Document Preferences`
3. confirm the intended style and `Fields` storage mode unless `Bookmarks` is genuinely required
4. run `ZoteroRefresh`

Do not treat a successful macro return code as proof that refresh actually happened.

## Repair Sequence
1. identify the canonical live source
2. inspect package parts and current field state
3. rebuild missing live citations and bibliography if needed
4. initialize style in Word
5. refresh in Word
6. reopen from disk and verify the rendered result
7. verify that non-target content was not lost
8. only then decide whether a static copy is needed

## Bibliography Span Check
Do not accept `ADDIN ZOTERO_BIBL = 1` by itself.

Also verify:
- the bibliography field does not terminate inside reference 1
- the first bibliography `fldCharType="end"` closes after the intended reference block
- the reference list is one continuous Zotero-managed block

## Static Export
1. duplicate `name_zotero.docx` to `name.docx`
2. unlink only on `name.docx`
3. preserve non-Zotero fields such as page numbering unless asked otherwise
4. special-case the Zotero bibliography anchor paragraph
5. verify the rendered reference list immediately after export

Bibliography anchor gotcha:
- reference 1 may live in the same paragraph as the `ADDIN ZOTERO_BIBL` field
- naive field stripping can silently delete reference 1

## Static-File Verification
For `name.docx`, verify:
- `ZOTERO_ITEM = 0`
- `ZOTERO_BIBL = 0`
- `References` is followed immediately by reference 1
- the heading is not orphaned from the bibliography
- body text matches the vetted live source
- bookmarks or navigation artifacts do not render visibly

## Modified-Citation Prompt
If Word/Zotero says the citation was modified:
- inspect `plainCitation`
- inspect `formattedCitation`
- inspect `citationItems` order
- inspect the rendered result text

If they disagree:
- normalize the field payload to the rendered result
- if the mismatch is only order/range collapse, reorder `citationItems`
- do not call the file repaired while repeated prompts remain

## Collection and Attachment Gate
- Every cited item must resolve to a local Zotero item.
- If the project has a target collection, cited items should belong to it unless the user opts out.
- Add a child attachment or stable child link when reasonably possible.
- If a paywalled PDF cannot be obtained, report the item as metadata-only rather than silently calling the set fully curated.

## Automation Notes
- macOS Word macros: `ZoteroRefresh`, `ZoteroAddEditCitation`, `ZoteroAddEditBibliography`
- AppleScript form: `run VB macro macro name "ZoteroRefresh"`
- If automation hits a modal dialog it cannot clear, reduce the blocker to that one click
