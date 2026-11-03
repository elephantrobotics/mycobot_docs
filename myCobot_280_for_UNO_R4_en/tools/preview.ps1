# Fast local preview of the whole book — builds in seconds, not minutes.
#
#   .\tools\preview.ps1           # whole book
#   .\tools\preview.ps1 -R4Only   # UNO R4 chapters only
#   .\tools\preview.ps1 -NoOpen   # build without launching a browser
#
# Writes _preview.html in the book root and opens it. Images are referenced
# from disk rather than embedded, which is what makes this fast: the PDF build
# base64-encodes 475 images into a ~330 MB file, this does not.

param(
    [switch]$R4Only,
    [switch]$NoOpen
)

$ErrorActionPreference = "Stop"
$book = Split-Path -Parent $PSScriptRoot
$tools = $PSScriptRoot
$md  = Join-Path $env:TEMP "mycobot_preview.md"
$out = Join-Path $book "_preview.html"

if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Error "pandoc not found. Install from https://pandoc.org/installing.html"
}

$title = if ($R4Only) { "myCobot 280 for Arduino UNO R4 (R4 chapters)" }
         else         { "myCobot 280 for Arduino UNO R4" }

$sw = [Diagnostics.Stopwatch]::StartNew()

$args = @((Join-Path $tools "build_book.py"), $book, $md)
if ($R4Only) { $args += "--r4-only" }
python @args

pandoc $md -f gfm -t html5 --standalone --toc --toc-depth=3 `
    --metadata title="$title" --css (Join-Path $tools "book.css") -o $out

$sw.Stop()
"{0}  ({1:N1} s, {2:N1} MB)" -f $out, $sw.Elapsed.TotalSeconds, ((Get-Item $out).Length / 1MB)

if (-not $NoOpen) { Start-Process $out }
