# GitLab 入门到精通教程

> **定位**：实战运维 / 使用者层级。从第一次见到 GitLab，到能独立部署、配置、跑 CI/CD、做基础安全扫描、做日常运维。
>
> **来源**：GitLab 官方文档 ([docs.gitlab.com](https://docs.gitlab.com/)) v19.2，抓取时间 2026-07-04。每条事实都打 `[官方]` / `[本机验证]` / `[本机未验证]` 标签。
>
> **本机环境**：Windows 11 / Docker 29.6.1 / git 2.53.0 / kubectl 1.36.1。
>
> **不在范围**：源码、Geo 多区域复制、自定义认证后端、Operator 高级用法、Duo 模型微调（这些是"精通开发者"层级，超出实操教程）。

## 目录

> 一级是顶级章节位置，二级是该章节会讲的主题缩进展示，快速扫读用。
>
> 📖 **本目录的链接指向合并文件内的 anchor**（不是 `chapters/XX.md` 文件路径），方便在单文件版本里点跳。

- [00 · 写在前面](#ch00)
  - 关于“入门到精通”
  - 来源标签约定
  - 本教程基于的 GitLab 版本
  - 阅读建议
- [01 · 工具介绍：GitLab 是什么](#ch01)
  - 1.1 一句话定义
  - 1.2 产品矩阵（按部署形态）
  - 1.3 订阅层级
  - 1.4 三大自建部署形态（[官方] /install/）
  - 1.5 与同类工具对比
  - 1.6 谁应该用 GitLab
  - 1.7 一个 GitLab 能给你什么
- [02 · 架构与组件](#ch02)
  - 2.1 GitLab 服务端不是单一进程
  - 2.2 三种部署形态怎么选
  - 2.3 端口规划
  - 2.4 存储规划（[官方] /install/requirements/）
  - 2.5 与 CI Runner 的关系（[官方] /runner/install/）
- [03 · 部署（简化版）](#ch03)
  - 3.1 前置清单（5 行）
  - 3.2 路径 A · Docker（推荐，5 分钟起）
  - 3.3 路径 B · Linux Omnibus（单机 VM 生产）
    - 3.3.1 装完到哪里去看初始 root 密码
  - 3.4 部署后必做（清单）
  - 3.5 不在本章范围（其他部署）
- [04 · 初始配置](#ch04)
  - 4.1 配置文件结构（Omnibus）
  - 4.2 用户、组、角色（核心概念）
  - 4.3 配置 SMTP 发邮件（含 QQ 邮箱踩坑）
  - 4.4 配置 HTTPS / SSL
  - 4.5 注册策略（生产必改）
  - 4.6 配置 Container Registry
  - 4.7 配置 Pages（静态网站托管）
  - 4.8 关键参数确认（重新配置后）
- [05 · 日常操作](#ch05)
  - 5.0 5 分钟快速上手（[本机验证]）
  - 5.1 项目（Project）
  - 5.2 分支（Branch）与 Merge Request
  - 5.3 Issue（[官方] /user/project/issues/）
  - 5.4 规划工作（Planning，[官方] /user/get_started/get_started_planning_work/）
  - 5.5 管理代码（[官方] /user/get_started/get_started_managing_code/）
  - 5.6 Wiki
  - 5.7 Snippet（代码片段共享）
  - 5.8 Release（[官方] /user/project/releases/）
  - 5.9 Pages（静态站点，[官方] /user/project/pages/）
  - 5.10 容器 Registry + Package Registry（[官方] /user/packages/container_registry/）
  - 5.11 命令行工具：glab（[官方]）
- [06 · CI/CD](#ch06)
  - 6.1 核心概念
  - 6.2 第一个 Pipeline（[官方] /ci/quick_start/）
  - 6.3 YAML 关键字速查（[官方] /ci/yaml/）
  - 6.4 预定义变量（[官方] /ci/variables/predefined_variables/）
  - 6.5 GitLab Runner（[官方] /runner/install/）
  - 6.6 制品（Artifacts，[官方] /ci/yaml/#artifacts）
  - 6.7 缓存（Cache，[官方] /ci/yaml/#cache）
  - 6.8 变量与机密（[官方] /ci/variables/）
  - 6.9 多项目 Pipeline（[官方] /ci/pipelines/downstream_pipelines/）
  - 6.10 父子 Pipeline 复用（[官方] /ci/pipelines/parent_child_pipelines/）
  - 6.11 调度 Pipeline（Scheduled pipeline）
  - 6.12 Container Registry 与 CI 集成
- [07 · 安全扫描（Application Security Testing）](#ch07)
  - 7.1 订阅层级对照（[官方]）
  - 7.2 安全扫描工作流（[官方] /user/application_security/）
  - 7.3 开启安全扫描（最简方法，[官方]）
  - 7.4 各扫描详解
  - 7.5 在 MR 里看扫描结果
  - 7.6 Vulnerability Report
  - 7.7 安全策略（Policies，Premium+，[官方] /user/application_security/policies/）
  - 7.8 合规框架（Compliance Frameworks，Ultimate，[官方] /user/group/compliance_frameworks/）
  - 7.9 离线 / 私有部署的安全扫描
  - 7.10 实战：把安全扫描加进现有 pipeline
  - 7.11 收尾：风险降级与例外
- [08 · 运维：备份、升级、监控、故障排查](#ch08)
  - 8.1 备份（[官方] /omnibus/settings/backups/）
  - 8.2 升级
  - 8.3 监控（[官方] /administration/monitoring/）
  - 8.4 健康检查
  - 8.5 故障排查（[官方] /administration/troubleshooting/）
  - 8.6 安全维护
  - 8.7 升级前 checklist（铁律）
  - 8.8 容量规划速查
- [99 · 附录](#ch99)
  - A · 硬件要求速查
  - B · 命令速查
  - C · 关键概念术语表
  - D · 来源 + 验证报告

## 阅读路径

- **第一次看**：00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08
- **要部署**：重点看 02、03、04、08
- **要做 CI/CD**：重点看 06
- **跑安全扫描**：重点看 07
- **上线后出问题**：直接翻 08.5

## 版本信息

- **教程版本**：2.1（2026-07-05）
- **基于 GitLab**：v19.2（docs.gitlab.com 默认显示）
- **编辑工具**：openclaw-doc-scraper + 人工整理

---


---

# 00 · 写在前面 {#ch00}

> 本教程来源：**GitLab 官方文档** ([docs.gitlab.com](https://docs.gitlab.com/)) v19.2，本机实测环境为 Windows 11 / Docker 29.6.1 / git 2.53.0 / kubectl 1.36.1。

## 关于"入门到精通"

完整的 GitLab 教程如果写到"精通开发者"层（源码、Go 内部、Geo 多区域、自定义认证后端），是**几百页**的体量。本教程定位是**实战运维/使用者**层级：从第一次见到 GitLab，到能独立部署、配置、跑 CI/CD、做基础安全扫描、做日常运维。

**不在本教程范围**：
- GitLab 源码 / Rails 应用 / Go worker 二次开发
- Geo 多区域复制（跨国灾备）
- 自定义认证后端开发（如私有 OIDC provider）
- GitLab Operator 高级用法
- GitLab Duo 模型微调

需要这些内容请直接看 [docs.gitlab.com](https://docs.gitlab.com/) 的对应专章。

## 来源标签约定

每一条事实都打标签，便于读者判断可信度：

| 标签 | 含义 |
|------|------|
| `[官方]` | 直接引用 GitLab 官方文档原文，2026-07-04 抓取 |
| `[本机验证]` | 在本机环境（Windows 11 / Docker 29.6.1）实测过 |
| `[本机未验证]` | 在用户机器未跑过，仅基于官方文档引用 |
| `[推测]` | ❌ **不应出现**——一旦在终稿看到，立即删 |

## 本教程基于的 GitLab 版本

- **官方文档版本**：GitLab Docs **v19.2**（[官方]，2026-07-04 抓取，docs.gitlab.com 默认显示）
- **安装方式**：Linux Omnibus / Docker / Helm chart 三种主流自管方式
- **操作系统侧重**：Linux（最常见）。Windows 上 GitLab Runner 可装（[官方] /runner/install/windows/），但 GitLab 服务本身官方不推荐装 Windows 上（[官方] /install/requirements/）

## 阅读建议

- **第一次看**：按顺序读 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08
- **要部署**：重点看 02、03、04、08
- **要做 CI/CD**：重点看 06
- **跑安全扫描**：重点看 07
- **上线后出问题**：直接翻 08.5

---

# 01 · 工具介绍：GitLab 是什么 {#ch01}

## 1.1 一句话定义

**GitLab 是一个端到端的 DevSecOps 平台**（[官方] /user/get_started/）——把"软件从想法到上线运维"全流程装在一个工具里：源代码托管、Issue/MR 协作、CI/CD 流水线、容器/制品库、安全扫描、监控告警、IaC、API。

## 1.2 产品矩阵（按部署形态）

| 形态 | 适合谁 | 维护方 |
|------|--------|--------|
| **GitLab.com**（SaaS） | 个人 / 小团队 / 不想运维的人 | GitLab Inc. |
| **GitLab Self-Managed** | 企业内自建 | 你/你的团队 |
| **GitLab Dedicated** | 想要 SaaS 体验但要单租户隔离 | GitLab Inc. 运维，你独占实例 |
| **GitLab.com for Enterprise** | 大企业 GitLab.com 套餐 | GitLab Inc. |

> `[官方]` <https://docs.gitlab.com/subscriptions/>（订阅页）

## 1.3 订阅层级

| 层级 | 价格 | 关键差异 |
|------|------|---------|
| **Free** | 免费 | 核心功能 + 5 GB 存储 + 400 CI 分钟/月 |
| **Premium** | 商用付费 | + 多级审批 + 审计事件 + 50 GB 存储 |
| **Ultimate** | 高价 | + SAST/DAST/容器扫描完整套 + 合规框架 + 多因素强制 |
| **开源 / 教育 / 创业** | 免费 | 通过申请 [GitLab for Open Source](https://about.gitlab.com/solutions/open-source/) 等计划 |

> `[官方]` 三层级差异见 <https://about.gitlab.com/pricing/> 和 `/subscriptions/#gitlab-com-tier-comparison`

## 1.4 三大自管部署形态（[官方] /install/）

| 形态 | 简介 | 适合 |
|------|------|------|
| **Linux Omnibus** | 单 deb/rpm 包把 GitLab 全部组件装在一台/多台机器 | 传统运维 / 小到中型 / 不想折腾 K8s |
| **Docker 镜像** | 单容器或 `docker-compose` 跑 | 测试 / 小团队 / 已有 Docker 平台 |
| **Helm chart** | Kubernetes 原生，云原生可扩展 | 中到大型 / 已有 K8s / 需要弹性伸缩 |
| **GitLab Operator** | OpenShift 上的 Operator 模式 | OpenShift 用户 |

> **重要提示**（[官方] /charts/）：Helm chart **要求外部 PostgreSQL、外部 Redis、外部对象存储**（S3/MinIO/GCS/Azure Blob）——不是单 helm install 就能用的，要先备好这三件。

## 1.5 与同类工具对比

| 维度 | GitLab | GitHub | Gitea/Forgejo |
|------|--------|--------|---------------|
| 定位 | 一体化 DevSecOps | 代码托管 + Actions 生态 | 轻量自托管 Git |
| CI/CD | 内置（极强） | Actions（生态强） | 内置（够用） |
| 自托管难度 | 中（Omnibus）~ 难（Helm） | 中（Enterprise Server） | 极简 |
| 安全扫描 | Ultimate 自带完整 | 依赖第三方（CodeQL） | 无 |
| 制品库 | 内置（Container / Package / Generic） | Container only | 极简 |
| 适合规模 | 5 ~ 5000+ 人 | 任意 | 个人 / 小团队 |

## 1.6 谁应该用 GitLab

✅ **适合**：
- 想**少拼工具**——不想同时管 Jenkins + GitHub + Snyk + ArgoCD + Harbor
- 有**自托管 / 私有化部署**合规需求
- 大企业里 Dev / Ops / Security 三个团队要拉通
- 需要内置安全扫描（Ultimate）

❌ **不太适合**：
- 只想托管 Git 仓库 + 简单 CI → GitHub 更轻
- 个人项目 / 学习 → GitHub + Vercel 更快
- 团队 < 5 人 → Gitea 也够用，省资源

## 1.7 一次 GitLab 能给你什么

按 DevOps 生命周期对齐（[官方] /user/get_started/）：

| 生命周期阶段 | GitLab 能力 |
|------------|------------|
| **Manage**（组织） | 用户/组/子组/SSO |
| **Plan**（规划） | Epics、Issues、Iterations、OKRs、Roadmaps |
| **Create**（创建） | Git、Web IDE、Merge Requests、Code Owners |
| **Verify**（验证） | CI/CD pipelines、Runner、merge trains |
| **Package**（打包） | Container Registry、Package Registry（Maven/NPM/PyPI/Conan/NuGet）、Generic |
| **Secure**（安全） | SAST、DAST、Dependency Scanning、Container Scanning、Secret Detection、License Compliance |
| **Release**（发布） | Environments、Releases、Feature Flags、Pages、Review Apps |
| **Configure**（配置） | Terraform 集成、Kubernetes Agent |
| **Monitor**（监控） | Incident Management、Error Tracking、Tracing、Logs |
| **Govern**（治理） | Audit Events、Compliance Frameworks、Value Stream Analytics |

> 这张表的内容基于本教程抓取的 `/user/get_started/` 12 张卡片汇总（[官方]，详见 docs/gitlab-get-started/raw/）。

---

# 02 · 架构与组件 {#ch02}

## 2.1 GitLab 服务端不是单一进程

GitLab 由多个组件协作（[官方] /install/requirements/ + /architecture/architecture/），下面按角色分 3 类：

**核心进程**（Docker/Omnibus 默认全部启用）

| 组件 | 干啥 | 默认端口 |
|------|------|---------|
| **NGINX** | 反向代理 + HTTPS 终结 | 80 / 443 |
| **Puma** | Rails HTTP server，Web UI 和 API | 内网 |
| **Sidekiq** | 异步任务队列（邮件、合并、webhook 等） | 内网 worker |
| **Gitaly** | Git RPC 服务，封装所有 git 操作 | 8075（内网）/ 22（SSH） |
| **PostgreSQL** | 主数据库（用户/项目/MR/CI 元数据） | 5432 |
| **Redis** | Sidekiq 队列 + 缓存 + 实时特性 | 6379 |
| **Workhorse** | Git Smart HTTP + 附件上传代理 | 8181（内网） |

**可选进程**（按需启用）

| 组件 | 干啥 | 默认端口 |
|------|------|---------|
| **Container Registry** | Docker / OCI 镜像仓库 | 5000 |
| **Pages daemon** | 静态站点托管（GitLab Pages） | 8090 |
| **Mailroom** | 入站邮件 → MR/Issue 评论 | 内网 |
| **Prometheus + Grafana** | 自监控 | 9090 / 3000 |

**用户视角**：平时只用 Web UI（80/443）+ git 推拉（80/443 或 22）两个入口，其他全是内网，不需要你管。

## 2.2 三种部署形态怎么选

GitLab 服务端的 3 种官方打包方式（[官方] /install/）：

| 形态 | 怎么装 | 你要管什么 | 适合谁 |
|------|--------|-----------|--------|
| **Omnibus** | deb/rpm 包，5 分钟装好 | 1 台 Linux 机器 | 单机 VM 生产 |
| **Docker** | `docker run gitlab/gitlab-ce` | 1 个容器 | 本机试用 / 小团队 |
| **Helm chart** | `helm install` 到 K8s | K8s 集群 + 外部 Postgres/Redis/对象存储 | 已上 K8s / 大规模 |

**粗选原则**：
- **个人 / ≤ 50 人** → Docker（§3.2 路径 A，本教程主推）
- **50 ~ 500 人 / 自管服务器** → Omnibus（§3.3 路径 B，单机 VM）
- **> 500 人 / 已上 K8s** → Helm（本教程**不展开**；用 [官方 Charts 文档](https://docs.gitlab.com/charts/)）

> 💡 **三种形态打包的不一样，但装出来的软件是一套东西**——组件、配置（`gitlab.rb`）、命令（`gitlab-rails`、`gitlab-rake`、`gitlab-ctl`）核心能力**都通用**。

## 2.3 端口规划

自管 GitLab 需要在防火墙开的端口（[官方] /install/requirements/）：

| 端口 | 服务 | 对外？ |
|------|------|--------|
| 80, 443 | Web UI + HTTPS | ✅ 必须对外开放 |
| 22 | SSH 拉取代码 | ✅ 必须对外开放（或用 22 + 端口转发） |
| 5000 | Container Registry | ⚠️ 推荐开；不用可以关 |
| 8090 | GitLab Pages | 可选 |
| 5432 / 6379 / 8075 | PostgreSQL / Redis / Gitaly | ❌ **必须只监听内网或 unix socket** |

**重点**（[官方]）：
- 5432（Postgres）、6379（Redis）、8075（Gitaly）**绝对不能暴露公网**——会被人一把梭
- 这三个改用 `127.0.0.1` 绑定 + 本机 unix socket 通信，是默认且安全配置（Docker 容器内已经是这样）
- 5099/3000（Prometheus/Grafana）也是内网

## 2.4 存储规划

| 存什么 | 大小 | 说明 |
|--------|------|------|
| **应用 + 日志** | **≥ 40 GB**（[官方]） | 包本身 ~2.5 GB，要预留 OS + 日志增长 |
| **仓库（Gitaly）** | ≥ 仓库总大小 | Git 裸数据，I/O 最密集——**必须 SSD**（[官方] 原文 "particularly important for Gitaly"） |
| **数据库** | 10 ~ 12 GB 起 | 10 GB 起跳，Ultimate 订阅要 ≥ 12 GB |

**3 个不要做**（[官方]）：
1. ❌ 不要用 NFS / EFS / Azure Files 类网络文件系统放仓库
2. ❌ 不要用 burstable CPU 云主机类型（突发性能类）
3. ❌ 不要开 swap（或保证内存在 swap 触发前足够）

> 📈 **要 HA / 拿不准规模选哪个架构** → 看 [官方] /administration/reference_architectures/ 选 1k/2k/3k/5k/10k/25k/50k 参考架构；本教程不展开。

## 2.5 与 CI Runner 的关系

**GitLab 服务**（服务端）≠ **GitLab Runner**（CI 任务执行端），两回事：

| | GitLab Server | GitLab Runner |
|--|--------------|---------------|
| 是啥 | 服务端（Web UI/API） | 跑 CI job 的 agent 进程 |
| 装在哪 | 中央服务器 | 可独立机器 / 容器 / K8s |
| 通信 | — | 通过 token 注册 + pull job（无入站要求） |
| 自管默认有? | ✅ 必有 | ❌ **不自带，自己装** |
| GitLab.com 用户 | ✅ 自带 | ✅ 自带（每月 400 CI 分钟免费） |

**3 个 scope**（哪个层级注册，能跑哪些项目的 job）：

| Scope | 能跑哪个层级的 job |
|-------|-----------------|
| **Instance runner** | 整个实例所有项目 |
| **Group runner** | 组内所有项目 |
| **Project runner**（Specific）| 单个项目 |

注册 token 路径（[官方] /runner/register/）：
- Instance → Admin → CI/CD → Runners
- Group → Group Settings → CI/CD → Runners
- Project → Project Settings → CI/CD → Runners

详细安装见 §6.5。


---

# 03 · 部署（简化版） {#ch03}

> **本章只讲最常用的 1 条路径**：Docker（5 分钟起，测试和小团队首选）—— 含本机 [本机验证] 步骤。
>
> 其他部署（Linux Omnibus / Helm / Operator）在本章末尾简单提及，详细看 [官方] /install/。

## 3.1 前置清单

| 项 | 要求 |
|----|------|
| **CPU** | 2 核起步，4 核推荐（[官方] 最低 4 vCPU） |
| **内存** | **≥ 4 GB**（[官方] 最低 8 GB；本机 Docker 配额 12.6 GB，实测 GitLab 起来吃 ~9.7 GB）[本机验证] |
| **磁盘** | 10 GB 起步，**SSD 强烈推荐** |
| **端口** | 80 (HTTP) / 443 (HTTPS，可选) / 22 (SSH) |
| **域名** | 生产必须有可解析域名；测试可用 `localhost` 或内网 IP |

> ⚠️ **Windows + Docker Desktop** —— [官方] 不支持，但 [本机验证] 可正常跑。Docker Desktop 默认配额 12.6 GB，GitLab 起来后留给其他容器不多。

## 3.2 路径 A · Docker

### 3.2.1 拉镜像 + 启动（一行搞定）[本机验证]

```bash
# 1. 拉镜像（[本机验证] disk usage ~5.13 GB），固定 tag，不要用 latest
docker pull gitlab/gitlab-ce:19.1.1-ce.0

# 2. 启动（首次 3-5 分钟才 healthy）
docker run -d \
  --name gitlab-ce \
  --hostname gitlab.local \
  -p 80:80 -p 443:443 -p 22:22 \
  --restart unless-stopped \
  --shm-size 256m \
  gitlab/gitlab-ce:19.1.1-ce.0
```

**参数说明**：
- `--shm-size 256m` **必须**——PostgreSQL 在进程大时需要
- `-p 80:80` 走 HTTP，[本机验证] HTTPS (443) **默认没人监听**（坑 #1，见下）
- `-p 22:22` 是容器内 GitLab 内置 SSH；主机端口空闲时直连

### 3.2.2 等启动 + 验证（首次 3-5 分钟）[本机验证]

```bash
# 1. 等 healthy
docker ps --filter "name=gitlab-ce" --format "{{.Status}}"
# 输出从 "Up X seconds (health: starting)" → "(healthy)" 即就绪，约 4 分钟

# 2. 看具体组件（15 个，全部 run: 即完整）
docker exec gitlab-ce gitlab-ctl status

# 3. Web 可访问
curl -I http://localhost/users/sign_in
# 期望: HTTP/1.1 200 OK
```

### 3.2.3 初始 root 密码（必读）[本机验证]

GitLab 容器**首次启动后 24 小时内**会在容器内文件 `/etc/gitlab/initial_root_password` 自动生成一个随机 root 密码。

```bash
docker exec gitlab-ce cat /etc/gitlab/initial_root_password
```

输出形如：
```
# WARNING: This password is only valid if ALL of the following are true:
#          ...

Password: D/krzWJVKX2B5Aba25jKHQyCT8YMypkO29G4bCsIK8o=
```

复制 `Password:` 后面那串（**不要带前面的 `#` 注释**）到登录页。

> 💡 **Windows 提示**：PowerShell / Windows Terminal 下 `docker exec ... cat ...` 通常没问题；如果用 **Git Bash** 且出现 `the input device is not a TTY` 错误，加 `winpty` 前缀：`winpty docker exec gitlab-ce cat /etc/gitlab/initial_root_password`

**4 件必知**（[官方] /security/reset_user_password/）：
1. ⚠️ **24 小时后下次 `reconfigure` 时自动删**——文件末行原文 `NOTE: This file is automatically deleted after 24 hours on the next reconfigure run.` 不是到点就删
2. ⚠️ **首次登录后立即改密**（Web UI → 头像 → Edit profile → Access → Password and authentication → Change password）
3. 💡 **文件被删后怎么救**（生产最低 12 字符）：
   ```bash
   docker exec -it gitlab-ce gitlab-rails runner \
     "u=User.find_by_username('root'); u.password='abc12345xyz!@#abc'; u.password_confirmation='abc12345xyz!@#abc'; u.save!"
   ```
   > ⚠️ Git Bash 用户同样要加 `winpty`：`winpty docker exec -it gitlab-ce gitlab-rails runner "..."`
4. ⚠️ 任意一条不满足 → [官方] 重置流 <https://docs.gitlab.com/security/reset_user_password/#reset-the-root-password>

> 🔔 **下一步必读**：Web 登录成功后，**第一步先创建 Personal Access Token (PAT)**——详见 [§5.0.5](#ch05)。GitLab 17 起，git push / API 调用一律用 PAT，**不能用密码直接 push**。这一步漏掉的话 §5.0.2 第一次 `git push` 会失败。

### 3.2.4 ⚠️ 必踩的坑

| 坑 | 表现 | 解法 |
|----|------|------|
| **HTTPS/443 默认不通** | `curl https://localhost` 直接 "Connection refused" | 改用 `http://80`；启用 HTTPS 要配 `gitlab.rb` 的 `external_url 'https://...'` + 自签 / Let's Encrypt（[官方] /install/docker/installation/）|
| **内存不够** | GitLab 起不来 / `docker stats` OOM | 至少留 4 GB（Docker Desktop 配额 12.6 GB） |
| **`/api/v4/session` 返回 404** | GitLab 15.5+ 弃用了 | 改用 **Personal Access Token (PAT)**（详见 §5.0） |

---

## 3.3 路径 B · Linux Omnibus（单机 VM 生产）

> 💡 **本教程主推 Docker**。Omnibus 路径是给"生产 Linux VM、长期跑"场景留的，单条命令装好。

**Ubuntu / Debian：**

```bash
sudo apt update && sudo apt install -y curl openssh-server ca-certificates
curl "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh" | sudo bash
sudo EXTERNAL_URL="https://gitlab.example.com" apt install gitlab-ce
# 装完自动 reconfigure，浏览器访问 EXTERNAL_URL
```

**CentOS / RHEL / AlmaLinux / Rocky：** 把上面 `apt` 全部换成 `dnf`，`.deb.sh` 换 `.rpm.sh`。

> 🔥 **防火墙上**：`firewall-cmd --add-service=http --add-service=https --add-service=ssh --permanent && firewall-cmd --reload`

详细：[官方] /install/package/ubuntu/ 。

---

## 3.4 部署后必做（清单）

无论哪种部署（[官方] /install/next_steps/）：

- [ ] 用 root + `initial_root_password` 登录 → **立即改密码**
- [ ] **配置 SMTP**（详见 §4.3）—— 否则用户收不到任何邮件
- [ ] **禁用公开注册**（默认开放，有安全风险）
- [ ] 改 `external_url` 为真实域名（容器 / Omnibus 改完都跑一次 `gitlab-ctl reconfigure`）
- [ ] 设 cron 自动备份（§8.1）
- [ ] 防火墙只暴露 22/80/443，其他全关

---


### 3.3.1 装完到哪里去看初始 root 密码

Omnibus 装完会自动生成一个随机 root 密码，存到临时文件：

```bash
# 1. 读初始密码
sudo cat /etc/gitlab/initial_root_password
# 输出类似：
# # WARNING: This value is valid only in the first 24 hours ...
# Password: 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

# 2. 浏览器访问 EXTERNAL_URL
#    用户名: root
#    密  码: 上面那一串（去掉 'Password: ' 前缀和 ' ' 引号）

# 3. 登进去后立即改密码
#    右上角头像 → Edit profile → Password
```

**几点说明**（以下每条标注了可信度；前 4 条是「能在你本机容器里读到原文字的」——你 `gitlab-ce` 19.1.1 部署后由 Omnibus 实际生成的文件，不是凭官方文档推论）：

- **路径固定**：`/etc/gitlab/initial_root_password`，跟 `EXTERNAL_URL` 在哪无关 — **[官方]** `/install/next_steps/` 已抓原文。
- **24 小时后会删，但有个重要细节**：文件末行原文 `NOTE: This file is automatically deleted after 24 hours on the next reconfigure run.` —— **[本机验证]**。意思是「**24h 超时**且**你跑了下一次 reconfigure**」两个条件都满足才真的删；超时了但没 reconfigure，文件**还在**。`/install/next_steps/` 只提「文件位置」，这一句「next reconfigure run」是 Omnibus 实际生成文件里的原话。超时重置用 `sudo gitlab-rake gitlab:password:reset[root]`（[本教程 §附录 B]）。
- **`reconfigure` 是删除触发器，不是密码还魂**：同上原文 `on the next reconfigure run` 明确表明 reconfigure 是「删除」动作的一部分。严谨说法：**超时后的密码文件**在下一次 `gitlab-ctl reconfigure` 跑时被删；它**不会**被 reconfigure “重置倒计时”或“延期”。**[本机验证]**。
- **这个密码只在 4 个条件都满足时才有效**（文件首段 5 行 WARNING 逐字总结）—— **[本机验证]**：
  1. 你**安装前**用 `GITLAB_ROOT_PASSWORD` 环境变量设过密码，**或**用 `gitlab_rails['initial_root_password']` 设过；**或**不设、Omnibus 自己生成
  2. **不是在数据库初始化之后**才改的 `gitlab.rb`（否则 GitLab 已重置为另一套密码）
  3. 装好后你**没在 UI / CLI 改过 root 密码**
  4. 这个文件是当下这次安装生成的
  
  任意一条不满足 → 用 GitLab 自己的 reset 流（**[官方]** 文件 WARNING 里给了链接）：<https://docs.gitlab.com/security/reset_user_password/#reset-the-root-password>
- **不要 commit 到 git**：**路径推导**：`/etc/gitlab/` 不在代码仓库，不存在误 commit 风险；但该文件是否被 GitLab 的默认应用备份包含进来 —— Omnibus `backup-etc` 默认会备份 `/etc/gitlab` 整个目录（**[官方]** `/omnibus/settings/backups/` 已抓原文），所以**默认会被备份**，出备份时请记得加密（参见 §8.1 提醒）。
- **装包时已设过密码**（`GITLAB_ROOT_PASSWORD` 环境变量 / `gitlab_rails['initial_root_password']`）：文件第一段 WARNING 原文明写这两个变量名 —— **[本机验证]**：原文证明了「**这些变量名是 Omnibus 钦定的覆盖入口**」。**实际优先顺序**（环境变量 vs gitlab.rb 哪边优先、是否会生成 initial_root_password）—— **[未独立验证]**，以官方安装文档为准。
- **装不上 / 看不到这文件**：**[经验推测]** —— 多半是 `gitlab-ctl reconfigure` 没跑完，看 `sudo gitlab-ctl tail reconfigure` 日志。

---

## 3.5 不在本章范围（其他部署）

| 方式 | 适合 | 参考 |
|------|------|------|
| **Helm chart** | 大规模 / 云原生 / 已有 K8s + Postgres + Redis + S3 | [官方] /charts/ |
| **GitLab Operator** | OpenShift | [官方] /operator/ |
| **云上市场镜像** | 一键启动（AWS / GCP） | [官方] /install/aws/ |


---

# 04 · 初始配置 {#ch04}

## 4.1 配置文件结构（Omnibus）

> 🌿 进阶 · 配置文件

![Admin General Settings](images/gitlab-4.1-admin-settings.png)
*图：Admin → Settings → General 页（[本机验证] 实拍）。UI 设置最终都写到 `/etc/gitlab/gitlab.rb`；改完跑 `gitlab-ctl reconfigure` 生效*

Omnibus GitLab 主配置文件：**`/etc/gitlab/gitlab.rb`**（Ruby 语法，[官方] /omnibus/settings/configuration/）

改完任何配置必须跑：

```bash
sudo gitlab-ctl reconfigure    # 重新生成所有组件配置并应用
```

> ⚠️ **不要直接改 `/etc/gitlab/gitlab-secrets.json`**（密码/令牌），除非你知道后果。

### 常用配置项速查（[官方] /omnibus/settings/）

```ruby
# /etc/gitlab/gitlab.rb

# === 1. 外部 URL ===
external_url 'https://gitlab.example.com'

# === 2. 时区 ===
gitlab_rails['time_zone'] = 'Asia/Shanghai'

# === 3. 注册策略（默认开放注册，生产慎用） ===
gitlab_rails['gitlab_signup_enabled'] = false   # 关闭开放注册
gitlab_rails['gitlab_default_can_create_group'] = false   # 默认用户不能建组

# === 4. 备份（默认不自动跑，需要配 cron，详见 8.1） ===
gitlab_rails['manage_backup_path'] = true
gitlab_rails['backup_path'] = '/var/opt/gitlab/backups'
gitlab_rails['backup_archive_permissions'] = 0644
gitlab_rails['backup_pg_schema'] = nil
# backup_keep_time 默认是 0（永久保留）；下面这行设为保留 7 天（秒）
gitlab_rails['backup_keep_time'] = 604800

# === 5. SMTP（见下方详） ===
# 见 4.3 节

# === 6. 资源限制（防止吃光服务器） ===
puma['worker_processes'] = 4
sidekiq['max_concurrency'] = 25
postgresql['shared_buffers'] = "256MB"

# === 7. HTTPS / SSL（见下方详） ===
# 见 4.4 节

# === 8. SSH 端口（默认 22，改了的话） ===
gitlab_rails['gitlab_shell_ssh_port'] = 22

# === 9. 容器仓库 ===
registry_external_url 'https://registry.example.com'
gitlab_rails['registry_enabled'] = true
```

应用配置：

```bash
sudo gitlab-ctl reconfigure
```

> Docker 部署把同样的 `gitlab.rb` 字段塞到 `GITLAB_OMNIBUS_CONFIG` 环境变量里。

## 4.2 用户、组、角色（核心概念）

GitLab 权限模型（[官方] /user/permissions/）：

### 4.2.1 角色

| 角色（Role） | 能干啥 |
|--------------|--------|
| **Owner** | 全部，包括删项目、改成员角色、删组 |
| **Maintainer** | 改项目设置、push 受保护分支、跑 CI、合并 MR |
| **Developer** | push 非保护分支、创建 MR、跑 pipeline |
| **Reporter** | 看代码、开 Issue、评论 |
| **Guest** | 看公开 issue、评论 |
| **Minimal Access** | 几乎只能看到自己在该组里（用于大组织隔离） |

> Premium / Ultimate 还有 **Guest +**、**Planner**、**Auditor** 等额外角色。

### 4.2.2 可见性

| 级别 | 谁能看 |
|------|--------|
| **Private** | 仅成员 |
| **Internal** | 任意已登录用户 |
| **Public** | 任何人（包括未登录） |

## 4.3 配置 SMTP 发邮件

> 🌿 进阶 · 邮件功能必需

**没有 SMTP 就不要装 GitLab**——用户注册、密码重置、Issue 通知全部走邮件（[官方] /omnibus/settings/smtp/）。

### 4.3.1 用 QQ 邮箱（国内最常用）

⚠️ **第一步先拿授权码**（不是 QQ 登录密码）：

1. 登录 https://mail.qq.com → 顶部「**设置**」→「**账户**」
2. 翻到 **POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务** 这一节（[官方] QQ 邮箱帮助页）
3. 开启「**SMTP 发信功能**」 → 按提示**发送短信验证** → QQ 邮箱生成 **16 位授权码**（只显示一次，存好）

然后改 `/etc/gitlab/gitlab.rb`：

```ruby
# /etc/gitlab/gitlab.rb（QQ 邮箱 SSL 模式，端口 465）
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.qq.com"
gitlab_rails['smtp_port'] = 465                              # SSL；想用 STARTTLS 改成 587
gitlab_rails['smtp_user_name'] = "your-qq-number@qq.com"    # 你的完整 QQ 邮箱地址
gitlab_rails['smtp_password'] = "QQ邮箱授权码（16位）"       # ⚠️ 授权码，不是 QQ 登录密码
gitlab_rails['smtp_domain'] = "qq.com"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = false            # 465 SSL 直连，不走 STARTTLS
gitlab_rails['smtp_ssl'] = true                              # 端口 465 必须 true
gitlab_rails['smtp_openssl_verify_mode'] = 'peer'            # QQ 证书由受信 CA 签发

gitlab_rails['gitlab_email_from'] = 'your-qq-number@qq.com'
gitlab_rails['gitlab_email_reply_to'] = 'noreply@qq.com'

# 想用 STARTTLS（端口 587），改这几行：
# gitlab_rails['smtp_port'] = 587
# gitlab_rails['smtp_enable_starttls_auto'] = true
# gitlab_rails['smtp_ssl'] = false
```

`gitlab-ctl reconfigure` 后用 [§4.3.3](#433-测试邮件qq-邮箱专用步骤) 的测试命令验证。

### 4.3.2 通用测试方法（跨 SMTP 提供商）

无论用 QQ 邮箱 / Gmail / AWS SES / 自建 Postfix，下面 3 个方法**通用**：

**方法 A · Rake 任务**（[官方] 推荐，GitLab 16.0+）：

```bash
sudo gitlab-rake gitlab:notify_test_email['your@email.com','Test Subject','Test Body']
# 方括号参数必须引号包；含空格时用单引号
```

**方法 B · Rails 控制台**（所有 GitLab 版本可用）：

```bash
sudo gitlab-rails console
# 等到提示符出现（约 30 秒），然后输入：
Notify.test_email('your@email.com', 'Test Subject', 'Test Body').deliver_now
# Ctrl+D 退出
```

**方法 C · 看 production.log**（三种场景都要看）：

```bash
sudo gitlab-ctl tail gitlab-rails                 # 实时跟踪
# 或单独看 production.log
sudo tail -f /var/log/gitlab/gitlab-rails/production.log | grep -i smtp
```

### 4.3.3 测试邮件（QQ 邮箱专用步骤）

每次改完 `gitlab.rb` 都要跑这两步再测：

```bash
# 1. 让 GitLab 重新读配置（不重启服务）
sudo gitlab-ctl reconfigure

# 2. 发测试邮件（GitLab 16.0+ 推荐，官方 Rake 任务）
sudo gitlab-rake gitlab:notify_test_email['your-qq-number@qq.com','GitLab SMTP 测试','正文测试']
```

**实测反馈**（按这个顺序看输出）：

| 看到的输出 | 意思是 | 怎么修 |
|-----------|--------|--------|
| `Sent mail to ...`  + 收件箱收到邮件 | ✅ 通 | 收工 |
| `535 Error: authentication failed` | 用户名或密码错 | `smtp_user_name` 写完整邮箱 `xxx@qq.com`；`smtp_password` 改成 **16 位授权码**（不是 QQ 密码），拿码步骤见 §4.3.1 |
| `OpenSSL::SSL::SSLError` / `TLS connection failed` | SSL/STARTTLS 没配对 | 端口 465 时 `smtp_ssl = true` + `smtp_enable_starttls_auto = false`；端口 587 时反过来 |
| `connection timed out` 到 `smtp.qq.com:465` | 端口被运营商封 / 防火墙挡 | 改用 587 + STARTTLS，或在防火墙放行 465/587 出站 |
| 邮件发出去但进了垃圾箱 | DKIM/SPF 没配上 | 见下方「防进垃圾箱」段 |

**防进垃圾箱**（QQ 邮箱给 Gmail/Outlook 发特别容易进垃圾）：

QQ 邮箱要求发件人地址跟 SMTP 授权账号一致 —— `gitlab_email_from` 必须等于 `smtp_user_name`，否则 QQ 邮箱会改 From 或直接标垃圾：

```ruby
gitlab_rails['gitlab_email_from'] = 'your-qq-number@qq.com'   # 必须跟 smtp_user_name 一样
gitlab_rails['gitlab_email_from_name'] = 'GitLab'
```

需要在 QQ 邮箱「设置 → 反垃圾 → 设置邮件发送邮箱」里把 GitLab 服务器的 IP 加入白名单（白名单机制，避免被自家反垃圾拦截）。

> 旧版测试方法（GitLab 16.0 之前）仍可用，但不推荐：
> ```bash
> sudo gitlab-rails console
> Notify.test_email('your@email.com', 'Test Subject', 'Test Body').deliver_now
> # Ctrl+D 退出
> ```

### 4.3.4 失败模式 / 常见错误

按报错频次排序：

| # | 现象 | 根因 | 修复 |
|---|------|------|------|
| 1 | `535 Error: authentication failed` | `smtp_password` 写成了 QQ 登录密码而非授权码 | 见 §4.3.1 第 3 步拿 16 位授权码 |
| 2 | `OpenSSL::SSL::SSLError` / TLS 卡住 | 端口 465 配了 STARTTLS 或端口 587 配了 `smtp_ssl=true` | 二选一（参考 §4.3.1 配置表的 STARTTLS 注释） |
| 3 | `connection timed out` 到 `smtp.qq.com:465` | 国内运营商封禁 25/465 出站 | 改用 587 + STARTTLS；在防火墙放行 465/587 出站 |
| 4 | 邮件发出去但进垃圾箱 | `gitlab_email_from` ≠ `smtp_user_name`；缺 DKIM/SPF；GitLab 服务器 IP 未加白名单 | 见 §4.3.3 末尾「防进垃圾箱」段 |
| 5 | 改完 `gitlab.rb` 没生效 | 没跑 `gitlab-ctl reconfigure` | 改完任何 SMTP 配置**都必须** reconfigure；不要直接重启服务（reconfigure 已经会重载） |
| 6 | 生产发送量触发 QQ 日上限 | 个人 QQ 邮箱每天 50 封左右，企业邮箱更高 | 多人团队用腾讯企业邮箱 / SendGrid / Mailgun / AWS SES（[官方] /omnibus/settings/smtp/#microsoft-365） |
| 7 | 用 `gitlab_rails console` 测 SMTP 报错但实际邮件能发 | 测试命令拼写问题（如忘了 `.deliver_now`） | 务必带 `.deliver_now`；看返回对象类型不是 Exception |
| 8 | 465 端口测试 OK 但 587 报错 / 反之 | STARTTLS 和 SSL 不是同一回事 | 见 §4.3.1 配置注释——不能两个都开，也不能两个都不开 |

**预防清单**（生产上线前自检）：

- [ ] `gitlab-ctl reconfigure` 跑过（不要漏）
- [ ] 5.0.5 创建的 PAT 替换为真实 token，不是占位符
- [ ] QQ 邮箱白名单加了 GitLab 服务器 IP
- [ ] `gitlab_email_from` = `smtp_user_name`
- [ ] 选好端口（465 SSL **或** 587 STARTTLS，二选一）
- [ ] `gitlab-rake gitlab:notify_test_email` 跑通
- [ ] production.log 没有 `error` 或 `warn` 级别 SMTP 日志

## 4.4 配置 HTTPS / SSL

> 💡 **本机默认部署用 `http://localhost`，不需要看本节**。只有要在公网域名 / 内网域名提供 https 时才看。

### 4.4.1 Let's Encrypt 自动证书（[官方] /omnibus/settings/ssl/）

最省心的方式——前提是你有公网域名 + 80 端口能访问。

装包时已经设了 `EXTERNAL_URL="https://gitlab.example.com"`，Omnibus 会自动申请 Let's Encrypt 证书。

如果装包时是 http，事后改：

```ruby
# /etc/gitlab/gitlab.rb
external_url 'https://gitlab.example.com'
letsencrypt['enable'] = true
letsencrypt['contact_emails'] = ['admin@example.com']   # 证书到期前会发邮件
letsencrypt['auto_renew'] = true

# 可选：自动续期时间（默认 7 days before expiry，每天凌晨检查）
# letsencrypt['auto_renew_hour'] = 0
# letsencrypt['auto_renew_minute'] = 0
```

```bash
sudo gitlab-ctl reconfigure
```

### 4.4.2 用自己的证书

```ruby
# /etc/gitlab/gitlab.rb
external_url 'https://gitlab.example.com'

# 关闭 Let's Encrypt
letsencrypt['enable'] = false

# 把证书放进来
nginx['ssl_certificate'] = "/etc/gitlab/ssl/gitlab.example.com.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/gitlab.example.com.key"

# 自签证书要加这行（否则 git push 会失败）
nginx['ssl_self_signed'] = true
```

```bash
# 上面 /etc/gitlab/ssl/gitlab.example.com.{crt,key} 必须存在。常见来源：
#   1. 机构签发的证书：CA 发的 .crt + .key 上传到服务器
#   2. Let's Encrypt certbot：用 `certbot certonly --standalone -d gitlab.example.com` 生成
#   3. 自签证书：`openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/gitlab/ssl/gitlab.example.com.key -out /etc/gitlab/ssl/gitlab.example.com.crt -subj "/CN=gitlab.example.com"` 直接放位置

sudo mkdir -p /etc/gitlab/ssl
# 以下假设证书文件在本机当前目录；从远端拷过来的话先用 scp：
#   scp ./gitlab.example.com.crt root@gitlab:/etc/gitlab/ssl/
sudo cp my-cert.crt /etc/gitlab/ssl/gitlab.example.com.crt
sudo cp my-cert.key /etc/gitlab/ssl/gitlab.example.com.key
sudo chmod 600 /etc/gitlab/ssl/gitlab.example.com.key
sudo gitlab-ctl reconfigure
```

## 4.5 注册策略（生产必改）

默认任何人都能注册账号（[官方] /administration/settings/sign_up_restrictions/）——生产环境必须关。

### 4.5.1 关闭开放注册

**方式 A**：配置文件

```ruby
# /etc/gitlab/gitlab.rb
gitlab_rails['gitlab_signup_enabled'] = false
```

**方式 B**：UI（更直观）

`Admin area` → `Settings` → `General` → **Sign-up restrictions** → 关掉 `Sign-up enabled`

### 4.5.2 接入 SSO（LDAP / SAML / OAuth）

UI 路径：`Admin area` → `Settings` → `General` → **Sign-in restrictions** 或 **Authentication and Provisioning**

| 方式 | 适用 |
|------|------|
| **LDAP** | 公司 AD / OpenLDAP |
| **SAML** | 企业 SSO（Okta、Azure AD、Auth0、自建 SAML IdP） |
| **OAuth** | GitHub / Google / GitLab.com 等第三方 |
| **Generic OIDC** | 任何 OIDC 提供商 |

LDAP 配置示例（[官方] /administration/auth/ldap/）：

```ruby
# /etc/gitlab/gitlab.rb
gitlab_rails['ldap_enabled'] = true
gitlab_rails['prevent_ldap_sign_in'] = false

gitlab_rails['ldap_servers'] = {
  'main' => {
    'label' => 'LDAP',
    'host' => 'ldap.example.com',
    'port' => 636,
    'uid' => 'sAMAccountName',
    'bind_dn' => 'CN=GitLab,OU=Service,DC=example,DC=com',
    'password' => 'password',
    'encryption' => 'simple_tls',
    'verify_certificates' => true,
    'active_directory' => true,
    'allow_username_or_email_login' => true,
    'block_auto_created_users' => false,
    'base' => 'OU=Users,DC=example,DC=com',
    'user_filter' => '(memberOf=CN=GitLab-Users,OU=Groups,DC=example,DC=com)'
  }
}
```

## 4.6 配置 Container Registry

### 4.6.1 配 gitlab.rb

```ruby
# /etc/gitlab/gitlab.rb

# 1. URL：按部署类型填
#    本机默认部署（Docker，localhost）：registry_external_url 'http://registry.localhost:5000'   （**不是 https**）
#    公网域名（Let's Encrypt）：registry_external_url 'https://registry.example.com'
#    私网域名（自签证书）：registry_external_url 'https://registry.example.com:5000'
registry_external_url 'https://registry.example.com'

# 2. 证书：手动证书填以下两行；用 Let's Encrypt 可省
registry_nginx['ssl_certificate'] = "/etc/gitlab/ssl/registry.example.com.crt"
registry_nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/registry.example.com.key"
```

```bash
sudo gitlab-ctl reconfigure
```

### 4.6.2 测试（按部署类型选）

| 部署类型 | 测试 URL | 登录账号 |
|---------|---------|---------|
| 本机 Docker（默认） | `registry.localhost:5000` | root + §5.0.5 PAT |
| 公网 https | `registry.example.com` | GitLab 账号 |
| 自签证书 | `registry.example.com:5000` | GitLab 账号 + 加 `insecure-registries` 到 daemon.json |

下面以本机为例：

```bash
# 登录
docker login registry.localhost:5000
# Username: root
# Password: §5.0.5 创建的 PAT（需 read_repository + write_registry scope）

# 测试推送
docker pull alpine:latest
docker tag alpine:latest registry.localhost:5000/group/project/alpine:latest
docker push registry.localhost:5000/group/project/alpine:latest
```

## 4.7 配置 Pages（静态网站托管）

> 💡 本节讲 **server 端配置**；项目端 .gitlab-ci.yml 写法 + URL 规则见 [§5.9 Pages](#ch05)。

```ruby
# /etc/gitlab/gitlab.rb
pages_external_url 'https://pages.example.com'
# 配通 DNS 通配符 *.example.com 指向 GitLab 服务器
```

免费 Wildcard 证书：

```ruby
letsencrypt['enable'] = true
pages_nginx['redirect_http_to_https'] = true
```

## 4.8 关键参数确认（重新配置后）

```bash
sudo gitlab-rake gitlab:env:info    # 看环境 + 配置
sudo gitlab-rake gitlab:check       # 全面健康检查
sudo gitlab-ctl status              # 看进程状态
```

`gitlab:check` 会扫所有关键点：DB、Redis、SSH、Mail、SMTP、Gitaly 等等。生产部署完必跑一次。

---

# 05 · 日常操作 {#ch05}

> 本章基于本教程抓取的 `/user/get_started/` 12 张子主题卡片（[官方]），加上 GitLab 官方用户文档补充。
>
> **第 5.0 节 "5 分钟快速上手"** 是按本机实例（`gitlab-ce` 容器 @ `localhost`）实战验证过的精简流程。**5.1-5.11 节是功能完整指南**。

## 5.0 · 5 分钟快速上手（[本机验证]）

> 用本机实例（`gitlab-ce` 容器 @ `localhost`）实战验证过的最小流程，让新手从登录到会用。

### 5.0.1 登录 + 改密码 [本机验证]

![GitLab 登录页](images/gitlab-5.0.1-login.png)
*图：GitLab 19.1.1 登录页（[本机验证] 实拍）。输入 Username + Password 点 Sign in*

![首次登录后的引导页](images/gitlab-5.0.1a-first-login.png)
*图：GitLab 19 新用户首次登录后的 Home 主页（无项目时空状态）。GitLab 19 **不再强制引导**创建 group/project，老版本才有强制引导*

1. 浏览器打开 <http://localhost/>
2. 用 `root` + `initial_root_password` 登录（密码 `docker exec gitlab-ce cat /etc/gitlab/initial_root_password`）
3. ⚠️ **立即改密码**：右上角头像 → **Edit profile** → 左侧菜单 **Access** → **Password and authentication** → 点 `Change password`
   （GitLab 19.1.1 把"改密码"从 Account 页拆到单独的 Access 子菜单下，跟 SSH Keys / GPG Keys 同级；早期版本在 Account 页）

![改密码页](images/gitlab-5.0.1b-change-password.png)
*图：User Settings → Access → Password and authentication（[本机验证] 实拍）。`Change password` 区可改密码；下面的 `Two-factor Authentication` 也建议一并启用*
4. **失败模式**：`initial_root_password` 文件**24 小时后自动删**——改完新密码永不过期，不改会被锁外

### 5.0.2 创建项目 + 第一次 git push [本机验证]

**Web UI**：`+` (左上角) → **New project** → **Create blank project** 卡片 → 进入表单 → 命名 `hello-world` → 选 Visibility (Private 默认 OK) → 勾选 `Initialize repository with a README` → **Create project**

> **GitLab 19 改动**：新建项目从一步表单变成了**两步流程**——先选方式（空白/模板/导入），再填表单。

![创建项目入口（选方式）](images/gitlab-5.0.2a-new-project.png)
*图：Create new project 入口页（[本机验证] 实拍）。GitLab 19 把创建拆成 3 个卡片选项：**创建空白项目** / 从模板创建 / 导入项目；点 **创建空白项目** 进入下一步表单*

![创建空白项目表单](images/gitlab-5.0.2a-new-project-form.png)
*图：Create blank project 表单页（[本机验证] 实拍）。填 **项目名称** → 选 **可见性级别** (默认私有) → 勾 **使用自述文件初始化仓库** → 点 **新建项目***

![项目主页（初始）](images/gitlab-5.0.2b-project-home.png)
*图：刚创建的项目主页（[本机验证] 实拍）。左下"Set up CI/CD"是空 pipeline；默认 main 分支有 README；右上 Clone 提供 HTTPS/SSH URL*

```bash
# ⚠️ 用 HTTP/80，不是 HTTPS/443（443 默认没启，见第 3 章 3.3.5）
# ⚠️ 把 glpat-xxxxxxxxxxxxxxxxxxxx 替换为 5.0.5 创建的完整 PAT（以 glpat- 开头）
git clone http://root:glpat-xxxxxxxxxxxxxxxxxxxx@localhost/root/hello-world.git
cd hello-world

# 改 README，写一句 commit，push
echo "Hello from OpenClaw" >> README.md
git add . && git commit -m "first commit" && git push
```

> ⚠️ **PAT 含特殊字符（+/=` 等）的踩坑**：如果 PAT 里含有 `@ : / + %` 等字符，URL 直接拼接会报 `URL malformed` 或认证失败。两种解决：
> 1. **更稳**：用 SSH（详见 §5.1.3）—— 生成 SSH key 加到 GitLab，clone 用 `git clone git@localhost:root/hello-world.git`
> 2. **简单**：创建 PAT 时避开特殊字符（Scopes 选 `api, read_repository, write_registry` 后生成的 PAT 含 + 和 =）
>
> 跨平台坑：PowerShell 下的 `http://root:PAT@host/...` 嵌套 @ PowerShell 会报 `The URI prefix is not recognized`——推荐用 **Git Bash** 跑 git 命令，或改用 SSH。

[本机验证] 刷新项目主页 → 应看到新 commit + README 内容变化。

### 5.0.3 提第一个 Merge Request [本机验证]

```bash
git checkout -b feature/greeting       # 新分支
echo "# Hello World" > GREETING.md     # 改个东西
git add GREETING.md && git commit -m "Add greeting doc"
git push -u origin feature/greeting
```

Web：刷新项目页 → **Create merge request** → 标题"Add greeting doc" → 目标分支 `main` → **Create merge request** → **Merge**（含 squash / merge commit / rebase 三选一）。

![新建 MR 表单](images/gitlab-5.0.3b-create-mr-form.png)
*图：New merge request 页（[本机验证] 实拍）。Source branch = feature/greeting，Target branch = main。下方可填 Assignee / Reviewer / Milestone / Labels*

![MR 列表（合并后）](images/gitlab-5.0.3c-mr-list-after.png)
*图：Merge requests 列表页（[本机验证] 实拍）。Merged 显示合并状态；Open 是待合 MR*

![仓库 tree 视图](images/gitlab-5.0.3d-repo-tree.png)
*图：项目仓库 tree 视图（[本机验证] 实拍）。main 分支文件列表；点击文件看历史/ blame*

> 第一次推完，命令行会显示 "Create a pull request for X" 的 URL，**点它也直接进 MR 页面**。

### 5.0.4 建第一个 Issue [本机验证]

Web：项目页 → 左侧 **Issues**（GitLab 19 重命名为 **Work items**）→ **New issue** → 标题"Add CI/CD" → 描述支持 Markdown → **Create issue**。

![Work Items 列表](images/gitlab-5.0.4a-issues-list.png)
*图：项目 Work Items 列表页（[本机验证] 实拍）。GitLab 19 把 Issues + Tasks + Epics 合并成 Work Items；左边 status filter，右边排序*

![新建 Work Item 表单](images/gitlab-5.0.4b-new-work-item.png)
*图：New issue 表单（[本机验证] 实拍）。填标题 + 描述（支持 Markdown / attachments）；下方可指派 Assignee / Labels / Due date / Milestone*

> ⚠️ 没配 SMTP（04 章）之前，issue 评论 / @ 通知不发邮件，但**站内是能看**的。

### 5.0.5 创建 Personal Access Token (PAT) [本机验证]

> 🔔 **必读**：GitLab 17 起 **git push 不再支持密码认证**——所有 git push、clone、API 调用都要 PAT。§3 部署完进入下一步前**先做这一节**。

API + git via HTTPS 都要 PAT，不能再用密码（GitLab 17 删了密码 git push）。

**方法 1 · Web UI**：

- 右上头像 → **Edit profile** → 左侧菜单 **Access tokens**

![Access Tokens 列表](images/gitlab-5.0.5a-access-tokens.png)
*图：Personal access tokens 页（[本机验证] 实拍）。右上 **Add new token** 创建；列表显示已存在的 token（value 只在创建瞬间显示一次）*

**👉 在图 5.0.5a 右上点 **Add new token** 按钮** → 跳转到表单页（图 5.0.5b）：

![新增 PAT 表单](images/gitlab-5.0.5b-new-pat-form.png)
*图：Add new personal access token 表单页（[本机验证] 实拍）。填 Token name + Expiration date + Scopes（最少给 `api`/`read_repository`/`write_repository`）→ 点 **Create personal access token***

填表字段：

- **Token name**: `my-token-2026-07-05`（起个能记住用途的名字）
- **Expiration date**: `30` 天后（[官方] 最长 365 天；空值永久但官方不推荐）
- **Scopes**（按需勾，最少给）: `api`, `read_repository`, `write_repository`

完成后点 **Create personal access token** → ⚠️ **立即复制 token 值**（刷新页面就看不到了，只能重新生成）

**方法 2 · 容器内 root 视角**（更灵活，可批量）：

```bash
# 1. 写 ruby 脚本到本地
# 2. docker cp 到容器内
# 3. 在容器内 gitlab-rails runner 执行
```

最小 ruby 脚本：

```ruby
user = User.find_by_username("root")
t = user.personal_access_tokens.create!(
  name: "my-token-2026-07-05",
  scopes: [:api, :read_repository, :write_repository],
  expires_at: 30.days.from_now
)
puts "TOKEN=" + t.token
puts "TOKEN_LEN=" + t.token.length.to_s   # 应该 51
puts "EXPIRES=" + t.expires_at.to_s
```

[本机验证] 标准 PAT 长度 **51 字符**。Console 输出常含水平省略号 `…`（U+2026，**不是 PowerShell 截断产生的，可能是真的字符混进了 token**） → **必须验证** `Write-Host "Token length: $($tok.Length)"` 期望 51；若 < 51，说明 token 在复制粘贴时被替换为占位符，不是被截断，**重新生成一个 token 即可**。

### 5.0.6 5 分钟健康检查 [本机验证]

> 🔄 跨平台版本：下面 3 种任选其一（PowerShell 限 Windows；curl + jq 限 Linux/macOS 且需 `apt install jq` / `brew install jq`；Python 通用）。

#### Windows · PowerShell

```powershell
$hdr = @{ "PRIVATE-TOKEN" = "glpat-…" }   # 替换为你自己的 token
$me = Invoke-RestMethod 'http://localhost/api/v4/user' -Headers $hdr
Write-Host "✅ Logged in as $($me.username) (id=$($me.id))"

$v = Invoke-RestMethod 'http://localhost/api/v4/version' -Headers $hdr
Write-Host "✅ GitLab version: $($v.version)"

# 列已有项目
$ps = Invoke-RestMethod 'http://localhost/api/v4/projects?membership=true' -Headers $hdr
Write-Host "✅ Projects: $($ps.Count)"
```

#### Linux / macOS · curl + jq

```bash
TOKEN="glpat-…"   # 替换为你自己的 token

curl -sS --header "PRIVATE-TOKEN: $TOKEN" \
  http://localhost/api/v4/user \
  | jq -r '"✅ Logged in as \(.username) (id=\(.id))"'

curl -sS --header "PRIVATE-TOKEN: $TOKEN" \
  http://localhost/api/v4/version \
  | jq -r '"✅ GitLab version: \(.version)"'

curl -sS --header "PRIVATE-TOKEN: $TOKEN" \
  'http://localhost/api/v4/projects?membership=true' \
  | jq -r '"✅ Projects: \(. | length)"'
```

#### 跨平台 · Python 3（依赖最小）

```python
import urllib.request, json
TOKEN = "glpat-…"   # 替换为你自己的 token

def get(path):
    req = urllib.request.Request(
        f"http://localhost{path}",
        headers={"PRIVATE-TOKEN": TOKEN},
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)

me = get("/api/v4/user")
print(f"✅ Logged in as {me['username']} (id={me['id']})")

v = get("/api/v4/version")
print(f"✅ GitLab version: {v['version']}")

projects = get("/api/v4/projects?membership=true")
print(f"✅ Projects: {len(projects)}")
```

#### 跑通说明

跑通说明：① 容器正常 ② 鉴权正常 ③ API 可用 ④ PAT 有 scope 权限。

#### 常见失败模式

| 报错 | 意思 | 解法 |
|------|------|------|
| **`401 Unauthorized`** | PAT 失效 / 拼错 | 检查 `glpat-` 前缀；PAT 有效期是否过期（§5.0.5）；重新生成 PAT |
| **`404 Not Found`** | URL 错 | 默认 API 路径是 `/api/v4/...`（**不是 `/api/v3/`**） |
| **`curl: (7) Failed to connect to localhost`** | 容器未启 / 端口错 | `docker ps` 看 `gitlab-ce` 是否 up；`curl -I http://localhost/users/sign_in` 看 80 |
| **`jq: parse error`** | API 返回非 JSON（多为 5xx HTML 错误页） | 拿 `curl ... \| jq .` 看响应体；常见是 container 启动中、PostgreSQL 锁症 |
| **`{"message":"403 Forbidden"}`** | PAT 缺少 `api` scope | 重新创建 PAT，勾上 `api` scope（§5.0.5） |
| **返回 `{"message":"404"}` 但 instance 起来** | 你可能撞了反代 / 自管 GitLab | 拿 `gitlab.example.com` 验证一下 |

**进阶**：跑 `sudo gitlab-rake gitlab:env:info` 可见完整环境状态（在 container 内部跑需要 `docker exec -it gitlab-ce`）。

可视化检查：在 Web UI 也能看到 GitLab 整体状态：

![root 用户主页](images/gitlab-5.0.6-user-home.png)
*图：root 用户主页（[本机验证] 实拍）。顶部导航 Admin / Assigned / To-do 计数；下方 Activity / Projects / Starred projects tab*

![Admin Dashboard](images/gitlab-5.0.6-admin-dashboard.png)
*图：Admin area → Dashboard（[本机验证] 实拍）。实例整体统计：用户数 / 项目数 / 组件健康度；最下方 Version 标签可看 GitLab 完整版本号*

---

**完成到这里就够用了**。5.1-5.11 是功能完整指南，按需翻阅。

## 5.1 项目（Project）

### 5.1.1 创建一个空项目

> 🌱 入门 · 5 分钟
>
> 💡 **从 0 走通全流程**：[§5.0.2](#502-创建项目--第一次-git-push-本机验证) 已有 [本机验证] 步骤（Web UI + 第一次 git push）。
> 本节只讲 **5.0 没涵盖的扩展**：表单字段完整说明 + CLI 路径（glab）。

#### 表单字段完整说明

| 字段 | 必填？ | 说明 |
|------|--------|------|
| **Project name** | ✅ | 项目名（会作为 URL 一部分，**创建后不能改**） |
| **Project URL** | ✅ | `<namespace>/<project-name>`（namespace 是用户名或组名，可改） |
| **Visibility Level** | ✅ | Private / Internal / Public（默认 Private） |
| **Project deployment target** | ⚠️ | 部署目标（一般留空；勾选会启用 deploy board） |
| **Initialize repository with a README** | 可选 | 勾上会建 README.md（**首次推荐勾**，第二次创建同类型可不勾） |
| **Add `.gitignore`** | 可选 | 选语言模板（Python / Node / Go ...），GitLab 会预置 `.gitignore` |
| **Add License** | 可选 | 选协议（MIT / Apache-2.0 ...），会生成 `LICENSE` 文件 |
| **Enable Auto DevOps** | 可选 | 自动 CI/CD pipeline（**注意**：需 Runner，没装时会卡） |

#### CLI 路径（用 glab）

```bash
# 安装 glab CLI（[官方] https://gitlab.com/gitlab-org/cli）
# macOS: brew install glab
# Windows: winget install glab
# Linux: 见 https://gitlab.com/gitlab-org/cli#installation

# 登录
glab auth login --hostname gitlab.example.com

# 创建项目
glab project create my-project --visibility private --description "My new project"
```

### 5.1.2 从本地推一个已有仓库

```bash
cd my-existing-repo
# 本机部署用 localhost；改域名部署时把 localhost 替换为 gitlab.example.com 等
git remote add origin http://localhost/myuser/my-project.git
git push -u origin --all
git push -u origin --tags
```

### 5.1.3 Fork 一个项目

`项目主页` → **Fork** 按钮 → 选目标 namespace

> Fork 后会建立**上游关系**——上游更新你能同步。改 `Settings` → **General** → **Advanced** → **Remove fork relationship** 可断开。

### 5.1.4 导入外部仓库（[官方] /user/project/import/）

支持从 GitHub / Bitbucket / Gitea / Fogbugz / Phabricator 等导入：

`+` → **New project** → **Import project** → 选来源 → 授权 → 选 repo → 导入


### 5.1.5 Public vs Private 项目对比（两种入口，[本机验证]）

> 🌿 进阶 · 本节**不重复创建步骤**，详细流程见 [5.1.1](#511-创建一个空项目)。
> 本节聚焦两个对比维度：**Public vs Private（可见性）** + **首页入口 vs 侧栏 `+` 入口**。

#### 示例项目（本节用作对比的两个 root 仓库）

| 项目 | URL | 可见性 | 创建入口 |
|------|-----|--------|----------|
| `skills-repo` | `http://localhost/root/skills-repo` | **Public** | 首页中央 `Get started` → `Create blank` |
| `dev-code-sample` | `http://localhost/root/dev-code-sample` | **Private** | 左侧栏 `+` → `New project` → `Create blank` |

#### 对比维度 1：可见性（Visibility Level）

| 可见性 | 谁能 clone / pull | 谁能 push | 典型场景 |
|--------|------------------|-----------|----------|
| **Public** | 任何人（无需账号） | 仅项目成员 | 开源项目、文档站点、演示仓库 |
| **Private** | 仅项目成员 | 仅项目成员 | 公司内部代码、未发布的实验 |

> ⚠️ Visibility Level 一旦创建**通常不可改回更严格级别**（Public → Private 需要在项目设置中额外操作；[官方] /user/public_access/)。

![Public 项目 skills-repo 设置页](images/gitlab-5.1.5b-skills-repo-visibility.png)
*图：`root/skills-repo`（Public）项目 → Settings → General，展开"可见性，项目功能，权限"折叠区后可以看到**项目可见性 = 公开**（[本机验证]）*

![Private 项目 dev-code-sample 设置页](images/gitlab-5.1.5c-dev-sample-visibility.png)
*图：`root/dev-code-sample`（Private）项目 → Settings → General，展开"可见性，项目功能，权限"折叠区后可以看到**项目可见性 = 私有**（[本机验证]）*

> 💡 GitLab 19 把"常规设置"路径从 `/<project>/-/settings/general` 改成了 `/<project>/edit`，**常规设置 = `/edit`**，**仓库设置 = `/-/settings/repository`**。

#### 对比维度 2：创建入口（首页 vs 侧栏）

| 对比维度 | 首页入口 | 侧栏 `+` 入口 |
|----------|----------|---------------|
| **触发位置** | 浏览器打开 `http://localhost` 后页面中央 **Get started** 按钮 | 左侧导航栏顶部 **`+`** 下拉 |
| **默认 Visibility** | **Public**（默认选第一个卡片） | **Private**（默认选最后一个卡片） |
| **适合场景** | 快速建公开仓库演示 | 正式私有项目 |
| **入口明显程度** | 首页有醒目 CTA 按钮（新手友好） | 需要熟悉 GitLab 侧栏布局 |

> 💡 两个入口**最终都跳到同一个表单页**，差异只在「默认选项」。表单字段详见 [5.1.1](#511-创建一个空项目)。

---

### 5.1.6 创建用户和组（[本机验证]）

#### 创建用户（3 步完成）

**路径**：`Menu` → **Admin** → **New User**（或直接访问 `/admin/users/new`）

| 步骤 | 操作 |
|------|------|
| 1. 填写基本信息 | Name / Username / Email |
| 2. 选择访问级别 | **Regular**（普通用户）/ Admin（管理员） |
| 3. 点击 **Create user** | 自动发送激活邮件 |

本教程创建了 3 个普通用户（均选择 **Regular** 访问级别）：

| 用户 | Username | Email（示例） |
|------|----------|---------------|
| Alice | `alice` | `alice@example.local` |
| Bob | `bob` | `bob@example.local` |
| Carol | `carol` | `carol@example.local` |

#### 验证：用户创建表单截图

![创建用户 alice 表单已填状态](images/gitlab-5.1.6a-create-user-alice.png)
*图：Admin → New User 页面，alice 的 Name / Username / Email 均已填写（[本机验证]）*

#### 创建组（3 步完成）

**路径**：`Menu` → **Groups** → **Create group**（或直接访问 `/groups/new`）

| 字段 | 示例值 |
|------|--------|
| Group name | `Team Alpha` |
| Group URL / slug | `team-alpha`（自动从 name 生成） |
| Visibility Level | **Private**（默认） |

> **命名空间命名规范**（[官方] /user/namespace/）：只允许字母、数字、下划线、破折号；不能以 `-` 开头；全局唯一（与用户名冲突则拒绝）。

本教程创建了两个私有组：

| 组 | Slug | 可见性 |
|----|------|--------|
| Team Alpha | `team-alpha` | Private |
| Team Beta | `team-beta` | Private |

#### 组的项目共享（进阶）

组建好后，可以将项目分享给组，让组内所有成员自动获得访问权限：

分享操作路径（Web UI）：项目页 → **Settings** → **General** → **Permissions** → **Share with group**

---

### 5.1.7 成员权限对比表（[官方] + [本机验证]）

GitLab 权限体系分三层：**成员角色（Member Roles）** → **权限级别（Access Level）** → **具体能力**。

#### GitLab 内置角色（按权限从高到低）

| 角色 | 数值 | 代码含义 | 能做什么 | 不能做什么 |
|------|------|----------|----------|------------|
| **Owner** | 50 | `OWNER` | 全部权限，包括删除组/转移项目 | — |
| **Maintainer** | 40 | `MAINTAINER` | 管理项目设置 / CI / 保护分支 / 创建 release | 无法删除项目本身 |
| **Developer** | 30 | `DEVELOPER` | Push 代码 / 创建分支 / 创建 MR / 管理 Issue | 无法改项目设置 |
| **Reporter** | 20 | `REPORTER` | 克隆 / Pull / 下载 / 创建 Issue | 无法 push 代码 |
| **Guest** | 10 | `GUEST` | 只能看（公开内容）和评论 | 无法 clone |

#### 本教程的权限配置（[本机验证]）

| 用户 | Team Alpha 角色 | Team Beta 角色 | 可访问项目 |
|------|----------------|---------------|------------|
| alice | Developer (30) | Developer (30) | skills-repo + dev-code-sample |
| bob | Maintainer (40) | Reporter (20) | skills-repo + dev-code-sample |
| carol | Reporter (20) | Reporter (20) | skills-repo + dev-code-sample |

#### 组与项目权限叠加规则

- 项目直接授予权限（Project Member）和通过组继承的权限（Group Member）**取两者的最大值**
- alice 在 skills-repo 项目没有直接权限，但通过 alpha 组继承 Developer (30)；bob 通过 alpha 组继承 Maintainer (40)
- bob 在 beta 组只有 Reporter (20)，但他在 skills-repo 有来自 alpha 组的 Maintainer (40) → **最终权限取最高**

#### 最小权限原则建议

| 场景 | 推荐角色 |
|------|----------|
| 代码贡献开发者 | Developer |
| CI/CD 流水线维护者 | Maintainer |
| 仅查看不提交 | Reporter |
| 外部协作者 | Guest 或 Reporter |

---

## 5.2 分支（Branch）与 Merge Request

### 5.2.1 分支模型

GitLab 默认分支 `main`，也叫 **default branch**（[官方] /user/project/repository/branches/）。

![项目分支列表](images/gitlab-5.2-branches.png)
*图：项目 → 代码 → 分支 页（[本机验证] 实拍）。main 是默认分支、受保护；其他分支可在此查看/创建/删除*

```bash
# 创建并切换到新分支
git checkout -b feature/login-page

# 推送新分支
git push -u origin feature/login-page
```

### 5.2.2 受保护分支（Protected branch）

> 🌿 进阶 · 了解即可

![Repository Settings - Protected branches](images/gitlab-5.2-protected-branches.png)
*图：项目 Settings → Repository 页（[本机验证] 实拍）。展开 **Protected branches** 区块配置*

`Settings` → **Repository** → **Protected branches**：

- **Allowed to push**：Maintainers / Developers / No one
- **Allowed to merge**：Maintainers / Developers / No one
- **Allowed to force push**：勾选允许 force-push（一般不勾）
- **Require approval**：合并前要 N 个 approval

主分支（main / master）**默认就是 Protected**。

### 5.2.3 创建一个 Merge Request

> 🌱 入门 · 5 分钟
>
> 💡 **从 0 走通全流程**：[§5.0.3](#503-提第一个-merge-request-本机验证) 已有 [本机验证] 步骤（`git checkout -b` + `git push -u` + Web UI Merge）。
> 本节只讲 **5.0 没涵盖的扩展**：表单字段完整说明 + 创建 MR 的 4 种入口 + MR 默认分支选择策略。

#### 4 种入口

| 场景 | 入口 |
|------|------|
| **推完分支后 GitLab 弹提示** | `git push -u origin <branch>` 后看命令行输出的 "Create a pull request for..." 链接 |
| **项目菜单手动开** | `项目主页` → 顶部 **+** → **New merge request** |
| **Web IDE 直接开** | Web IDE 编辑器右上 `Source branch` → **Create merge request** |
| **Issue / Work item 直接开** | Issue 内关联 branch → 自动出 MR 创建按钮（5.3） |

#### 表单字段完整说明

| 字段 | 必填？ | 说明 |
|------|--------|------|
| **Title** | ✅ | MR 标题（默认取第一个 commit message） |
| **Description** | 推荐 | 用 Markdown 写改动说明；可加 task list（`- [ ]`） |
| **Source branch** | ✅ | 要合并的分支（如 `feature/greeting`） |
| **Target branch** | ✅ | 合到哪里（默认 `main`，**重要**：技术预览 MR 可选 `main` vs `release/x`） |
| **Assignee** | 可选 | 这个 MR 责任人（多人） |
| **Reviewer** | 可选 | 审查人（Premium/Ultimate 有多人并行 review + required reviewers） |
| **Milestone** | 可选 | 里程碑 |
| **Labels** | 可选 | 标签（多选） |
| **Merge options** | 可选 | squash / merge commit / rebase 三选一（默认 merge commit） |

创建后：CI 自动跑 → 审查 → 合并（详见 §5.2.4 高级玩法）。

#### 一句命令行开 MR（用 glab）

```bash
# 推完分支后
glab mr create --title "Add greeting doc" \
  --description "Adds GREETING.md with project intro" \
  --target-branch main
# 自动选 source branch = 当前分支
```

### 5.2.4 MR 高级玩法

| 功能 | 用法 |
|------|------|
| **Draft / WIP** | 标题前加 `Draft:` 或 `WIP:`，不会被合并 |
| **Squash commits** | 合并时把多个 commit 压成一个 |
| **Merge commit / Squash / Rebase** | 三种合并策略 |
| **Delete source branch** | 合并后自动删源分支 |
| **Linked issues** | 描述里写 `Closes #123` 合并时自动关 issue |
| **Code Owners** | `.gitlab/CODEOWNERS` 文件定义谁必须 review |
| **Approval rules** | Premium/Ultimate，要 N 人 approve 才能合 |
| **Merge trains** | Premium/Ultimate，排队合并避免相互冲突 |
| **Push rules** | Settings → Repository，限制 commit message 格式 |

### 5.2.5 解决冲突

`MR 页` → **Resolve conflicts** → Web IDE 或本地：

```bash
git checkout feature/login-page
git pull origin main
# 解决冲突文件
git add .
git commit -m "Resolve merge conflicts"
git push
```

## 5.3 Issue（[官方] /user/project/issues/）

### 5.3.1 创建一个 Issue

> 🌱 入门 · 5 分钟
>
> 💡 **从 0 走通全流程**：[§5.0.4](#504-建第一个-issue-本机验证) 已有 [本机验证] 步骤（顶菜单 → Work items → 填标题 → Create）。
> 本节只讲 **5.0 没涵盖的扩展**：表单字段完整说明 + GFM 描述模板 + 联动关闭 MR。

#### 表单字段完整说明

| 字段 | 必填？ | 说明 |
|------|--------|------|
| **Title** | ✅ | 一句话问题描述 |
| **Description** | 推荐 | Markdown / GFM；可加：复现步骤、期望行为、实际行为、版本、截图 |
| **Assignee** | 可选 | 责任人 |
| **Labels** | 可选 | 标签（多选：`bug` / `priority::high`） |
| **Milestone** | 可选 | 里程碑 |
| **Due date** | 可选 | 截止日期 |
| **Weight** | 可选 | 估时（数字，无单位；可点装备范围 [官方]） |
| **Confidential** | 可选 | 勾选对非成员隐藏（**安全敏感 issue 用**） |

填完后底部选项：Subscribe / Start typing or /spend 1h / Add weight。

#### GFM 描述模板示例（复制即可用）

```markdown
## 复现步骤
1. 打开 /login
2. 输入错误密码 3 次
3. 看到报错信息

## 期望
应该显示 "重试次数过多，请稍后再试"

## 实际
页面崩溃

## 环境
- 浏览器：Chrome 128
- OS：macOS 15.0
- GitLab 版本：19.1.1
```

#### 联动关闭（在 MR 描述里关联 Issue）

```markdown
Closes #123
# 或
Fixes #123
# 或
Resolves #123
```

MR 合并后这个 Issue 自动被关闭（关键字详见 [官方] /user/project/issues/issue_merge_requests/）

### 5.3.2 模板（Issue templates）

项目根目录建 `.gitlab/issue_templates/`：

```bash
mkdir -p .gitlab/issue_templates
cat > .gitlab/issue_templates/bug.md << 'EOF'
## Bug 报告

### 复现步骤
1. 
2. 
3. 

### 期望行为


### 实际行为


### 环境
- 浏览器：
- OS：
- 版本：
EOF
```

新建 Issue 时会自动出现 "Choose a template" 下拉。

### 5.3.3 Labels

`Issues` → **Labels**：

- 命名建议：`bug`、`enhancement`、`feature`、`docs`、`priority::high` 等
- 配合 scoped labels（`type::`、`priority::`）做过滤

### 5.3.4 Issue Boards（看板）

> 🌿 进阶 · 看板视图

![Issue Boards](images/gitlab-5.4-boards.png)
*图：项目 Boards 页（[本机验证] 实拍）。默认 3 列 Open / In Progress / Closed；卡片可拖到不同列；右上 + 新增列*

`项目菜单` → **Issues** → **Boards**：

类似 Trello/Kanban——默认列 `Open / In Progress / Closed`，可加自定义列。Issue 在列之间拖动改状态。

### 5.3.5 Milestones（里程碑）

`Issues` → **Milestones** → **New milestone**：

- 起止日期
- 关联 Issue
- 看进度条（已关闭 issue %）

![Milestones 列表](images/gitlab-5.6-milestones.png)
*图：项目 → 计划 → 里程碑 页（[本机验证] 实拍）。开放中/已关闭/全部三个标签页；右上 New milestone 创建；列表展示起止日期 + 进度条*

### 5.3.6 Epics（组层级，Premium+）

`Group` → **Epics** → **New epic**：

跨多个项目跟踪一个大主题。

## 5.4 规划工作（Planning，[官方] /user/get_started/get_started_planning_work/）

GitLab 12 个规划工具中，**本教程重点讲 5 个**（各项下指向具体子节）；剩余 7 个多需订阅层级，初学者不常用，列出 [官方] 路径供查阅。

### 本教程重点讲（5 个）

| 工具 | 用途 | 本教程哪里看 |
|------|------|--------------|
| **Issues** | 单个任务 | §5.3 |
| **Milestones** | 阶段性目标（带进度条） | §5.3.5 |
| **Epics**（Premium+） | 大主题跨项目 | §5.3.6 |
| **Issue Boards** | 可视化看板 | §5.3.4 |
| **Wikis** | 文档协作 | §5.6 |

### 其余 7 个（按需查阅官方）

| 工具 | 订阅层级 | [官方] 路径 |
|------|---------|-----------|
| **Iterations** (Sprint) | Premium+ | /user/iterations/ |
| **Tasks**（Issue 子任务） | Free | /user/tasks/ |
| **OKRs**（目标 + 关键结果） | Premium+ | /user/okrs/ |
| **Roadmaps**（时间线视图） | Premium+ | /user/group/roadmap/ |
| **Time tracking**（`/estimate` + `/spend`） | Free | /user/project/time_tracking/ |
| **Insights**（数据图表） | Free | /user/project/insights/ |
| **Requirements**（需求跟踪） | Premium+ | /user/project/requirements/ |

## 5.5 管理代码（[官方] /user/get_started/get_started_managing_code/）

完整工作流（[官方]）：

1. **创建仓库**（Project）→ 5.1
2. **写代码**：
   - Web Editor（编辑单个文件）
   - Web IDE（编辑多个文件，VS Code 内核）
   - 本地克隆 + IDE
   - Remote Workspaces（云端开发环境）
3. **保存并推送** → commit + push
4. **Code Review** → MR
5. **合并** → merge to default branch
6. **保护** → Protected branches + Code Owners

## 5.6 Wiki

> 🌿 进阶 · 文档协作

![Wiki 首页](images/gitlab-5.5-wiki.png)
*图：项目 Wiki 页（[本机验证] 实拍）。首页 `home` 可点编辑；右侧 Pages 列表；底部 Create your first page 入口*

`项目菜单` → **Wiki** → **Create your first page**：

- 每页是单独 Markdown
- 支持版本历史（看旧版本、对比 diff）
- 支持 Sidebar（在 `_sidebar.md`）

## 5.7 Snippet（代码片段共享）

> 🌿 进阶 · 个人/团队代码片段

![New Snippet](images/gitlab-5.7-snippet-new.png)
*图：New snippet 页（[本机验证] 实拍）。填 Title + 文件（多文件）+ Visibility + 选语言；下方 snippets editor 自动高亮*

`+` → **New snippet**：

- **Visibility**：Private / Internal / Public
- 支持多文件、语法高亮、评论

## 5.8 Release（[官方] /user/project/releases/）

> 🌿 进阶 · 发版本管理

![New Release 表单](images/gitlab-5.8-release-new.png)
*图：New release 页（[本机验证] 实拍）。基于 Git tag 创建；填 Title / Release notes（Markdown）；可上传 binary assets*

`项目菜单` → **Deployments** → **Releases** → **New release**：

- Tag（基于某个 Git tag）
- Release notes（Markdown）
- 关联 Milestone
- 上传二进制（assets）
- 可触发 release pipeline

## 5.9 Pages（静态站点，[官方] /user/project/pages/）

> 🌿 进阶 · 静态网站托管

#### 步骤

1. **根目录建 `.gitlab-ci.yml`**：

```yaml
pages:
  stage: deploy
  script:
    - mkdir .public
    - cp -r * .public
  artifacts:
    paths:
      - .public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

2. **推送到默认分支**（`main`）：

```bash
git add .gitlab-ci.yml
git commit -m "Add GitLab Pages"
git push origin main
```

3. **查看部署结果**：

- `项目菜单` → **Settings → Pages**（或 **Deployments → Pages**）看状态
- 默认 URL 形如 `http://<group>.example.com/<project>/`（**HTTPS 启用**后变 `https://`）
- Web IDE 改 HTML / Markdown 后 push，**30 秒内**自动重新部署

#### 限制 / 常见坑

- 例子里的 `.public` 是 CI 运行时建的，**项目里看不到**（是 artifact 路径）
- 需要 Runner（§6.5）才能跑 pipeline
- URL 的 `<group>.example.com` 是**外部 URL 的主机名**：本机部署（§3.2 默认）会变成 `http://root.localhost/<project>` 之类（看 §3.2 启动时 `--hostname` 怎么设）

## 5.10 容器 Registry + Package Registry（[官方] /user/packages/container_registry/）

> 🌿 进阶 · 镜像 / 包管理

![Package Registry](images/gitlab-5.10-packages.png)
*图：项目 Package registry 页（[本机验证] 实拍）。GitLab 19 把 Container Registry / Maven / NPM / PyPI / Conan / NuGet / Generic 等统一显示在 Packages 页*

每个项目自带一个 registry。

**默认 URL**：`<external_url 去掉 http(s):// 后前面加 registry.>`。按 §3.2 默认 Docker 部署（`http://localhost`），访问：

| 项目路径 | Registry URL |
|---------|--------------|
| 本机默认部署（Docker，localhost） | `registry.localhost:5000` |
| 带端口的（Omnibus 同端口） | `registry.example.com:5000` |

**登录 + 推送**（下面以本机 `registry.localhost:5000` 为例）：

```bash
# 1. 登录（用户名/密码走 GitLab 账号，不是 GitLab 密码）
docker login registry.localhost:5000
#   Username: root
#   Password: §5.0.5 创建的 PAT（**需要 read_repository + write_registry 两个 scope**）

# 2. 构建 + 推送
docker build -t registry.localhost:5000/mygroup/myproject/myimage:latest .
docker push registry.localhost:5000/mygroup/myproject/myimage:latest

# 3. 在 GitLab → Project → Packages → Container Registry 看刚才推的镜像
```

## 5.11 命令行工具：`glab`（[官方]）

> 🌿 进阶 · 终端党

![glab 项目页](images/gitlab-5.11-glab-install.png)
*图：GitLab.com 的 glab 项目页（[本机验证] 实拍）。glab 是 GitLab 官方 CLI；安装文档 + release 包都在这个项目*

[GitLab CLI](https://gitlab.com/gitlab-org/cli)：

```bash
# 安装
# macOS: brew install glab
# Windows: winget install glab
# Linux: 见官方 install 指南

# 登录（本机部署）
glab auth login --hostname localhost

# 常用命令
glab issue list                           # 看 issue
glab issue create --title "Bug" --description "..."   # 创建 issue
glab mr list                              # 看 MR
glab mr create --title "..." --description "..." --target-branch main
glab mr checkout 123                      # 切到 MR 的分支
glab pipeline list                        # 看 CI pipeline
glab ci status                            # 看当前 pipeline 状态
glab api /projects                        # 调 GitLab API
glab repo clone mygroup/myproject         # 克隆项目
```

> 本机未装 glab（[本机未验证]），命令来自 [官方] 文档。



---

# 06 · CI/CD {#ch06}

> **核心**：[官方] /ci/quick_start/ 是最快上手路径，本章基于它扩展。

## 6.1 核心概念

| 术语 | 含义 |
|------|------|
| **Pipeline** | 一次提交触发的一整套流程 |
| **Stage** | 阶段，按顺序执行（如 build → test → deploy） |
| **Job** | 阶段里的一个具体任务（每个 job 独立 runner） |
| **Runner** | 跑 job 的 agent 进程（独立机器上） |
| **`.gitlab-ci.yml`** | 项目根的 YAML 配置，定义 pipeline |
| **Artifact** | job 跑完产出的文件（可下载、可在后续 job 用） |
| **Cache** | 跨 job 复用的临时文件（依赖、构建缓存） |

## 6.2 第一个 Pipeline（[官方] /ci/quick_start/）

### 6.2.1 GitLab.com 用户

直接跳到 6.2.3——GitLab.com 自带 instance runner，不用装 Runner。

### 6.2.2 自管 GitLab 用户

先确认有 Runner：`Settings` → **CI/CD** → **Runners** 展开：

- ✅ 有绿色圆圈 + `active` → 可以直接用
- ❌ 没 Runner → 见 6.5 节安装 Runner

### 6.2.3 写 .gitlab-ci.yml

项目根目录新建 `.gitlab-ci.yml`：

```yaml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  environment: production
```

> ⚠️ `.gitlab-ci.yml` 缩进和空格敏感，用**空格缩进，不要 tab**（[官方]）。

提交后自动触发 pipeline。

### 6.2.4 看 Pipeline 状态

![Pipelines 列表](images/gitlab-6.1-pipelines-list.png)
*图：项目 Pipelines 页（[本机验证] 实拍）。列表显示每次 commit 触发的 pipeline 状态（pending/running/passed/failed）；点击看 stages / jobs 详情*

`项目菜单` → **Build** → **Pipelines**：

- 列表：所有 pipeline
- 单个 pipeline ID：阶段流程图
- 单个 job：详细日志

### 6.2.5 Pipeline Editor

![Pipeline Editor](images/gitlab-6.2-ci-editor.png)
*图：项目 CI/CD Editor（[本机验证] 实拍）。左侧 YAML 编辑器，右侧实时模拟 pipeline 结构（stages / jobs 树）；下方 Lint 按钮校验语法*

`项目菜单` → **Build** → **Pipeline editor**：

- 浏览器内编辑 .gitlab-ci.yml
- **Lint** 按钮验证语法
- 自动 commit 到当前分支

## 6.3 YAML 关键字速查（[官方] /ci/yaml/）

### 6.3.1 全局 / job 通用

```yaml
default:
  image: alpine:latest          # 默认所有 job 用的 Docker 镜像
  before_script:                # job 跑前先执行
    - apt-get update
  after_script:                 # job 跑后执行（即使失败）
    - echo "cleanup"

# 单 job
my-job:
  stage: test                  # 阶段
  image: node:20               # 单 job 的镜像（覆盖 default）
  tags:                        # 指定 runner tag
    - docker
  rules:                       # 触发条件
    - if: $CI_COMMIT_BRANCH == "main"
  needs: ["other-job"]         # 不按 stage 顺序，提早跑
  allow_failure: true          # 失败不算 pipeline 失败
  retry:
    max: 2
    when: runner_system_failure
  timeout: 30 minutes          # 超时
  parallel: 5                  # 并行跑 5 个
```

### 6.3.2 关键关键字

| 关键字 | 用途 |
|--------|------|
| `stages` | 自定义阶段顺序 |
| `stage` | job 所属阶段 |
| `script` | 必填，跑的命令 |
| `before_script` / `after_script` | 跑前/跑后 |
| `image` | Docker 镜像 |
| `services` | 伴随容器（数据库等） |
| `tags` | runner 标签筛选 |
| `rules` | 触发条件（推荐用 rules 不用 only/except） |
| `needs` | DAG 依赖 |
| `dependencies` | 引用其他 job 的 artifact |
| `artifacts` | 产出文件 |
| `cache` | 跨 job 缓存 |
| `variables` | job 级环境变量 |
| `environment` | 关联部署环境 |
| `coverage` | 解析测试覆盖率 |
| `trigger` | 触发下游 pipeline |
| `include` | 复用 YAML 片段 |
| `extends` | 继承另一个 job 配置 |

### 6.3.3 完整示例

```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: registry.example.com/mygroup/myproject

# 公共 job（被 extends 用）
.base:
  before_script:
    - apt-get update -qq
    - apt-get install -y -qq curl

# 真实 job
build:
  extends: .base
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker build -t $DOCKER_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $DOCKER_IMAGE:$CI_COMMIT_SHORT_SHA
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

test:
  stage: test
  image: alpine:3.20
  script:
    - echo "running tests"
    - apk add --no-cache curl
    - curl --version
  coverage: '/Coverage: \d+\.\d+/'

deploy:
  stage: deploy
  image: alpine:3.20
  script:
    - echo "deploy $DOCKER_IMAGE:$CI_COMMIT_SHORT_SHA to production"
  environment:
    name: production
    url: https://example.com
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  when: manual  # 手动点才跑
```

## 6.4 预定义变量（[官方] /ci/variables/predefined_variables/）

| 变量 | 含义 |
|------|------|
| `$CI_COMMIT_REF_NAME` | 当前分支或 tag 名 |
| `$CI_COMMIT_SHORT_SHA` | commit 短 hash |
| `$CI_COMMIT_BRANCH` | 分支名 |
| `$CI_PROJECT_DIR` | 仓库根目录 |
| `$CI_PIPELINE_ID` | pipeline 编号 |
| `$CI_JOB_ID` / `$CI_JOB_NAME` | job 编号 / 名称 |
| `$GITLAB_USER_LOGIN` | 触发者用户名 |
| `$CI_REGISTRY` / `$CI_REGISTRY_IMAGE` | 容器 registry 地址 / 项目镜像路径 |
| `$CI_DEFAULT_BRANCH` | 默认分支（main） |

## 6.5 GitLab Runner（[官方] /runner/install/）

![Admin Runners](images/gitlab-6.3-runners.png)
*图：Admin → Runners 页（[本机验证] 实拍）。注册到实例的 Runner 列表；每条显示状态 / 标签 / executor 类型 / 上次联系时间*

### 6.5.1 Runner 是什么 & 架构位置

> 📘 **Runner 的定义、与 GitLab 的关系、3 scope 总览 → [§2.5](#ch02)** 已讲过，本节不重复。
>
> 本节聚焦**安装 + 注册 + 配置**的实战步骤。

**简述**：Runner 是独立进程，跑 CI 任务的 agent。**GitLab 服务端不自带 Runner**（GitLab.com 用户除外，[官方] /ci/quick_start/）。

### 6.5.2 Runner 三种 scope

| 类型 | 谁能用 |
|------|--------|
| **Instance runner** | 整个实例所有项目 |
| **Group runner** | 组内所有项目 |
| **Project runner**（specific runner） | 单个项目 |

### 6.5.3 Runner 安装（Linux，[官方] /runner/install/linux-repository/）

```bash
# 加仓库（Ubuntu/Debian）
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash

# 装包
sudo apt install gitlab-runner

# 注册 Runner（交互式）
sudo gitlab-runner register

# 提示输入：
#   GitLab instance URL:  https://gitlab.example.com/
#   Registration token:   从 GitLab UI 拿（Admin → Runners，或 Group → Runners，或 Project → Settings → CI/CD → Runners）
#   Description:          my-runner-01
#   Tags:                 docker,linux   （逗号分隔）
#   Optional maintenance note:
#   Executor:             docker          （或 shell、kubernetes、virtualbox 等）
#   Default Docker image: alpine:latest
```

注册完会生成 `/etc/gitlab-runner/config.toml`。

```bash
# 看 Runner 状态
sudo gitlab-runner list
sudo gitlab-runner status
sudo gitlab-runner verify

# 看日志
sudo journalctl -u gitlab-runner -f
```

### 6.5.4 Runner on Windows（[官方] /runner/install/windows/）

```powershell
# 用 Chocolatey 或手动下载 exe
choco install gitlab-runner

# 注册成 Windows service
gitlab-runner.exe register
gitlab-runner.exe install
gitlab-runner.exe start
```

### 6.5.5 Runner on Docker（[官方] /runner/install/docker/）

```bash
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

### 6.5.6 Runner Executor 类型

| Executor | 说明 | 隔离性 |
|----------|------|--------|
| **shell** | 直接在 Runner 机器上跑命令 | ❌ 无 |
| **docker** | 每个 job 一个新容器 | ✅ |
| **docker+machine** | 自动扩缩容（云上） | ✅ |
| **kubernetes** | 每个 job 一个 K8s pod | ✅✅ |
| **ssh** | 通过 SSH 到远程机器跑 | ❌ |
| **virtualbox / Parallels** | 跑在 VM | ✅ |
| **custom** | 自己写 executor | 自定义 |

> **生产推荐**：docker 或 kubernetes executor。

### 6.5.7 关键 config.toml 配置（docker executor）

> 💡 本教程以本机 Docker 部署为案例——`url` 写 `http://localhost`。生产域部署时换 `https://gitlab.example.com/` 即可。

```toml
# /etc/gitlab-runner/config.toml
concurrent = 4   # 最多同时跑 4 个 job

[[runners]]
  name = "docker-runner"
  url = "http://localhost/"      # 本机部署用 http://localhost；生产域名改 https://gitlab.example.com/
  token = "glrt-xxx"             # 从注册时拿的 token，写这里
  executor = "docker"
  [runners.docker]
    image = "alpine:latest"
    privileged = false
    volumes = ["/cache"]
    pull_policy = "if-not-present"
    network_mode = "bridge"
    shm_size = 0
  [runners.cache]                # 默认本地卷缓存；需要 S3/GCS/Azure 看 [官方] /runner/configuration/advanced-configuration/#the-runners-cache-section
    Type = "volume"

```

修改后：

```bash
sudo gitlab-runner restart
```

## 6.6 制品（Artifacts，[官方] /ci/yaml/#artifacts）

> 🌿 进阶 · 产物存储

```yaml
build:
  stage: build
  script:
    - make build
  artifacts:
    paths:
      - dist/
    expire_in: 1 week     # 1 周后自动清理
    name: "$CI_JOB_NAME-$CI_COMMIT_SHORT_SHA"
```

下载：Pipeline → Job → 右侧 **Download** 按钮

在后续 job 用：

```yaml
deploy:
  stage: deploy
  script:
    - ls -la dist/    # build job 的 artifact 自动可用
  dependencies:
    - build
```

> `dependencies` 缺省会拿**所有前序 job** 的 artifact，显式声明节省空间。

## 6.7 缓存（Cache，[官方] /ci/yaml/#cache）

> 🌿 进阶 · 提速

```yaml
build:
  cache:
    key: ${CI_COMMIT_REF_SLUG}    # 按分支缓存
    paths:
      - node_modules/
      - .cache/
    policy: pull-push             # 默认；可设 push（只写）或 pull（只读）
```

artifact vs cache：

| | artifact | cache |
|--|---------|-------|
| **作用** | 传递构建产物给后续 job | 加速重复构建 |
| **可见** | Pipeline UI 可下载 | 不可见 |
| **保留** | 可配 expire_in | 默认 job 后删 |

## 6.8 变量与机密（[官方] /ci/variables/）

> 🌳 高级 · 密钥管理

### 6.8.1 三种 scope

| Scope | 在哪设 | 谁能改 |
|-------|--------|--------|
| **Instance** | Admin → Settings → CI/CD → Variables | 管理员 |
| **Group** | Group → Settings → CI/CD → Variables | Maintainer+ |
| **Project** | Project → Settings → CI/CD → Variables | Maintainer+ |
| **Job** | .gitlab-ci.yml 的 `variables:` 关键字 | 任何人 |
| **Pipeline** | 手动 / API 触发时传 | 触发者 |

### 6.8.2 Protected / Masked

UI 加变量时勾选：
- **Protect variable**：只在受保护分支/tag 上可用
- **Mask variable**：日志里会变成 `**********`（防密码泄漏到日志）

> ⚠️ **Mask 限制**：必须是 Base64 / 单 token 不能包含特殊字符匹配规则，否则会被完全 mask 掉无法用。

### 6.8.3 在 job 里用

```yaml
deploy:
  script:
    - echo "Token is $DEPLOY_TOKEN"   # 自动展开
    - curl -H "Authorization: Bearer $DEPLOY_TOKEN" https://api.example.com/deploy
```

## 6.9 多项目 Pipeline（[官方] /ci/pipelines/downstream_pipelines/）

> 🌳 高级 · 跨项目编排

触发子 pipeline：

```yaml
trigger-downstream:
  stage: deploy
  trigger:
    project: mygroup/subproject
    branch: main
    strategy: depend
```

父项目用子项目的产物（multi-project pipeline artifacts）：

```yaml
needs:
  - project: mygroup/shared-lib
    job: build
    ref: main
    artifacts: true
```

## 6.10 父子 Pipeline 复用（[官方] /ci/pipelines/parent_child_pipelines/）

> 🌳 高级 · 拆 job 复用

把多个 job 拆成多个 YAML 文件：

```yaml
# .gitlab-ci.yml（父）
include:
  - local: 'ci/build.yml'
  - local: 'ci/test.yml'
  - local: 'ci/deploy.yml'
```

子 YAML 文件用 `trigger: include` 触发：

```yaml
# ci/deploy.yml
deploy-staging:
  stage: deploy
  trigger:
    include: deploy/staging.yml
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

## 6.11 调度 Pipeline（Scheduled pipeline）

`Project` → **Build** → **Pipeline schedules** → **New schedule**：

- Cron 表达式
- 目标分支
- 变量覆盖
- 时区

## 6.12 Container Registry 与 CI 集成

> 🌳 高级 · Registry 集成

GitLab CI 内置 `$CI_REGISTRY_IMAGE` 变量指向项目镜像路径：

```yaml
build-image:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
```

`$CI_REGISTRY_USER` / `$CI_REGISTRY_PASSWORD` 是 GitLab CI 自动提供的内置变量。

---

# 07 · 安全扫描（Application Security Testing） {#ch07}

> GitLab 内置安全扫描 **强烈依赖订阅层级**：[官方] /user/application_security/

## 7.1 订阅层级对照（[官方]）

| 扫描类型 | Free | Premium | Ultimate |
|---------|------|---------|----------|
| **Secret Detection**（密钥检测） | ✅ | ✅ | ✅ |
| **Dependency Scanning**（依赖扫描） | ✅* | ✅ | ✅ |
| **Container Scanning**（容器镜像扫描） | ✅* | ✅ | ✅ |
| **SAST**（静态分析） | ❌ | ❌ | ✅ |
| **DAST**（动态分析） | ❌ | ❌ | ✅ |
| **Fuzz Testing**（模糊测试） | ❌ | ❌ | ✅ |
| **API Fuzzing** | ❌ | ❌ | ✅ |
| **Coverage-guided Fuzz Testing** | ❌ | ❌ | ✅ |
| **License Compliance** | ❌ | ✅ | ✅ |
| **IaC Scanning** | ✅* | ✅ | ✅ |
| **Compliance Pipelines** | ❌ | ❌ | ✅ |

\* Free 层有，但默认不开或有限制。

## 7.2 安全扫描工作流（[官方] /user/application_security/）

> 🌳 高级 · 安全 DevOps

![DevOps Adoption 不可用](images/gitlab-7.3-devops-adoption.png)
*图：[本机验证] CE 版访问 `/admin/devops_adoption` 返回 404 —— DevOps Adoption 报告是 **GitLab Ultimate / Enterprise** 专属功能（[官方] /admin/devops_adoption/），CE / Premium 没有。这是真实现状截图，提示升级。*

GitLab 把安全工具链整合成一条流水线，跟 CI 一起跑：

```
Detect → Triage → Analyze → Remediate
   ↑                                ↓
   └────── Optimize ←───────────────┘
```

- **Detect**：CI/CD 自动跑
- **Triage**：在 MR 和 Vulnerability Report 里看
- **Analyze**：看详情、查影响范围
- **Remediate**：改代码、关 issue
- **Optimize**：调规则减少误报

## 7.3 开启安全扫描（最简方法：[官方]）

> 🌳 高级 · 开安全扫描

### 7.3.1 用 Auto DevOps 模板（最快）

`Project` → **Settings** → **CI/CD** → **Security scanning** → 勾选要开的扫描

或者在 `.gitlab-ci.yml` 里 include 官方模板：

```yaml
include:
  - template: Jobs/SAST.gitlab-ci.yml
  - template: Jobs/Secret-Detection.gitlab-ci.yml
  - template: Jobs/Dependency-Scanning.gitlab-ci.yml
  - template: Jobs/Container-Scanning.gitlab-ci.yml
```

> 💡 GitLab 14.6+ 用 `Jobs/SAST.gitlab-ci.yml` 新路径（旧 `Security/SAST.gitlab-ci.yml` 仍可用，但新部署推荐 `Jobs/`）。本教程统一用 `Jobs/`。

GitLab 官方模板位置：[gitlab-org/gitlab/-/tree/main/lib/gitlab/ci/templates/Jobs](https://gitlab.com/gitlab-org/gitlab/-/tree/main/lib/gitlab/ci/templates/Jobs)

### 7.3.2 完整示例（开 5 种扫描）

```yaml
# .gitlab-ci.yml

stages:
  - test
  - scan
  - build

# 1. SAST（静态分析）
include:
  - template: Jobs/SAST.gitlab-ci.yml

# 2. Secret Detection（密钥）
  - template: Jobs/Secret-Detection.gitlab-ci.yml

# 3. Dependency Scanning（依赖漏洞）
  - template: Jobs/Dependency-Scanning.gitlab-ci.yml

# 4. Container Scanning（容器镜像）
  - template: Jobs/Container-Scanning.gitlab-ci.yml

# 5. IaC Scanning（基础设施即代码）
  - template: Jobs/IaC-Scanning.gitlab-ci.yml

# 跑 SAST 阶段
sast:
  stage: scan
  variables:
    SAST_EXCLUDED_PATHS: "spec, test, tests, tmp, node_modules"
```

## 7.4 各扫描详解

> 🌳 高级 · 7 种扫描器

### 7.4.1 Secret Detection（密钥检测，[官方] /user/application_security/secret_detection/）

**功能**：扫代码里有没有泄露的密钥（API key、私钥、token、密码）。

支持的密钥类型：AWS、GCP、Azure、GitHub PAT、Slack token、数据库连接串、私钥等几十种。

**触发**：

```yaml
include:
  - template: Jobs/Secret-Detection.gitlab-ci.yml
```

**查看结果**：`Project` → **Secure** → **Vulnerability report**

### 7.4.2 Dependency Scanning（依赖扫描，[官方] /user/application_security/dependency_scanning/）

**功能**：扫 `package.json`、`requirements.txt`、`pom.xml`、`Gemfile.lock`、`go.mod` 等依赖文件，看有没有已知漏洞（CVE）。

**支持语言**：
- JavaScript / Node.js
- Python
- Java / Scala
- Ruby
- Go
- PHP
- .NET
- Rust（部分）
- C/C++（部分）

**触发**：

```yaml
include:
  - template: Jobs/Dependency-Scanning.gitlab-ci.yml
```

可生成 SBOM（Software Bill of Materials，软件物料清单）——CycloneDX 格式。

### 7.4.3 Container Scanning（容器镜像扫描，[官方] /user/application_security/container_scanning/）

**功能**：扫 Docker 镜像里的 OS 包和语言库漏洞。

```yaml
include:
  - template: Jobs/Container-Scanning.gitlab-ci.yml

container_scanning:
  variables:
    CS_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
    # 或指定其他镜像: CS_IMAGE: alpine:3.20
```

底层用 [Trivy](https://github.com/aquasecurity/trivy) 或 [Grype](https://github.com/anchore/grype)。

### 7.4.4 SAST（静态分析，[官方] /user/application_security/sast/）

**功能**：扫源码里潜在漏洞（SQL 注入、XSS、命令注入、路径遍历、硬编码凭证、不安全反序列化等）。

**支持语言**：
- C/C++
- C#
- Go
- Java / Kotlin / Scala
- JavaScript / TypeScript
- Python
- Ruby
- PHP
- Swift

**触发**：

```yaml
include:
  - template: Jobs/SAST.gitlab-ci.yml
```

### 7.4.5 DAST（动态分析，[官方] /user/application_security/dast/）

**功能**：跑起来后模拟攻击，扫运行时漏洞。

**特点**：
- 需要应用**部署到测试环境**才能扫
- 跑时间长
- Ultimate 才能用

```yaml
include:
  - template: Jobs/DAST.gitlab-ci.yml

dast:
  variables:
    DAST_TARGET_URL: "https://staging.example.com"
    DAST_AUTH_USERNAME: "test-user"
    DAST_AUTH_PASSWORD: "$DAST_TEST_PASSWORD"   # 用 protected/masked 变量
```

### 7.4.6 IaC Scanning（[官方] /user/application_security/iac_scanning/）

**功能**：扫 Terraform/Ansible/Kubernetes manifests 里的错误配置。

```yaml
include:
  - template: Jobs/IaC-Scanning.gitlab-ci.yml
```

检测项：S3 bucket 公开、SSH 0.0.0.0/0、密码硬编码、缺失加密等。

### 7.4.7 License Compliance（[官方] /user/application_security/license_compliance/）

**功能**：扫依赖用了什么开源许可证，告诉你是否有 GPL 等强传染协议。

Premium+ 功能。

## 7.5 在 MR 里看扫描结果

提交 MR → GitLab 自动跑扫描 → 结果在 MR 页面 **Security** 标签显示：

- 🔴 **Critical / High**：必须修
- 🟡 **Medium**：建议修
- 🟢 **Low**：可选

在 MR 里加 comments、讨论、关掉误报。

## 7.6 Vulnerability Report

`Project` → **Secure** → **Vulnerability report`：

- 按严重程度、扫描器、状态过滤
- **状态**：Detected / Confirmed / Dismissed / Resolved
- **Dismiss reason**：Acceptable risk / False positive / Used in tests / Mitigated

## 7.7 安全策略（Policies，Premium+，[官方] /user/application_security/policies/）

`Secure` → **Policies**：

- **Scan Execution Policy**：强制某些项目必须跑哪些扫描
- **Merge Request Approval Policy**：MR 必须 X 人 approve 才能合
- **Pipeline Execution Policy**：强制注入特定 CI 阶段

## 7.8 合规框架（Compliance Frameworks，Ultimate，[官方] /user/group/compliance_frameworks/）

把组打上合规标签（如 `SOC 2`、`ISO 27001`），组内项目自动套上对应合规策略。

## 7.9 离线 / 私有部署的安全扫描

[官方] /user/application_security/offline_deployments/：

- Self-Managed Ultimate 默认连 GitLab 漏洞数据库
- 离线环境要 [镜像漏洞数据库](https://docs.gitlab.com/user/application_security/offline_deployments/) 到内网

## 7.10 实战：把安全扫描加进现有 pipeline

现有 pipeline 改 3 处：

```yaml
# 1. 加 stage
stages:
  - build
  - test
  - scan         # ← 加这个
  - deploy

# 2. include 模板
include:
  - template: Jobs/SAST.gitlab-ci.yml
  - template: Jobs/Secret-Detection.gitlab-ci.yml
  - template: Jobs/Dependency-Scanning.gitlab-ci.yml

# 3. （可选）SAST 排除路径
variables:
  SAST_EXCLUDED_PATHS: "spec, test, tests, tmp, node_modules"
  DS_EXCLUDED_PATHS: "spec, test, tests, tmp, node_modules, public"
```

第一次跑可能很慢（要拉 analyzer 镜像），跑过就快了。

## 7.11 收尾：风险降级与例外

发现漏洞但暂时没法修？两种处理：

**方式 1：在 UI 里 Dismiss**

`Secure` → **Vulnerability report** → 选中 → **Dismiss** → 选原因

**方式 2：用 .gitlab/severity_override.yml 永久压制**

```yaml
# .gitlab/severity_override.yml
# 格式: 漏洞ID: 新严重度
# 但 ID 通常是动态的，实用的是用 paths:
package-1:
  paths:
    - "node_modules/some-lib/**"
  severity: low
```

详见 [官方] /user/application_security/vulnerabilities/severity/。

---

# 08 · 运维：备份、升级、监控、故障排查 {#ch08}

> 全部基于 [官方] 文档。Omnibus 默认已经做了很多运维工作，但要按生产标准走还得手动配。

## 8.1 备份（[官方] /omnibus/settings/backups/）

### 8.1.1 两类备份

| 类型 | 命令 | 内容 |
|------|------|------|
| **应用备份**（`gitlab-backup`） | 仓库、DB、CI 数据、LFS、制品、Container Registry | GitLab 业务数据 |
| **配置备份**（`gitlab-ctl backup-etc`） | `/etc/gitlab/` 目录 | gitlab.rb + gitlab-secrets.json + SSL 证书 |

> ⚠️ **关键**：`gitlab-secrets.json` 包含 2FA 加密密钥、CI secure variables。**丢了这个文件 = 全部 2FA 用户锁死 + CI 密钥失效**。必须异地备份。

### 8.1.2 应用备份（Omnibus）

```bash
# 手动备份（备份到 /var/opt/gitlab/backups/）
sudo gitlab-backup create

# 默认会跳过某些目录（看日志），用 BACKUP= 跳过额外目录
sudo gitlab-backup create SKIP=tar

# 改备份路径
# /etc/gitlab/gitlab.rb
# gitlab_rails['backup_path'] = '/mnt/backups'
# gitlab_rails['backup_archive_permissions'] = 0644
# gitlab_rails['backup_keep_time'] = 604800   # 保留 7 天（秒）
```

### 8.1.3 配置备份

```bash
# 备份 /etc/gitlab/ 到 /etc/gitlab/config_backup/
sudo gitlab-ctl backup-etc

# 自定义路径
sudo gitlab-ctl backup-etc --backup-path /secret/gitlab/backups/

# 清理旧配置备份（按 backup_keep_time）
sudo gitlab-ctl backup-etc --delete-old-backups
```

### 8.1.4 自动备份（cron）

[官方] /omnibus/settings/backups/ 推荐：

```bash
sudo crontab -e -u root
```

```cron
# 每天凌晨 2 点跑应用备份 + 保留 7 天
0 2 * * * /opt/gitlab/bin/gitlab-backup create CRON=1 SKIP=tar

# 每天凌晨 4 点跑配置备份（保留 7 天）
15 4 * * 2-6 /opt/gitlab/bin/gitlab-ctl backup-etc && cd /etc/gitlab/config_backup && cp $(ls -t | head -n1) /secret/gitlab/backups/
```

### 8.1.5 备份传到异地

```bash
# 用 rsync 推送到异地
0 3 * * * rsync -avz /var/opt/gitlab/backups/ backup-server:/backups/gitlab/

# 或用 rclone 推到对象存储（S3 / MinIO）
0 3 * * * rclone sync /var/opt/gitlab/backups/ s3:my-bucket/gitlab/
```

### 8.1.6 Docker 部署备份

```bash
# 应用备份（容器内执行）
docker exec -t <container-name> gitlab-backup create

# 配置备份
docker exec -t <container-name> /bin/sh -c 'gitlab-ctl backup-etc && cd /etc/gitlab/config_backup && cp $(ls -t | head -n1) /secret/gitlab/backups/'

# 备份目录必须是挂载的 volume，否则容器重启就丢
```

### 8.1.7 恢复（[官方] /administration/backup_restore/restore_gitlab/）

```bash
# 1. 停服务（避免恢复时还在写入）
sudo gitlab-ctl stop puma
sudo gitlab-ctl stop sidekiq

# 2. 恢复（BACKUP= 是时间戳，不带 _gitlab_backup.tar）
sudo gitlab-backup restore BACKUP=1700000000_2024_01_01_12.0.0

# 3. 恢复配置文件
sudo mv /etc/gitlab /etc/gitlab.bak
sudo tar -xf gitlab_config_*.tar -C /
sudo gitlab-ctl reconfigure
sudo gitlab-ctl restart
sudo gitlab-rake gitlab:check

# 4. 验证
sudo gitlab-rake gitlab:check SANITIZE=true
```

> ⚠️ **恢复只能在相同或更新的 GitLab 版本上做**——降级恢复通常不行。

## 8.2 升级

### 8.2.1 版本升级策略（[官方]）

GitLab 采用 **Y 模式版本号**（如 `17.5.3`）：

- `<major>.<minor>.<patch>`
- 每月发布一个 minor 版本
- **每个 minor 版本只支持到下一个月 minor 发布 + 1 个月**
- 强烈建议**永远升到最新 minor**

**升级路径**：
- 同一 minor 内（如 `17.5.0` → `17.5.3`）：直接升
- 跨 minor（如 `17.5` → `17.8`）：必须按顺序逐个 minor 升，**不能跳**
- 跨 major（如 `17.x` → `18.x`）：同样逐个 minor 升到当前 major 最后一个，再升下一个 major 的第一个 minor

[官方] 升级路径表：<https://docs.gitlab.com/update/#upgrade-paths>

### 8.2.2 Omnibus 升级

```bash
# 1. 先备份（铁律：升之前必备份）
sudo gitlab-backup create
sudo gitlab-ctl backup-etc

# 2. 看官方升级路径（按 minor 走）
# https://docs.gitlab.com/update/#upgrade-paths

# 3. Ubuntu
sudo apt update
sudo apt install gitlab-ce

# RHEL
sudo dnf update gitlab-ce

# 4. 自动 reconfigure（包升级时会自动跑）
# 如果没自动跑：
sudo gitlab-ctl reconfigure

# 5. 验证
sudo gitlab-rake gitlab:check
sudo gitlab-rake gitlab:env:info
```

### 8.2.3 Docker 升级

```bash
# 1. 备份
docker exec -t <container> gitlab-backup create

# 2. 改 docker-compose.yml 的 image tag
# image: gitlab/gitlab-ce:19.1.1-ce.0  # ← 新版本（CE 版，不是 EE；要 EE 版换成 gitlab/gitlab-ee:VERSION-ee.0）

# 3. 拉新镜像 + 重启
docker compose pull
docker compose up -d

# 4. 验证
docker exec -t <container> gitlab-rake gitlab:check
```

### 8.2.4 Helm 升级

```bash
# 1. 备份（Helm 部署的备份命令不同）
# https://docs.gitlab.com/charts/backup-restore/

# 2. 升级
helm upgrade --install gitlab gitlab/gitlab \
  --version <new-version> \
  -f values.yaml

# 3. 看升级状态
kubectl get pods -n gitlab
helm status gitlab -n gitlab
```

## 8.3 监控（[官方] /administration/monitoring/）

### 8.3.1 Prometheus + Grafana（Omnibus 自带）

Omnibus GitLab 默认开启 Prometheus 监控：

```ruby
# /etc/gitlab/gitlab.rb
prometheus_monitoring['enable'] = true
grafana['enable'] = true

# 暴露 Prometheus
prometheus['listen_address'] = '0.0.0.0:9090'
```

访问：
- Prometheus: `http://gitlab.example.com:9090`
- Grafana: `http://gitlab.example.com:3000`（默认账号 `admin`，密码在 `/etc/gitlab/initial_root_password` 或 gitlab.rb 的 `grafana['admin_password']`）

### 8.3.2 关键 Metrics

| Metric | 看什么 |
|--------|--------|
| `gitlab_transaction_duration_seconds` | 请求响应时间 |
| `sidekiq_jobs_processed_total` | Sidekiq 任务处理速度 |
| `pg_stat_activity_count` | 数据库连接数 |
| `gitlab_cache_operation_duration_seconds` | Redis 缓存命中率 |
| `puma_threads_running` / `puma_threads_max` | Puma 线程池使用 |

### 8.3.3 告警规则

Prometheus alerting rules 配置在 `/etc/gitlab/gitlab-prometheus/alerts/*.yml`，关键告警：

- Sidekiq 队列堆积 > N
- Puma 线程池耗尽
- 数据库连接耗尽
- 磁盘空间 < 10%
- GitLab Rails 5xx 错误率上升
- Gitaly RPC 超时

### 8.3.4 导出 metrics 到外部 Prometheus

```ruby
# /etc/gitlab/gitlab.rb
prometheus['monitor_kubernetes'] = false   # 关闭 K8s 自动发现（如果是 VM 部署）
```

然后用联邦 Prometheus 抓取 `http://gitlab:9090/federate`。

## 8.4 健康检查

### 8.4.1 gitlab:check（Rake task）

```bash
sudo gitlab-rake gitlab:check
# 输出会扫：GitLab Shell、GitLab Workhorse、Sidekiq、Puma、PostgreSQL、Redis、Gitaly 等等
```

### 8.4.2 gitlab:env:info

```bash
sudo gitlab-rake gitlab:env:info
# 看环境信息（版本、组件版本、配置）
```

### 8.4.3 gitlab:doctor

```bash
sudo gitlab-rake gitlab:doctor
# 深入诊断，会问一堆 y/n
```

### 8.4.4 README 探针

GitLab 自带 `/-/readiness` 和 `/-/liveness` 端点（[官方] /user/admin_area/monitoring/health_check/）：

```bash
curl http://gitlab.example.com/-/readiness
curl http://gitlab.example.com/-/liveness
curl http://gitlab.example.com/-/health
```

K8s 探针：

```yaml
livenessProbe:
  httpGet:
    path: /-/liveness
    port: http
  initialDelaySeconds: 300
  periodSeconds: 15

readinessProbe:
  httpGet:
    path: /-/readiness
    port: http
  initialDelaySeconds: 60
  periodSeconds: 10
```

## 8.5 故障排查（[官方] /administration/troubleshooting/）

### 8.5.1 看日志

```bash
# Omnibus 集中日志位置
/var/log/gitlab/                              # 主日志目录
/var/log/gitlab/gitlab-rails/production.log   # Rails 应用日志（最常用）
/var/log/gitlab/nginx/                        # Nginx 日志
/var/log/gitlab/sidekiq/current               # Sidekiq 日志
/var/log/gitlab/postgresql/                   # PG 日志
/var/log/gitlab/redis/current                 # Redis 日志
/var/log/gitlab/gitaly/current                # Gitaly 日志
/var/log/gitlab/prometheus/current            # Prometheus 日志
```

```bash
# 实时 tail
sudo gitlab-ctl tail                          # 所有
sudo gitlab-ctl tail nginx                    # 单个组件
sudo gitlab-ctl tail sidekiq
```

### 8.5.2 常见问题

**1) "We're sorry, but something went wrong" 白页**

```bash
sudo gitlab-ctl tail gitlab-rails/production
# 通常看 JS 编译错误、worker timeout、PG/Redis 连接错误
```

**2) Sidekiq 队列堆积**

```bash
# 看队列状态
sudo gitlab-rails runner "Sidekiq::Queue.all.each { |q| puts \"#{q.name}: #{q.size}\" }"

# 看 stuck jobs
sudo gitlab-rails runner "puts Sidekiq::Workers.new.each.sum { |_p, ps| ps['stuck'] }.size"

# 重启 Sidekiq
sudo gitlab-ctl restart sidekiq
```

**3) gitlab-rake gitlab:check 报错**

输出会具体提示哪个组件失败，看对应章节排查。

**4) Gitaly 慢 / 卡**

```bash
# 看 Gitaly 日志
sudo gitlab-ctl tail gitaly

# 检查仓库是否在 NFS 上（极差性能）
mount | grep git

# 检查 Gitaly storage 路径
cat /etc/gitlab/gitlab.rb | grep git_data_dirs
```

**5) 磁盘空间满**

```bash
# 看哪个目录占空间
du -sh /var/opt/gitlab/* | sort -h

# 清理旧备份（按 backup_keep_time 自动清理）
sudo gitlab-ctl backup-etc --delete-old-backups
# 或手动
ls -lah /var/opt/gitlab/backups/
sudo rm <old-backup-file>
```

**6) 502 Bad Gateway**

```bash
# 通常是 Puma 挂了
sudo gitlab-ctl restart puma
sudo gitlab-ctl tail puma
```

**7) Email 不发**

```bash
# 测试 SMTP
sudo gitlab-rake gitlab:notify_test_email[your@email.com,'Subject','Body']

# 看 Rails 日志
sudo gitlab-ctl tail gitlab-rails/production | grep -i smtp
```

**8) CI Runner "couldn't connect to docker daemon"**

Runner 配 docker executor 但没挂 `/var/run/docker.sock` 或没 `--docker-privileged`：

```toml
# /etc/gitlab-runner/config.toml
[[runners]]
  executor = "docker"
  [runners.docker]
    privileged = true   # 或挂 docker.sock
    volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
```

**9) 数据库迁移卡住**

```bash
# 看迁移状态
sudo gitlab-rake db:migrate:status

# 检查 PG 锁
sudo gitlab-rails runner "ActiveRecord::Base.connection.execute('SELECT * FROM pg_locks WHERE NOT granted')"
```

**10) 内存爆了**

```bash
# 看谁吃最多内存
ps aux --sort=-%mem | head

# 限制 Sidekiq 并发（gitlab.rb）
sidekiq['max_concurrency'] = 10   # 默认 25

# 限制 Puma workers
puma['worker_processes'] = 2   # 默认是 CPU 核数
```

### 8.5.3 终极：进 Rails console 排查

```bash
sudo gitlab-rails console
```

打开 IRB 一样的 Ruby shell，可以查 GitLab 数据库、调模型、调方法。生产环境慎用，但这是终极工具。

```ruby
# 看用户
User.find_by(username: 'alice')

# 看项目
Project.find_by_full_path('mygroup/myproject')

# 改用户密码（root 账号 24 小时密码失效的替代方案）
user = User.find_by(email: 'admin@example.com')
user.password = 'NewSecurePassword123'
user.password_confirmation = 'NewSecurePassword123'
user.save!

# 看 pipeline 状态
Ci::Pipeline.last(5).each { |p| puts "#{p.id}: #{p.status}" }

# 看 stuck MR
MergeRequest.where(state: 'opened').where('updated_at < ?', 30.days.ago).count
```

退出：`Ctrl+D`

## 8.6 安全维护

### 8.6.1 升级 OS 包

```bash
# Ubuntu
sudo apt update && sudo apt upgrade -y

# RHEL
sudo dnf update -y

# GitLab 包升级
sudo apt install gitlab-ce   # 或 dnf
sudo gitlab-ctl reconfigure
```

### 8.6.2 轮换 gitlab-secrets.json

定期备份这个文件到**加密**异地存储（密码管理器 / 加密云盘 / 离线盘）。

**不要**直接 commit 到 git。

### 8.6.3 审计日志（[官方] /administration/audit_events/）

Premium+ 才有 audit log，记录所有敏感操作（创建用户、改权限、删除项目、改密钥）。定期下载归档。

## 8.7 升级前 checklist（铁律）

> 来自 [官方] 升级文档 + 实战经验

- [ ] **已备份**（`gitlab-backup create` + `gitlab-ctl backup-etc`）
- [ ] **备份异地验证**（不能在同盘——盘坏了备份也丢）
- [ ] **升级路径核对**（看 [官方] upgrade paths 表）
- [ ] **停机窗口预估**（通常 30-60 分钟）
- [ ] **测试环境先升**（如有）
- [ ] **看 release notes**（breaking changes + deprecations）
- [ ] **DB migration 检查**（跨 minor 升级 PG 也会升级，需要时间）
- [ ] **SMTP / OAuth 配置还在**（升级不会动 gitlab.rb）
- [ ] **升完跑 `gitlab-rake gitlab:check`**

## 8.8 容量规划速查

按用户数选配置——具体表看 **[§99-A · 硬件要求速查](#99-)**。

> 📌 **详细架构参考**（1k / 2k / 3k / 5k / 10k / 25k / 50k 机器数 / 节点拆分）：[官方] /administration/reference_architectures/。

---

# 99 · 附录 {#ch99}

## A · 硬件要求速查

> 📌 运维场景使用本表 → 详见 [§8.8 容量规划速查](#ch08)

[官方] /install/requirements/

| 规模 | vCPU | RAM | Storage | 备注 |
|------|------|-----|---------|------|
| 测试 / 单人 | 2 | 4 GB | 40 GB | 不推荐生产 |
| 小团队（≤ 50） | 4 | 8 GB | 100 GB SSD | |
| 中型（50~200） | 8 | 16 GB | 200 GB SSD | 单机 |
| 中大型（200~1000） | 16 | 32 GB | 500 GB SSD | 单机（性能临界） |
| 大型（1000+） | 多节点拆 | 多节点拆 | 多节点拆 | 见 [官方] /administration/reference_architectures/ 选 1k/2k/3k/5k/10k/25k/50k 参考架构 |

**强制要求**（[官方]）：
- 内存 **≥ 8 GB**（更少要按 memory_constrained_envs 模式配）
- Gitaly 用 **SSD**
- **关 swap**（或保证不触发）
- 节点间延迟 < 5 ms（HA）
- 不要用 NFS / EFS / Azure Files

---

# 附录 B · 命令速查

## gitlab-ctl

| 命令 | 用途 |
|------|------|
| `sudo gitlab-ctl reconfigure` | 应用 gitlab.rb 配置 |
| `sudo gitlab-ctl restart` | 重启全部服务 |
| `sudo gitlab-ctl stop` / `start` | 停 / 启 |
| `sudo gitlab-ctl status` | 看服务状态 |
| `sudo gitlab-ctl tail` | tail 所有日志 |
| `sudo gitlab-ctl tail nginx` | tail 单服务 |
| `sudo gitlab-ctl backup-etc` | 备份配置 |
| `sudo gitlab-ctl prometheus-up` / `prometheus-down` | 启停 Prometheus |

## gitlab-rake

| 命令 | 用途 |
|------|------|
| `sudo gitlab-rake gitlab:env:info` | 环境信息 |
| `sudo gitlab-rake gitlab:check` | 健康检查 |
| `sudo gitlab-rake gitlab:doctor` | 深度诊断 |
| `sudo gitlab-rake gitlab:password:reset[root]` | 重置 root 密码 |
| `sudo gitlab-rake gitlab:notify_test_email[a@b.com,'sub','body']` | 测试邮件 |
| `sudo gitlab-rake gitlab:smtp:secret:edit EDITOR=vim` | 编辑 SMTP 加密凭证 |
| `sudo gitlab-rake gitlab:cleanup:project_uploads` | 清理孤儿上传文件 |
| `sudo gitlab-rake gitlab:import:repos` | 导入裸仓库 |

## gitlab-rails console

```bash
sudo gitlab-rails console
# IRB-like Ruby shell
# Ctrl+D 退出
```

常用：

```ruby
User.find_by(username: 'alice')
User.where(email: '%@example.com').count
Project.find_by_full_path('group/project')
MergeRequest.where(state: 'opened').count
Ci::Pipeline.last(5)
ApplicationSetting.current_settings
```

## gitlab-runner

| 命令 | 用途 |
|------|------|
| `sudo gitlab-runner register` | 注册 runner |
| `sudo gitlab-runner list` | 看所有 runner |
| `sudo gitlab-runner verify` | 验证 runner 状态 |
| `sudo gitlab-runner restart` | 重启 |
| `sudo gitlab-runner unregister --name <name>` | 注销 runner |

## glab（GitLab CLI，[官方] https://gitlab.com/gitlab-org/cli）

```bash
glab auth login --hostname gitlab.example.com
glab project create my-project
glab issue list
glab issue create --title "..." --description "..."
glab mr list
glab mr create --title "..." --description "..."
glab mr checkout 123
glab pipeline list
glab ci status
glab ci run
glab api /projects
glab repo clone group/project
```

## git（核心子集）

```bash
git clone <url>
git status
git add <file>
git commit -m "..."
git push -u origin <branch>
git pull
git fetch
git checkout -b <branch>
git branch -a
git log --oneline --graph --all
git diff <branch1> <branch2>
git stash
git stash pop
git rebase -i HEAD~3
git reset --hard HEAD~1
```

## docker（GitLab 容器用）

```bash
docker ps                    # 看跑着的容器
docker ps -a                 # 包括停的
docker logs -f <container>   # 实时日志
docker exec -it <container> bash   # 进容器
docker exec -t <container> gitlab-backup create
docker compose up -d
docker compose pull
docker compose down
docker volume ls
```

## kubectl（Helm 部署用）

```bash
kubectl get pods -n gitlab
kubectl describe pod <pod> -n gitlab
kubectl logs -f <pod> -n gitlab
kubectl exec -it <pod> -n gitlab -- bash
kubectl get events -n gitlab --sort-by='.lastTimestamp'
```

---

# 附录 C · 关键概念术语表

| 术语 | 含义 |
|------|------|
| **Omnibus** | GitLab 的 Linux 单包形式（deb/rpm） |
| **Helm chart** | K8s 包管理方式部署 GitLab |
| **Gitaly** | Git RPC 服务，封装所有 git 操作 |
| **Sidekiq** | Ruby 异步任务队列 |
| **Puma** | Rails HTTP server |
| **Workhorse** | Git Smart HTTP / 附件代理 |
| **Praefect** | Gitaly Cluster 协调器（HA） |
| **Runner** | CI 任务执行 agent |
| **Executor** | Runner 的执行环境（shell/docker/kubernetes 等） |
| **Pipeline** | 一次提交触发的一整套 CI 流程 |
| **Job** | Pipeline 中的一个具体任务 |
| **Stage** | Job 的分组阶段（按顺序执行） |
| **Artifact** | Job 产物，可下载或传给后续 job |
| **Cache** | 跨 job 缓存（node_modules 等） |
| **MR** | Merge Request |
| **Issue Board** | 看板式 Issue 管理 |
| **Epic** | 组层级的大主题（Premium+） |
| **OKR** | Objective + Key Result，目标管理 |
| **Iteration** | 类似 Sprint 的时间盒 |
| **Geo** | GitLab 多区域复制（灾难恢复） |
| **DIND** | Docker-in-Docker（CI 里跑 Docker） |
| **MTA** | Mail Transfer Agent（Postfix 等） |
| **.gitlab-ci.yml** | CI/CD 配置文件（项目根） |
| **glab** | GitLab 官方命令行工具 |
| **GitLab Duo** | AI 助手（代码补全、Chat） |

---

# 附录 D · 来源 + 验证报告

> 所有事实的来源标签：

| 章节 | 标签 | 抓取时间 |
|------|------|---------|
| 01 工具介绍 | `[官方]` docs.gitlab.com 多个页面 | 2026-07-04 |
| 02 架构组件 | `[官方]` /install/requirements/、/charts/、/install/docker/ | 2026-07-04 |
| 03 部署 - SaaS（已移除） | 用户不要了；gitlab.com 注册流程自行查看 | 2026-07-05 |
| 03 部署 - Omnibus | `[官方]` /install/package/ubuntu/、/install/package/almalinux/ | 2026-07-04 |
| 03 部署 - Docker | `[官方]` /install/docker/installation/ + `[本机验证]` docker 29.6.1 在本机 | 2026-07-04 |
| 03 部署 - Helm | `[官方]` /charts/、/charts/installation/ + `[本机未验证]` helm 未装 | 2026-07-04 |
| 04 配置 | `[官方]` /omnibus/settings/、/omnibus/settings/smtp/、/administration/encrypted_configuration/ | 2026-07-04 |
| 05 日常操作 | `[官方]` 12 张 /user/get_started/ 子页面（本教程前面抓过）+ /user/project/* | 2026-07-04 |
| 06 CI/CD | `[官方]` /ci/quick_start/、/ci/yaml/、/runner/install/、/ci/variables/ | 2026-07-04 |
| 07 安全扫描 | `[官方]` /user/application_security/ + 各扫描器页面 | 2026-07-04 |
| 08 运维 | `[官方]` /omnibus/settings/backups/、/update/、/administration/monitoring/、/administration/troubleshooting/ | 2026-07-04 |

## 已知未验证 / 留白

| 内容 | 状态 | 原因 |
|------|------|------|
| Helm chart 实际部署命令 | `[本机未验证]` | 本机未装 helm |
| Linux Omnibus 安装命令 | `[官方]` | 本机为 Windows，没在 Linux 上跑 |
| 真实 git push / git clone 流程 | `[官方]` | 本机有 git 2.53 但未连真实 GitLab 实例 |
| 备份恢复全流程 | `[官方]` | 未实测 |
| 升级流程 | `[官方]` | 未实测 |

## 已知限制

1. **Windows 上跑 GitLab 服务**：官方不推荐（[官方] /install/docker/installation/ 明确说）。教程里的 Omnibus 和 Docker 安装命令都在 Linux 上跑。Windows 用户可以装 **GitLab Runner**（[官方] /runner/install/windows/）。
2. **Helm 部署需要外部 PG / Redis / 对象存储**：本教程没展开生产级 Helm 部署的所有细节——参考 [官方] /charts/installation/。
3. **没有覆盖**：Geo 多区域、Operator 高级用法、自定义认证后端、GitLab Duo 模型微调——这些是"精通开发者"层级的内容，超出本教程范围。
4. **GA/订阅差异**：很多功能依赖订阅层级。Free / Premium / Ultimate 差异见 7.1 节。

## 下一步建议

按本教程走完后，建议深入的方向：

1. **看 [官方] /administration/reference_architectures/**——选适合你规模的架构
2. **看 [官方] /update/#upgrade-paths**——搞清升级路径
3. **CI/CD 进阶**：看 [官方] /ci/yaml/ 完整关键字
4. **Runner 调优**：看 [官方] /runner/configuration/advanced-configuration/
5. **安全合规**：看 [官方] /user/application_security/policies/
6. **Helm 生产**：看 [官方] /charts/installation/deployment/