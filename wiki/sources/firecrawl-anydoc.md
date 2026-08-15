---
type: source
created: 2026-08-07
updated: 2026-08-07
tags: [tooling, document-parsing, rust, open-source, firecrawl, agent-tooling]
source_path: raw/web/github-firecrawl-anydoc-convert-word-powerpoint-excel-opendocument-rtf-epub-csv-/index.md
ingested: 2026-W31 (Sat-Sat)
---

# Firecrawl anydoc: Rust Library for Document-to-Markdown Conversion

Firecrawl (Aug 2026). Libreria Rust che converte 13 formati (Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, PDF) in GitHub-Flavored Markdown con latenza single-digit millisecond.

## Caratteristiche

- **Sub-5ms** conversione markdown, 500 file docx in 1.7s
- Binding per Node.js, Python, browser (WebAssembly)
- Ships come **Agent Skill** (`npx skills add firecrawl/anydoc`): compatibile con Claude Code, Codex, Cursor, OpenCode
- MIT license, open-source
- Powers Firecrawl Parse (API hosted con OCR per scanned pages)

## Performance segnalate (X thread @nickscamara_)

L'annuncio [[raw/web/unknown-2084669934194266370/index]] (8.8k likes). Test community: 15-page PDF parsed in 64ms, large .xlsx da 92s (SheetJS) a 61ms, 1400 libri PDF 57% convertibili direttamente senza OCR in 3 minuti.

## Limiti

- Immagini/flattened PDF richiedono OCR (non incluso nella libreria, disponibile via API hosted)
- Formati scanned/handwritten non gestiti nativamente

## Connessioni

Tooling di parsing che abbassa la latenza del preprocessing documentale per agenti. Rilevante praticamente per il vault stesso: l'inbox-fetcher usa trafilatura per HTML; anydoc coprirebbe i formati office non attualmente gestiti.
