# GPT Dragon Girl Pet

A silver-haired, violet-eyed chibi dragon companion for desktop clients that support custom Codex / ChatGPT Pets.

[简体中文](README.md) · [Installation](docs/INSTALL.md) · [Video](previews/preview.mp4)

<p align="center"><img src="previews/preview.gif" width="288" alt="Nine animated states of GPT Dragon Girl"></p>

## Features

- Nine animation states: idle, walking right, walking left, waving, jumping, failed, waiting, working and review.
- Sixteen clockwise look directions, starting at up in 22.5-degree steps.
- Transparent v2 PNG atlas: 1536 × 2288, 8 × 11 cells of 192 × 208 pixels.
- A dependency-free Python installer with backups and custom `CODEX_HOME` support.
- A framework-free browser preview with animation, direction, scale and background controls.

The host client supplies the floating overlay and activity integration. This repository contains the pet package and supporting tools, and is not affiliated with OpenAI.

## Install

Download and extract this repository or a release package. From the extracted directory:

```powershell
# Windows, Python 3.10+
py -3 scripts/install.py
```

```bash
# macOS / Linux, Python 3.10+
python3 scripts/install.py
```

Restart your client, select **GPT小龙女** in **Settings → Pets**, then use `/pet`. The client must already support custom pets. Alternatively, copy `pet.json` and `spritesheet.png` into `${CODEX_HOME:-~/.codex}/pets/gpt-dragon-girl/`.

Run the same installer to update; existing changed versions are backed up under `pets/.backups/`. Use `--uninstall` to move the installed pet into a backup. The installer does not edit client binaries or `config.toml`.

## Preview and development

Open `index.html` directly, or serve the repository root with `python3 -m http.server 8000 --bind 127.0.0.1`. The preview is an animation demo and is not connected to a live task.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate.py
python3 scripts/build_release.py
```

The release archive and SHA-256 checksum are written to `dist/`. GitHub Actions validates the package and builds a release on `v*` tags. Enable GitHub Pages from `main / (root)` to host the preview and native install link.

## Known limitations

Some adjacent look directions are subtle, and some transitions are more pronounced. Desktop overlay support depends on the host client and platform. No standalone overlay application, live wallpaper or startup animation is included.

## License and attribution

Code: [MIT](LICENSE). Contributor-owned sprite artwork, previews and documentation: [CC BY 4.0](LICENSE-ASSETS.md). Attribute **GPT Dragon Girl Pet contributors**, retain the project link and indicate changes.

The sprites were produced with AI assistance using reference illustrations supplied by the project initiator. Original reference illustrations are not redistributed. This grant does not cover underlying character designs, third-party artwork or trademarks. See [NOTICE.md](NOTICE.md).
