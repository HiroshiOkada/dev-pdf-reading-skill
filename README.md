# PDF Extraction Tool

A lightweight command-line tool to extract text from local or remote PDF files, with support for Japanese text.

## Features
- Extract text from local PDF files.
- Extract text from remote PDF URLs.
- Limit extraction to the first N characters (useful for summaries).
- Optimized for "light" operation (text extraction, not OCR).

## Installation

You can run this tool using `uv` without installing it globally, or install it via `uv tool`.

### Run via uvx (Github)
Once pushed to GitHub:
```bash
uvx --from git+https://github.com/YourUsername/dev-pdf-reading-skill pdf-tool <source>
```

### Development
```bash
uv sync
uv run pdf-tool <source>
```

## Usage

```bash
# Local file
pdf-tool document.pdf

# Remote URL
pdf-tool https://example.com/doc.pdf

# Limit to first 1000 characters
pdf-tool document.pdf --limit 1000
```

## Requirements
- Python >= 3.10
- Windows (as per requirement, though likely cross-platform)
