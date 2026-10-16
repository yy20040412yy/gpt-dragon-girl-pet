# 发布到 GitHub

建议仓库名：`gpt-dragon-girl-pet`。可直接使用项目目录创建公开仓库。

## 使用 GitHub CLI

安装 Git、GitHub CLI 后，在项目根目录执行：

```bash
gh auth login
git init -b main
git add .
git commit -m "Release GPT Dragon Girl pet v1.0.0"
gh repo create gpt-dragon-girl-pet --public --source . --remote origin --push
```

已有 Git 仓库与首次提交时，跳过 `git init`、`git add` 和 `git commit`。Git 尚未设置提交身份时，先设置自己的 Git 作者名和邮箱。仓库名已被使用时，请选择新名称，避免向无关仓库推送。

## 使用 GitHub 网页

1. 在 <https://github.com/new> 创建名为 `gpt-dragon-girl-pet` 的 Public 仓库，不预先生成 README 或许可证。
2. 选择 **uploading an existing file**，上传解压后的项目内容，保留目录结构。
3. 提交到 `main`。使用 Git 推送完整目录可确保 `.github/` 工作流与 `.nojekyll` 一并上传。

## 开启在线预览

在仓库 **Settings → Pages** 中选择 **Deploy from a branch**，选择 **main** 和 **/(root)**，点击保存。

标准项目页面地址形如 `https://<owner>.github.io/gpt-dragon-girl-pet/`。页面会从这个地址识别仓库并生成安装链接。若使用自定义域名，在 `preview.js` 顶部的 `PUBLISHED_REPOSITORY` 填入真实的 `owner/repository`；在设置前保留手动安装入口。

## 发布安装包

推送版本标签，已包含的 GitHub Actions 会验证并创建 Release：

```bash
git tag v1.0.0
git push origin v1.0.0
```

如仓库关闭了 Actions，可自行运行：

```bash
python3 scripts/build_release.py
gh release create v1.0.0 dist/gpt-dragon-girl-pet.zip dist/SHA256SUMS.txt --title "GPT 小龙女 v1.0.0" --notes-file docs/RELEASE_NOTES.md
```

发布内容包括图集、清单、预览、安装工具及许可文件。仓库不包含原始参考插画、个人账户记录或本地生成过程的内部日志。
