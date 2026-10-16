#!/usr/bin/env python3
"""Build a small installable archive without local settings or private files."""
import argparse
import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = ("pet.json", "spritesheet.png", "checksums.json", "LICENSE",
         "LICENSE-ASSETS.md", "NOTICE.md", "docs/INSTALL.md", "scripts/install.py")


def build(output):
    output.mkdir(parents=True, exist_ok=True)
    archive = output / "gpt-dragon-girl-pet.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for name in FILES:
            package.write(ROOT / name, arcname=name)
    sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / "SHA256SUMS.txt").write_text(sha + "  " + archive.name + "\n", encoding="utf-8")
    print(str(archive))
    return archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    build(parser.parse_args().output.expanduser().resolve())
