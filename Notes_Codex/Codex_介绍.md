# Codex — AI 编程助手介绍

## 什么是 Codex？

Codex 是 OpenAI 推出的**开源终端内编码代理**（open-source terminal-based coding assistant），能够直接在终端中理解任务、读写文件、运行命令，帮助开发者完成从简单脚本到复杂项目的一系列编程工作。

Codex 这个名字指代的是当前这套代理交互系统，而非早期 OpenAI 的 Codex 语言模型。

## 核心能力

- **代码读写与修改** — 通过 patch 工具精确编辑文件，无需手动复制粘贴
- **终端命令执行** — 直接在 Shell（Windows PowerShell）中运行命令，查看输出结果
- **文件与项目探索** — 使用 
g（ripgrep）等工具快速搜索代码库
- **多步骤任务规划** — 通过 Plan 工具拆解复杂任务，逐步执行并跟踪进度
- **子代理并行工作** — 支持创建子代理并行处理独立子任务
- **MCP 服务器集成** — 可连接外部工具（数据库、API、浏览器等）
- **多模态支持** — 可查看图片、生成图像、创建视频等
- **插件系统** — 支持 Browser、Chrome、GitHub、HyperFrames、Remotion 等插件扩展能力

## 工作模式

| 模式 | 说明 |
|------|------|
| **Default** | 默认模式，自主执行任务，必要时向用户提问 |
| **Plan** | 计划模式，先制定详细计划再实施，适合复杂或模糊任务 |

## 审批策略

| 策略 | 说明 |
|------|------|
| never | 不请求审批，自动执行 |
| on-failure | 仅在命令失败时请求审批 |
| on-request | 每次执行命令前请求审批 |
| untrusted | 交互式审批模式 |

## 常用指令与工具

- pply_patch — 创建或修改文件
- shell_command — 运行 Shell 命令
- update_plan — 更新任务计划
- web_search — 网络搜索获取最新信息
- iew_image — 查看本地图片

## 使用提示

- Codex 会读取项目中的 AGENTS.md 文件来了解项目惯例与约束
- 支持安装 **Skills**（技能包）来扩展特定领域能力，如图片生成、PDF 处理、浏览器控制等
- 所有对话和上下文在 **Codex 桌面应用**（Codex Desktop）中管理，支持线程、自动化和工作区依赖

## 链接

- [Codex GitHub 仓库](https://github.com/openai/codex)
- OpenAI 官方网站：https://openai.com

---

*本文档由 Codex 自动生成*
