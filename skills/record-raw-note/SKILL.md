---
name: record-raw-note
description: Capture new original notes into `E:\笔记-L（本地知识仓库）\原始笔记` from user prompts. Use when Agent needs to turn rough ideas, troubleshooting logs, code snippets, terminal commands, or session takeaways into one-note-per-file Markdown documents with the required YAML frontmatter fields `id`, `name`, `description`, and `metadata`.
---

# Record Raw Note

## Workflow

1. Read [references/raw-note-rules.md](references/raw-note-rules.md) when the note schema or naming rules matter.
2. Distill the user input into three fields before writing:
   - `name`: concise note title that preserves the main subject.
   - `description`: one sentence explaining what the note records.
   - `body`: raw Markdown content. Preserve code, commands, and outputs when they carry technical meaning.
3. Write the note with [scripts/create_raw_note.py](scripts/create_raw_note.py) instead of hand-authoring frontmatter.
4. Return the created file path to the user.

## Writing Rules

- Write exactly one note per Markdown file.
- Use the required frontmatter fields only: `id`, `name`, `description`, `metadata`.
- Record the storage timestamp in `metadata.stored_at` as an ISO 8601 string with timezone offset.
- Preserve user-provided code and terminal commands inside fenced code blocks when possible.
- If the user does not provide a good title, derive one from the dominant subject instead of using a generic placeholder.

## File Naming

The source document requires using the note name plus creation time for filenames. This skill normalizes that rule as:

```text
<sanitized-name>_<YYYY-MM-DD_HH-mm-ss>.md
```

Keep Chinese titles when present. Replace Windows-invalid filename characters and collapse whitespace to hyphens.

## Script Usage

Use the bundled script for every write:

```powershell
python .\scripts\create_raw_note.py `
  --name "Docker 镜像加速" `
  --description "记录 Docker 镜像加速配置与验证命令。" `
  --body-file .\note-body.md
```

Optional arguments:

- Pass `--output-dir` only when testing or when the raw note directory changes.
- Pass `--created-at` only when reconstructing an older note and an explicit timestamp is required.

## Output Contract

- Emit a completed Markdown note file.
- Do not leave placeholder frontmatter values.
- Report the saved absolute path and the generated note id after writing.