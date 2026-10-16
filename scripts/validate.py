#!/usr/bin/env python3
"""Check package geometry, occupied cells, transparency and file checksums."""
import hashlib
import json
from pathlib import Path
import sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def validate():
    manifest = json.loads((ROOT / "pet.json").read_text(encoding="utf-8"))
    animations = json.loads((ROOT / "animations.json").read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "checksums.json").read_text(encoding="utf-8"))
    assert manifest["id"] == "gpt-dragon-girl", "Unexpected pet ID"
    assert manifest["spriteVersionNumber"] == 2, "Expected sprite version 2"
    assert manifest["spritesheetPath"] == "spritesheet.png", "Unexpected sprite path"
    for name in ("pet.json", "spritesheet.png"):
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        assert actual == expected[name], "Checksum mismatch: " + name
    with Image.open(ROOT / manifest["spritesheetPath"]) as sheet:
        assert sheet.size == (1536, 2288), "Invalid v2 atlas dimensions"
        assert sheet.mode == "RGBA", "Atlas must have RGBA transparency"
        assert sheet.getchannel("A").getextrema() == (0, 255), "Missing transparency"
        assert len(animations["states"]) == 9, "Expected nine animation states"
        occupied = 0
        for row in range(11):
            count = animations["states"][row]["frames"] if row < 9 else 8
            if row < 9:
                assert animations["states"][row]["row"] == row, "Invalid animation row"
            for col in range(8):
                cell = sheet.crop((192 * col, 208 * row, 192 * (col + 1), 208 * (row + 1)))
                visible = cell.getchannel("A").getbbox() is not None
                assert visible == (col < count), f"Unexpected occupancy: row {row}, col {col}"
                occupied += int(visible)
    print(json.dumps({"ok": True, "spriteVersionNumber": 2, "states": 9,
                      "lookDirections": 16, "occupiedCells": occupied,
                      "atlasSha256": expected["spritesheet.png"]}, indent=2))


if __name__ == "__main__":
    try:
        validate()
    except (AssertionError, OSError, ValueError, KeyError) as exc:
        print("Validation failed: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
