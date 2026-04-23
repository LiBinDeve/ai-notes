# Raw Note Rules

## Scope

Use this reference when creating notes for the raw note stage of the note-management workflow.

## Required Schema

Every raw note is one Markdown file with this frontmatter shape:

```yaml
id:
name:
description:
metadata: {}
```

Populate all fields. Record the storage timestamp in `metadata.stored_at`.

## Content Rules

- Keep one note per file.
- Keep the body as raw capture material.
- Allow plain text, code blocks, terminal commands, and command output.

## Storage Location

Write raw notes to:

```text
E:\笔记-L（本地知识仓库）\原始笔记
```

## Filename Convention Used By This Skill

The project rule says to name files with the note name plus creation time. This skill uses:

```text
<sanitized-name>_<YYYY-MM-DD_HH-mm-ss>.md
```

This keeps the title readable while preserving creation time in the filename.