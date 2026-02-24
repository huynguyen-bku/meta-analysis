#!/bin/bash
# Export manuscript_JABES_2026.md to paper.docx
# Run from any location — script resolves its own directory

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PANDOC="/home/duyle/miniconda3/envs/duylv/bin/pandoc"

cd "$SCRIPT_DIR"

$PANDOC manuscript_JABES_2026.md \
  -o paper.docx \
  --standalone

echo "Done: $SCRIPT_DIR/paper.docx"
