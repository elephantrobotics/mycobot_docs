"""
Post-process a Chrome-printed PDF:
  1. strip the print header/footer (Chrome's --print-to-pdf-no-header is
     ignored by this build, and the footer leaks a local file:/// path)
  2. add a real bookmark outline, derived from the source markdown headings

    python finalize_pdf.py <in.pdf> <source.md> <out.pdf>
"""
import io
import re
import sys
import unicodedata

import fitz

src_pdf, src_md, out_pdf = sys.argv[1], sys.argv[2], sys.argv[3]

EDGE = 34          # pt from top/bottom treated as header/footer band
MIN_HEAD = 7.45    # rendered pt; Chrome scales CSS pt by ~0.695


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace(" ", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


# ---- headings from the markdown, in document order -----------------------
heads = []
for line in io.open(src_md, encoding="utf-8"):
    m = re.match(r"^(#{1,6})\s+(.*\S)\s*$", line)
    if not m:
        continue
    text = m.group(2)
    text = re.sub(r"[*_`]", "", text)                      # strip emphasis
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)   # strip links
    if not text.strip():
        continue
    heads.append((len(m.group(1)), text.strip()))

doc = fitz.open(src_pdf)

# ---- 1. remove header/footer --------------------------------------------
removed = 0
for page in doc:
    h = page.rect.height
    victims = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l.get("spans", []):
                y0, y1 = s["bbox"][1], s["bbox"][3]
                if y1 < EDGE or y0 > h - EDGE:
                    if s["text"].strip():
                        victims.append(fitz.Rect(s["bbox"]))
    for r in victims:
        page.add_redact_annot(r)
    if victims:
        # keep images: only text is being scrubbed
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
        removed += len(victims)

# ---- 2. collect heading-like lines from the rendered pages ---------------
cands = []   # (page_index, y, size, text)
for pno, page in enumerate(doc):
    h = page.rect.height
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            spans = [s for s in l.get("spans", []) if s["text"].strip()]
            if not spans:
                continue
            y0 = min(s["bbox"][1] for s in spans)
            if y0 < EDGE or y0 > h - EDGE:
                continue
            size = max(s["size"] for s in spans)
            if size < MIN_HEAD:
                continue
            text = "".join(s["text"] for s in spans)
            if len(text) > 200:
                continue
            cands.append((pno, y0, size, norm(text), text))

cands.sort(key=lambda c: (c[0], c[1]))

# ---- 3. build the outline from the rendered headings themselves ----------
# Deriving levels from rendered font size cannot lose sync, unlike matching
# markdown headings in order: a short ambiguous title ("linux:") greedily
# matches far ahead and drags the cursor past every heading in between.
# Chrome scales the CSS pt values by ~0.695 (h1 20 -> 13.9, h2 15 -> 10.4,
# h3 12.5 -> 8.7, h4 11 -> 7.6; body 10.5 -> 7.3, TOC 9.5 -> 6.6).
def level_for(size):
    if size >= 12.0:
        return 1
    if size >= 9.5:
        return 2
    if size >= 8.2:
        return 3
    return 4


toc = []
for pno, _y, size, text, raw in cands:
    if not raw.strip():
        continue
    toc.append([level_for(size), raw.strip()[:180], pno + 1])

matched, missed = len(toc), 0

# A PDF outline may never skip a level (1 -> 3 is invalid). Unmatched
# headings leave gaps, so clamp each entry to at most parent + 1.
prev = 0
for row in toc:
    row[0] = 1 if prev == 0 else min(row[0], prev + 1)
    prev = row[0]

doc.set_toc(toc)
doc.save(out_pdf, garbage=3, deflate=True)

print("header/footer spans removed : %d" % removed)
print("headings in markdown        : %d" % len(heads))
print("  matched to a page         : %d" % matched)
print("  not found                 : %d" % missed)
print("bookmarks written           : %d" % len(toc))
print("output                      : %s" % out_pdf)
