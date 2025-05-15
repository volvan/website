#!/usr/bin/env bash
set -euo pipefail

# Ensure snapshots directory exists
mkdir -p snapshots

# Determine the next snapshot index
previous=$(find snapshots -maxdepth 1 -type f -name 'data-*.md' \
    | sed -En 's/.*data-([0-9]+)\.md/\1/p' \
    | sort -n \
    | tail -n1)
if [[ -z "$previous" ]]; then
  next=1
else
  next=$((previous + 1))
fi

output_file="snapshots/data-${next}.md"

echo "Creating snapshot: $output_file"

# Snapshot current directory structure (excluding unwanted paths)
{
  tree -I 'venv|.git|.idea|__pycache__|snapshots|static/img|*.png|*.jpg|*.jpeg|*.gif|*.bmp|*.svg|*.webp|*.ico'
  echo
} >> "$output_file"

# Find and record each file (excluding unwanted dirs, nested __pycache__, and images)
find . \
  \( \
    -path "./.venv"            -o -path "./.venv/*" \
    -o -path "./.git"         -o -path "./.git/*" \
    -o -path "./.idea"        -o -path "./.idea/*" \
    -o -path "./snapshots"    -o -path "./snapshots/*" \
    -o -path "*/__pycache__"  -o -path "*/__pycache__/*" \
    -o -path "./static/img"    -o -path "./static/img/*" \
    -o -iname "*.png"         -o -iname "*.jpg"         \
    -o -iname "*.jpeg"        -o -iname "*.gif"         \
    -o -iname "*.bmp"         -o -iname "*.svg"         \
    -o -iname "*.webp"        -o -iname "*.ico"         \
  \) \
  -prune -o -type f -print | while IFS= read -r file; do
    # Strip leading './'
    echo "${file#./}" >> "$output_file"
    echo '```' >> "$output_file"
    cat "$file" >> "$output_file"
    echo '```' >> "$output_file"
    echo >> "$output_file"
done

echo "Snapshot complete."