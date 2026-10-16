# GPT 小龙女 · Dragon Girl Pet

白紫色、银白长发的小龙女，陪你一起写代码。

[在线预览](https://yy20040412yy.github.io/gpt-dragon-girl-pet/) · [下载 v1.0.0](https://github.com/yy20040412yy/gpt-dragon-girl-pet/releases/tag/v1.0.0) · [English](README.en.md) · [安装指南](docs/INSTALL.md) · [视频预览](previews/preview.mp4) · [素材授权](LICENSE-ASSETS.md)

<p align="center">
  <img src="previews/preview.gif" width="288" alt="GPT 小龙女九组动作动画预览">
</p>

这是一个面向支持自定义 Pets 的 Codex / ChatGPT 桌面客户端的社区桌宠项目，提供完整 v2 精灵图、安装脚本与浏览器动作预览。角色采用银白长发、紫眸、双角、淡紫龙翼和鳞片尾巴的 Q 版设计。

本项目与 OpenAI 无隶属关系。它是桌宠素材包和配套工具，悬浮显示、拖动及任务状态切换由宿主客户端提供。

## 你会得到什么

- 九组动作：待机、向右走、向左走、挥手、跳跃、失败反应、等待输入、思考工作、检查结果。
- 十六个顺时针视线方向，从向上开始，每隔 22.5° 一格。
- 透明 PNG 精灵图：1536 × 2288，8 列 × 11 行，单格 192 × 208。
- 跨平台 Python 安装器：支持自定义 `CODEX_HOME`，替换旧版本前自动备份。
- 不依赖前端框架的动作预览页，可切换动作、方向、大小和背景。

## 安装

下载仓库 ZIP 并解压，或下载 Release 中的 `gpt-dragon-girl-pet.zip`。在解压后的项目目录运行：

Windows PowerShell：

```powershell
py -3 scripts/install.py
```

macOS / Linux：

```bash
python3 scripts/install.py
```

安装器需要 Python 3.10 或更高版本，无需安装第三方库。完成后重新打开客户端，在 **设置 → Pets** 中选择 **GPT小龙女**，使用 `/pet` 显示桌宠。如果当前客户端没有自定义 Pets 功能，安装文件不会为其新增该功能。

默认安装到 `~/.codex/pets/gpt-dragon-girl/`。设置了 `CODEX_HOME` 时会使用该目录，也可以传入 `--codex-home`。安装器只写入本桌宠目录和版本备份，不修改客户端程序或 `config.toml`。

不使用脚本时，按照[手动安装步骤](docs/INSTALL.md)复制 `pet.json` 和 `spritesheet.png` 即可。

## 动作与视线

| 行号（从 0 开始） | 状态 | 帧数 | 展示用途 |
| --- | --- | --- | --- |
| 0 | `idle` | 6 | 待机、呼吸与眨眼 |
| 1 | `running-right` | 8 | 向右移动 |
| 2 | `running-left` | 8 | 向左移动 |
| 3 | `waving` | 4 | 挥手问好 |
| 4 | `jumping` | 5 | 起跳与落地 |
| 5 | `failed` | 8 | 失败或受阻 |
| 6 | `waiting` | 6 | 等待输入 |
| 7 | `running` | 6 | 思考工作 |
| 8 | `review` | 6 | 检查结果 |
| 9–10 | `look` | 16 | 顺时针环视 |

实际触发时机与播放速度由客户端决定。网页预览采用便于观看的演示速度，不等同于客户端的实时状态连接。

<p align="center"><img src="previews/look.gif" width="240" alt="十六方向环视预览"></p>

## 浏览器预览

直接打开仓库根目录的 `index.html`。也可以在项目目录运行：

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

访问 `http://127.0.0.1:8000`。在 Windows 上把 `python3` 换成 `py -3`。

发布者可在 GitHub 仓库 **Settings → Pages → Deploy from a branch → main / (root)** 启用在线预览。通过标准 GitHub Pages 项目地址访问时，页面会根据仓库地址生成原生 `codex://` 安装链接；本地预览保留文件下载与手动安装说明。

## 开发与打包

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate.py
python3 scripts/build_release.py
```

校验涵盖文件校验和、清单、图集尺寸、透明通道、使用帧与空白格。`dist/` 中会生成安装 ZIP 和 SHA-256 文件。修改正式图集或清单后，请同步更新 `checksums.json`。

GitHub Actions 会运行基础校验及临时目录安装检查；推送 `v*` 标签会打包并创建 GitHub Release。详见[发布步骤](docs/PUBLISHING.md)。

## 当前限制

- 部分相邻视线方向的区别较轻，个别方向切换略明显；保留现有成品，欢迎后续改善。
- 安装文件可在不同系统复制使用，桌面悬浮与互动是否可用取决于客户端版本和平台。
- 不包含独立常驻桌宠程序、动态壁纸或客户端加载动画。

## 授权与来源

代码使用 [MIT](LICENSE)。本项目贡献者有权许可的精灵图、动画预览和文档使用 [CC BY 4.0](LICENSE-ASSETS.md)，署名为 **GPT Dragon Girl Pet contributors**，并保留项目链接及修改说明。

角色素材由 AI 辅助生成，并参考发起者提供的插画进行 Q 版化与动画制作。原始参考插画未随仓库分发；角色设计、原插画及商标等第三方权利不由本项目转授。来源和授权范围见 [NOTICE.md](NOTICE.md)。

欢迎通过 Issue 报告安装问题、动作问题，或提交动作改进。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
