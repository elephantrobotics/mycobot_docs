# Build a bookmarked PDF of the book. Slow — see tools/preview.ps1 for a
# seconds-fast HTML preview instead.
#
#   .\tools\build_pdf.ps1                       # whole book  (~10 min, ~139 MB)
#   .\tools\build_pdf.ps1 -R4Only               # R4 chapters (~3 min,  ~39 MB)
#   .\tools\build_pdf.ps1 -Out C:\path\my.pdf
#
# Pipeline: concatenate in SUMMARY order -> pandoc (embeds every image as a
# data: URI) -> headless Chrome -> strip Chrome's print header/footer and add
# a bookmark outline.
#
# Chrome's --print-to-pdf emits no outline and, in current builds, ignores
# --print-to-pdf-no-header; both are handled by tools/finalize_pdf.py.

param(
    [switch]$R4Only,
    [string]$Out
)

$ErrorActionPreference = "Stop"
$book  = Split-Path -Parent $PSScriptRoot
$tools = $PSScriptRoot
$tmp   = Join-Path $env:TEMP "mycobot_pdf"
New-Item -ItemType Directory -Force $tmp | Out-Null

if (-not $Out) {
    $name = if ($R4Only) { "myCobot_280_UNO_R4_guide.pdf" } else { "myCobot_280_for_UNO_R4_en.pdf" }
    $Out = Join-Path (Split-Path -Parent $book) $name
}

$chrome = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $chrome) { Write-Error "No Chrome or Edge found for PDF printing." }

$md   = Join-Path $tmp "book.md"
$html = Join-Path $tmp "book.html"
$raw  = Join-Path $tmp "raw.pdf"
$title = if ($R4Only) { "myCobot 280 for Arduino UNO R4 (R4 chapters)" }
         else         { "myCobot 280 for Arduino UNO R4" }

$sw = [Diagnostics.Stopwatch]::StartNew()

"[1/4] concatenating..."
$args = @((Join-Path $tools "build_book.py"), $book, $md)
if ($R4Only) { $args += "--r4-only" }
python @args

"[2/4] rendering HTML with embedded images (slow)..."
pandoc $md -f gfm -t html5 --standalone --self-contained --toc --toc-depth=3 `
    --metadata title="$title" --css (Join-Path $tools "book.css") -o $html

"[3/4] printing to PDF..."
& $chrome --headless --disable-gpu --no-sandbox `
    --run-all-compositor-stages-before-draw --virtual-time-budget=150000 `
    "--print-to-pdf=$raw" ("file:///" + ($html -replace '\\', '/')) | Out-Null

"[4/4] stripping header/footer and adding bookmarks..."
python (Join-Path $tools "finalize_pdf.py") $raw $md $Out

$sw.Stop()
"{0}  ({1:N1} min, {2:N1} MB)" -f $Out, $sw.Elapsed.TotalMinutes, ((Get-Item $Out).Length / 1MB)
