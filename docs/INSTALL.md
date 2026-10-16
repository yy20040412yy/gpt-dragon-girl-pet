# 安装与卸载

## 安装

1. 解压桌宠安装包或仓库 ZIP，进入包含 `pet.json` 的文件夹。
2. Windows PowerShell 运行 `py -3 scripts/install.py`；macOS / Linux 运行 `python3 scripts/install.py`。
3. 重新打开支持自定义 Pets 的桌面客户端。
4. 在“设置 → Pets”中选择“GPT小龙女”，输入 `/pet` 显示。

脚本需要 Python 3.10 或以上，不需要 Pillow。没有 Python 时可手动安装。

## 手动安装

将同一版本的 `pet.json` 和 `spritesheet.png` 放入：

| 系统 | 默认目录 |
| --- | --- |
| Windows | `%USERPROFILE%\.codex\pets\gpt-dragon-girl\` |
| macOS / Linux | `~/.codex/pets/gpt-dragon-girl/` |

如果设置了 `CODEX_HOME`，将 `.codex` 换成该环境变量指向的目录。不要只复制 PNG 或把 v2 图集标成 v1。

## 指定目录

```bash
python3 scripts/install.py --codex-home /path/to/codex-home
python3 scripts/install.py --dry-run
```

Windows 使用 `py -3` 替换 `python3`，带空格的路径需要加引号。

## 更新与备份

重新运行安装脚本。相同文件不会重复写入；替换不同版本前，旧目录会完整移动到 `<CODEX_HOME>/pets/.backups/`，脚本会打印备份位置。

如需恢复旧版本，退出客户端，将当前桌宠文件夹移走，再把备份文件夹复制为 `pets/gpt-dragon-girl/`。

## 卸载

```bash
python3 scripts/install.py --uninstall
```

指定过安装目录时，加上相同的 `--codex-home`。卸载会把桌宠移到备份目录，不删除素材。客户端中可切换到其他桌宠或关闭桌宠显示。

## 常见问题

| 情况 | 操作 |
| --- | --- |
| 找不到桌宠 | 核对实际 `CODEX_HOME`，确认两个文件在同一目录，再重启客户端 |
| 客户端没有 Pets 入口 | 使用提供自定义 Pets 功能的客户端；安装脚本无法补充宿主功能 |
| 提示校验和不一致 | 重新下载完整安装包；自行改过素材时重新生成 `checksums.json` |
| 页面安装按钮没有响应 | 浏览器需允许打开桌面应用；也可使用脚本或手动复制 |

## English quick start

Run `python3 scripts/install.py` (Windows: `py -3 scripts/install.py`) from the extracted package. Python 3.10+ is required; third-party packages are not. The default destination is `~/.codex/pets/gpt-dragon-girl/`, with `CODEX_HOME` respected. Restart the client, select GPT小龙女 under Settings → Pets, and use `/pet`. To uninstall while keeping a backup, add `--uninstall`.
