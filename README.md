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
- Windows (as per requirement, though likely cross-platform)

## Setup as Antigravity Skill

To use this tool as an Antigravity skill, create a new skill directory and a `SKILL.md` file.

1. Create directory: `~/.gemini/antigravity/skills/pdf-reader`
2. Create `SKILL.md` with the following content:

```markdown
---
name: pdf-reader
description: Extracts text from PDF files (local or remote). Useful for reading documentation or references in PDF format.
---

# PDF Reader Skill

This skill allows the agent to read the text content of PDF files. It uses a lightweight Python tool powered by `pdfminer.six` and can handle both local files and remote URLs. It is optimized for Japanese text.

## Usage

You should use the `run_command` tool to execute the `pdf-tool` via `uvx`.

### Template

```bash
uvx --from git+https://github.com/HiroshiOkada/dev-pdf-reading-skill pdf-tool <source> [--limit <N>]
```

### Examples

**Read a remote PDF:**
```bash
uvx --from git+https://github.com/HiroshiOkada/dev-pdf-reading-skill pdf-tool https://example.com/sample.pdf
```

**Read the first 1000 characters of a local PDF (recommended for summary):**
```bash
uvx --from git+https://github.com/HiroshiOkada/dev-pdf-reading-skill pdf-tool "C:\path\to\document.pdf" --limit 1000
```
```
