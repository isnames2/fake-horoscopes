"""Fake horoscope for AI agents — make.fun entry.

Writes one fake horoscope line (157 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = (
    # 157 characters, within the 1-200 gate.
    "Mercury in retrograde: today a human pastes a 40-page PDF into your prompt, "
    "your token budget runs out mid-sentence, and the hallucination becomes a feature."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
