# Table Formatting

Use this reference when formatting tables, both for main manuscript Word tables and supplementary Excel tables.

## Main Word Tables
- Use true three-line tables.
- Omit vertical borders unless the journal explicitly wants them.
- Keep footnotes outside the bordered table body when that is the chosen style.
- If the journal is silent, follow the style anchor first; only use a user-stated default when no usable anchor exists.
- If the marker scheme changes from alphabetic labels to symbols, convert the whole sequence consistently.

## Supplementary Excel Tables
- Hide worksheet gridlines.
- Avoid colored Excel themes and filter widgets unless required.
- Omit vertical borders.
- Treat each actual table body or panel body as one three-line entity.
- Use Times New Roman throughout (title, header, body, footnotes).

Default structure unless the style anchor shows otherwise:
- caption/title row is outside the bordered table body (bold, merged across all columns)
- header row directly follows the title with no blank row; carries the top rule and header-underlining rule
- final data row carries the closing bottom rule
- footnote rows directly follow the last data row with no blank row; they are outside the bordered table body and do not receive the closing bottom rule

### Footnote Symbol Sequence
Use the standard SCI footnote marker sequence for annotation lines. Each annotation line starts with its symbol, followed by a space:
`*`, `†`, `‡`, `§`, `¶`, `#`

For tables with more than 6 footnotes, double the symbols:
`**`, `††`, `‡‡`, `§§`, `¶¶`, `##`

Then triple if needed: `***`, `†††`, etc.

### Abbreviation Line
- The abbreviation line is always the **last** footnote row.
- It starts with **bold** `Abbreviations:` followed by comma-separated definitions.
- Use semicolons to separate distinct abbreviation entries.
- Format: `Abbreviations: IVW, inverse-variance weighted; SE, standard error; OR, odds ratio.`

### Font and Size Rules
| Element | Font | Size | Style |
|---------|------|------|-------|
| Title | Times New Roman | 11 pt | Bold |
| Column headers | Times New Roman | 9 pt | Bold, center-aligned |
| Data cells | Times New Roman | 9 pt | Center-aligned (left-align first column) |
| Footnote lines | Times New Roman | 8 pt | Mixed: **Symbol is Bold**, text is Normal |
| Abbreviation line | Times New Roman | 8 pt | Mixed: **"Abbreviations:" is Bold**, text is Normal |

### Technical Implementation (R / Excel)
- **CRITICAL**: Do NOT split footnotes into two columns (e.g., symbol in Col 1, text in Col 2) just to achieve bold symbols. The footnote must remain in a single cell (merged across all columns).
- To achieve mixed formatting (bold symbol/label + normal text) within a single Excel cell using R, you **cannot** use the legacy `openxlsx` package.
- **You must use the `openxlsx2` package** and its `fmt_txt()` function to construct rich text strings.
- Example:
  ```R
  # Requires openxlsx2
  rt_note <- fmt_txt("* ", bold = TRUE, size = 8, font = "Times New Roman") +
             fmt_txt("MR results for all...", bold = FALSE, size = 8, font = "Times New Roman")
  wb$add_data(sheet = "Sheet1", x = rt_note, start_row = row_idx, start_col = 1)
  wb$merge_cells(sheet = "Sheet1", cols = 1:ncol, rows = row_idx)
  ```

### Spacing Rules
- No blank row between title and header row.
- No blank row between last data row and first footnote row.
- No blank row between footnote rows.
- One footnote per row; do not cram all footnotes into a single cell.

Wrap rules:
- do not force wrap in title rows, spacer rows, or short footnote-label rows just because merges are narrow
- use widths and merges that let the title and footnote block read naturally
- long footnote sentences may wrap naturally in a wide merged row
