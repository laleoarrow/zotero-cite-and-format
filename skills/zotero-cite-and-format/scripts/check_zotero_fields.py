#!/usr/bin/env python3
"""Strict structural gate for citation-bearing Zotero DOCX manuscripts.

Require at least one live citation field and exactly one live bibliography field.
Also check each `ADDIN ZOTERO_ITEM` field for the expected run sequence:
begin -> instrText -> separate -> visible citation text -> end.
"""

from __future__ import annotations

import sys
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def main(docx_path: str) -> int:
    path = Path(docx_path)
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 2

    with ZipFile(path) as zf:
        root = etree.fromstring(zf.read("word/document.xml"))

    bad = []
    citation_count = 0
    bibliography_count = 0
    for p_idx, para in enumerate(root.xpath("//w:p", namespaces=NS), start=1):
        runs = para.xpath("./w:r", namespaces=NS)
        for i, run in enumerate(runs):
            instr = "".join(run.xpath("./w:instrText/text()", namespaces=NS))
            if "ADDIN ZOTERO_BIBL" in instr:
                bibliography_count += 1
            if "ADDIN ZOTERO_ITEM" not in instr:
                continue
            citation_count += 1

            prev = runs[i - 1] if i - 1 >= 0 else None
            nxt = runs[i + 1] if i + 1 < len(runs) else None
            nxt2 = runs[i + 2] if i + 2 < len(runs) else None
            nxt3 = runs[i + 3] if i + 3 < len(runs) else None

            def fld(run_obj):
                if run_obj is None:
                    return ""
                vals = run_obj.xpath("./w:fldChar/@w:fldCharType", namespaces=NS)
                return vals[0] if vals else ""

            visible_text = ""
            if nxt2 is not None:
                visible_text = "".join(nxt2.xpath("./w:t/text()", namespaces=NS))

            if not (
                fld(prev) == "begin"
                and fld(nxt) == "separate"
                and visible_text
                and fld(nxt3) == "end"
            ):
                bad.append(
                    {
                        "paragraph": p_idx,
                        "run_index": i + 1,
                        "prev": fld(prev),
                        "next": fld(nxt),
                        "visible_text": visible_text,
                        "next3": fld(nxt3),
                        "instr_head": instr[:120],
                    }
                )

    if citation_count == 0:
        print("NO_ZOTERO_CITATION_FIELDS")
        return 1

    if bibliography_count == 0:
        print("NO_ZOTERO_BIBLIOGRAPHY_FIELD")
        return 1

    if bibliography_count > 1:
        print(f"MULTIPLE_ZOTERO_BIBLIOGRAPHY_FIELDS: {bibliography_count}")
        return 1

    if bad:
        print("BROKEN_ZOTERO_FIELDS")
        for item in bad:
            print(item)
        return 1

    print(
        "OK: "
        f"{citation_count} Zotero citation fields have "
        "begin/instr/separate/text/end structure; "
        "1 Zotero bibliography field is present"
    )
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: check_zotero_fields.py /path/to/file.docx")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
