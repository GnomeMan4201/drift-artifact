#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path

ARTIFACT = Path("artifact/drift_artifact_v2.html")


def main() -> int:
    if not ARTIFACT.is_file():
        raise SystemExit(f"missing artifact: {ARTIFACT}")

    text = ARTIFACT.read_text(encoding="utf-8")
    if len(text.strip()) < 1000:
        raise SystemExit("artifact is unexpectedly small")

    lower = text.lower()
    required = ["<html", "<head", "<body"]
    missing = [marker for marker in required if marker not in lower]
    if missing:
        raise SystemExit("missing required HTML markers: " + ", ".join(missing))

    parser = HTMLParser()
    parser.feed(text)
    parser.close()

    print(f"validated {ARTIFACT} ({len(text):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
