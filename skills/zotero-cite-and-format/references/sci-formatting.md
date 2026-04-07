# SCI Formatting Hygiene / SCI 通用格式卫生

Unless the target journal says otherwise, treat these as general Word-manuscript rules for English SCI submissions:

1. Use real Word character formatting for superscript, subscript, italic, bold, and small caps. Do not fake these with Unicode look-alike glyphs.
2. For scientific notation, prefer `a × 10^n` with a real multiplication sign `×` and a truly superscripted exponent. In Word terms, the exponent should be plain text in its own run with superscript formatting applied, not a pasted Unicode form such as `10⁻3`.
3. Do not let Markdown notation leak into the manuscript-facing Word files. Syntax such as `10^-6^`, `H~2~O`, backticks, or similar source markup is not acceptable in either the Zotero-editable manuscript or the static submission copy.
4. Do not normalize hyphen, minus, en dash, and em dash blindly. Preserve one role per symbol and keep the manuscript's convention consistent unless the target journal explicitly wants a different style.
5. Use true italic formatting for material that field convention marks as italic, such as Latin species names or other biologic labels that genuinely require italics. Do not replace italics with styled Unicode characters.
6. Use real symbol characters when the symbol itself carries meaning, such as Greek letters, `≤`, `≥`, `±`, and `×`. Do not silently downgrade them to plain-text approximations unless the journal or submission system requires it.
7. If the user asks for formatting-only cleanup, keep the change at run level whenever possible. Do not rewrite prose, renumber citations, or refresh Zotero unless explicitly requested. The only exception is normalizing the typography of identifiers that are already intentionally retained in the prose.
8. If verification uses XML extraction, `pdftotext`, or similar text-only views, remember that correctly superscripted text may flatten during extraction. Judge the final formatting from Word or rendered PDF output, not from plain extracted text alone.
9. Do not let code-style monospace or inline backticks leak into narrative manuscript sections merely because the source text came from Markdown, notebooks, or scripts. Journal-facing prose should read like prose unless the target journal explicitly requires a software or reproducibility notation in the main text. User preference for reproducibility detail should normally be satisfied in Methods supplements, appendices, or separate technical artifacts rather than by making the main narrative read like code.
10. Do not leave local-environment narration such as "in the current workspace", agent-process notes, temporary paths, or machine-specific statements in manuscript-facing sections such as Data Availability, Methods, footnotes, acknowledgments, or supplements unless the journal explicitly requests them.

## Quick Diagnostic

| Symptom | Likely issue | Fix |
|---------|-------------|-----|
| `10⁻³` in Word | Unicode fake superscript | Replace with real Word superscript run |
| `10^-6^` in Word | Markdown leak | Apply real superscript formatting |
| Hyphen used for minus | Ambiguous dash usage | Use true minus U+2212 for math |
| `foo()` in Results | Code-style prose leak | Rewrite as methodological prose |
| Species name not italic | Missing italic run | Apply italic at run level |
