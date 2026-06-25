> ⚠️ **本文档是网络链接版**，方便发布到不支持本地图片的平台。
> **图片来源：** jsdelivr CDN（GitHub 仓库 `langren34/doc` 镜像）
> **图片地址前缀：** `https://cdn.jsdelivr.net/gh/langren34/doc@main/`
> **备用地址（GitHub 直连，国内访问可能慢）：** `https://raw.githubusercontent.com/langren34/doc/main/`
>
> 如需切换备用地址，批量替换 `https://cdn.jsdelivr.net/gh/langren34/doc@main/` → `https://raw.githubusercontent.com/langren34/doc/main/` 即可。
> **本文档不与本地版同步**——本地的源文档（用相对路径 `anythingllm-official-images/...`）是权威版本。

---

# AnythingLLM 完全使用手册（Windows 版）

> **以官方文档 https://docs.anythingllm.com/ 为依据**，结合本地实操编写。
>
> **版本**：基于 AnythingLLM v1.14.2（2026-06 抓取），覆盖 Windows 10/11 Home + Professional
>
> **配套资料**：
> - 官方原文缓存：`tmp\anythingllm-fresh\`（39 个 .md 页面）
> - 官方配图：`docs\anythingllm-official-images\`（5 张）

---

## 目录

### 第一篇 · 入门
- [第 1 章 AnythingLLM 是什么](#第-1-章-anythingllm-是什么)
- [第 2 章 Windows 安装](#第-2-章-windows-安装)
- [第 3 章 验证安装](#第-3-章-验证安装)

### 第二篇 · 基础
- [第 4 章 三个核心组件](#第-4-章-三个核心组件)
- [第 5 章 第一次配置向导](#第-5-章-第一次配置向导)
- [第 6 章 工作区与对话](#第-6-章-工作区与对话)
- [第 7 章 RAG：让 AI 翻你的文档](#第-7-章-rag让-ai-翻你的文档)

### 第三篇 · 进阶
- [第 8 章 AI Agents](#第-8-章-ai-agents)
- [第 9 章 MCP 兼容性](#第-9-章-mcp-兼容性)
- [第 10 章 Agent Flows](#第-10-章-agent-flows)
- [第 11 章 Model Router](#第-11-章-model-router)
- [第 12 章 Scheduled Jobs](#第-12-章-scheduled-jobs)
- [第 13 章 Chat UI 详解](#第-13-章-chat-ui-详解)
- [第 14 章 System Prompt 与变量](#第-14-章-system-prompt-与变量)

### 第四篇 · 运维
- [第 15 章 数据与隐私](#第-15-章-数据与隐私)
- [第 16 章 更新与升级](#第-16-章-更新与升级)
- [第 17 章 故障排查](#第-17-章-故障排查)
- [第 18 章 卸载](#第-18-章-卸载)

### 附录
- [附录 A 官方资源链接](#附录-a-官方资源链接)
- [附录 B 第三方扩展](#附录-b-第三方扩展)

---

# 第一篇 · 入门

## 第 1 章 AnythingLLM 是什么

![AnythingLLM 官方介绍图](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/01-introduction-header.png)
*图 1-1：AnythingLLM 官方头部图（来源：docs.anythingllm.com/introduction）*

### 1.1 一句话定义（官方原文）

> **AnythingLLM is the easiest to use, all-in-one AI application that can do RAG, AI Agents, and much more with no code or infrastructure headaches.**
>
> — 来源：https://docs.anythingllm.com/introduction

翻译：**AnythingLLM 是最容易上手的全能 AI 应用**，能搞定 RAG、AI Agents 等各种活儿，**零代码、零基础设施烦恼**。

### 1.2 谁开发的

- **公司**：Mintplex Labs, Inc.
- **创始人**：Timothy Carambat
- **背景**：Y Combinator Summer 2022 校友
- **核心团队**（来自官方）：
  - Sean Hatfield（工程师）
  - Marcello Fitton（工程师）
  - Tiff Tang（设计师）
  - 社区贡献者

### 1.3 核心能力

AnythingLLM 是个**全家桶**，但官方强调这 3 大核心：

| 能力 | 解释 | 典型场景 |
|---|---|---|
| **RAG**（检索增强生成） | 让 AI 先翻你的资料再回答 | 问 100 份合同里的"保密期" |
| **AI Agents** | 让 AI 自己调用工具干活 | 让 AI 自己上网搜、自己写文件 |
| **多模型自由切换** | LLM/Embedder/Vector DB 全可换 | 今天 GPT-4o，明天换 DeepSeek |

### 1.4 两种产品形态

官方提供 **Desktop** 和 **Docker** 两种产品，**本文只讲 Windows Desktop**。

| 维度 | **Desktop**（本文重点） | **Docker** |
|---|---|---|
| 安装难度 | 一键安装 exe | 需要懂 Docker |
| 适用 | 个人 / 小团队 | 企业 / 多用户 / 服务器 |
| 内置 LLM | ✅ 自带 Ollama | ❌ 自己接 |
| 多用户权限 | ❌ 单用户 | ✅ |
| 适合 | 想本地隐私玩 AI | 想自建 ChatGPT 替代 |

### 1.5 适合谁

| 你是不是 | 那就适合 |
|---|---|
| 想本地用 AI，怕隐私泄露 | ✅ Desktop |
| 不想配环境，下载即用 | ✅ Desktop |
| 想在国产 AI 上做 RAG | ✅ Desktop |
| 想给团队搭 AI 知识库 | ✅ Docker |
| 只想聊天不传文件 | ❌ 用 ChatGPT 就够 |

---

## 第 2 章 Windows 安装

![Windows 安装官方图](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/02-windows-header.png)
*图 2-1：官方 Windows 安装指南头部图*

### 2.1 系统要求

**来自官方原文**：

> ⚠️ **OPERATING SYSTEM NOTICE**
> AnythingLLM is intended to be used on an user account of **Windows Home**. Other versions of windows (Enterprise or Server) **may not work**. We target for **Windows 11**.

| 项 | 要求 |
|---|---|
| **操作系统** | Windows 10 / Windows 11（Home 或 Professional） |
| **架构** | x86 64-bit 或 ARM 64-bit |
| **不推荐** | Enterprise / Server 版本（可能不工作） |

### 2.2 下载安装包

**官方下载链接**（任选一个）：

- 🖥️ **x86 64-bit**：[AnythingLLMDesktop.exe](https://cdn.anythingllm.com/latest/AnythingLLMDesktop.exe)
- 💪 **ARM 64-bit**（Surface Pro X 等）：[AnythingLLMDesktop-Arm64.exe](https://cdn.anythingllm.com/latest/AnythingLLMDesktop-Arm64.exe)

> 💡 不知道自己电脑是哪种？按 `Win + I` → 系统 → 系统类型，会显示"基于 x64 的处理器"或"基于 ARM64 的处理器"。

### 2.3 安装步骤

**官方原文关键警告**：

> ⚠️ We **do not** recommend installing AnythingLLM Desktop for "all users" on a Windows machine.
> Instead, install for "**Current User** only**. Installing for all users will cause issues with the app and is not supported.

翻译：**千万不要选"所有用户"，必须选"仅当前用户"**。

**步骤**：

1. 双击下载的 `AnythingLLMDesktop.exe`
2. 看到安装界面，按提示走
3. **关键一步**：选安装范围时选 `仅为我(Just me)` 或 `Current User`，**不要**选 `任何人(Everyone)`
4. 等待安装完成（首次会自动下载 GPU 支持包）
5. 桌面会生成 AnythingLLM 图标

![安装过程图](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/03-install-process.png)
*图 2-2：官方安装过程截图*

### 2.4 首次启动

**官方原文**：

> Click on the application name "**AnythingLLM**" on your desktop to boot up AnythingLLM!
>
> _your first boot may take a minute or two to complete on some systems, but subsequent boots will be near instant._

- 双击桌面 **AnythingLLM** 图标
- **首次启动 1-2 分钟**（下载依赖、初始化数据库）
- 后续启动几秒钟

![AnythingLLM 桌面打开图](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/04-desktop-open.png)
*图 2-3：官方启动后的桌面截图*

### 2.5 内置 Ollama + GPU 自动检测

**官方原文**：

> 💡 **Local LLM support**
> AnythingLLM desktop includes a built-in local LLM powered via Ollama. This is a super convenient way to get started with LLMs without any additional setup.
>
> In order for AnythingLLM to leverage your GPU (NVIDIA or AMD) or even NPU we need to install some extra dependencies. This will be done automatically during installation.

**关键信息**：

| 项 | 说明 |
|---|---|
| **内置 LLM** | AnythingLLM Desktop 自带 Ollama，不需要自己装 |
| **GPU 支持** | 自动检测 NVIDIA / AMD / NPU |
| **GPU 依赖** | 安装时自动下载，无需手动操作 |
| **没用 GPU 的后果** | UI 会显示警告，本地 LLM 只能跑 CPU（慢） |

### 2.6 故障排除（官方文档原文）

#### 错误 A：安装时提示 "AnythingLLM cannot be closed"

![安装错误图](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/05-installation-error.png)
*图 2-4：官方错误截图*

**官方原因 1：之前装过的还在后台**

> Since v1.11.0, AnythingLLM minimizes to the system tray when closed.

**解决方法**：
1. 看任务栏右下角系统托盘（时钟旁边），找 AnythingLLM 图标
2. 右键 → "Quit AnythingLLM" 彻底退出
3. 再点安装程序的 "Retry" 重试

**官方原因 2：之前给"所有用户"装过**

**解决方法**：
1. 右键桌面 AnythingLLM 图标 → "打开文件所在的位置"
2. 找到 `Uninstall AnythingLLM.exe`
3. 运行卸载（可能要管理员权限）
4. 重新安装，**这次只选"当前用户"**

> ✅ 官方保证：**以上操作不会删除你的数据或设置**，可以放心操作。

#### 错误 B：GPU 支持从 CDN 下载/解压失败

**官方原文**：

> ⚠️ We do not recommend trying to fix this issue manually as it is very prone to user error and would break when we upgrade to later versions of Ollama in AnythingLLM.
>
> You can avoid all of this by just installing AnythingLLM and Ollama separately and then connecting AnythingLLM to your local Ollama instance.

**官方推荐方案**：

| 方案 | 难度 | 适合 |
|---|---|---|
| **跳过本地 LLM** | ⭐ | 只想用云端 AI（OpenAI、DeepSeek 等） |
| **单独装 Ollama** | ⭐⭐ | 想用本地 LLM + 折腾得起 |
| **手动下载 GPU 文件** | ⭐⭐⭐⭐⭐ | 高级用户（不推荐） |

**如果非要用本地 LLM 又遇到这错误**：

1. 找到 `%APPDATA%\Local\Programs\AnythingLLM\ollama_install.log`
2. 看里面写的 Ollama 版本号（比如 `0.13.0`）
3. 根据版本号手动下载以下文件（NVIDIA GPU）：
   - `https://cdn.anythingllm.com/support/ollama/<version>/bins.7z`
   - `https://cdn.anythingllm.com/support/ollama/<version>/cudav13.7z`
4. 解压到 `%APPDATA%\Roaming\anythingllm-desktop\storage\engines\ollama\lib\ollama\`
5. 在 `...ollama\` 目录建一个空文件 `.ollama-version`（无扩展名），写版本号
6. 重启 AnythingLLM

> ⚠️ 官方明确说"不推荐手动修"——因为升级时又会失败。

---

## 第 3 章 验证安装

### 3.0 安装成功的截图（实操）

![安装成功后的真实界面](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/06-current-workspace-annotated.png)
*图 3-1：AnythingLLM v1.14.2 启动后的真实界面（标注了 6 个主要按钮）*

### 3.1 检查安装

启动 AnythingLLM 后，你应该看到主界面（左下角是 AnythingLLM logo、右边是聊天区）。如果是这样，**安装成功**。

### 3.2 数据存储位置

AnythingLLM 默认把数据存在这里：

```
%APPDATA%\Roaming\anythingllm-desktop\storage\
├── .env                    # 配置（API key 等）
├── documents/              # 你上传的文档
├── vector-cache/           # 向量缓存
├── engines/                # Ollama 等本地引擎
└── plugins/                # 插件/Agent skills
```

> 💡 完整路径：按 `Win + R` → 粘贴 `%APPDATA%\Roaming\anythingllm-desktop\storage\` 回车。

### 3.3 检查版本

点左上角 AnythingLLM logo，**关于**或**设置**里能看到当前版本号。本手册基于 **v1.14.2**。

---

# 第二篇 · 基础

## 第 4 章 三个核心组件

AnythingLLM 把"AI 应用"拆成三个独立的组件，**每个组件都可以换**：

```
[你的文档] → [Embedder 嵌入器] → [Vector DB 向量库] → 检索
                                                        ↓
                                            [LLM Provider] → 生成回答
```

### 4.1 LLM Provider（语言模型）

**职责**：负责"思考"和"写答案"。你问什么、它怎么答，全看这个。

**官方支持的选项**（来自 https://docs.anythingllm.com/features/language-models）：

#### 🌐 云端 LLM（要 API Key）

| 提供商 | 模型举例 | 适合 |
|---|---|---|
| **OpenAI** | GPT-4o, GPT-4.1, o1 | 通用最强 |
| **Anthropic** | Claude 3.5/3.7 Sonnet | 长文档、写代码 |
| **Google Gemini** | Gemini 2.0/2.5 | 多模态 |
| **Azure OpenAI** | 同 OpenAI | 企业合规 |
| **AWS Bedrock** | 多家模型混合 | AWS 生态 |
| **Groq** | Llama, Mixtral | 超快推理 |
| **Mistral AI** | Mistral Large | 欧洲合规 |
| **Cohere** | Command R+ | RAG 专用 |
| **Hugging Face** | 各种开源 | 自由度高 |
| **OpenRouter** | 100+ 模型 | 一站式 |
| **Perplexity AI** | 带搜索的模型 | 联网搜索 |
| **Together AI** | 开源模型 | 便宜 |
| **TrueFoundry** | 企业网关 | 企业部署 |
| **APIpie** | 多模型聚合 | 聚合服务 |
| **OpenAI (generic)** | 兼容 OpenAI 协议 | **国内 AI 用这个**接 |

#### 🏠 本地 LLM（不要钱，但要电脑跑得动）

| 选项 | 说明 |
|---|---|
| **AnythingLLM Default** | 自带 Ollama，零配置 |
| **LM Studio** | 图形界面下载模型 |
| **LocalAI** | OpenAI 兼容的本地服务 |
| **Ollama** | 命令行管理本地模型 |
| **KobaldCPP** | CPU/GPU 通用 |

### 4.2 Embedder（嵌入器）

**职责**：把你的文档变成"向量"（一串数字）。这样 AI 才能"理解"你的文档并搜索。

**官方支持的选项**（来自 https://docs.anythingllm.com/features/embedding-models）：

#### 🌐 云端
| 提供商 | 模型 |
|---|---|
| **OpenAI** | text-embedding-3-small/large |
| **Azure OpenAI** | 同上（Azure 部署） |
| **Cohere** | embed-english-v3 等 |

#### 🏠 本地
| 选项 | 说明 |
|---|---|
| **AnythingLLM Default** | 自带，开箱即用 |
| **LM Studio** | 兼容 OpenAI embedding |
| **LocalAI** | 同上 |
| **Ollama** | nomic-embed-text 等 |

### 4.3 Vector Database（向量数据库）

**职责**：存文档的"向量"，让 AI 快速找到"最相关的几段"。

**官方支持的选项**（来自 https://docs.anythingllm.com/features/vector-databases）：

#### 🌐 云端
- **AstraDB**（DataStax）
- **Pinecone**
- **Qdrant**
- **Weaviate**
- **Zilliz**（Milvus 云）

#### 🏠 本地
- **LanceDB**（默认，99% 用户不用改）
- **Chroma**
- **Milvus**

> 💡 **新手建议**：默认的 LanceDB + AnythingLLM Default Embedder + AnythingLLM Default LLM，先跑通再说。

### 4.4 工作区 vs 全局配置

| 概念 | 范围 | 怎么改 |
|---|---|---|
| **全局配置**（系统设置） | 影响所有工作区 | 侧边栏底部 ⚙️ → LLM / Embedder / Vector DB |
| **工作区配置** | 只影响当前工作区 | 工作区右侧 ⚙️ → 改 LLM / 系统提示 / 温度等 |

---

## 第 5 章 第一次配置向导

> 📌 这一步是**最关键**的——配置错了后面全错。

### 5.1 决策流程

```
Step 1: 选 LLM  ← 看 5.2
Step 2: 选 Embedder  ← 看 5.3
Step 3: 选 Vector DB  ← 看 5.4（默认 LanceDB，别改）
Step 4: 填 API Key  ← 看 5.5（云端 LLM 必需）
```

### 5.2 LLM 选哪个（决策树）

```
你想要？
├─ 完全免费、本地跑
│  └─ AnythingLLM Default（Ollama）⚠️ 电脑要能跑得动
│
├─ 国产、中文好、便宜
│  ├─ DeepSeek → 用 OpenAI 兼容协议接
│  ├─ Qwen → 用 OpenAI 兼容协议接
│  ├─ Kimi（Moonshot）→ 用 OpenAI 兼容协议接
│  └─ 智谱 GLM → 用 OpenAI 兼容协议接
│
├─ 英文最强、不在乎钱
│  └─ OpenAI GPT-4o / Claude 3.5 Sonnet
│
└─ 联网搜索
   └─ Perplexity AI
```

### 5.3 Embedder 选哪个

| 你选的 LLM | 配套 Embedder |
|---|---|
| OpenAI | OpenAI text-embedding-3-small |
| AnythingLLM Default（Ollama） | AnythingLLM Default（自带） |
| 国内 AI（DeepSeek/Qwen 等） | AnythingLLM Default（本地） |

### 5.4 Vector DB 选哪个

**默认 LanceDB**，别改。99% 用户不需要碰这个。

### 5.5 实际操作：填 API Key（云端 LLM 必需）

**实操截图（实测）**：

**步骤 1**：点侧边栏底部 ⚙️（扳手图标），进入设置页：

![设置页入口](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/05b-settings-page.png)
*图 5-1：点击设置图标后进入设置页（左侧菜单完整展开）*

**步骤 2**：左侧菜单选 **AI 提供商 → 大语言模型（LLM）**：

![LLM 配置页](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/05c-llm-config.png)
*图 5-2：LLM 配置页（显示当前 DeepSeek 提供商 + API Key + 模型名）*

下面继续讲操作步骤：


> 📍 这里配 OpenAI / DeepSeek / Anthropic 等云端 LLM 都要填。

**步骤**：

1. 点侧边栏底部 **⚙️ 设置图标**（或工作区右侧的 ⚙️）
2. 左边菜单选 **AI 提供商 → 大语言模型（LLM）**
3. 选你的提供商（OpenAI / Anthropic / DeepSeek 等）
4. 填 **API Key**（在对应厂商的开放平台注册账号拿）
5. 填 **Base URL**（国产 AI 必填，如 `https://api.deepseek.com/v1`）
6. 填 **聊天模型名**（如 `deepseek-chat` / `gpt-4o-mini`）
7. 点 **Save Changes**

> ⚠️ **国产 AI 通用接法**：选 `OpenAI (generic)` 这个 provider，Base URL 和模型名填对应厂商的就行。

### 5.6 验证配置

回到工作区，聊天区顶部应该显示你选的模型名。点它能切换。

---

## 第 6 章 工作区与对话

### 6.1 工作区是什么

> **工作区 = 一个独立的 AI 助手**，带自己的人设、文档、记忆。

举例：
- 工作区 `产品手册` → 喂 100 份 PDF，让 AI 回答产品问题
- 工作区 `代码助手` → 喂代码库，问编程问题
- 工作区 `私人日记` → 记录想法的私人 AI

### 6.2 创建第一个工作区

**操作步骤**（实测过）：

1. 点侧边栏的 **+ 号**（新建工作区）
2. 在弹窗的「工作区名称」框里输入名字，比如 `我的第一个 AI 助手`
3. 点 **Save** 按钮
4. 新工作区出现在侧边栏

![新建工作区对话框](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/06-new-workspace-dialog.png)
*图 6-1：弹出"新工作区"对话框（实测）*

### 6.3 切换工作区

侧边栏点工作区名 → 切换。所有聊天内容、文档、人设都跟着工作区走。

![建好的工作区](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/06-new-workspace-done.png)
*图 6-2：My_AI_Assistant 工作区创建完成（实测，OCR 操作）*

### 6.4 新建对话

侧边栏底部 **+ New Thread** → 开新对话。每个对话独立保存。

### 6.5 删除工作区 / 对话

- **工作区**：右键侧边栏工作区名 → Delete
- **对话**：右键侧边栏对话 → Delete

### 6.6 上传第一个文档

**操作步骤**：

1. 选好工作区
2. 把文件**拖到聊天区**任意位置，或点输入框下方的 **上传文件** 按钮
3. 等它解析完（侧边栏会显示文档名）
4. 解析时间参考：
   - 1 MB 文档 ≈ 30 秒
   - 10 MB 文档 ≈ 2-3 分钟
   - 100 MB 文档 ≈ 15-20 分钟

**支持格式**（来自官方）：
- 📄 PDF, Word (.docx)
- 📝 纯文本 (.txt), Markdown (.md)
- 📊 CSV, Excel
- 🌐 网页 (.html)
- 📋 代码文件 (.py, .js, .ts, .java 等)

### 6.7 第一次对话

1. 在输入框打字
2. 按 **Enter** 或点 ↑ 发送按钮
3. 等 3-10 秒看 AI 回答
4. 如果你上传了文档，AI 回答下面会有 **引用编号**（📌 [1] [2]），点开看原文出处

**提问模板**：

| 场景 | 模板 |
|---|---|
| 总结 | `请用 3 句话总结我上传的文档的核心内容。` |
| 找特定信息 | `我上传的文档里有没有提到 [关键词]？如果有，请引用原文。` |
| 对比 | `对比文档中 X 和 Y 的 [维度]，列出差异。` |
| 多文档 | `对比所有上传文档中关于 [话题] 的说法。` |

### 6.8 重新生成 / 编辑回答

- **重新生成**：AI 回答下方点 🔄 图标
- **编辑**：点 ✏️ 图标可以改 AI 的回答，或重新提问
- **反馈**：👍/👎 给 AI 回答打分（帮助官方改进）

---

## 第 7 章 RAG：让 AI 翻你的文档

> RAG = Retrieval-Augmented Generation（检索增强生成）
> 简单说：**让 AI 先翻你资料再回答**，不靠死记硬背。

### 7.1 Attached vs RAG（两种文档使用方式）

来自 https://docs.anythingllm.com/chatting-with-documents/introduction

| 方式 | 怎么用 | 适合 |
|---|---|---|
| **Attached**（附加） | 把整个文档**塞进 prompt** 里发给 LLM | 文档很小（< LLM 上下文） |
| **RAG**（检索） | 先**检索相关片段**，再发给 LLM | 文档大、要找特定信息 |

**AnythingLLM 默认用 RAG**，因为大多数文档比 LLM 上下文大。

### 7.2 RAG 工作流（官方图）

官方示意图（来自 docs.anythingllm.com/chatting-with-documents/introduction）：

![Attached vs RAG](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/07-chatting-with-documents/chatting-with-documents_introduction_1.png)
*图 7-1：Attached vs RAG 官方示意图*

![Document Pinning](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/07-chatting-with-documents/chatting-with-documents_introduction_4.png)
*图 7-2：文档钉住（Document Pinning）功能*

```
[上传文档]
    ↓
[分块] Chunking（默认 1000 字符一块，相邻重叠 200 字符）
    ↓
[Embedder 把每块变向量]
    ↓
[存入 Vector DB]
    ↓
[你问问题]
    ↓
[Embedder 把问题变向量]
    ↓
[在 Vector DB 找最像的 N 块]
    ↓
[把 N 块内容 + 你的问题一起发给 LLM]
    ↓
[LLM 基于片段回答，附带引用]
```

### 7.3 调优 RAG 参数

**设置路径**：工作区设置 → 文本拆分和分块首选项

| 参数 | 默认 | 调小 | 调大 |
|---|---|---|---|
| **文本块大小** | 1000 字符 | 500（更精确检索） | 2000（更多上下文） |
| **文本块重叠** | 200 字符 | 100（减少冗余） | 400（避免断章） |

> ⚠️ 官方建议：**只在了解副作用时再调**，新手用默认即可。

### 7.4 Document Pinning（钉文档）

工作区设置里有个 **Pin Document** 功能：把某个文档**永远**当成上下文，不用每次都检索。

**适用**：常被引用的小文档（比如"产品介绍"、"代码规范"）。

### 7.5 为什么 AI 不引用我的文档？

**可能原因**（来自官方）：
1. 文档**还没解析完**（看侧边栏）
2. 文档格式问题（扫描版 PDF 需先 OCR）
3. Embedder 模型不匹配
4. 问题太泛，AI 觉得不需要引用

**解决**：
- 等解析完成（侧边栏文档不再闪烁）
- 换 Embedder（试试 text-embedding-3-large）
- 提问时明确说"请基于文档回答"

### 7.6 引用机制

AI 回答下方会出现 **📌 [1] [2] [3]** 这样的引用编号。点击可以查看：
- 引用的是哪段原文
- 来自哪个文档
- 原文内容预览

---

# 第三篇 · 进阶

## 第 8 章 AI Agents

> AI Agent = 能**自己调用工具**干活的 AI
> 来源：https://docs.anythingllm.com/agent/overview

### 8.1 Agent vs Chat 的区别

| | 普通 Chat | Agent |
|---|---|---|
| 你问 | "北京天气" | "提醒我明天带伞" |
| AI 怎么答 | 看训练数据瞎编 | 真的去查日历、加提醒 |
| 能不能调用工具 | ❌ | ✅ |

### 8.2 内置 Skills（官方 14 个）

来自 https://docs.anythingllm.com/agent/usage/overview

| Skill | 干啥 |
|---|---|
| **RAG Search** | 在工作区文档里搜 |
| **Web Browsing** | 浏览器搜（带视觉理解） |
| **Web Scraping** | 抓指定网页内容 |
| **Save Files** | 把 AI 输出存成文件 |
| **List Documents** | 列出工作区文档 |
| **Summarize Documents** | 总结文档 |
| **Chart Generation** | 生成图表（matplotlib） |
| **SQL Agent** | 跑 SQL 查询 |
| **File System Agent** | 操作本地文件 |
| **Document Generation Agent** | 生成文档 |
| **Gmail Agent** | 读/发 Gmail |
| **Google Calendar Agent** | 操作 Google 日历 |
| **Outlook Agent** | 操作 Outlook |

### 8.3 启用 Agent

**官方配置页面截图**：

![Agent 配置](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/08-agent/agent_setup_1.png)
*图 8-1：Agent 配置入口（侧边栏设置 → 代理技能）*

![Agent Skills 按钮](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/08-agent/agent_setup_2.png)
*图 8-2：Agent Skills 配置页*

**步骤**（来自 https://docs.anythingllm.com/agent/setup）：

1. 工作区设置 → **Agents** 标签
2. 启用 Agent Mode（v1.11.1+ 默认开启）
3. 选要启用的 Skills
4. 配相关 API（如 Gmail Agent 需要 OAuth 认证）
5. 保存

### 8.4 Intelligent Tool Selection（智能工具选择）

来自 https://docs.anythingllm.com/agent/intelligent-tool-selection

- 当 LLM **原生支持 function calling** 时，AI 会**自己决定**用哪个工具
- 不需要你手动指定

### 8.5 自定义 Skill

来自 https://docs.anythingllm.com/agent/custom/introduction

可以写自己的 Skill，需要：
- `plugin.json`（描述）
- `handler.js`（逻辑）
- 详见官方 developer guide

---

## 第 9 章 MCP 兼容性

> MCP = Model Context Protocol
> 来源：https://docs.anythingllm.com/mcp-compatibility/overview

### 9.1 什么是 MCP

官方示意图：

![MCP 概览](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/09-mcp-compatibility/mcp-compatibility_overview_1.png)
*图 9-1：MCP 协议工作原理*

![MCP Desktop](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/09-mcp-compatibility/mcp-compatibility_overview_3.png)
*图 9-2：Desktop 版 MCP 接入示意*

**MCP 是 Anthropic 提出的标准协议**，让 AI 能连接任何"外部工具服务器"。

打个比方：
- AI = 手机
- MCP = USB-C 接口
- MCP 服务器 = U 盘 / 键盘 / 显示器（各种外设）

只要你的工具按 MCP 协议做了，AnythingLLM 就能用。

### 9.2 Desktop 版 MCP 配置

来自 https://docs.anythingllm.com/mcp-compatibility/desktop

**步骤**：

1. 侧边栏底部 ⚙️ → **工具** → **MCP 服务器**
2. 点 **Add MCP Server**
3. 填：
   - **名称**：随便起
   - **传输方式**：stdio / SSE / streamable-HTTP
   - **命令**（stdio）或 **URL**（SSE/HTTP）
4. 点 **Test** 验证连接
5. 保存

**stdio 示例**（连接本地 MCP 服务器）：

```json
{
  "name": "filesystem",
  "transport": "stdio",
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
}
```

### 9.3 常用 MCP 服务器

| MCP 服务器 | 功能 |
|---|---|
| `@modelcontextprotocol/server-filesystem` | 操作本地文件 |
| `@modelcontextprotocol/server-git` | Git 操作 |
| `@modelcontextprotocol/server-github` | GitHub 集成 |
| `@modelcontextprotocol/server-postgres` | Postgres 数据库 |
| `@modelcontextprotocol/server-puppeteer` | 浏览器自动化 |

---

## 第 10 章 Agent Flows

> 来源：https://docs.anythingllm.com/agent-flows/overview
> Agent Flow = **可视化拖拽工作流**，把多个步骤串起来

### 10.1 Flow vs Agent

| | Agent | Flow |
|---|---|---|
| 触发 | 你说一句话 | 你按按钮 / 定时 |
| 执行 | AI 自己决定步骤 | 固定的步骤链 |
| 适合 | 不确定的任务 | 重复的流程 |

### 10.2 5 种 Block

来自 https://docs.anythingllm.com/agent-flows/overview

| Block | 功能 |
|---|---|
| **Web Scraper** | 抓网页 |
| **API Call** | 调任意 HTTP API |
| **LLM Instruction** | 让 LLM 跑提示 |
| **Read File** | 读文件 |
| **Write File** | 写文件 |

### 10.3 4 步入门

来自 https://docs.anythingllm.com/agent-flows/getting-started

1. 创建 Flow
2. 拖 Block 到画布
3. 连线（Block 之间的箭头）
4. 点 **Run** 执行

### 10.4 教程示例：HackerNews Flow

官方教程截图：

![Flow 入门](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/10-agent-flows/agent-flows_getting-started_1.png)
*图 10-1：创建新 Flow*

![Flow 画布](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/10-agent-flows/agent-flows_getting-started_3.png)
*图 10-2：Flow 画布编辑*

![Flow 完成](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/10-agent-flows/agent-flows_getting-started_5.png)
*图 10-3：Flow 完成运行状态*

来自 https://docs.anythingllm.com/agent-flows/tutorial-hackernews

**做啥的**：自动抓 HackerNews 头条 → 让 LLM 总结 → 存成文件。

**步骤**：
1. Web Scraper 抓 `https://news.ycombinator.com/`
2. LLM Instruction："总结这些新闻"
3. Write File：存到 `summary.txt`

### 10.5 调试 Flow

来自 https://docs.anythingllm.com/agent-flows/debugging-flows

每个 Block 都有**输出日志**，能看到每步的输入输出。

---

## 第 11 章 Model Router

> 来源：https://docs.anythingllm.com/model-router/overview
> Model Router = **根据任务自动选模型**

### 11.1 什么是 Model Router

官方截图：

![Model Router](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/11-model-router/model-router_overview_1.png)
*图 11-1：Model Router 路由规则示意*

举例：
- 简单问答 → 用 GPT-4o-mini（便宜）
- 复杂推理 → 用 GPT-4o（贵但强）
- 中文 RAG → 用 DeepSeek（中文好）
- **Model Router 自动判断**用哪个

### 11.2 设置

来自 https://docs.anythingllm.com/model-router/setup

1. 侧边栏底部 ⚙️ → **模型路由器**
2. 选"路由器"模型（用便宜的，如 GPT-4o-mini）
3. 配路由规则：
   - 关键词匹配 → 用某模型
   - 任务类型 → 用某模型
   - 默认 → 用某模型
4. 保存

---

## 第 12 章 Scheduled Jobs

> 来源：https://docs.anythingllm.com/scheduled-jobs/overview
> Scheduled Job = **定时任务**，让 AI 自动跑

### 12.1 场景

- 每天早上 9 点：AI 自动汇总昨天的工作区消息
- 每周一：AI 自动生成周报
- 每月 1 号：AI 自动备份

### 12.2 创建任务

官方截图：

![任务创建](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/12-scheduled-jobs/scheduled-jobs_getting-started_1.png)
*图 12-1：创建新定时任务*

![Cron Builder](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/12-scheduled-jobs/scheduled-jobs_scheduling_1.png)
*图 12-2：Cron 表达式图形化构建器*

来自 https://docs.anythingllm.com/scheduled-jobs/getting-started

1. 侧边栏底部 ⚙️ → **工具** → **计划好的任务**
2. 点 **+ New Job**
3. 填：
   - **名称**：`每日工作汇报`
   - **工作区**：选哪个工作区
   - **Cron 表达式**：`0 9 * * *`（每天 9 点）
   - **Prompt**：`总结这个工作区昨天的新消息`
4. 保存

### 12.3 Cron 表达式

来自 https://docs.anythingllm.com/scheduled-jobs/scheduling

格式：`分 时 日 月 周`

| 表达式 | 含义 |
|---|---|
| `0 9 * * *` | 每天 9:00 |
| `0 9 * * 1` | 每周一 9:00 |
| `0 0 1 * *` | 每月 1 号 0:00 |
| `*/30 * * * *` | 每 30 分钟 |

> 💡 官方提供了**图形化 Cron Builder**，不用手写表达式。

### 12.4 查看运行结果

来自 https://docs.anythingllm.com/scheduled-jobs/viewing-runs

点任务 → **Runs** 标签 → 看每次运行的时间、状态、输出。

---

## 第 13 章 Chat UI 详解

来源：https://docs.anythingllm.com/chat-ui

### 13.1 顶部区域

- **左侧**：工作区名 + 上传 / 设置图标
- **中间**：当前对话名
- **右侧**：当前模型名（点击切换）

### 13.2 侧边栏（左）

- **顶部**：搜索框 + 工作区列表
- **中部**：对话历史
- **底部**：4 个图标
  - 🔗 链接（share）
  - 📖 文档
  - 🎮 游戏（？可能是社区功能）
  - 🔧 工具

### 13.3 聊天区（中央）

- **顶部**：模型名 + 全屏按钮
- **中部**：消息流（你 + AI）
- **底部**：
  - 输入框（占位文字 `发送消息`）
  - `+ 工具` 按钮（左侧）
  - 麦克风 🎤（语音输入）
  - ↑ 发送按钮（最右）
  - 三个快捷按钮：`创建代理` / `编辑工作区` / `上传文件`

### 13.4 消息操作

每条 AI 回答下面有 4 个图标：

| 图标 | 功能 |
|---|---|
| 🔄 | 重新生成回答 |
| ✏️ | 编辑 / 重新提问 |
| 👍 / 👎 | 反馈（帮助官方改进） |
| 📌 | 显示引用来源 |

---

## 第 14 章 System Prompt 与变量

### 14.1 System Prompt 是什么

> System Prompt = 给 AI 的"人设 / 行为准则"
> 来源：
来源：https://docs.anythingllm.com/features/system-prompt-variables

工作区设置 → **System Prompt** → 填你的"人设"。

### 14.2 变量语法

**单花括号** `{var}`（不是 `{{var}}`）。

### 14.3 常用变量

官方截图：

![System Prompt 变量](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/14-features/features_system-prompt-variables_3.png)
*图 14-1：System Prompt 变量实际使用示例*

| 变量 | 含义 | 例子 |
|---|---|---|
| `{date}` | 当前日期 | `2026-06-25` |
| `{user-name}` | 当前用户名 | `Zhang San` |
| `{system-prompt}` | 系统提示（用于嵌套） | — |
| `{workspace}` | 当前工作区名 | `产品手册助手` |
| `{time}` | 当前时间 | `20:30` |

### 14.4 示例

```
你是 AnythingLLM 的助手。当前日期是 {date}。
请基于工作区 "{workspace}" 的文档回答用户问题。
- 简洁、不啰嗦
- 列点说明优于长段落
- 不确定就直说，别瞎编
```

### 14.5 Memories（记忆功能）

官方截图：

![Memories 设置](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/14-features/features_memories_1.png)
*图 14-2：Memories 配置入口*

![Memories 侧边栏](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/14-features/features_memories_2.png)
*图 14-3：Memories 侧边栏显示*

> 来源：https://docs.anythingllm.com/features/memories

AnythingLLM 可以让 AI **跨工作区记住**某些信息（比如用户的偏好）。

**类型**：
- **全局记忆**：所有工作区共享
- **工作区记忆**：只当前工作区

**使用**：在对话中说"记住我xxx"，AI 会自动存为记忆。

---

# 第四篇 · 运维

## 第 15 章 数据与隐私

### 15.1 数据存储位置

AnythingLLM Desktop 把所有数据存在：

```
%APPDATA%\Roaming\anythingllm-desktop\
├── .env                          # 配置文件（含 API key）
├── storage/
│   ├── documents/                # 上传的文档
│   ├── vector-cache/             # 向量缓存
│   ├── engines/                  # 本地 LLM 引擎
│   ├── plugins/                  # Agent skills
│   └── [workspaces]/             # 各工作区数据
└── logs/                         # 日志
```

**打开方式**：`Win + R` → 粘贴 `%APPDATA%\Roaming\anythingllm-desktop\` → 回车

### 15.2 隐私模式（来自官方）

官方截图：

![Privacy 设置](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/14-features/features_privacy-and-data-handling_2.png)
*图 15-1：隐私与数据处理设置页*

> 来源：https://docs.anythingllm.com/features/privacy-and-data-handling

**官方承诺**：
- ? 默认**完全本地运行**（除非要调云端 LLM）
- ? **不上传你的文档**到 AnythingLLM 服务器
- ? **API key 本地存储**（在 `.env` 里）
- ? **遥测数据可关闭**

**遥测设置**：系统设置 → 通用设置 → 关闭遥测

### 15.3 安全与访问

官方截图：

![密码保护](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/14-features/features_security-and-access_2.png)
*图 15-2：单用户密码保护*

> 来源：https://docs.anythingllm.com/features/security-and-access

| 功能 | 适用版本 | 说明 |
|---|---|---|
| 单用户模式 | Desktop | 默认 |
| 多用户 + 权限 | Docker / Cloud | 企业版 |

**Desktop 默认无登录**，任何能用电脑的人都能打开。**如果是公用电脑，建议设置 Windows 账户密码**。

### 15.4 备份

**关键要备份的**：
```
%APPDATA%\Roaming\anythingllm-desktop\storage\.env          # API key 配置
%APPDATA%\Roaming\anythingllm-desktop\storage\documents\   # 文档
%APPDATA%\Roaming\anythingllm-desktop\storage\[workspaces]\ # 工作区
```

**不需备份**：vector-cache（会自动重建）

---

## 第 16 章 更新与升级

![更新页面](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/02-installation-desktop/installation-desktop_update_1.png)
*图 16-1：官方更新页面*

> 来源：https://docs.anythingllm.com/installation-desktop/update

### 16.1 怎么更新

**方式 1：桌面应用内自动更新**

- 启动时自动检查更新
- 有更新会提示，点 **Update**
- 自动下载并安装（要重启）

**方式 2：手动下载**

1. 去 [anythingllm.com/download](https://anythingllm.com/download)
2. 下载最新 `AnythingLLMDesktop.exe`
3. 双击安装（会覆盖旧版本）
4. **数据不丢**（数据在 `%APPDATA%` 里，不在安装目录）

### 16.2 更新注意事项

| 项 | 行为 |
|---|---|
| **数据** | ? 保留 |
| **API Key** | ? 保留 |
| **文档** | ? 保留 |
| **工作区** | ? 保留 |
| **本地 LLM 模型** | ? 保留（除非主版本升级） |

### 16.3 查看版本

- 启动时标题栏显示版本号
- 或：设置 → 关于

---

## 第 17 章 故障排查

> 来源：https://docs.anythingllm.com/installation-desktop/debug

### 17.1 调试日志

官方截图：

![Debug 页面](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/02-installation-desktop/installation-desktop_debug_1.png)
*图 17-1：官方调试日志页面*

**日志位置**：
```
%APPDATA%\Roaming\anythingllm-desktop\logs\
```

**日志类型**：
- `app.log` — 主程序日志
- `collector.log` — 文档解析
- `ollama_install.log` — Ollama 安装
- `event-logs`（在 UI 里）— 事件日志

### 17.2 常见问题

#### Q1: AI 不回答 / 一直转圈

**可能**：
1. LLM Provider 配置错
2. API Key 失效或欠费
3. 网络问题（云端 LLM）

**解决**：
1. 检查设置 → AI 提供商 → LLM 配置
2. 测试 API Key 能不能用（在厂商开放平台）
3. 看日志有没有报错

#### Q2: 上传文档失败 / Fetch failed on upload

**来源**：https://docs.anythingllm.com/fetch-failed-on-upload

**原因**：Embedder 服务连接失败

**解决**：
1. 检查 Embedder 配置（默认 AnythingLLM Embedder 不需要 API Key）
2. 换云端 Embedder（OpenAI）测试
3. 重启 AnythingLLM

#### Q3: Ollama 连接失败

**来源**：https://docs.anythingllm.com/ollama-connection-troubleshooting

**常见原因**：
- Ollama 没启动
- 端口冲突
- 防火墙

**解决**：
1. 检查 Ollama 是否运行
2. 重启 Ollama 服务
3. 改 AnythingLLM 里的 Ollama 连接地址

#### Q4: Agent 不调用工具

**来源**：https://docs.anythingllm.com/agent-not-using-tools

**原因**：
- 用的 LLM 不支持 function calling
- Agent 没启用

**解决**：
1. 换支持 function calling 的 LLM（GPT-4o、Claude 3.5 等）
2. 工作区设置 → Agents → 启用 Agent Mode

#### Q5: 安装失败 / 闪退

参考第 2.6 节"故障排除"。

### 17.3 完全重置

如果实在搞不定，**重置整个应用**：

1. 卸载 AnythingLLM（控制面板 → 程序）
2. **保留** `%APPDATA%\Roaming\anythingllm-desktop\storage\.env`（API key）
3. 重新安装
4. 把 `.env` 放回原位

> ?? 不要删除 `storage` 目录，否则你的所有数据都没了。

---

## 第 18 章 卸载

![卸载页面](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/02-installation-desktop/installation-desktop_uninstall_1.png)
*图 18-1：官方卸载页面*

> 来源：https://docs.installation-desktop/uninstall

### 18.1 卸载步骤

**方式 1：Windows 设置**

1. `Win + I` → 应用 → 已安装的应用
2. 找 AnythingLLM → 点 **卸载**
3. 确认

**方式 2：安装目录**

1. 桌面右键 AnythingLLM 图标 → 打开文件所在的位置
2. 双击 `Uninstall AnythingLLM.exe`
3. 确认

### 18.2 卸载后清理

卸载默认**保留**数据在 `%APPDATA%\Roaming\anythingllm-desktop\`，方便重装时恢复。

**如果想彻底删除数据**：

1. 删除整个 `%APPDATA%\Roaming\anythingllm-desktop\` 目录
2. 删除 `%APPDATA%\Local\Programs\AnythingLLM\` 目录（如有残留）

---

# 附录

## 附录 A 官方资源链接

### 官方文档
- ?? [AnythingLLM 文档首页](https://docs.anythingllm.com/)
- ?? [下载页](https://anythingllm.com/download)
- ?? [官方路线图](https://docs.anythingllm.com/roadmap)

### 官方社区
- ?? [GitHub 仓库](https://github.com/Mintplex-Labs/anything-llm)
- ?? [Discord 社区](https://discord.gg/Dh4zSZCdsC)
- ?? [Twitter](https://twitter.com/mintplexlabs)

### 版本历史
来自 https://docs.anythingllm.com/changelog/overview

| 版本 | 关键特性 |
|---|---|
| **v1.14.2** | 最新 |
| v1.14.1 | — |
| v1.14.0 | — |
| v1.13.0 | OpenAI 兼容协议接入国内 AI |
| v1.12.x | — |
| v1.11.1+ | Agent Mode 默认开启 |
| v1.11.0 | 系统托盘最小化 |

## 附录 B 第三方扩展

### B.1 Desktop Assistant（桌面助手）

![Desktop Assistant](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/B1-desktop-assistant/desktop-assistant_features_1.png)
*图 B-1：Desktop Assistant 功能*

> 来源：https://docs.anythingllm.com/desktop-assistant/introduction

**做啥的**：把 AnythingLLM 嵌入到任何桌面应用里（带快捷键唤醒）。

**安装**：https://docs.anythingllm.com/desktop-assistant/introduction

### B.2 Browser Extension（浏览器扩展）

> 来源：https://docs.anythingllm.com/browser-extension/install

**做啥的**：在任何网页上右键 → 让 AnythingLLM 处理选中内容。

### B.3 Meeting Assistant（会议助手）

![Meeting Assistant](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/B2-meeting-assistant/meeting-assistant_features_1.png)
*图 B-2：Meeting Assistant 功能*

> 来源：https://docs.anythingllm.com/meeting-assistant/introduction

**做啥的**：自动加入会议、转录音、生成纪要。

### B.4 Channels（聊天渠道）

![Telegram 接入](https://cdn.jsdelivr.net/gh/langren34/doc@main/anythingllm-official-images/B3-channels/channels_telegram_1.png)
*图 B-3：Telegram 接入配置*

> 来源：https://docs.anythingllm.com/channels/telegram

**支持**：Telegram 等第三方聊天平台接入 AnythingLLM。

### B.5 Mobile（移动端）

> 来源：https://docs.anythingllm.com/mobile/overview

**iOS / Android** 官方 App（需 AnythingLLM Cloud 订阅）。

### B.6 Community Hub（社区资源）

> 来源：https://docs.anythingllm.com/community-hub/about

**官方社区资源市场**：
- 下载社区制作的 Agent Skills
- 下载社区制作的 System Prompts
- 上传你自己的（[upload 指南](https://docs.anythingllm.com/community-hub/upload)）
- 导入别人的（[import 指南](https://docs.anythingllm.com/community-hub/import)）

---

# ?? 完结

**你刚掌握了**：
1. ? AnythingLLM 是什么、能干啥
2. ? Windows 安装 + 故障排除
3. ? 三大核心组件（LLM / Embedder / Vector DB）
4. ? 第一次配置（选 LLM、填 API Key）
5. ? 工作区、对话、文档
6. ? RAG 工作原理
7. ? AI Agents + 内置 Skills
8. ? MCP 协议接入外部工具
9. ? Agent Flows 可视化工作流
10. ? Model Router 智能路由
11. ? Scheduled Jobs 定时任务
12. ? Chat UI 详解
13. ? System Prompt + 变量 + Memories
14. ? 数据存储、隐私、备份
15. ? 更新、卸载
16. ? 故障排查
17. ? 第三方扩展

## ?? 推荐后续学习路径

| 你想做什么 | 看哪一章 |
|---|---|
| 让 AI 帮你查资料 | 第 6、7 章 |
| 让 AI 帮你自动化工作 | 第 8、10 章 |
| 接外部工具（GitHub、Notion 等） | 第 9 章 |
| 多模型智能调度（省钱） | 第 11 章 |
| 每天定时跑 AI 任务 | 第 12 章 |
| 数据迁移 / 备份 | 第 15 章 |

> **有问题？**
> - ?? 官方文档：https://docs.anythingllm.com/
> - ?? 提 issue：https://github.com/Mintplex-Labs/anything-llm/issues
> - ?? Discord：https://discord.gg/Dh4zSZCdsC
>
> **最后更新**：2026-06-25（基于 AnythingLLM v1.14.2 官方文档）

