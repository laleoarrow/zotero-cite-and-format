# Official Sources

Use these sources before making any operational claim that affects a manuscript, a Zotero field, or submission behavior.

## Zotero official knowledge base

- Using the Zotero Word Plugin  
  https://www.zotero.org/support/word_processor_plugin_usage

- Word Processor Plugins  
  https://www.zotero.org/support/word_processor_integration

- Word Processor Plugin Troubleshooting  
  https://www.zotero.org/support/word_processor_plugin_troubleshooting

- Cite preferences  
  https://www.zotero.org/support/preferences/cite

- Connector HTTP server  
  https://www.zotero.org/support/dev/client_coding/connector_http_server

- Moving documents between word processors  
  https://www.zotero.org/support/kb/moving_documents_between_word_processors

- Word field codes  
  https://www.zotero.org/support/kb/word_field_codes

- Existing citations not detected  
  https://www.zotero.org/support/kb/existing_citations_not_detected

- Troubleshooting errors in word processor documents  
  https://www.zotero.org/support/kb/debugging_broken_documents

- Citations not updating  
  https://www.zotero.org/support/kb/citations_not_updating

Operational rules grounded in the official Zotero support pages above:

- Editable Word source documents should normally store citations as `Fields`; Zotero explicitly says to use `Bookmarks` only when Word/LibreOffice compatibility is actually needed.
- If citation output is wrong, fix the Zotero item metadata first and then use `Refresh`; do not hand-edit the live bibliography in the Zotero source document and assume it will stay correct.
- `Unlink Citations` is irreversible and belongs on a final copy only, not on the Zotero-editable source manuscript.
- Opening a Word or LibreOffice manuscript in another processor without Zotero's conversion workflow can break active citations; use Zotero's documented transfer steps or explicit interoperability mode instead of ad hoc opening/saving.

## Zotero official Word integration repositories

- macOS Word integration  
  https://github.com/zotero/zotero-word-for-mac-integration

- Windows Word integration  
  https://github.com/zotero/zotero-word-for-windows-integration

Use the integration repos only when implementation detail matters, such as macro names, initialization flow, or document-preference behavior.

## Journal author instructions

Always verify the target journal's submission rules from its official author instructions.

Do not assume one publisher's policy applies to all of its journals, and do not assume different publishers handle references, file formats, or submission systems the same way.

Major official entry points by publisher and platform (checked 2026-04-02):

- ARVO / IOVS journal author instructions  
  IOVS Instructions to Authors  
  https://iovs.arvojournals.org/ss/forauthors.aspx

- Elsevier journal Guide for Authors pages on ScienceDirect  
  Example: American Journal of Ophthalmology Guide for Authors  
  https://www.sciencedirect.com/journal/american-journal-of-ophthalmology/publish/guide-for-authors

- Wiley Author Help Center and manuscript preparation guidance  
  https://authors.wiley.com/help/index.html  
  https://authorservices.wiley.com/author-resources/Journal-Authors/Prepare/manuscript-preparation-guidelines.html/index.html

- Springer Nature / Springer journal submission-guidelines pages  
  Springer support entry point:  
  https://support.springer.com/en/support/solutions/articles/6000083753-locate-submission-instructions-for-a-springer-journal  
  Example Springer journal pattern:  
  https://link.springer.com/journal/10384/submission-guidelines

- Taylor & Francis Author Services and journal Instructions for Authors pages  
  https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/get-familiar-with-the-instructions-for-authors/

- Oxford University Press / Oxford Academic author-guidelines pages  
  Example OUP author-guidelines pattern:  
  https://academic.oup.com/oxfordopenjournals/pages/author_guidelines

- BMJ Author Hub  
  https://authors.bmj.com/

- Frontiers author guidelines  
  https://www.frontiersin.org/guidelines/author-guidelines

- PLOS submission-guidelines pages  
  Example: PLOS Medicine Submission Guidelines  
  https://journals.plos.org/plosmedicine/s/submission-guidelines  
  Example: PLOS ONE Submission Guidelines  
  https://journals.plos.org/plosone/s/submission-guidelines

- MDPI Instructions for Authors pages  
  General authors portal:  
  https://www.mdpi.com/authors  
  Example journal instructions pattern:  
  https://www.mdpi.com/journal/J/instructions

- Wolters Kluwer / Lippincott journals  
  Lippincott author portal:  
  https://journals.lww.com/authorservices/pages/default.aspx  
  Editorial Manager tutorial noting that journal-specific Instructions for Authors are reached from each journal's submission banner:  
  https://www.wolterskluwer.com/en/expert-insights/authors-editorial-manager-tutorial

Publisher- or journal-specific examples relevant to citation-manager behavior:

- Elsevier explicitly advises authors using citation plug-ins to remove field codes before submission. Verified example: American Journal of Ophthalmology Guide for Authors, reference management section.  
  https://www.sciencedirect.com/journal/american-journal-of-ophthalmology/publish/guide-for-authors

- MDPI journal instructions commonly state that bibliography software such as EndNote, Zotero, Mendeley, and Reference Manager is acceptable, while later-stage formatting must still follow the journal instructions. Verified example journal page:  
  https://www.mdpi.com/journal/J/instructions

This matters because some journals explicitly instruct authors to remove field codes before submission, while others accept reference-manager-generated manuscripts provided that the final file complies with journal-specific formatting and submission requirements.
