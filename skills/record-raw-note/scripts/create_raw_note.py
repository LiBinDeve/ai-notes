from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import uuid
from pathlib import Path


RAW_NOTES_DIR = Path(r"E:\笔记-L（本地知识仓库）\原始笔记")
DEFAULT_TZ = dt.timezone(dt.timedelta(hours=8))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a raw note markdown file with required frontmatter."
    )
    parser.add_argument("--name", required=True, help="Note title.")
    parser.add_argument("--description", required=True, help="One-line note summary.")
    parser.add_argument(
        "--body",
        help="Markdown body content. Use this for short notes or tests.",
    )
    parser.add_argument(
        "--body-file",
        type=Path,
        help="Path to a UTF-8 markdown body file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=RAW_NOTES_DIR,
        help="Directory where the note file should be written.",
    )
    parser.add_argument(
        "--created-at",
        help="ISO 8601 datetime string. Defaults to current time in Asia/Shanghai offset.",
    )
    args = parser.parse_args()
    if bool(args.body) == bool(args.body_file):
        parser.error("Provide exactly one of --body or --body-file.")
    return args


def parse_created_at(raw_value: str | None) -> dt.datetime:
    if raw_value:
        created_at = dt.datetime.fromisoformat(raw_value)
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=DEFAULT_TZ)
        return created_at
    return dt.datetime.now(DEFAULT_TZ)


def sanitize_name(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]+', "-", value.strip())
    cleaned = re.sub(r"\s+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    cleaned = cleaned.strip(" .-_")
    return cleaned or "untitled-note"


def read_body(args: argparse.Namespace) -> str:
    if args.body is not None:
        return args.body.rstrip() + "\n"
    return args.body_file.read_text(encoding="utf-8").rstrip() + "\n"


def render_note(note_id: str, name: str, description: str, stored_at: str, body: str) -> str:
    frontmatter = [
        "---",
        f"id: {json.dumps(note_id, ensure_ascii=False)}",
        f"name: {json.dumps(name, ensure_ascii=False)}",
        f"description: {json.dumps(description, ensure_ascii=False)}",
        "metadata:",
        f"  stored_at: {json.dumps(stored_at, ensure_ascii=False)}",
        "---",
        "",
    ]
    return "\n".join(frontmatter) + body


def main() -> int:
    args = parse_args()
    created_at = parse_created_at(args.created_at)
    stored_at = created_at.isoformat()
    safe_name = sanitize_name(args.name)
    filename = f"{safe_name}_{created_at.strftime('%Y-%m-%d_%H-%M-%S')}.md"
    note_id = f"raw-{created_at.strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}"
    body = read_body(args)

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    note_text = render_note(note_id, args.name.strip(), args.description.strip(), stored_at, body)
    output_path.write_text(note_text, encoding="utf-8")

    print(f"created: {output_path}")
    print(f"note_id: {note_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())