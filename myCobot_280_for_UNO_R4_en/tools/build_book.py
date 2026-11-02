"""
Concatenate a GitBook into one markdown file, in SUMMARY.md order,
rewriting relative asset paths to absolute ones so images survive.

    python build_pdf.py <book-dir> <out.md> [--r4-only]
"""
import os
import re
import sys
import urllib.parse

book = os.path.abspath(sys.argv[1])
out_md = os.path.abspath(sys.argv[2])
r4_only = "--r4-only" in sys.argv

# (?<!!) so this never swallows an image - the match starts at '[', so a
# startswith('!') guard inside the callback would never fire.
LINK = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)]+)\)')
IMG = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
# upstream mixes markdown images with raw <img src="..."> using \ and / separators
HTML_IMG = re.compile(r'<img\s+([^>]*?)src\s*=\s*["\']([^"\']+)["\']([^>]*?)/?>',
                      re.I | re.S)
# ...and some <img> tags have an unquoted src, sometimes with no closing '>'
HTML_IMG_BARE = re.compile(r'<img\s+[^>]*?src\s*=\s*([^"\'\s>]+)[^>]*>?', re.I)
VIDEO_EXT = (".mp4", ".mov", ".avi", ".webm")

# --- read SUMMARY.md into an ordered (depth, title, path) list -------------
entries = []
with open(os.path.join(book, "SUMMARY.md"), encoding="utf-8") as fh:
    for line in fh:
        m = re.match(r'^(\s*)\*\s*\[([^\]]+)\]\(([^)]+)\)', line)
        if not m:
            m2 = re.match(r'^(\s*)\*\s+(.+?)\s*$', line)
            if m2 and "](" not in line:
                entries.append((len(m2.group(1)) // 3, m2.group(2).strip(), None))
            continue
        indent, title, path = m.groups()
        path = urllib.parse.unquote(path.split("#")[0]).strip()
        entries.append((len(indent) // 3, title.strip(), path))

if r4_only:
    keep = ("-M5" not in t for t in ())
    entries = [
        (d, t, p) for (d, t, p) in entries
        if p is None or (
            "-M5" not in p
            and not any(k in p for k in ("/ROS/", "myBlockly", "Accessories",
                                        "SupportingResources", "demo-en"))
        )
    ]

seen = set()
parts = []
missing = []
missing_assets = []

for depth, title, rel in entries:
    if rel is None:
        parts.append("\n\n# %s\n" % title)
        continue
    src = os.path.normpath(os.path.join(book, rel))
    if not os.path.isfile(src):
        missing.append(rel)
        continue
    if src in seen:
        continue
    seen.add(src)
    srcdir = os.path.dirname(src)

    with open(src, encoding="utf-8", errors="replace") as fh:
        body = fh.read()

    # demote headings so the book nests correctly under its section
    shift = min(depth + 1, 4)
    body = re.sub(r'^(#{1,6})\s', lambda m: "#" * min(len(m.group(1)) + shift, 6) + " ",
                  body, flags=re.M)

    def resolve(target):
        """Absolute path for an asset reference, or None if unusable."""
        t = urllib.parse.unquote(target.strip().split("#")[0])
        t = t.replace("\\", "/")                    # upstream mixes separators
        ap = os.path.normpath(os.path.join(srcdir, t))
        return ap if os.path.isfile(ap) else None

    def fix_img(m):
        alt, target = m.group(1), m.group(2).strip()
        if target.startswith(("http://", "https://", "data:")):
            return m.group(0)
        if target.lower().split("#")[0].endswith(VIDEO_EXT):
            return "*[video: %s]*" % os.path.basename(target)
        ap = resolve(target)
        if ap is None:
            missing_assets.append((rel, target))
            return "*[missing image: %s]*" % os.path.basename(target)
        return "![%s](<%s>)" % (alt, ap.replace("\\", "/"))

    def fix_html_img(m):
        target = m.group(2).strip()
        if target.startswith(("http://", "https://", "data:")):
            return m.group(0)
        if target.lower().split("#")[0].endswith(VIDEO_EXT):
            return "*[video: %s]*" % os.path.basename(target)
        ap = resolve(target)
        if ap is None:
            missing_assets.append((rel, target))
            return "*[missing image: %s]*" % os.path.basename(target)
        # drop the inline zoom styling; it does not survive to print anyway
        return "![](<%s>)" % ap.replace("\\", "/")

    def fix_html_img_bare(m):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "data:")):
            return m.group(0)
        if target.lower().split("#")[0].endswith(VIDEO_EXT):
            return "*[video: %s]*" % os.path.basename(target)
        ap = resolve(target)
        if ap is None:
            missing_assets.append((rel, target))
            return "*[missing image: %s]*" % os.path.basename(target)
        return "![](<%s>)" % ap.replace("\\", "/")

    # Embedded players cannot render in print, and their poster="" attribute
    # makes pandoc --self-contained abort trying to fetch an empty resource.
    body = re.sub(r'<video\b.*?</video\s*>', "\n*[embedded video omitted]*\n",
                  body, flags=re.I | re.S)
    body = re.sub(r'<video\b[^>]*>|</video\s*>|<source\b[^>]*>', "",
                  body, flags=re.I)

    body = IMG.sub(fix_img, body)
    body = HTML_IMG.sub(fix_html_img, body)
    body = HTML_IMG_BARE.sub(fix_html_img_bare, body)

    # turn internal cross-links into plain text; they mean nothing in a PDF
    def fix_link(m):
        text, target = m.group(1), m.group(2).strip()
        if m.group(0).startswith("!"):
            return m.group(0)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        return text
    body = LINK.sub(fix_link, body)

    parts.append("\n\n" + "#" * max(shift, 1) + " " + title + "\n\n" + body)

with open(out_md, "w", encoding="utf-8") as fh:
    fh.write("\n".join(parts))

print("pages written   : %d" % len(seen))
print("missing pages   : %d" % len(missing))
for m in missing[:10]:
    print("    ", m)
print("missing assets  : %d" % len(missing_assets))
for src, tgt in missing_assets[:10]:
    print("     %s -> %s" % (src, tgt))
print("output          :", out_md)
