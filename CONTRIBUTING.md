# 贡献指南

欢迎修复安装问题、改善帧间动作，或补充文档。

1. Fork 项目并创建分支。
2. 只修改与本次目标有关的文件；不要提交原始参考插画、账户信息或生成工具的内部记录。
3. 保持 v2 图集为 1536 × 2288、8 列 × 11 行、单格 192 × 208。动作行和有效帧数见 `animations.json`。
4. 修改素材或 `pet.json` 后更新 `checksums.json`，运行 `python3 scripts/validate.py`。
5. 打开 `index.html` 查看受影响动作，再发起 Pull Request，说明改动和检查结果。

提交代码表示同意按 MIT 许可相关代码贡献；提交自己有权许可的图像、预览或文档表示同意按 CC BY 4.0 许可相应贡献。请保留原作者署名与第三方来源，不提交无权分发的素材。

格式参考：

- [官方 Pets 说明](https://learn.chatgpt.com/docs/pets)
- [官方桌面客户端安装深链接](https://learn.chatgpt.com/docs/reference/commands#pets)

这些是公开的兼容性参考；项目不复制其他开源桌宠仓库的实现代码。
