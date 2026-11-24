from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
front, body = text.removeprefix("---\n").split("\n---\n", 1)
fields = dict(line.split(": ", 1) for line in front.splitlines())
assert fields["name"] == "release-note-editor"
assert fields["description"].strip() and body.strip()
assert "SKILL.md" in (ROOT / "README.md").read_text(encoding="utf-8")
