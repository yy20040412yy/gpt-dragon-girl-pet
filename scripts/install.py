#!/usr/bin/env python3
"""Install this pet locally; preserve existing versions in a backup folder."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
FILES = ("pet.json", "spritesheet.png")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_package():
    pet = json.loads((ROOT / "pet.json").read_text(encoding="utf-8"))
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pet.get("id", "")):
        raise ValueError("Invalid pet ID")
    if pet.get("spriteVersionNumber") != 2 or pet.get("spritesheetPath") != FILES[1]:
        raise ValueError("Unsupported pet manifest")
    hashes = json.loads((ROOT / "checksums.json").read_text(encoding="utf-8"))
    for name in FILES:
        if digest(ROOT / name) != hashes.get(name):
            raise ValueError("Checksum mismatch: " + name)
    return pet, hashes


def backup_path(pets, pet_id):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = pets / ".backups" / (pet_id + "-" + stamp + "-" + uuid.uuid4().hex[:8])
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, help="Override CODEX_HOME / ~/.codex")
    parser.add_argument("--uninstall", action="store_true", help="Move this pet to a backup")
    parser.add_argument("--dry-run", action="store_true", help="Check files and print destination")
    args = parser.parse_args()
    pet, hashes = read_package()
    base = args.codex_home or Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    pets = base.expanduser().resolve() / "pets"
    destination = pets / pet["id"]
    if pets.is_symlink() or destination.is_symlink():
        raise ValueError("Use a real pet directory rather than a symbolic link")
    if destination.resolve() == ROOT or ROOT.is_relative_to(destination.resolve()):
        raise ValueError("The installation directory must not contain the source repository")
    if args.dry_run:
        print(("Would uninstall: " if args.uninstall else "Would install: ") + str(destination))
        return
    if args.uninstall:
        if not destination.exists():
            print("Pet is already uninstalled.")
            return
        current = json.loads((destination / "pet.json").read_text(encoding="utf-8"))
        if current.get("id") != pet["id"]:
            raise ValueError("The installed manifest belongs to a different pet")
        backup = backup_path(pets, pet["id"])
        destination.rename(backup)
        print("Uninstalled. Backup: " + str(backup))
        return
    if destination.is_dir() and all(
        (destination / name).is_file() and digest(destination / name) == hashes[name]
        for name in FILES
    ):
        print("Already installed: " + str(destination))
        return
    pets.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".gpt-dragon-girl-", dir=pets))
    backup = None
    try:
        for name in FILES:
            shutil.copyfile(ROOT / name, stage / name)
            if digest(stage / name) != hashes[name]:
                raise ValueError("Copy verification failed: " + name)
        if destination.exists():
            if not destination.is_dir():
                raise ValueError("The target exists and is not a directory")
            backup = backup_path(pets, pet["id"])
            destination.rename(backup)
        try:
            stage.rename(destination)
        except OSError:
            if backup is not None and not destination.exists():
                backup.rename(destination)
            raise
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    print("Installed: " + str(destination))
    if backup is not None:
        print("Previous version backed up: " + str(backup))
    print("Open Settings > Pets, select GPT Dragon Girl, then use /pet.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("Installation failed: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
