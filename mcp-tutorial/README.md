> ⚠️ **本文档是网络链接版**，方便发布到不支持本地图片的平台。
> **图片来源：** jsdelivr CDN（GitHub 仓库 `langren34/doc` 镜像）
> **图片地址前缀：** `https://cdn.jsdelivr.net/gh/langren34/doc@main/`
> **备用地址（GitHub 直连，国内访问可能慢）：** `https://raw.githubusercontent.com/langren34/doc/main/`
>
> 如需切换备用地址，批量替换 `https://cdn.jsdelivr.net/gh/langren34/doc@main/` → `https://raw.githubusercontent.com/langren34/doc/main/` 即可。
> **本文档不与本地版同步**——本地的源文档（用相对路径 `images/...`）是权威版本。

---

# MCP 完全入门指南：从协议原理到 Claude Code 实战

> 目标读者：想系统理解 **Model Context Protocol（MCP）** 的初学者与开发者。
> 本文基于 [MCP 中文站](https://mcpcn.com/docs/introduction/) 与 [Claude Code 官方中文文档](https://code.claude.com/docs/zh-CN/agents) 整理，涵盖协议基础、三大原语、传输机制、实战开发、Claude Code 集成、Channels 进阶与安全调试。

---

## 目录

- [1. 什么是 MCP：AI 时代的上下文集成协议](#1-什么是-mcpai-时代的上下文集成协议)
- [2. 为什么需要 MCP：传统 AI 集成的困境](#2-为什么需要-mcp传统-ai-集成的困境)
- [3. MCP 核心架构：Host / Client / Server](#3-mcp-核心架构host--client--server)
- [4. 连接生命周期：初始化、消息交换、终止](#4-连接生命周期初始化消息交换终止)
- [5. 三大原语：Resources、Tools、Prompts](#5-三大原语resourcestoolsprompts)
- [6. 传输机制：stdio、SSE、HTTP、WebSocket](#6-传输机制stdiossehttpwebsocket)
- [7. 实战：用 Python 写一个 MCP Server](#7-实战用-python-写一个-mcp-server)
- [8. 在 Claude Code 中使用 MCP](#8-在-claude-code-中使用-mcp)
- [9. 用 Agent SDK 编程调用 MCP](#9-用-agent-sdk-编程调用-mcp)
- [10. 进阶：Channels 让外部事件推动会话](#10-进阶channels-让外部事件推动会话)
- [11. 安全与权限：零信任与人在环路](#11-安全与权限零信任与人在环路)
- [12. 调试与最佳实践](#12-调试与最佳实践)
- [13. 总结](#13-总结)

---

## 1. 什么是 MCP：AI 时代的上下文集成协议

**MCP（Model Context Protocol，模型上下文协议）** 是一个开放标准，用于把 AI 代理（Agent）安全、高效地连接到外部工具和数据源 [官方：mcpcn.com/introduction]。

你可以把它理解为 **AI 应用的 "USB-C 接口"**：

- 过去，每接入一个新数据源（数据库、API、文件系统），开发者都要为 AI 应用写一套定制集成代码。
- MCP 出现后，数据源的作者只需实现一个 **MCP Server**，任何支持 MCP 的 AI 应用（Host）都能直接插上使用。

> "MCP 不仅仅是一个技术标准，它是 AI 应用架构的范式转变。从孤立的 AI 模型到具备丰富上下文感知能力的智能系统，MCP 正在重新定义 AI 与现实世界的交互方式。" [官方：mcpcn.com/introduction]

### 1.1 MCP 解决什么问题

MCP 主要解决三类问题 [官方：mcpcn.com/introduction]：

| 问题 | 传统做法 | MCP 做法 |
|------|---------|---------|
| 重复造轮子 | 每个数据源单独写集成 | 一次实现，到处复用 |
| 安全 nightmare | 直接暴露 API 给 AI | 协议层统一做权限控制 |
| 维护负担 | 数据源变更要改应用代码 | 服务器升级不影响 Host |

### 1.2 与 Claude Code 的关系

Claude Code 是 Anthropic 推出的编码 Agent，它通过 MCP 把 Claude 连接到 [GitHub、数据库、Slack、浏览器、监控系统等](https://code.claude.com/docs/zh-CN/mcp) [官方：code.claude.com/mcp]。例如：

- "查询 PostgreSQL 数据库，看看上周新增用户"
- "检查 Sentry 里的最新错误，并创建一个 PR 修复"
- "根据 Figma 设计更新邮件模板"

这些指令背后，都是 MCP 服务器在替 Claude 与外部系统交互。

---

## 2. 为什么需要 MCP：传统 AI 集成的困境

在 MCP 出现之前，要让 AI 访问企业数据，通常需要：

1. **重复造轮子**：为每个数据源写专用集成代码。
2. **安全性 nightmare**：直接把 API 权限交给 AI，难以细粒度控制。
3. **维护负担**：数据源接口一变，AI 应用代码就要改。
4. **扩展瓶颈**：每增加一个新功能，都要改核心 AI 应用。

MCP 通过 **标准化协议层** 把这些问题解耦：

- **Host**：启动连接的 LLM 应用（如 Claude Desktop、IDE、Agent SDK 应用）。
- **Client**：在 Host 内部与 Server 保持 1:1 连接。
- **Server**：暴露特定功能（数据、工具、提示词）。
- **本地数据源 / 远程服务**：Server 实际访问的对象。

![MCP 架构图](https://cdn.jsdelivr.net/gh/langren34/doc@main/mcp-tutorial/images/mcp-architecture.png)
*图 1：MCP 标准架构 — Host 通过 Client 与多个 Server 通信，Server 再访问本地或远程数据源 [官方：mcpcn.com/architecture]*

### 2.1 企业级价值

MCP 中文站给出了几个量化收益指标 [官方：mcpcn.com/introduction]：

- 开发效率提升 **70%**：复用现有 MCP 服务器，无需重复开发。
- 维护成本降低 **60%**：标准化接口减少集成维护工作量。
- 上线时间缩短 **50%**：丰富的预构建集成加速产品交付。

> 这些数字来自 MCP 中文站的宣传材料，实际收益取决于团队规模与集成复杂度。但它们准确地描述了 **"标准化接口 + 生态复用"** 带来的杠杆效应。

---

## 3. MCP 核心架构：Host / Client / Server

MCP 遵循 **客户端-服务器架构**，其中 Host 应用程序可以连接到多个 Server [官方：mcpcn.com/architecture]。

### 3.1 四个核心角色

| 角色 | 说明 | 示例 |
|------|------|------|
| **Host** | 启动连接的 LLM 应用程序 | Claude Desktop、IDE、Agent SDK 应用 |
| **Client** | 与 Server 保持 1:1 连接 | 每个 Server 对应一个 Client 实例 |
| **Server** | 通过 MCP 暴露功能 | 文件系统 Server、数据库 Server、GitHub Server |
| **Data Source** | Server 访问的数据或服务 | 本地文件、PostgreSQL、远程 API |

### 3.2 为什么 Client 与 Server 是 1:1

MCP 规定一个 Client 只连接一个 Server，但一个 Host 可以同时拥有多个 Client。这样设计的好处是：

- **隔离性**：每个 Server 崩溃不会影响其他 Server。
- **权限最小化**：每个连接只拥有该 Server 所需的权限。
- **生命周期独立**：Server 可以独立启动、停止、重新连接。

### 3.3 协议层与传输层

MCP 架构分为两层 [官方：mcpcn.com/architecture]：

1. **协议层（Protocol）**：处理消息帧、请求/响应链接、高级通信模式。核心类包括 `Protocol`、`Client`、`Server`。
2. **传输层（Transport）**：处理客户端与服务器之间的实际通信。MCP 支持多种传输机制，所有传输都使用 **JSON-RPC 2.0** 交换消息 [官方：mcpcn.com/architecture]。

![MCP 分层](https://cdn.jsdelivr.net/gh/langren34/doc@main/mcp-tutorial/images/mcp-architecture.png)
*图 2：协议层与传输层解耦 — 同一套 MCP 协议可以跑在 stdio、SSE、HTTP、WebSocket 等多种传输之上 [官方：mcpcn.com/architecture]*

---

## 4. 连接生命周期：初始化、消息交换、终止

MCP 连接的生命周期分为三个阶段 [官方：mcpcn.com/architecture]：

### 4.1 初始化（Initialization）

1. Client 发送 `initialize` 请求，携带协议版本与能力声明。
2. Server 响应自己的协议版本与能力。
3. Client 发送 `initialized` 通知作为确认。
4. 之后开始正常消息交换。

```text
Client -> Server: initialize
Server -> Client: initialize response
Client -> Server: initialized notification
```

### 4.2 消息交换（Message Exchange）

初始化后，支持两种模式：

- **请求-响应（Request-Response）**：一方发送请求，另一方返回结果或错误。
- **通知（Notification）**：一方发送单向消息，不期望响应。

MCP 使用 JSON-RPC 2.0，主要消息类型包括 [官方：mcpcn.com/architecture]：

| 类型 | 说明 |
|------|------|
| `Request` | 期望得到响应的请求 |
| `Notification` | 不期望响应的单向消息 |
| `Result` | 请求成功的响应 |
| `Error` | 请求失败的响应 |

标准错误代码基于 JSON-RPC [官方：mcpcn.com/architecture]：

```typescript
enum ErrorCode {
  ParseError = -32700,
  InvalidRequest = -32600,
  MethodNotFound = -32601,
  InvalidParams = -32602,
  InternalError = -32603
}
```

### 4.3 终止（Termination）

任何一方都可以主动关闭连接：

- 调用 `close()` 进行干净关闭。
- 传输层断开。
- 发生错误条件。

---

## 5. 三大原语：Resources、Tools、Prompts

MCP 定义了三种核心原语，分别对应 "数据"、"动作"、"模板" [官方：mcpcn.com/concepts]。

![MCP 三大原语](https://cdn.jsdelivr.net/gh/langren34/doc@main/mcp-tutorial/images/mcp-primitives.png)
*图 3：Resources、Tools、Prompts 的控制权与用途对比。三者分别由应用程序、模型、用户控制 [官方：mcpcn.com/concepts]*

### 5.1 Resources（资源）

**资源**允许 Server 暴露可被 Client 读取并用作 LLM 上下文的数据 [官方：mcpcn.com/resources]。

- 资源由唯一的 **URI** 标识，例如 `file:///home/user/report.pdf`、`postgres://database/customers/schema`。
- 资源可以是 **文本**（UTF-8）或 **二进制**（base64）。
- 资源是 **应用程序控制** 的：Client 决定何时、如何使用它们。Claude Desktop 目前要求用户先明确选择资源 [官方：mcpcn.com/resources]。

资源发现方式 [官方：mcpcn.com/resources]：

- `resources/list`：列出具体资源。
- `resources/templates/list`：列出 URI 模板，用于动态构造资源 URI。

资源读取使用 `resources/read`，响应包含 `contents` 数组，每个元素有 `uri`、`mimeType`，以及 `text` 或 `blob` 之一。

资源还支持实时更新 [官方：mcpcn.com/resources]：

- `notifications/resources/list_changed`：资源列表变更通知。
- `resources/subscribe` + `notifications/resources/updated`：订阅特定资源的内容更新。

### 5.2 Tools（工具）

**工具**允许 Server 暴露可执行的函数，让 LLM 与外部系统交互、执行计算或在现实世界中采取行动 [官方：mcpcn.com/tools]。

- 工具是 **模型控制** 的：Server 暴露工具，供 AI 模型在人工审批后自动调用。
- 每个工具通过 `tools/list` 发现，通过 `tools/call` 调用。
- 工具定义包含 `name`、`description`、`inputSchema`（JSON Schema）。

示例工具定义 [官方：mcpcn.com/tools]：

```json
{
  "name": "calculate_sum",
  "description": "将两个数字相加",
  "inputSchema": {
    "type": "object",
    "properties": {
      "a": { "type": "number" },
      "b": { "type": "number" }
    },
    "required": ["a", "b"]
  }
}
```

工具错误处理的原则：工具错误应该在 **结果对象内** 报告，而不是作为 MCP 协议级错误。这样 LLM 能看到错误并可能纠正 [官方：mcpcn.com/tools]：

```json
{
  "isError": true,
  "content": [
    { "type": "text", "text": "错误：缺少必要参数" }
  ]
}
```

### 5.3 Prompts（提示词）

**提示词**允许 Server 定义可重用的提示模板和工作流，Client 可以将其呈现给用户和 LLM [官方：mcpcn.com/prompts]。

- 提示词是 **用户控制** 的：用户明确选择是否使用。
- 通过 `prompts/list` 发现，`prompts/get` 获取具体提示内容。
- 提示词可以接受参数、嵌入资源上下文、引导多步工作流。

提示词结构 [官方：mcpcn.com/prompts]：

```json
{
  "name": "analyze-code",
  "description": "分析代码以寻找潜在的改进",
  "arguments": [
    { "name": "language", "description": "编程语言", "required": true }
  ]
}
```

动态提示词可以嵌入资源，例如把日志文件和代码文件一起作为上下文 [官方：mcpcn.com/prompts]。

### 5.4 Sampling（采样）：Server 反过来请求 LLM

**采样**是 MCP 的一个强大功能，允许 Server 通过 Client 请求 LLM 补全，从而实现复杂的代理行为，同时保持安全性和隐私性 [官方：mcpcn.com/sampling]。

采样流程 [官方：mcpcn.com/sampling]：

1. Server 发送 `sampling/createMessage` 请求。
2. Client 审查请求，可修改它。
3. Client 从 LLM 采样。
4. Client 审查补全结果。
5. Client 返回结果给 Server。

这种 **人在环路（human-in-the-loop）** 设计确保用户能控制 LLM 看到和生成的内容。

采样请求支持 [官方：mcpcn.com/sampling]：

- `messages`：对话历史（文本或图片）。
- `modelPreferences`：模型选择偏好（cost/speed/intelligence priority）。
- `systemPrompt`：系统提示词（Client 可修改或忽略）。
- `includeContext`：上下文包含范围（`none` / `thisServer` / `allServers`）。
- `temperature`、`maxTokens`、`stopSequences`、`metadata`。

> 注意：MCP 中文站指出，**采样功能目前在 Claude Desktop 客户端中尚不支持** [官方：mcpcn.com/sampling]。它更多用于自定义 Agent SDK 应用或未来客户端。

## 7. 实战：用 Python 写一个 MCP Server

本节我们将实现一个最简单的 MCP Server：提供两个工具，一个是 "打招呼"，一个是 "计算两个数字之和"。这个例子虽小，但涵盖了 **Server 声明、工具发现、工具调用、错误处理** 的完整流程。

### 7.1 环境准备

MCP 官方提供 Python SDK：`mcp`。我们用 `uv` 管理项目（你也可以用 `pip`）。

```bash
# 创建项目
uv init mcp-hello-server
cd mcp-hello-server

# 创建虚拟环境并安装依赖
uv venv
uv add mcp
```

> 命令中的 `uv` 是 Astral 出品的 Python 包管理器，如果你更习惯 `pip`/`venv` 也完全等价。重点是安装 `mcp` 包。

### 7.2 最小 Server 代码（基于当前 Python MCP SDK）

> [本机验证] 以下代码在 `mcp` 包当前版本实测可运行，输出工具列表与调用结果正确。不同 SDK 版本的 API 可能略有差异，请以你安装版本的文档为准。

创建 `server.py`：

```python
from mcp.server.fastmcp import FastMCP

# 初始化 MCP Server
mcp = FastMCP("hello-server")

@mcp.tool()
def greet(name: str) -> str:
    """向用户打招呼"""
    return f"你好，{name}！欢迎使用 MCP。"

@mcp.tool()
def add(a: float, b: float) -> float:
    """计算两个数字之和"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

关键点：

- `FastMCP` 是当前 Python SDK 推荐的高级 API，自动处理工具发现、调用协议与生命周期。
- `@mcp.tool()` 装饰器把函数注册为 MCP Tool，函数名即工具名，docstring 即工具描述，参数类型由类型注解自动生成 JSON Schema。
- `mcp.run(transport="stdio")` 启动基于标准输入输出的传输，适合作为本地子进程被 Host 启动。

### 7.3 运行与测试

由于 stdio Server 需要 Host 来启动它，我们可以直接用 MCP Inspector 或自己写一个最小 Client 来测试。这里用最简单的 Python Client：

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        env=None,
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("工具列表：", [t.name for t in tools.tools])

            result = await session.call_tool("add", {"a": 3, "b": 5})
            print("add 结果：", result.content[0].text)

asyncio.run(main())
```

> 这个 Client 示例来自 MCP 官方 quickstart 的核心骨架 [官方：mcpcn.com/development/build-client]。

### 7.4 添加 Resources 和 Prompts

你可以扩展上面的 Server，增加：

- `resources/list` 与 `resources/read`：暴露一个 `greeting://{name}` 资源。
- `prompts/list` 与 `prompts/get`：暴露一个 `code-review` 提示模板。

MCP 中文站的资源与提示词章节有完整示例 [官方：mcpcn.com/resources]、[官方：mcpcn.com/prompts]。

---

## 8. 在 Claude Code 中使用 MCP

Claude Code 通过 MCP 把 Claude 连接到外部工具。配置方式有三种：

- 命令行：`claude mcp add ...`
- 项目级 `.mcp.json`：与团队共享
- 用户级 `~/.claude.json`：仅自己使用

### 8.1 安装范围：local / project / user

Claude Code 支持三个配置范围 [官方：code.claude.com/mcp]：

| 范围 | 加载位置 | 与团队共享 | 存储位置 |
|------|---------|-----------|---------|
| local | 仅当前项目 | 否 | `~/.claude.json` 中该项目路径下 |
| project | 仅当前项目 | 是（通过版本控制） | 项目根目录 `.mcp.json` |
| user | 所有项目 | 否 | `~/.claude.json` 中 |

### 8.2 用命令行添加本地 stdio Server

把我们刚才写的 `server.py` 添加到 Claude Code：

```bash
claude mcp add --transport stdio hello-server -- python /absolute/path/to/server.py
```

> 一定要用 `--` 分隔 Claude 选项与 Server 命令参数 [官方：code.claude.com/mcp]。

### 8.3 添加远程 HTTP Server

例如连接 GitHub MCP Server：

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

或连接 PostgreSQL：

```bash
claude mcp add --transport stdio db -- npx -y @modelcontextprotocol/server-postgres \
  "postgresql://readonly:pass@prod.db.com:5432/analytics"
```

### 8.4 在 `.mcp.json` 中配置

项目级 `.mcp.json` 示例 [官方：code.claude.com/mcp]：

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PAT}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://readonly:pass@prod.db.com:5432/analytics"
      ]
    }
  }
}
```

> `.mcp.json` 支持环境变量扩展：`${VAR}` 或 `${VAR:-default}` [官方：code.claude.com/mcp]。注意：`env` 字段只传给 Server 进程，不会从 `settings.json` 的 `env` 自动传播 [官方：code.claude.com/debug-your-config]。

### 8.5 管理与调试

常用命令 [官方：code.claude.com/mcp]：

```bash
claude mcp list          # 列出所有配置的服务器
claude mcp get github    # 查看某个服务器的详细信息
claude mcp remove github # 删除服务器
```

在 Claude Code 会话中：

```text
/mcp
```

`/mcp` 面板显示每个连接的服务器、工具数量、连接状态。如果 Server 启动失败，可以运行 `claude --debug mcp` 查看 stderr 输出 [官方：code.claude.com/debug-your-config]。

### 8.6 自动重新连接与工具更新

Claude Code 支持 [官方：code.claude.com/mcp]：

- **自动重新连接**：HTTP/SSE 服务器断开时，会以指数退避重试最多 5 次。
- **动态工具更新**：Server 发送 `list_changed` 通知时，Claude Code 自动刷新可用工具列表。

---

## 9. 用 Agent SDK 编程调用 MCP

Claude Code 终端之外，你也可以在自己的 Python/TypeScript 应用里用 **Claude Agent SDK** 调用 MCP Server。

### 9.1 最小示例：查询文档 MCP Server

```python
import asyncio
import os
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async def main():
    options = ClaudeAgentOptions(
        mcp_servers={
            "claude-code-docs": {
                "type": "http",
                "url": "https://code.claude.com/docs/mcp",
            }
        },
        allowed_tools=["mcp__claude-code-docs__*"],
    )

    async for message in query(
        prompt="Use the docs MCP server to explain what hooks are in Claude Code",
        options=options,
    ):
        if isinstance(message, ResultMessage) and message.subtype == "success":
            print(message.result)

asyncio.run(main())
```

> 这个示例直接来自 Claude Code Agent SDK 文档 [官方：code.claude.com/agent-sdk/mcp]。

### 9.2 工具命名规则

Agent SDK 中，MCP 工具的命名格式为 [官方：code.claude.com/agent-sdk/mcp]：

```text
mcp__<server-name>__<tool-name>
```

例如，名为 `github` 的 Server 中的 `list_issues` 工具，在 Agent SDK 中叫 `mcp__github__list_issues`。

### 9.3 用 `allowedTools` 授权

MCP 工具需要明确授权。推荐用 `allowedTools` 通配符 [官方：code.claude.com/agent-sdk/mcp]：

```python
allowed_tools=[
    "mcp__github__*",      # 允许 github 服务器所有工具
    "mcp__db__query",      # 只允许 db 的 query 工具
]
```

> 官方建议：对于 MCP 访问，优先使用 `allowedTools`，而不是 `permissionMode: "bypassPermissions"`。后者会关闭大多数安全提示，范围过大 [官方：code.claude.com/agent-sdk/mcp]。

### 9.4 检查连接状态

SDK 在每个 `query()` 开始时发送 `system` 消息（subtype 为 `init`），其中包含每个 MCP 服务器的连接状态。你可以在启动时检查 `status` 字段是否为 `needs-auth` 或失败 [官方：code.claude.com/agent-sdk/mcp]。

---

## 10. 进阶：Channels 让外部事件推动会话

标准 MCP 是 **拉模式**：Claude 主动调用 Server 的工具。但很多时候我们需要 **推模式**：外部事件（CI 失败、监控警报、Telegram 消息）主动进入 Claude Code 会话。

**Channels** 就是 Claude Code 对 MCP 推送能力的扩展 [官方：code.claude.com/channels]。

### 10.1 什么是 Channel

Channel 是一个 MCP Server，它把事件推送到运行中的 Claude Code 会话，让 Claude 在你不在终端时也能对外部事件做出反应 [官方：code.claude.com/channels]。

典型场景：

- CI 失败后自动把日志推给 Claude，让它分析原因。
- Telegram 消息到达 Claude，Claude 回复后把答案发回 Telegram。
- 监控警报触发，Claude 自动查询日志和数据库。

### 10.2 Channel 架构

![Channel 架构](https://cdn.jsdelivr.net/gh/langren34/doc@main/mcp-tutorial/images/channel-architecture.svg)
*图 4：Channel 架构 — 外部系统（Telegram / Discord / Webhook）通过本地 Channel Server 把事件推送到 Claude Code 会话 [官方：code.claude.com/channels-reference]*

Claude Code 把 Channel Server 作为子进程生成，通过 stdio 通信。Channel Server 在本地监听 HTTP 或轮询聊天平台 API，当事件发生时推送 `notifications/claude/channel` 通知 [官方：code.claude.com/channels-reference]。

### 10.3 最小 webhook channel 示例

下面是官方文档中的最小单向 webhook channel（用 Bun + TypeScript） [官方：code.claude.com/channels-reference]：

```typescript
#!/usr/bin/env bun
import { Server } from '@modelcontextprotocol/sdk/server/index.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

const mcp = new Server(
  { name: 'webhook', version: '0.0.1' },
  {
    capabilities: {
      experimental: { 'claude/channel': {} },
    },
    instructions: 'Events from the webhook channel arrive as <channel source="webhook" ...>. They are one-way: read them and act, no reply expected.',
  },
)

await mcp.connect(new StdioServerTransport())

Bun.serve({
  port: 8788,
  hostname: '127.0.0.1',
  async fetch(req) {
    const body = await req.text()
    await mcp.notification({
      method: 'notifications/claude/channel',
      params: {
        content: body,
        meta: { path: new URL(req.url).pathname, method: req.method },
      },
    })
    return new Response('ok')
  },
})
```

配置 `.mcp.json`：

```json
{
  "mcpServers": {
    "webhook": { "command": "bun", "args": ["./webhook.ts"] }
  }
}
```

启动 Claude Code 时启用 channel：

```bash
claude --dangerously-load-development-channels server:webhook
```

> 研究预览期间，自定义 Channel 不在 Anthropic 的允许列表中，需要用 `--dangerously-load-development-channels` 测试 [官方：code.claude.com/channels]。

### 10.4 双向 Channel 与权限中继

双向 Channel 还需要公开一个 **reply 工具**，让 Claude 能把回复发回聊天平台。官方 fakechat 插件展示了完整实现 [官方：code.claude.com/channels-reference]。

Channel 还可以中继权限提示：当 Claude 调用需要批准的工具时，你可以通过手机上的 Telegram/Discord 回复 "是" 或 "否"，远程批准 [官方：code.claude.com/channels-reference]。

![权限中继](https://cdn.jsdelivr.net/gh/langren34/doc@main/mcp-tutorial/images/channel-permission-relay.svg)
*图 5：Channel 权限中继 — Claude Code 把权限提示转发到 Channel Server，Server 发送到聊天应用，用户回复后 Server 把判决传回 Claude Code [官方：code.claude.com/channels-reference]*

### 10.5 支持的 Channels

研究预览阶段官方提供 [官方：code.claude.com/channels]：

- **Telegram**：需要 BotFather 创建机器人，配置 `TELEGRAM_BOT_TOKEN`。
- **Discord**：在 Discord 开发者门户创建机器人，启用消息内容意图。
- **iMessage**：macOS 专用，读取 Messages 数据库。
- **fakechat**：本地演示，无需外部服务，适合测试。

---

## 11. 安全与权限：零信任与人在环路

MCP 把强大能力交给 AI，安全设计至关重要。两个来源都反复强调以下原则。

### 11.1 传输安全

- 远程连接使用 **TLS**。
- 验证连接来源，必要时实现身份验证 [官方：mcpcn.com/architecture]。

### 11.2 输入验证

- 根据 JSON Schema 验证所有参数。
- 净化文件路径和系统命令，防止命令注入与目录遍历 [官方：mcpcn.com/tools]。
- 验证 URL 和外部标识符。

### 11.3 访问控制与审计

- 实现细粒度授权，限制每个 Server 能访问的资源。
- 审计工具使用、资源访问、采样请求 [官方：mcpcn.com/architecture]。
- 对资源密集型操作做速率限制。

### 11.4 人在环路（Human-in-the-loop）

MCP 的 **Sampling** 和 **Channel 权限中继** 都设计成人在环路：

- Sampling 中，Client 必须向用户展示提示词，用户可修改或拒绝。
- Channel 权限中继中，远程用户可以通过手机批准/拒绝工具调用 [官方：code.claude.com/channels-reference]。

### 11.5 Claude Code 的权限模式

Claude Code 本身对 MCP 工具有多层控制 [官方：code.claude.com/agent-sdk/mcp]：

- `allowedTools`：显式允许特定 MCP 工具。
- `permissionMode`：控制整体工具批准策略。
- 推荐：**优先使用 `allowedTools` 通配符**，而不是 `bypassPermissions`。

---

## 12. 调试与最佳实践

### 12.1 常用调试命令

在 Claude Code 中 [官方：code.claude.com/debug-your-config]：

| 命令 | 用途 |
|------|------|
| `/mcp` | 查看 MCP 服务器连接状态与工具数量 |
| `/doctor` | 检查配置问题、重复安装、无效设置文件 |
| `/status` | 查看活跃设置源与托管设置状态 |
| `claude --debug mcp` | 启动并查看 MCP 服务器 stderr |
| `claude doctor` | 不启动会话，直接打印诊断 |

### 12.2 常见错误与修复

来自 Claude Code 官方调试文档 [官方：code.claude.com/debug-your-config]：

| 症状 | 原因 | 修复 |
|------|------|------|
| `.mcp.json` 中的 Server 不加载 | 文件放在 `.claude/` 下 | 项目 MCP 配置应在项目根目录的 `.mcp.json` |
| 添加的项目 Server 不出现 | 一次性批准提示被关闭 | 运行 `/mcp` 查看状态并批准 |
| Server 从某些目录启动失败 | `command` 或 `args` 使用相对路径 | 对本地脚本使用绝对路径 |
| Server 启动时缺少环境变量 | 变量在 `settings.json` `env` 中 | `.mcp.json` 中每个 Server 的 `env` 单独设置 |
| 工具调用超时 | 默认工具超时较短 | 在 `.mcp.json` 中加 `"timeout": 600000` |

### 12.3 最佳实践清单

- **工具命名清晰**：`name` 和 `description` 要描述性强，包含示例用法。
- **参数 JSON Schema 完整**：必填字段、类型、范围都要声明。
- **错误处理在结果对象内**：让 LLM 能看到错误并纠正，而不是直接断开连接。
- **资源用 URI 明确标识**：自定义 URI scheme 要文档化。
- **提示词模板化**：用参数减少重复，嵌入资源作为上下文。
- **最小权限原则**：每个 Server 只暴露必要的工具和数据。
- **日志与监控**：记录协议事件、消息流、性能指标。

### 12.4 上下文成本意识

Claude Code 文档给出了一张功能加载流程图 [官方：code.claude.com/features-overview]：

![上下文加载](https://cdn.jsdelivr.net/gh/langren34/doc@main/mcp-tutorial/images/context-loading.svg)
*图 6：Claude Code 功能加载流程 — CLAUDE.md 在每个请求中加载；MCP 工具名称启动时加载，完整架构延迟到使用；Skills 描述启动时加载，完整内容使用时加载；Hooks 外部运行 [官方：code.claude.com/features-overview]*

理解这张图能帮助你做成本控制：

- CLAUDE.md 太大会持续消耗上下文。
- MCP 工具数量多时要启用 **工具搜索（tool search）** 以按需加载 [官方：code.claude.com/mcp]。
- 不用的 Server 及时断开，减少噪音。

---

## 13. 总结

MCP 的核心价值可以用三句话概括：

1. **标准化**：一次实现，到处复用。Server 作者不需要知道 Host 是什么 LLM；Host 也不需要知道 Server 内部怎么实现。
2. **安全**：协议层提供统一的权限、审计、人在环路控制，而不是让 AI 直接拥有外部 API 的完整权限。
3. **生态**：从文件系统、数据库、GitHub，到 Telegram/Discord 推送，MCP 正在形成一个可插拔的 AI 工具生态。

### 学习路径建议

- **初学者**：先理解 Host/Client/Server 架构，动手写一个 Python MCP Server（第 7 章）。
- **进阶者**：在 Claude Code 中接入真实 Server（GitHub、PostgreSQL），体验自然语言驱动外部工具（第 8 章）。
- **开发者**：用 Agent SDK 把 MCP 集成到自己的应用，或尝试 Channels 实现事件驱动（第 9、10 章）。

### 参考链接

- [MCP 官方介绍（英文）](https://modelcontextprotocol.io/introduction)
- [MCP 中文站](https://mcpcn.com/docs/introduction/)
- [Claude Code 文档 — MCP](https://code.claude.com/docs/zh-CN/mcp)
- [Claude Code 文档 — Channels](https://code.claude.com/docs/zh-CN/channels)
- [Claude Code 文档 — 调试配置](https://code.claude.com/docs/zh-CN/debug-your-config)

---

> 版本说明：本文基于 2026-07-23 抓取的 MCP 中文站与 Claude Code 中文文档整理。MCP 协议与 Claude Code 都在快速迭代，建议以官方最新文档为准。
