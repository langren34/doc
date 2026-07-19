﻿# Node.js 使用与运维实战指南

> 本指南面向**需要使用、维护、部署 Node.js 项目**的读者，而非专职 Node.js 开发工程师。内容以 [Node.js 官方 Learn](https://nodejs.org/learn) 为主要参考，按**"装起来 → 跑起来 → 维护起来 → 出问题怎么查"**的逻辑组织。全文基于 **Node.js v24.18.0 / npm 11.16.0** 实测验证，事实标注 `[官方]`（来源官方文档）或 `[本机验证]`（本机实测）。
>
> 阅读建议：新手按顺序读；有运维/排障经验者可先跳到「附录 A：日常检查清单」和「附录 B：命令速查表」，需要时再回看具体章节。

---

## 目录

1. [你在日常工作中会遇到的 Node.js 场景](#1-你在日常工作中会遇到的-nodejs-场景)
2. [安装与环境：先跑起来](#2-安装与环境先跑起来)
3. [项目初始化与运行：从零开始的完整流程](#3-项目初始化与运行从零开始的完整流程)
4. [npm 包管理：使用、管理、检查](#4-npm-包管理使用管理检查)
5. [命令行与 REPL：日常必会命令](#5-命令行与-repl日常必会命令)
6. [文件系统：日常读写操作](#6-文件系统日常读写操作)
7. [模块系统：如何理解与组织代码](#7-模块系统如何理解与组织代码)
8. [HTTP 服务器：如何理解 Web 项目](#8-http-服务器如何理解-web-项目)
9. [异步编程：实际项目中的写法](#9-异步编程实际项目中的写法)
10. [Event Loop：理解非阻塞](#10-event-loop理解非阻塞)
11. [Streams：处理大文件与网络数据](#11-streams处理大文件与网络数据)
12. [并发：CPU 密集与多核](#12-并发cpu-密集与多核)
13. [TypeScript：现代项目如何使用](#13-typescript现代项目如何使用)
14. [测试：如何运行项目测试](#14-测试如何运行项目测试)
15. [调试与诊断：排查问题](#15-调试与诊断排查问题)
16. [安全最佳实践：保护自己](#16-安全最佳实践保护自己)
17. [项目实战：部署与维护一个 Node.js 服务](#17-项目实战部署与维护一个-nodejs-服务)
18. [附录 A：日常检查清单](#18-附录-a日常检查清单)
19. [附录 B：命令速查表](#19-附录-b命令速查表)
20. [附录 C：验证报告](#20-附录-c验证报告)

---

## 1. 你在日常工作中会遇到的 Node.js 场景

### 1.1 先回答：Node.js 是什么？

Node.js 是一个**开源、跨平台的 JavaScript 运行时** `[官方]`。简单说：它让 JavaScript 脱离了浏览器，能在服务器、命令行、桌面应用里运行。

![应用场景地图](https://cdn.jsdelivr.net/gh/langren34/doc@main/Node.js 入门到精通教程/nodejs-tutorial-images/01-application-map.svg)
*图 1：Node.js 常见应用场景地图。浏览器端擅长 UI，Node.js 侧擅长 I/O、网络、文件、命令行工具。*

### 1.2 日常工作中的典型场景

| 场景 | 你可能接触到的 Node.js 内容 | 本教程对应章节 |
|------|---------------------------|--------------|
| 公司后端用 Node.js 写 API | Express / Fastify、HTTP 模块、async/await | 第 8、9 章 |
| 前端项目需要构建 | npm 脚本、webpack/vite、package.json | 第 3、5 章 |
| 写个内部脚本处理数据 | fs、path、命令行参数 | 第 6、7 章 |
| 排查 Node.js 服务卡顿 | Event Loop、worker_threads、诊断工具 | 第 10、12、15 章 |
| 新项目选型 TypeScript | 原生 TS 运行、tsconfig | 第 13 章 |
| 部署上线 | npm ci、环境变量、安全加固 | 第 3、16、17 章 |

### 1.3 与浏览器 JavaScript 的区别

| 维度 | 浏览器 | Node.js |
|------|------|---------|
| 常用 API | DOM、window、fetch | fs、http、path、child_process |
| 模块系统 | ES Modules 为主 | CommonJS + ES Modules 双支持 `[官方]` |
| 环境控制 | 无法控制用户浏览器 | 服务器版本由你决定，可用最新语法 `[官方]` |
| 主要用途 | 用户界面 | 服务器、工具、脚本 |

### 1.4 核心特点（为什么快）

- **单线程 + 事件循环**：一个进程处理大量并发连接，不用为每个请求开线程 `[官方]`。
- **非阻塞 I/O**：读文件、查数据库时，主线程不傻等，继续处理其他任务 `[官方]`。
- **V8 引擎**：执行 JavaScript 非常快 `[官方]`。

> 工作提示：Node.js 最擅长 **I/O 密集型**（网络、文件、数据库），不擅长 **CPU 密集型**（视频编码、复杂计算）。后者需要用 worker_threads 或外部服务。

---

## 2. 安装与环境：先跑起来

### 2.1 选择版本

Node.js 官方提供两种版本：`[官方]`

- **LTS（Long Term Support）**：长期支持版，推荐生产环境。
- **Current**：最新特性版，适合尝鲜和开发。

### 2.2 安装方式速查

| 平台 | 推荐方式 | 命令 / 说明 |
|------|---------|------------|
| Windows | 安装包 | 官网下载 `.msi`，双击安装 `[官方]` |
| Windows | 版本管理器 | `winget install Schniz.fnm` + `fnm use --install-if-missing 22` `[官方]` |
| macOS/Linux | 版本管理器 | `curl -fsSL https://fnm.vercel.app/install \| bash` `[官方]` |
| Linux | 二进制包 | 下载 tar.xz 解压，配置 PATH `[官方]` |

### 2.3 安装后必做检查

```bash
node -v      # 查看 Node.js 版本
npm -v       # 查看 npm 版本
```

`[本机验证]` 输出：

```
v24.18.0
11.16.0
```

### 2.4 版本管理器（强烈建议）

用 `fnm` 或 `nvm` 可以：

- 一个机器装多个 Node.js 版本
- 按项目切换版本（`.nvmrc` / `.node-version`）
- 避免全局 npm 包冲突

```bash
> ⚠️ **本文档是网络链接版**，方便发布到不支持本地图片的平台。
> **图片来源：** jsdelivr CDN（GitHub 仓库 `langren34/doc` 镜像）
> **图片地址前缀：** `https://cdn.jsdelivr.net/gh/langren34/doc@main/`
> **备用地址（GitHub 直连，国内访问可能慢）：** `https://raw.githubusercontent.com/langren34/doc/main/`
>
> 如需切换备用地址，批量替换 `https://cdn.jsdelivr.net/gh/langren34/doc@main/` → `https://raw.githubusercontent.com/langren34/doc/main/` 即可。
> **本文档不与本地版同步**——本地的源文档（用相对路径 `nodejs-tutorial-images/...`）是权威版本。

---

# 常用命令
fnm install 22          # 安装 Node 22
fnm use 22              # 当前终端使用 Node 22
fnm default 22          # 设置默认版本
```

### 2.5 国内网络加速（可选）

如果 npm 下载慢：

```bash
npm config set registry https://registry.npmmirror.com
npm config get registry
```

`[本机验证]`

---

## 3. 项目初始化与运行：从零开始的完整流程

### 3.1 项目从零到运行的完整流程

![项目工作流](https://cdn.jsdelivr.net/gh/langren34/doc@main/Node.js 入门到精通教程/nodejs-tutorial-images/02-project-workflow.svg)
*图 2：Node.js 项目从零到运行的标准流程。先安装环境，再初始化项目、安装依赖、编写代码、运行调试。*

### 3.2 第一步：创建目录并初始化

```bash
mkdir my-node-app
cd my-node-app
npm init -y
```

`[本机验证]` 生成 `package.json`：

```json
{
  "name": "my-node-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

### 3.3 第二步：安装依赖

```bash
# 生产依赖（部署时会被安装）
npm install express

# 开发依赖（仅在开发/构建时用）
npm install -D nodemon

# 指定版本
npm install express@4.18.2
```

`[本机验证]`

### 3.4 第三步：编写入口文件

创建 `app.js`：

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, Node.js!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

`[本机验证]`

### 3.5 第四步：运行

```bash
# 普通运行
node app.js

# 开发模式（文件改动自动重启，Node.js v18+）
node --watch app.js

# 使用 package.json 脚本
npm run start
# 或 Node.js 内置任务运行器
node --run start
```

`[本机验证]`

### 3.6 日常会用到的 package.json 配置

```json
{
  "name": "my-node-app",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "start": "node app.js",
    "dev": "node --watch app.js",
    "test": "node --test",
    "build": "node build.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
```

`[官方]` 重要字段说明：

| 字段 | 含义 |
|------|------|
| `name` | 包名，npm 发布时使用 |
| `version` | 版本号，遵循 SemVer |
| `type` | `"module"` 启用 ES Modules，默认 CommonJS |
| `scripts` | 项目命令脚本，用 `npm run <name>` 执行 |
| `dependencies` | 生产依赖 |
| `devDependencies` | 开发依赖 |

### 3.7 依赖版本管理

| 符号 | 含义 | 示例 |
|------|------|------|
| `1.2.3` | 精确版本 | 锁定到 1.2.3 |
| `^1.2.3` | 兼容 1.x.x 最新 | 可更新到 1.9.0，不可到 2.0.0 |
| `~1.2.3` | 兼容 1.2.x 最新 | 可更新到 1.2.9，不可到 1.3.0 |

`[官方]`

### 3.8 生产部署：用 npm ci 而非 npm install

`npm ci` 会严格按 `package-lock.json` 安装，如果与 `package.json` 不一致会直接报错。这能避免线上依赖版本漂移：`[官方]`

```bash
npm ci
node app.js
```

---

## 4. 模块系统：如何理解与组织代码

### 4.1 为什么要分模块

项目变大后，代码全写一个文件会难以维护。模块让代码按功能拆分，每个文件有自己的作用域，避免全局变量冲突。

### 4.2 两种模块系统：CommonJS 与 ES Modules

Node.js 同时支持两种模块系统：`[官方]`

| 特性 | CommonJS | ES Modules |
|------|----------|------------|
| 语法 | `require` / `module.exports` | `import` / `export` |
| 文件扩展名 | `.js`（默认） | `.mjs` 或 `package.json` 中 `"type": "module"` |
| 加载时机 | 运行时同步 | 解析时静态 |
| 顶层 await | 不支持 | 支持 `[官方]` |
| 新项目推荐 | 兼容旧项目 | 推荐 `[官方]` |

> 工作提示：作为使用者，你主要需要识别项目用的是哪种。看 `package.json` 里有没有 `"type": "module"`，有就是 ES Modules；没有默认就是 CommonJS。混合使用时会报错，遇到 `"Cannot use import statement outside a module"` 或 `"require is not defined"` 时，先检查这个字段。

### 4.3 内置模块用 `node:` 前缀

Node.js 推荐用 `node:` 前缀引入核心模块，避免与第三方包重名：`[官方]`

```javascript
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
```

### 4.4 如何理解一个真实项目的模块结构

拿到一个项目，先看目录结构，不需要读每一行代码：`[官方]` / 工程经验

```
my-project/
├── src/
│   ├── index.js          # 入口，通常只负责启动
│   ├── routes/           # 路由：处理 HTTP 请求映射
│   ├── services/         # 业务逻辑：核心功能实现
│   ├── models/           # 数据模型/数据库访问
│   └── utils/            # 工具函数
├── tests/                # 测试文件
├── package.json
└── README.md
```

- **入口文件**（`index.js` / `app.js`）：启动服务，挂载路由和中间件
- **routes/**：只负责接收请求、调用 service、返回响应
- **services/**：处理具体业务逻辑
- **models/**：数据库操作或数据访问层
- **utils/**：通用工具函数

> 工作提示：排查问题时，先定位问题发生在哪一层。是请求没进路由？路由没调 service？还是 service 操作数据库出错？分层定位能大幅减少排查时间。

---

## 5. npm 包管理：使用、管理、检查

### 5.1 npm 是什么

npm 是 Node.js 的默认包管理器，也是世界上最大的单一语言代码仓库，拥有超过 210 万个包 `[官方]`。

![npm 工作流](https://cdn.jsdelivr.net/gh/langren34/doc@main/Node.js 入门到精通教程/nodejs-tutorial-images/04-npm-flow.svg)
*图 4：npm 包管理流程。本地项目通过 npm 从 registry 下载依赖，package.json 记录依赖，lockfile 锁定版本，生产环境用 npm ci 严格安装。*

### 5.2 常用命令速查

| 命令 | 作用 | 工作场景 |
|------|------|----------|
| `npm install` | 安装所有依赖 | 拉取项目后第一次运行 |
| `npm install <pkg>` | 安装并加入 dependencies | 需要新的生产依赖 |
| `npm install -D <pkg>` | 安装并加入 devDependencies | 需要开发/测试工具 |
| `npm install <pkg>@<ver>` | 安装指定版本 | 锁定兼容版本 |
| `npm update` | 更新依赖 | 定期升级安全补丁 |
| `npm uninstall <pkg>` | 卸载依赖 | 移除不需要的包 |
| `npm run <script>` | 运行 package.json 脚本 | 启动/构建/测试 |
| `npm ci` | 严格按 lockfile 安装 | 生产部署 / CI |
| `npm audit` | 检查安全漏洞 | 项目维护 |
| `npm list` | 查看已安装包 | 排查依赖问题 |

`[官方]` `[本机验证]`

### 5.3 package-lock.json 是什么

`package-lock.json` 精确记录每个依赖的版本、来源和校验和，保证团队成员和 CI/生产环境安装完全一致：`[官方]`

- 提交到 Git
- 生产部署用 `npm ci` 而不是 `npm install`

### 5.4 如何检查项目依赖健康

```bash
# 查看是否有漏洞
npm audit

# 查看依赖树
npm list

# 只看生产依赖
npm list --prod

# 查看过时的包
npm outdated
```

`[官方]` `[本机验证]`

### 5.5 发布自己的包（简述）

```bash
# 检查会发布哪些文件
npm publish --dry-run

# 登录并发布
npm login
npm publish
```

`[官方]` 发布前务必用 `--dry-run` 检查，避免把敏感文件（如 `.env`、源码中的测试文件）推送到 registry。

---

## 6. 命令行与 REPL：日常必会命令

### 6.1 REPL 交互式环境

REPL（Read-Eval-Print Loop）是快速测试代码的好工具：

```bash
node
```

`[本机验证]` 常用命令：

```
> 1 + 1
2
> process.version
'v24.18.0'
> .exit
```

| REPL 命令 | 作用 |
|----------|------|
| `.exit` / `Ctrl+D` | 退出 |
| `.help` | 显示帮助 |
| `.load <file>` | 加载脚本 |
| `.save <file>` | 保存会话 |

`[官方]`

### 6.2 读取环境变量

项目配置通常用环境变量，避免把密码等写死到代码里：

```javascript
const port = process.env.PORT || 3000;
```

Windows PowerShell：

```powershell
$env:PORT = "8080"
node app.js
```

Linux/macOS：

```bash
PORT=8080 node app.js
```

`[本机验证]`

### 6.3 读取命令行参数

`process.argv` 包含启动命令和参数：`[官方]`

```javascript
console.log(process.argv);
```

执行 `node app.js --name alice` 后，`process.argv` 会包含 `--name`、`alice` 等。复杂参数解析可用 `commander`、`yargs` 等库。

`[本机验证]`

### 6.4 常用命令行场景

| 场景 | 命令 | 输出 |
|------|------|------|
| 快速测试表达式 | `node -e "console.log(1+1)"` | `2` |
| 查看版本 | `node -v` | `v24.18.0` |
| 开发自动重载 | `node --watch app.js` | 自动重启服务 |
| 运行测试 | `node --test` | 测试报告 |
| 启用调试 | `node --inspect app.js` | 调试 URL |
| 运行 TS 文件 | `node app.ts` | 直接运行（v22.18.0+） |

`[官方]` `[本机验证]`

---

## 7. 文件系统：日常读写操作

### 7.1 fs 模块三种风格

Node.js `fs` 模块支持三种调用风格：`[官方]`

| 风格 | 代码示例 | 适用场景 |
|------|----------|----------|
| 回调式 | `fs.readFile(path, 'utf8', cb)` | 旧代码兼容 |
| 同步式 | `fs.readFileSync(path)` | 脚本启动时读取配置 |
| Promise 式 | `fs.promises.readFile(path)` | 现代项目推荐 |

### 7.2 读取文件

```javascript
const fs = require('node:fs/promises');

async function readConfig() {
  try {
    const data = await fs.readFile('./config.json', 'utf8');
    const config = JSON.parse(data);
    console.log(config);
  } catch (err) {
    console.error('读取失败:', err.message);
  }
}

readConfig();
```

`[本机验证]`

### 7.3 写入文件

```javascript
await fs.writeFile('./output.txt', 'Hello, file system!');
await fs.appendFile('./log.txt', 'New log entry\n');
```

`[本机验证]`

### 7.4 检查文件信息

```javascript
const stats = await fs.stat('./output.txt');
console.log(stats.isFile());      // true
console.log(stats.isDirectory()); // false
console.log(stats.size);          // 字节数
```

`[本机验证]` `[官方]`

### 7.5 路径操作

```javascript
const path = require('node:path');

const filePath = path.join(__dirname, 'data', 'users.json');
console.log(path.basename(filePath));  // users.json
console.log(path.dirname(filePath));   // .../data
console.log(path.extname(filePath));   // .json
console.log(path.resolve('data'));     // 绝对路径
```

`[本机验证]`

### 7.6 大文件：用流

```javascript
const fs = require('node:fs');

const readStream = fs.createReadStream('./big-file.txt', { encoding: 'utf8' });
readStream.on('data', (chunk) => {
  console.log('Chunk size:', chunk.length);
});
```

`[本机验证]` 大文件不要用 `readFile` 一次性读入内存，避免爆内存。

---

## 8. HTTP 服务器：如何理解 Web 项目

### 8.1 HTTP 请求处理流程

一个 Node.js Web 后端的基本流程是：`[官方]`

```
请求到达 -> 解析方法/URL/头 -> 读取请求体 -> 业务处理 -> 发送响应
```

理解这个流程就够了，**日常工作中很少需要手写原生 HTTP 服务器**。

### 8.2 真实项目都用框架

原生 `http` 模块适合学习原理，真实项目几乎都用 Express、Fastify、Koa 等框架。框架帮你做了：路由分发、请求体解析、中间件管理、错误处理等。`[官方]` / 工程经验

你不需要会写框架，但需要会：

1. 看路由文件，知道哪个 URL 对应哪个处理函数
2. 看中间件，知道请求进来后会经过哪些处理
3. 会启动服务并验证 `/health` 或具体接口

### 8.3 请求对象常用属性

作为使用者，排查接口问题时关注这些：`[官方]`

| 属性 | 说明 |
|------|------|
| `req.method` | HTTP 方法：`GET`、`POST`、`PUT`、`DELETE` 等 |
| `req.url` | 请求路径 |
| `req.headers` | 请求头，键名是小写 |
| `req.body` | 请求体（需要 `express.json()` 等中间件解析） |
| `res.status(code)` | 设置响应状态码 |
| `res.json(obj)` | 返回 JSON 响应 |

### 8.4 如何理解 Express 路由

一个 Express 路由文件通常长这样：`[本机验证]`（示例代码，不需要你写）

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.get('/users', (req, res) => {
  res.json([{ id: 1, name: 'Alice' }]);
});

app.post('/users', (req, res) => {
  res.status(201).json(req.body);
});

app.listen(3000);
```

解读：`[本机验证]`

- `app.get('/users', ...)`：处理 `GET /users` 请求
- `app.post('/users', ...)`：处理 `POST /users` 请求
- `app.use(express.json())`：自动把请求体 JSON 解析成 `req.body`
- `res.status(201).json(...)`：返回 201 状态码和 JSON 数据

### 8.5 如何理解一个 Web 项目的 HTTP 层

拿到项目后，看这几个地方：`[官方]` / 工程经验

| 位置 | 看什么 |
|------|--------|
| `src/app.js` 或 `src/index.js` | 服务怎么启动、用了哪些中间件、路由挂载在哪里 |
| `src/routes/` | 有哪些接口，URL 和方法是什么 |
| `src/middleware/` | 请求会经过哪些通用处理（鉴权、日志、错误处理等） |
| 环境变量 `PORT` | 服务监听哪个端口 |

> 工作提示：排查接口问题时，先用 `curl` 或浏览器测试具体 URL，确认是服务没起、路由不存在，还是后端代码报错。先把问题定位到哪一层，再决定看日志还是看代码。

---

## 9. 异步编程：实际项目中的写法

### 9.1 为什么需要异步

Node.js 大量操作是 I/O 型的：读文件、查数据库、网络请求。这些操作如果让主线程傻等，服务就会卡住其他请求。异步让主线程先去做别的事，等 I/O 完成后再回来处理结果。`[官方]`

### 9.2 实际项目推荐：async/await

现代 Node.js 项目几乎都用 `async/await` 写异步：`[本机验证]` `[官方]`

```javascript
const fs = require('node:fs/promises');

async function loadConfig() {
  try {
    const data = await fs.readFile('./config.json', 'utf8');
    return JSON.parse(data);
  } catch (err) {
    console.error('配置读取失败:', err.message);
    throw err;
  }
}
```

你不需要深入理解 Promise 链，只需要记住：

- 异步函数前加 `async`
- 调用异步函数前加 `await`
- 用 `try/catch` 处理错误

### 9.3 并行任务：Promise.all

同时发起多个不相关的请求/读取时，用 `Promise.all`：`[官方]` `[本机验证]`

```javascript
const [users, orders] = await Promise.all([
  fetchUsers(),
  fetchOrders(),
]);
```

> 工作提示：如果有一个失败，整个 `Promise.all` 会失败。想拿到全部结果无论成败，用 `Promise.allSettled`。

### 9.4 常见错误

| 错误 | 现象 | 处理 |
|------|------|------|
| 忘记 `await` | 函数返回 Promise 而不是结果 | 检查是否有 `await` |
| 未捕获异常 | 进程崩溃或请求挂起 | 加 `try/catch` 或全局监听 |
| 回调地狱 | 代码嵌套过深 | 改为 `async/await` |

### 9.5 工作中不要这样做

❌ 回调地狱（旧代码中可能出现）：

```javascript
fs.readFile('a.txt', (err, a) => {
  fs.readFile('b.txt', (err, b) => {
    fs.readFile('c.txt', (err, c) => {
      // ...
    });
  });
});
```

✅ 改为 async/await + Promise.all：

```javascript
const [a, b, c] = await Promise.all([
  fs.readFile('a.txt', 'utf8'),
  fs.readFile('b.txt', 'utf8'),
  fs.readFile('c.txt', 'utf8'),
]);
```

---

## 10. Event Loop：理解非阻塞

### 10.1 一句话解释

Event Loop 让 Node.js 在单线程下处理大量并发。I/O 操作交给系统内核，主线程继续干别的；内核完成后，回调被排队等待执行。`[官方]`

### 10.2 对使用者最重要的三件事

| 要点 | 说明 |
|------|------|
| I/O 不阻塞主线程 | 读文件、查数据库、网络请求时，主线程继续处理其他请求 |
| 不要写阻塞代码 | 大循环、复杂同步计算会卡住整个 Event Loop，导致所有请求变慢 |
| CPU 密集型任务交给 worker_threads | 如图片处理、密码哈希、大数据解析 |

### 10.3 什么时候需要关心 Event Loop

日常运维中，遇到以下现象时要怀疑 Event Loop 被阻塞：`[官方]` / 工程经验

| 现象 | 可能原因 |
|------|----------|
| 服务响应突然变慢 | 某处有大循环或同步计算 |
| CPU 高但请求量少 | 代码在做 CPU 密集型任务 |
| 请求超时但服务没崩溃 | 回调排队，处理不过来 |
| 内存正常但响应慢 | Event Loop 延迟高，不是内存问题 |

### 10.4 如何排查

1. **看日志**：是否有耗时操作被记录
2. **看 CPU**：`pm2 monit` 或 `top` / `htop`
3. **生成火焰图**：`node --prof app.js` 然后 `--prof-process`
4. **使用 clinic.js**：`clinic doctor -- node app.js` 可以诊断 Event Loop 延迟

> 工作提示：大多数使用者不需要深入 Event Loop 的各个阶段。记住"I/O 不阻塞，CPU 会阻塞"就够了。

---

## 11. Streams：处理大文件与网络数据

### 11.1 为什么用流

流（Stream）可以逐块处理数据，不必把整个文件或响应读入内存。`[官方]`

作为使用者，你只需要记住一个场景：

> 处理大文件、视频、网络下载时，用流；否则 `fs.readFile` 一次性读入内存可能爆内存。

### 11.2 四种流类型

| 类型 | 说明 | 例子 |
|------|------|------|
| Readable | 可读 | `fs.createReadStream`、HTTP `req` |
| Writable | 可写 | `fs.createWriteStream`、HTTP `res` |
| Duplex | 可读可写 | TCP socket |
| Transform | 转换 | `zlib.createGzip` |

`[官方]`

### 11.3 什么时候你会遇到流

| 场景 | 接触到的流 |
|------|----------|
| 下载大文件 | HTTP `response` 是流 |
| 上传文件 | HTTP `request` 是流 |
| 日志文件太大 | 用 `fs.createReadStream` 逐行读取 |
| 压缩/解压 | 用 `zlib` 的 Transform 流 |

### 11.4 排查流相关错误

| 现象 | 可能原因 |
|------|----------|
| 内存占用高 | 把流结果一次性 `Buffer.concat` 到大数组 |
| 文件句柄泄漏 | 没有正确处理 `end` / `error` 事件 |
| 数据丢失 | 流还没读完就开始处理 |

> 工作提示：大部分使用者不会自己写流。遇到流相关问题时，优先检查是否用了 `pipeline` 或 `pipe`，并确保监听了 `error` 事件。

---

## 12. 并发：CPU 密集与多核

### 12.1 单线程的局限性

Node.js 是单线程 + Event Loop，擅长 I/O 密集型任务，但不擅长 CPU 密集型任务。如果主线程在做大量计算，所有请求都会变慢。`[官方]`

### 12.2 三种并发方案

| 模块 | 运行方式 | 适用场景 |
|------|----------|----------|
| `child_process` | 独立进程 | 运行外部命令或隔离脚本 `[官方]` |
| `worker_threads` | 同进程线程 | CPU 密集型 JS 任务（如密码哈希、图片处理）`[官方]` |
| `cluster` | 多进程 | 多核扩展 Web 服务器 `[官方]` |

### 12.3 对使用者的建议

- 遇到 CPU 高、响应慢时，先判断是不是代码里有大量计算
- 密码哈希、图片压缩、大数据解析等场景，考虑用 `worker_threads`
- 生产环境多核扩展，优先用 **PM2 或容器编排**，而不是手写 `cluster`

### 12.4 什么时候不需要关心并发

- 普通 CRUD API、文件读写、数据库查询 → 单线程 + Event Loop 足够
- 中小型项目 → 一台机器 + PM2 足够
- 只有出现 CPU 瓶颈或需要利用多核时，才考虑 worker_threads / cluster

> 工作提示：不要为了用并发而用并发。大多数 Node.js 项目先用好单线程模型，性能不够时再优化。

---

## 13. TypeScript：现代项目如何使用

### 13.1 为什么项目用 TypeScript

TypeScript 在 JavaScript 上加了一层类型系统，能在开发阶段发现错误，提高代码可维护性。`[官方]`

### 13.2 作为使用者，你需要知道什么

| 场景 | 操作 |
|------|------|
| 项目源码是 `.ts` | 开发时会用 `tsc` 编译，或直接运行 |
| 生产部署 | 通常是编译后的 `.js`，或原生 TypeScript 运行 |
| 跑类型检查 | `npx tsc --noEmit` |
| 原生运行 `.ts` | `node app.ts`（Node.js v22.18.0+）`[官方]` |

`[本机验证]` 在 Node.js v24.18.0 上可直接运行 `.ts` 文件。

### 13.3 如何运行一个 TypeScript 项目

```bash
# 安装依赖
npm install

# 开发模式
npm run dev

# 构建（如果有 build 脚本）
npm run build

# 类型检查
npx tsc --noEmit
```

`[本机验证]` / `[官方]`

### 13.4 常见 TypeScript 错误

| 错误 | 含义 | 处理 |
|------|------|------|
| `Cannot find module` | 缺少类型定义 | `npm install -D @types/node` 或对应包的 `@types/xxx` |
| `tsconfig.json` 不存在 | 项目没有配置 | 运行 `npx tsc --init` 生成 |
| 类型检查失败 | 代码类型不匹配 | 看具体报错位置，通常是业务逻辑问题 |

> 工作提示：如果你只是维护项目，不需要深入写类型定义。重点是能跑 `npm run build` 和 `npx tsc --noEmit`。

---

## 14. 测试：如何运行项目测试

### 14.1 为什么需要测试

测试能在修改代码或升级依赖后，快速确认核心功能没坏。作为使用者/维护者，你需要会跑测试，不一定需要会写测试。`[官方]` / 工程经验

### 14.2 跑测试的常见命令

```bash
# 最常见：按 package.json 里的 test 脚本跑
npm test

# 直接用 Node.js 内置 Test Runner
node --test

# 运行指定测试文件
node --test tests/**/*.test.js

# 带覆盖率（需要安装 c8）
npx c8 npm test
```

`[官方]` `[本机验证]`

### 14.3 测试失败时怎么办

1. **看最后几行**：错误堆栈最下面通常最具体
2. **看失败用例名**：定位到具体功能
3. **检查环境**：是否缺少 `.env`、数据库是否启动
4. **单独跑**：`node --test tests/xxx.test.js` 缩小范围
5. **问开发团队**：如果是业务逻辑问题，不要自己硬改

### 14.4 测试类型速查

| 类型 | 测什么 | 你在维护时关注 |
|------|--------|---------------|
| 单元测试 | 单个函数/模块 | 改通用工具后跑 |
| 集成测试 | 多个模块协作 | 改数据库/接口后跑 |
| API 测试 | HTTP 接口 | 升级框架/依赖后跑 |
| E2E 测试 | 端到端流程 | 大版本升级后跑 |

> 工作提示：维护者不需要精通测试框架。升级依赖后跑一遍 `npm test`，全绿再部署，是最稳妥的做法。

---

## 15. 调试与诊断：排查问题

![排查流程](https://cdn.jsdelivr.net/gh/langren34/doc@main/Node.js 入门到精通教程/nodejs-tutorial-images/07-troubleshooting.svg)
*图 8：Node.js 日常问题排查流程。先判断能否启动，再判断是性能问题还是逻辑问题，然后选择对应工具。*

### 15.1 常用排查命令

```bash
# 版本信息
node -v
npm -v

# 依赖状态
npm list
npm audit

# 查看脚本
npm run
```

### 15.2 console 调试

```javascript
console.log('value:', value);
console.error('error:', err);
console.table(users);
console.time('loop');
// ...
console.timeEnd('loop');
```

`[本机验证]`

### 15.3 使用 Chrome DevTools 调试

```bash
node --inspect app.js
```

然后在 Chrome 打开 `chrome://inspect` 连接 Node.js 进程。`[官方]`

### 15.4 性能分析

```bash
# 生成 CPU 火焰图
node --prof app.js
node --prof-process isolate-*.log > profile.txt

# 内存接近上限时生成堆快照
node --heapsnapshot-near-heap-limit=3 app.js
```

`[官方]`

### 15.5 工作中常见错误速查

| 现象 | 可能原因 | 排查方法 |
|------|----------|----------|
| 服务启动后无响应 | 阻塞了 Event Loop | 检查是否有大循环、同步计算 |
| 端口被占用 | 3000 端口已有进程 | `netstat -ano \| findstr :3000` |
| 模块找不到 | `node_modules` 缺失或路径错误 | `npm install`、检查 require 路径 |
| 依赖版本不兼容 | 版本范围太宽 | `npm list`、`package-lock.json` |
| 内存泄漏 | 全局缓存未清理 | Heap Snapshot 分析 |

---

## 16. 安全最佳实践：保护自己

### 16.1 依赖安全

- 用 `npm ci` 部署，强制遵循 lockfile `[官方]`
- 用 `npm audit` 检查已知漏洞 `[官方]`
- 用 `--ignore-scripts` 安装来源不明的包 `[官方]`
- 设置最小发布年龄：

```bash
npm config set min-release-age 1
```

`[官方]`

### 16.2 常见攻击与防护

| 攻击 | 防护措施 |
|------|----------|
| 原型污染 | 用 `Object.create(null)`、验证 JSON 输入、冻结原型 `[官方]` |
| 时序攻击 | 用 `crypto.timingSafeEqual` 比较秘密 `[官方]` |
| DoS | 配置超时、限制连接、使用反向代理 `[官方]` |
| 恶意第三方包 | 审查包内容、固定版本、lockfile、冷却期 `[官方]` |

### 16.3 安全代码示例

```javascript
const crypto = require('node:crypto');

const isEqual = crypto.timingSafeEqual(
  Buffer.from(userInput),
  Buffer.from(expectedSecret)
);
```

`[官方]`

---

## 17. 项目实战：部署与维护一个 Node.js 服务

> 本章目标：假设你拿到一个**别人开发好的 Node.js 项目**（比如一个 Express 后端服务），你需要把它**在本地跑起来、部署到服务器、日常维护、出问题能排查**。本章不讲代码怎么写，只讲怎么用。

### 17.1 拿到项目后，先看这三个文件

进入一个 Node.js 项目，第一件事不是改代码，而是读配置：`[本机验证]`

```bash
ls -la        # Linux/macOS
Get-ChildItem # Windows PowerShell
```

重点关注三个文件：

| 文件 | 看什么 |
|------|--------|
| `package.json` | `scripts` 里有哪些命令，`engines` 要求什么 Node 版本，`dependencies` 依赖量 |
| `.env.example` / `.env` | 需要哪些环境变量（端口、数据库地址、密钥等） |
| `README.md` | 项目作者写的启动说明 |

`[本机验证]` 以 `tmp/todo-api-enhanced` 项目为例，先看 `package.json`：

```bash
cat package.json
# Windows PowerShell:
Get-Content package.json
```

关键输出：

```json
{
  "scripts": {
    "start": "node src/app.js",
    "dev": "node --watch src/app.js",
    "test": "node --test tests/**/*.test.js",
    "lint": "eslint src tests"
  },
  "engines": {
    "node": ">=22.0.0"
  }
}
```

这说明：`[本机验证]`

- 启动命令是 `npm start` 或 `node src/app.js`
- 开发模式用 `npm run dev`（自动重载）
- 测试用 `npm test`
- 需要 Node.js 22 以上

### 17.2 检查环境并安装依赖

#### 17.2.1 确认 Node.js 版本

```bash
node -v
```

如果版本低于 `package.json` 里的 `engines.node` 要求，用 `fnm` / `nvm` 切换：`[官方]`

```bash
# fnm 示例
fnm install 22
fnm use 22
node -v
```

#### 17.2.2 安装依赖

开发环境第一次拉取项目：`[官方]`

```bash
npm install
```

生产环境部署（严格按 lockfile，保证一致性）：`[官方]`

```bash
npm ci
```

`[本机验证]` 在 `tmp/todo-api-enhanced` 项目中，两条命令均可正常执行。`npm ci` 会忽略 `package.json` 版本范围，严格安装 `package-lock.json` 中锁定的版本。

> 工作提示：如果项目包含原生模块（如 `better-sqlite3`），Windows 上可能需要 `npm approve-scripts <pkg>`。`[本机验证]`

### 17.3 配置环境变量并启动

#### 17.3.1 复制环境变量模板

```bash
# Linux/macOS
cp .env.example .env

# Windows PowerShell
Copy-Item .env.example .env
```

`[本机验证]` 然后按项目说明修改 `.env`，例如：

```text
PORT=3000
NODE_ENV=development
LOG_LEVEL=info
```

#### 17.3.2 查看可用脚本

```bash
npm run
```

`[本机验证]` 输出示例：

```text
Lifecycle scripts included in todo-api-enhanced@1.0.0:
  start
    node src/app.js
  test
    node --test tests/**/*.test.js

available via `npm run`:
  dev
    node --watch src/app.js
  lint
    eslint src tests
  lint:fix
    eslint src tests --fix
  format
    prettier --write src tests
```

#### 17.3.3 启动服务

开发模式（自动重载）：`[本机验证]`

```bash
npm run dev
```

生产模式：`[本机验证]`

```bash
npm start
```

正常启动后应看到类似日志：

```text
[2026-07-19 20:46:37 +0800] INFO: Database initialized
[2026-07-19 20:46:37 +0800] INFO: Server running at http://localhost:3000
```

#### 17.3.4 快速验证服务是否可用

```bash
# Linux/macOS
curl http://localhost:3000/health

# Windows PowerShell
Invoke-RestMethod -Uri http://localhost:3000/health
```

`[本机验证]` 返回：

```json
{ "status": "ok", "timestamp": "2026-07-19T12:46:37.560Z" }
```

### 17.4 运行测试

很多项目会把测试命令写在 `package.json` 的 `scripts.test` 里。使用前先跑一遍测试，确认项目基本功能正常：`[本机验证]`

```bash
npm test
```

预期输出：

```text
▶ Todo API
  ✔ GET /health returns ok
  ✔ POST /todos creates a todo
  ✔ GET /todos lists todos
  ✔ PUT /todos/:id updates a todo
  ✔ DELETE /todos/:id removes a todo
  ✔ POST /todos rejects empty title
✔ Todo API (65.9766ms)
ℹ tests 6
ℹ pass 6
ℹ fail 0
```

> 工作提示：测试失败时，先看最后几行的错误堆栈，通常是最具体的错误信息。

### 17.5 部署方式对比

| 部署方式 | 适用场景 | 优点 | 缺点 |
|----------|----------|------|------|
| 直接 `node app.js` | 本地开发、临时测试 | 最简单 | 进程崩溃不自动重启 |
| `node --watch` | 本地开发 | 改文件自动重启 | 不适合生产 |
| PM2 | 单机生产环境 | 进程守护、自动重启、日志聚合 | 需要单独安装 |
| Docker | 标准化部署、多环境一致 | 环境隔离、便于迁移 | 需要 Docker 基础 |
| Docker Compose | 单机多服务 | 配置简单、数据持久化 | 不适合大规模集群 |
| Kubernetes | 大规模集群 | 高可用、自动扩缩容 | 学习成本高 |
| Serverless | 低频/事件驱动 | 按需付费 | 有冷启动、生态绑定 |

`[官方]` / 工程经验

### 17.6 使用 PM2 部署（传统服务器）

PM2 是 Node.js 最常用的进程管理器，适合传统服务器部署。`[官方]`

#### 17.6.1 安装与启动

```bash
npm install -g pm2
pm2 start src/app.js --name todo-api
```

`[官方]` 命令语法，实际运行需根据环境安装 PM2。

#### 17.6.2 常用 PM2 命令

```bash
pm2 status              # 查看进程状态
pm2 logs todo-api       # 查看实时日志
pm2 logs todo-api --lines 50  # 查看最近 50 行
pm2 reload todo-api     # 零停机重启
pm2 restart todo-api    # 重启
pm2 stop todo-api       # 停止
pm2 delete todo-api     # 删除
pm2 monit               # 监控面板
```

`[官方]`

#### 17.6.3 设置开机自启

```bash
pm2 save        # 保存当前进程列表
pm2 startup     # 生成开机自启脚本，按提示执行
```

`[官方]`

#### 17.6.4 PM2 配置文件（可选）

复杂项目可以用 `ecosystem.config.js`：

```javascript
module.exports = {
  apps: [{
    name: 'todo-api',
    script: 'src/app.js',
    instances: 'max',        // 使用全部 CPU 核心
    exec_mode: 'cluster',    // 集群模式
    env: {
      NODE_ENV: 'production',
      PORT: 3000,
    },
    log_file: './logs/combined.log',
    error_file: './logs/error.log',
    out_file: './logs/out.log',
    max_memory_restart: '500M',
  }],
};
```

`[官方]` 启动方式改为：

```bash
pm2 start ecosystem.config.js
pm2 save
```

### 17.7 使用 Docker 部署

#### 17.7.1 关键 Dockerfile 解读

一个典型的生产 Dockerfile 长这样（不需要你写，但要能看懂）：`[本机验证]`（文件已实际存在）

```dockerfile
FROM node:22

WORKDIR /app

# 先复制依赖文件，利用缓存层
COPY package*.json ./
RUN npm ci --omit=dev

# 再复制源码
COPY src ./src
COPY .env.example ./.env.example

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://127.0.0.1:3000/health', (res) => { process.exit(res.statusCode === 200 ? 0 : 1) })"

CMD ["node", "src/app.js"]
```

`[本机验证]` 说明：

- `FROM node:22`：基础镜像
- `npm ci --omit=dev`：只安装生产依赖，保证镜像干净
- `HEALTHCHECK`：Docker 定期访问 `/health` 判断容器是否健康
- `CMD`：容器启动命令

#### 17.7.2 使用 Docker Compose 启动

`docker-compose.yml`：`[本机验证]`（文件已实际存在）

```yaml
services:
  todo-api:
    build: .
    container_name: todo-api
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - LOG_LEVEL=info
      - PORT=3000
      - DB_PATH=/data/todos.db
    volumes:
      - todo-data:/data
    restart: unless-stopped

volumes:
  todo-data:
```

启动命令：`[官方]`

```bash
docker compose up -d --build
```

常用运维命令：`[官方]`

```bash
docker compose ps           # 查看运行状态
docker compose logs -f      # 查看实时日志
docker compose down         # 停止并删除容器
docker compose down -v      # 停止并删除数据卷（慎用）
docker compose pull         # 拉取最新镜像
docker compose up -d --build # 重新构建并启动
```

> 工作提示：`volumes` 把数据库文件持久化到 `todo-data` 卷里，否则 `docker compose down` 会丢失数据。

### 17.8 日志查看与监控

#### 17.8.1 实时日志

```bash
# PM2
pm2 logs todo-api

# Docker Compose
docker compose logs -f
```

#### 17.8.2 日志级别调整

通过环境变量 `LOG_LEVEL` 控制日志详细程度：`[本机验证]`

```text
LOG_LEVEL=debug   # 最详细，排查问题用
LOG_LEVEL=info    # 正常运行
LOG_LEVEL=warn    # 只显示警告和错误
LOG_LEVEL=error   # 只显示错误
```

#### 17.8.3 监控指标

| 监控项 | 命令/工具 | 正常范围 |
|--------|----------|----------|
| CPU | `pm2 monit` / 系统监控 | 持续 < 80% |
| 内存 | `pm2 monit` / `docker stats` | 低于 `max_memory_restart` |
| 磁盘 | `df -h` / `Get-Volume` | 日志文件不过大 |
| 服务可用性 | 定时请求 `/health` | 返回 200 |
| 错误率 | 日志中 ERROR 数量 | 无突增 |

### 17.9 升级依赖与热更新

#### 17.9.1 安全升级流程

```bash
# 1. 查看有哪些包有漏洞
npm audit

# 2. 查看可更新版本
npm outdated

# 3. 升级指定包（推荐先更新 patch/minor，major 需确认 breaking change）
npm update express

# 4. 跑测试
npm test

# 5. 提交 lockfile
npm ci  # 验证 lockfile 是否一致
```

`[官方]` `[本机验证]`

> 工作提示：升级后务必跑测试，并查看 CHANGELOG。`npm update` 不会跨 major 版本，需要手动改 `package.json`。

#### 17.9.2 热更新部署

| 场景 | 操作 |
|------|------|
| PM2 | `pm2 reload todo-api`（零停机） |
| Docker Compose | `docker compose up -d --build`（会重建容器，有短暂中断） |
| 需要零停机 Docker | 用蓝绿部署或滚动更新，Docker Compose 本身不支持 |

### 17.10 常见问题排查

| 现象 | 可能原因 | 排查命令 |
|------|----------|----------|
| 启动报错 `Cannot find module` | `node_modules` 缺失 | `npm install` 或 `npm ci` |
| 端口被占用 | 3000 端口已有进程 | `netstat -ano \| findstr :3000` |
| 数据库连不上 | `DB_PATH` 或连接串错误 | 检查 `.env` |
| 请求返回 404 | 路由配错或前缀不对 | 看 `app.js` 或框架路由配置 |
| 请求返回 500 | 代码异常 | 看日志堆栈 |
| 请求返回 400 | 参数校验失败 | 检查请求体格式 |
| 服务占用内存越来越高 | 内存泄漏 | 生成 Heap Snapshot 分析 |
| CPU 突然飙高 | 阻塞 Event Loop 或死循环 | 用 `--prof` 生成火焰图 |
| 日志不输出 | `LOG_LEVEL` 太高 | 检查 `.env` 中的 `LOG_LEVEL` |

### 17.11 生产部署检查清单

部署到生产前逐项确认：`[官方]` / 工程经验

- [ ] 服务器 Node.js 版本满足 `package.json` 的 `engines` 要求
- [ ] 使用 `npm ci` 安装依赖（不是 `npm install`）
- [ ] 环境变量已配置（PORT、数据库、密钥、LOG_LEVEL 等）
- [ ] `.env` 未提交到 Git，`.env.example` 已提交
- [ ] 日志目录有写权限，且配置了日志轮转
- [ ] 配置了反向代理（Nginx/Caddy）和 HTTPS
- [ ] 配置了进程守护（PM2 / systemd / Docker）
- [ ] 配置了健康检查（请求 `/health`）
- [ ] 数据库或持久化数据有备份策略
- [ ] 运行了 `npm audit` 并处理高危漏洞
- [ ] 测试已通过

### 17.12 本章小结

作为 Node.js 的**使用者/维护者**，你不需要会写每个 API，但需要会：

1. **读配置**：`package.json`、`.env`、`README.md`
2. **起服务**：`npm install` → `npm run` → 验证 `/health`
3. **会部署**：PM2 / Docker / Docker Compose 三选一
4. **看日志**：用日志定位问题，而不是猜
5. **懂升级**：`npm audit` → `npm update` → 跑测试 → 热更新
6. **能排查**：从现象到命令，按表逐项定位

> 下一章是附录，可以先收藏「附录 A：日常检查清单」和「附录 B：命令速查表」，工作中遇到问题时翻查。

---

## 18. 附录 A：日常检查清单

### 18.1 接手一个 Node.js 项目时

- [ ] 运行 `node -v` 和 `npm -v` 确认版本
- [ ] 查看 `package.json` 的 `engines` 字段（如果有）
- [ ] 运行 `npm install` 或 `npm ci`
- [ ] 查看 `README.md` 中的启动命令
- [ ] 运行 `npm run` 查看所有可用脚本
- [ ] 启动开发服务器：`npm run dev` 或 `node --watch app.js`
- [ ] 运行测试：`npm test`

### 18.2 提交代码前

- [ ] 代码能正常启动
- [ ] 测试通过
- [ ] `npm audit` 没有高危漏洞
- [ ] `package-lock.json` 已提交

### 18.3 生产部署前

- [ ] 使用 `npm ci` 安装依赖
- [ ] 配置环境变量（端口、数据库、密钥等）
- [ ] 设置进程管理器（PM2/systemd）
- [ ] 配置反向代理（Nginx/Caddy）
- [ ] 开启日志收集
- [ ] 配置监控告警

### 18.4 遇到问题时

- [ ] 先看报错堆栈（最下面的错误信息最具体）
- [ ] 检查 `node_modules` 是否完整
- [ ] 检查环境变量是否设置
- [ ] 检查端口是否被占用
- [ ] 用 `node --inspect` 调试
- [ ] 查看日志

---

## 19. 附录 B：命令速查表

### 19.1 Node.js 命令

| 命令 | 说明 | 使用频率 |
|------|------|----------|
| `node -v` | 查看版本 | 高 |
| `node app.js` | 运行脚本 | 高 |
| `node --watch app.js` | 开发模式自动重启 | 高 |
| `node -e "script"` | 执行单行脚本 | 中 |
| `node --run <script>` | 运行 package.json 脚本 | 中 |
| `node --test` | 运行内置测试 | 中 |
| `node --inspect app.js` | 启用调试 | 中 |
| `node app.ts` | 原生运行 TypeScript（v22.18.0+） | 中 |

### 19.2 npm 命令

| 命令 | 说明 | 使用频率 |
|------|------|----------|
| `npm init -y` | 初始化项目 | 高 |
| `npm install` | 安装依赖 | 高 |
| `npm install <pkg>` | 安装生产依赖 | 高 |
| `npm install -D <pkg>` | 安装开发依赖 | 高 |
| `npm uninstall <pkg>` | 卸载依赖 | 高 |
| `npm run <script>` | 运行脚本 | 高 |
| `npm ci` | 生产部署安装 | 高 |
| `npm audit` | 安全检查 | 中 |
| `npm list` | 查看依赖树 | 中 |
| `npm outdated` | 查看可更新包 | 中 |
| `npm publish --dry-run` | 预览发布内容 | 低 |

### 19.3 常用模块速查

| 模块 | 用途 | 示例场景 |
|------|------|----------|
| `node:fs/promises` | 文件读写 | 读取配置、写日志 |
| `node:path` | 路径处理 | 拼接跨平台路径 |
| `node:http` | 原生 HTTP | 学习/轻量服务 |
| `node:events` | 事件驱动 | 自定义事件 |
| `node:stream` | 流处理 | 大文件、网络数据 |
| `node:child_process` | 子进程 | 调用外部命令 |
| `node:worker_threads` | 工作线程 | CPU 密集型任务 |
| `node:cluster` | 多核集群 | 扩展服务器 |
| `node:crypto` | 加密哈希 | 密码哈希、签名 |
| `node:process` | 进程信息 | 环境变量、参数 |

---

## 20. 附录 C：验证报告

### 20.1 验证环境

| 项目 | 值 |
|------|-----|
| 操作系统 | Windows_NT 10.0.26200 |
| Node.js 版本 | v24.18.0 `[本机验证]` |
| npm 版本 | 11.16.0 `[本机验证]` |
| Shell | PowerShell |
| 验证时间 | 2026-07-19 |

### 20.2 验证原则

按 MEMORY.md 技术文档铁律：每条写入文档的事实必须标注来源。本附录记录所有 `[本机验证]` 命令的实际运行结果。

### 20.3 命令验证清单

| 序号 | 命令/代码 | 预期结果 | 实际结果 | 状态 |
|------|-----------|----------|----------|------|
| 1 | `node -v` | 显示版本 | `v24.18.0` | ✅ |
| 2 | `npm -v` | 显示版本 | `11.16.0` | ✅ |
| 3 | `node hello.js` | 输出 Hello | `Hello, Node.js!` | ✅ |
| 4 | `node -e "console.log(1+1)"` | 输出 2 | `2` | ✅ |
| 5 | `node --watch app.js` | 启动监听 | 正常启动 | ✅ |
| 6 | `node --run start` | 运行脚本 | 正常执行 | ✅ |
| 7 | `npm init -y` | 生成 package.json | 生成成功 | ✅ |
| 8 | `npm install express` | 安装 express | 安装成功 | ✅ |
| 9 | `npm install -D nodemon` | 安装 dev 依赖 | 安装成功 | ✅ |
| 10 | `npm uninstall express` | 卸载依赖 | 卸载成功 | ✅ |
| 11 | `npm config get registry` | 显示 registry | 正常输出 | ✅ |
| 12 | `npm ci` | 按 lockfile 安装 | 正常执行 | ✅ |
| 13 | CommonJS require 模块 | 正确导入导出 | `5 3` | ✅ |
| 14 | ESM import/export | 正确导入导出 | `5 3` | ✅ |
| 15 | `fs.readFile` / `fs.writeFile` / `fs.stat` | 文件读写正常 | 运行成功 | ✅ |
| 16 | `path.join` / `path.resolve` | 路径拼接正确 | 运行成功 | ✅ |
| 17 | `fs.createReadStream` | 流式读取 | 运行成功 | ✅ |
| 18 | `http.createServer` | 启动 HTTP 服务器 | 运行成功 | ✅ |
| 19 | `http` 读取请求体 | 正确拼接 Buffer | 运行成功 | ✅ |
| 20 | `http` 返回 JSON | 返回正确 JSON | 运行成功 | ✅ |
| 21 | `Promise` / `async/await` | 异步执行正常 | 运行成功 | ✅ |
| 22 | `Promise.all` | 等待所有 Promise | `['A', 'B']` | ✅ |
| 23 | 顶层 `await` | 模块顶层可用 | 运行成功 | ✅ |
| 24 | `setTimeout(0)` vs `setImmediate` 在 I/O 中 | immediate 先输出 | `immediate` 先于 `timeout` | ✅ |
| 25 | `process.nextTick` | 当前操作后执行 | `1 3 2` | ✅ |
| 26 | `EventEmitter` | 事件触发与监听 | 运行成功 | ✅ |
| 27 | Todo API 完整 CRUD | 增删改查正常 | curl 测试通过 | ✅ |
| 28 | 查看 `package.json` 的 `scripts` 和 `engines` | 了解启动命令和版本要求 | 输出 `start`/`dev`/`test` 脚本及 `node >=22` | ✅ |
| 29 | `npm install` | 安装项目依赖 | 安装成功 | ✅ |
| 30 | `npm ci` | 严格按 lockfile 安装 | 安装成功 | ✅ |
| 31 | `cp .env.example .env` / `Copy-Item` | 复制环境变量模板 | 文件复制成功 | ✅ |
| 32 | `npm run` | 查看可用脚本 | 列出 `start`/`dev`/`test`/`lint` | ✅ |
| 33 | `npm start` | 生产模式启动 | 服务器正常监听 | ✅ |
| 34 | `npm run dev` | 开发模式启动 | 自动重载运行 | ✅ |
| 35 | `npm test` | 运行项目测试 | 6 通过 0 失败 | ✅ |
| 36 | `curl http://localhost:3000/health` | 验证服务可用 | 返回 `{status:ok}` | ✅ |
| 37 | `npm audit` | 检查依赖漏洞 | 正常输出 | ✅ |
| 38 | `npm outdated` | 查看可更新依赖 | 正常输出 | ✅ |
| 39 | `Dockerfile` / `docker-compose.yml` | 部署文件存在 | 文件已创建 | ✅ |
| 40 | `npm run lint` | 代码规范检查 | 通过 | ✅ |

### 20.4 验证脚本说明

所有 `[本机验证]` 标记的代码均在本机 PowerShell 中实际执行。原教程验证脚本为 `tmp/validate-tutorial.js`，日志为 `tmp/nodejs-tutorial-validation.log`；第17章增强版项目验证在 `tmp/todo-api-enhanced/` 目录下完成，并运行了 `npm run lint`、`npm test` 等命令。

### 20.5 免责声明

- 本教程基于 **Node.js v24.18.0** 验证。低版本可能不支持某些 API（如原生 TypeScript 运行、`node --run` 等）。
- 部分命令（如 `curl`、`ffmpeg`）需要系统单独安装。
- 生产部署请参考官方安全最佳实践。

---

**教程完**。建议按章节顺序动手实践，每学完一章尝试修改示例代码并观察结果。遇到问题时，先查「附录 A：日常检查清单」和「附录 B：命令速查表」。
