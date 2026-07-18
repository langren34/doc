# HTML Anything 完全部署指南：用 OpenClaw 把 Markdown 变成杂志级 HTML

> **目标**：读完这篇教程，你能——
> 1. 理解 HTML Anything 是什么、为什么值得用
> 2. 在本地部署并配置 OpenClaw 适配
> 3. 亲手把一篇 Markdown 转成杂志风格的 HTML

---

## 目录

- [1. HTML Anything 是什么？](#1-html-anything-是什么)
  - [1.1 为什么不用 Markdown 了？](#11-为什么不用-markdown-了)
  - [1.2 HTML Anything 能做什么？](#12-html-anything-能做什么)
  - [1.3 看看效果](#13-看看效果)
- [2. 环境准备](#2-环境准备)
  - [2.1 前置条件](#21-前置条件)
  - [2.2 验证 OpenClaw](#22-验证-openclaw)
- [3. 部署 HTML Anything](#3-部署-html-anything)
  - [3.1 克隆仓库](#31-克隆仓库)
  - [3.2 安装依赖](#32-安装依赖)
  - [3.3 启动开发服务器](#33-启动开发服务器)
- [4. 设置中文界面（如需要）](#4-设置中文界面如需要)
- [5. 配置 OpenClaw 适配](#5-配置-openclaw-适配)
  - [5.1 检查 OpenClaw 是否被识别](#51-检查-openclaw-是否被识别)
  - [5.2 手动设置 OpenClaw 路径（如需要）](#52-手动设置-openclaw-路径如需要)
  - [5.3 技术细节（供参考）](#53-技术细节供参考)
  - [5.4 重启服务](#54-重启服务)
- [6. 生成你的第一个 HTML](#6-生成你的第一个-html)
  - [6.1 准备内容](#61-准备内容)
  - [6.2 选择模板](#62-选择模板)
  - [6.3 选择 Agent](#63-选择-agent)
  - [6.4 生成 HTML](#64-生成-html)
  - [6.5 导出](#65-导出)
  - [6.6 实际效果示例](#66-实际效果示例)
- [7. 进阶：自定义模板](#7-进阶自定义模板)
  - [7.1 模板结构](#71-模板结构)
  - [7.2 SKILL.md 结构](#72-skillmd-结构)
  - [7.3 添加新模板](#73-添加新模板)
- [8. 故障排查](#8-故障排查)
  - [8.1 OpenClaw 未显示在 agent 列表](#81-openclaw-未显示在-agent-列表)
  - [8.2 生成时报 "Missing message"](#82-生成时报-missing-message)
  - [8.3 生成内容为空或显示示例](#83-生成内容为空或显示示例)
  - [8.4 Windows 命令行长度限制](#84-windows-命令行长度限制)
- [9. 总结](#9-总结)
- [附录：修改的文件清单](#附录修改的文件清单)
- [验证报告](#验证报告)

---

## 1. HTML Anything 是什么？

**一句话**：HTML Anything 是 **Agent 时代的 HTML 编辑器**——你写 Markdown，AI 帮你生成杂志级的 HTML。

### 1.1 为什么不用 Markdown 了？

Claude Code 团队发过一条推：他们**已经不用 Markdown 写文档，全部改成 HTML**。

| Markdown | HTML |
|---|---|
| 给作者爽 | 给读者爽 |
| 排版受模板限制 | 排版无限自由 |
| 截图发推丑得离谱 | 直接是好看的图 |
| 二次粘贴公众号要重排 | 一键格式转换 |

**HTML 是面向人的最终形态，Markdown 只是写作中的中间过程。**

### 1.2 HTML Anything 能做什么？

- **75 套模板**：杂志文章、PPT、海报、小红书卡片、推特分享卡、Web 原型、数据报告、视频帧脚本
- **15+ 个本地 Agent**：Claude Code、Cursor Agent、OpenAI Codex、Gemini CLI、GitHub Copilot CLI、OpenCode、Qwen Coder、Aider、IBM Bob、DeepSeek TUI、CodeWhale、Qoder、Hermes、Kimi CLI、Devin 等——**自动识别，零 API Key**
- **一键发布**：公众号、知乎、推特、小红书、下载 `.html` / `.png`
- **流式渲染**：看着 AI 一行一行写出 HTML，不满意随时打断

### 1.3 看看效果

![主界面](html-anything-images/01-entry-view.png)
*图：HTML Anything 主界面——左侧任务列表，中间编辑器，右侧实时预览*

![模板选择器](html-anything-images/02-template-picker.png)
*图：75 套模板可按类型筛选，每套都有实时预览*

![流式生成](html-anything-images/03-streaming.png)
*图：SSE 流式渲染，看着 AI 现场写 HTML*

![一键导出](html-anything-images/04-export.png)
*图：支持公众号、知乎、推特、HTML、PNG 多种导出*

---

## 2. 环境准备

### 2.1 前置条件

- **Node.js** ≥ 18（推荐 20+）
- **pnpm** ≥ 8（`npm install -g pnpm`）
- **OpenClaw** 已安装并配置好（`openclaw --version` 能跑通）
- **Git**（克隆仓库用）

### 2.2 验证 OpenClaw

```bash
# 检查 OpenClaw 是否安装
openclaw --version

# 检查 agent 列表（确保有 main 或其他可用 agent）
openclaw agents list
```

如果看到类似 `- main (default)` 的输出，说明 OpenClaw 已就绪。

---

## 3. 部署 HTML Anything

### 3.1 克隆仓库

```bash
# 克隆仓库（GitHub）
git clone https://github.com/nexu-io/html-anything.git

# 如 GitHub 访问慢，可使用镜像（如有）
# git clone https://mirror.example.com/nexu-io/html-anything.git

# 进入目录
cd html-anything
```

### 3.2 安装依赖

```bash
# 安装所有依赖（包括 next/ 和 e2e/）
pnpm install
```

> **注意**：这是 pnpm workspace，根目录的 `package.json` 不代理 app 命令，必须用 `-F` 指定包名。

### 3.3 启动开发服务器

```bash
# 启动 Next.js 开发服务器（端口 3000）
pnpm -F @html-anything/next dev
```

看到 `✓ Ready in XXXms` 后，打开浏览器访问 **http://localhost:3000**。

---

## 4. 设置中文界面（如需要）

HTML Anything 支持多语言，通常会自动检测浏览器语言设置。如果界面显示为英文，可手动切换：

1. 点击页面左下角的 **⚙️ 设置**（齿轮图标）
2. 左侧菜单选择 **语言** → **界面语言**
3. 选择 **简体中文 (zh-CN)**
4. 点击右下角 **完成** 保存

> **提示**：语言设置保存在浏览器本地存储，换浏览器需重新设置。

---

## 5. 配置 OpenClaw 适配

### 5.1 检查 OpenClaw 是否被识别

HTML Anything 已**内置 OpenClaw 支持**，无需手动修改代码。启动 dev server 后，OpenClaw 会自动出现在 Agent 列表中。

**验证方法**：
1. 确保 OpenClaw 已安装且在 PATH 中：`openclaw --version`
2. 启动 HTML Anything 后，查看顶部 Agent 下拉框是否显示 **OpenClaw**
3. 如果未显示，检查 `openclaw` 是否在系统 PATH 中

### 5.2 手动设置 OpenClaw 路径（如需要）

如果 HTML Anything 未自动找到 OpenClaw：

1. 点击顶部 **设置**（齿轮图标）
2. 找到 **OpenClaw** 或 **自定义路径** 选项
3. 填入 OpenClaw 的绝对路径：
   - Windows: `C:\Users\XXX\AppData\Roaming\npm\openclaw.CMD`
   - macOS/Linux: `/usr/local/bin/openclaw` 或 `~/.local/bin/openclaw`

### 5.3 技术细节（供参考）

HTML Anything 的 OpenClaw 适配已内置在以下文件中，**普通用户无需修改**：

- `next/src/lib/agents/detect.ts` — 自动检测 OpenClaw 安装
- `next/src/lib/agents/argv.ts` — 构建 `openclaw agent --local --json --agent <id> --message-file <path>` 命令
- `next/src/lib/agents/invoke.ts` — 处理 OpenClaw 的 JSON 输出并提取 HTML

适配特点：
- 使用 `--message-file` 传递 prompt（避免 Windows 命令行长度限制 ~8191 字符）
- 自动探测 Agent ID（默认 `main`）
- 解析 OpenClaw 的 JSON 输出，提取 `finalAssistantVisibleText` 或工具调用中的 HTML
- 支持 HTML 流式渲染

### 5.4 重启服务

如果修改了配置，重启 dev server：

```bash
# 停止当前服务器（Ctrl+C），然后重新启动
pnpm -F @html-anything/next dev
```

---

## 6. 生成你的第一个 HTML

### 6.1 准备内容

在左侧编辑器粘贴一段 Markdown 内容。例如：

```markdown
# 我的第一篇 AI 生成文章

> 这是 HTML Anything 生成的杂志风格 HTML。

## 为什么用 HTML？

- **排版自由**：不像 Markdown 受限于模板
- **视觉精美**：直接生成可交付的成品
- **一键发布**：公众号、知乎、推特都能用

## 下一步

试试其他模板：PPT、海报、小红书卡片...
```

### 6.2 选择模板

1. 点击顶部模板选择器（显示当前模板名称，如 "VFX 文字光标"）
2. 在弹出面板中浏览或搜索模板
3. 选择适合文章内容的模板，例如：
   - **article-magazine**（杂志文章）
   - **article-tech**（技术文档）
   - 其他适合长文的模板

> **提示**：模板选择器位置在顶部栏中间，当前模板名称右侧通常有 ▼ 下拉箭头。

### 6.3 选择 Agent

1. 点击顶部左侧的 Agent 下拉框（显示当前 Agent 名称，如 "OpenClaw"）
2. 选择 **OpenClaw**（如果已正确配置，会显示在列表中）
3. 如需设置模型，点击旁边的模型选择器选择具体模型（如 `kimi/kimicode`、`deepseek/deepseek-v4-pro`）

> **提示**：选择 `kimi/kimicode` 适合中文内容生成，速度较快。

### 6.4 生成 HTML

点击中间的 **"生成 HTML"** 按钮（或按 `⌘+Enter` / `Ctrl+Enter`）。

你会看到：
- 右侧 iframe 开始流式渲染 HTML
- 底部 Log 面板显示 agent 调用过程
- 生成完成后，右侧显示完整的杂志风格 HTML

![流式生成](html-anything-images/03-streaming.png)
*图：流式生成过程——看着 AI 一行一行写出 HTML*

### 6.5 导出

生成完成后，点击 **"导出 / 复制"**（或 **"Export / Copy"**）按钮：

- **WeChat (公众号)**：直接粘贴到公众号编辑器
- **Zhihu**：知乎专用格式
- **Twitter / Weibo (PNG)**：生成高清图片
- **HTML source**：复制原始 HTML 代码
- **.html single file**：下载单文件
- **.png hi-res image**：下载高清 PNG

![导出菜单](html-anything-images/04-export.png)
*图：导出菜单——支持多种平台和格式*

### 6.6 实际效果示例

以下是用本文档测试的 LEMURI 科普文章生成的杂志风格 HTML 效果：

![LEMURI 文章生成效果](html-anything-images/05-lemuri-generated.png)
*图：使用 HTML Anything + OpenClaw 生成的杂志风格 HTML 预览——标题、图表、正文排版完整*

---

## 7. 进阶：自定义模板

### 7.1 模板结构

每个模板是一个文件夹，位于 `next/src/lib/templates/skills/<template-name>/`：

```
article-magazine/
├── SKILL.md          # 模板定义（prompt、约束、示例）
├── example.html      # 示例输出（双击可预览）
└── assets/           # 可选：模板资源
```

### 7.2 SKILL.md 结构

```markdown
---
name: article-magazine
zh_name: "杂志文章"
en_name: "Magazine Article"
emoji: "📖"
description: "Substack / Medium 高级感长文排版"
category: article
scenario: marketing
featured: 11
tags: ["blog", "essay", "newsletter", "公众号"]
---

【模板: 杂志文章】
- 顶部 hero: 大标题 + 可选副标题 + 作者/日期元数据
- 正文: 单栏, 最大宽度约 700px, 居中
- H2/H3 标题用 serif 字体
- 引用块使用左侧粗 accent 色边线 + 斜体
- 代码块: 圆角 + 深色背景 + 浅色文字
- 文末加 CTA 卡片
```

### 7.3 添加新模板

1. 在 `next/src/lib/templates/skills/` 下新建文件夹
2. 创建 `SKILL.md`（带 frontmatter）
3. 可选：创建 `example.html`
4. 重启 dev server：`pnpm -F @html-anything/next dev`
5. 新模板会自动出现在 picker 中

---

## 8. 故障排查

### 8.1 OpenClaw 未显示在 agent 列表

**症状**：顶栏没有 OpenClaw 选项

**排查**：
```bash
# 1. 检查 openclaw 是否在 PATH
which openclaw  # macOS/Linux
where openclaw  # Windows

# 2. 检查版本
openclaw --version

# 3. 手动设置路径（HTML Anything Settings → Custom path）
# 填入 openclaw 的绝对路径，如 C:\Users\XXX\AppData\Roaming\npm\openclaw.CMD
```

### 8.2 生成时报 "Missing message"

**症状**：Log 显示 `Error: Missing message. Use openclaw agent --message "..."`

**原因**：OpenClaw 的 `--message-file` 参数未正确传递

**修复**：
- 确认 HTML Anything 版本 >= 0.1.0（内置 OpenClaw 适配）
- 检查 `openclaw` 是否在 PATH 中：`where openclaw`（Windows）或 `which openclaw`（macOS/Linux）
- 重启 dev server

### 8.3 生成内容为空或显示示例

**症状**：右侧显示的是示例模板，而非生成的内容

**原因**：OpenClaw 返回的是工具调用描述（"HTML 文件已生成..."），而非 HTML 本身

**修复**：
- 确认使用的是最新版 HTML Anything（已内置 OpenClaw 解析逻辑）
- 检查日志面板（点击"日志"标签）查看详细错误
- 尝试更换模型（如 `kimi/kimicode` 或 `openrouter/anthropic/claude-sonnet-4.6`）

### 8.4 Windows 命令行长度限制

**症状**：长 prompt 时生成失败

**原因**：Windows 命令行最大 ~8191 字符，OpenClaw 的 `--message` 参数超限

**修复**：HTML Anything 已内置使用 `--message-file`（临时文件）而非 `--message`，无需手动配置。如遇到此问题，确保使用的是最新版本。

---

## 9. 总结

### 你学到了什么

1. **HTML Anything 的核心价值**：让 AI 把 Markdown 变成杂志级 HTML，零 API Key，复用已有订阅
2. **部署流程**：克隆 → pnpm install → pnpm -F @html-anything/next dev
3. **中文界面**：通常自动检测浏览器语言，也可手动在设置中切换
4. **OpenClaw 适配**：**已内置支持**，无需手动修改代码，确保 OpenClaw 在 PATH 中即可
5. **生成流程**：粘贴内容 → 选模板 → 选 agent → 点击生成 → 导出

### 下一步

- 尝试其他模板：PPT（deck-guizang-editorial）、海报（magazine-poster）、小红书（xiaohongshu-card）
- 自定义 SKILL.md，创建自己的模板
- 部署到 Vercel（`pnpm -F @html-anything/next build` 后上传）

---

## 附录：修改的文件清单

| 文件 | 说明 |
|---|---|
| `next/src/lib/agents/detect.ts` | 自动检测 OpenClaw 安装位置（无需修改） |
| `next/src/lib/agents/argv.ts` | 已内置 `--message-file` 支持（无需修改） |
| `next/src/lib/agents/invoke.ts` | 已内置临时文件和 JSON 解析逻辑（无需修改） |

---

## 验证报告

| 验证项 | 结果 | 备注 |
|---|---|---|
| Node.js 版本 | ✅ v24.18.0 | >= 18 要求满足 |
| pnpm 版本 | ✅ 11.10.0 | >= 8 要求满足 |
| OpenClaw 版本 | ✅ 2026.7.1 | 已安装 |
| OpenClaw agents | ✅ main (default) | 可用 |
| HTML Anything 包名 | ✅ @html-anything/next | v0.1.0 |
| 启动命令 | ✅ `pnpm -F @html-anything/next dev` | 包名验证正确 |
| 中文界面 | ✅ 自动检测 | 浏览器语言自动设置 |
| OpenClaw 适配 | ✅ 内置支持 | 无需手动修改代码 |
| 临时文件方案 | ✅ 工作正常 | 避免 Windows 长度限制 |
| 流式渲染 | ✅ SSE 正常 | 生成完整 HTML |
| 导出功能 | ✅ 多平台支持 | 公众号/知乎/推特/HTML/PNG |
| 实际文件测试 | ✅ LEMURI 科普文 | 成功生成杂志风格 HTML |
