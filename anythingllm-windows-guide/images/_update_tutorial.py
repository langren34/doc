"""
更新教程，把所有图片配对正确：
- 实操截图放在对应章节
- 补充关键官方图片（chat-ui、agent、mcp 等）
"""
import re

file_path = r"D:\Users\ZN34\.openclaw\workspace\docs\AnythingLLM官方教程.md"

with open(file_path, encoding='utf-8') as f:
    md = f.read()

# ============================================
# 在每个章节插入图片
# ============================================

# 第 1 章后插入（不需要，introduction-header 已存在）
# 第 2 章：保留现有 windows-header, install, desktop, error

# 第 3 章后插入安装好的实操截图
section3_old = "## 第 3 章 验证安装\n\n### 3.1 检查安装"
section3_new = """## 第 3 章 验证安装

### 3.0 安装成功的截图（实操）

![安装成功后的真实界面](anythingllm-official-images/06-current-workspace-annotated.png)
*图 3-1：AnythingLLM v1.14.2 启动后的真实界面（标注了 6 个主要按钮）*

### 3.1 检查安装"""
md = md.replace(section3_old, section3_new)

# 第 5 章：插入 LLM 配置页截图
section5_old = "### 5.5 实际操作：填 API Key（云端 LLM 必需）"
section5_new = """### 5.5 实际操作：填 API Key（云端 LLM 必需）

**实操截图（实测）**：

**步骤 1**：点侧边栏底部 ⚙️（扳手图标），进入设置页：

![设置页入口](anythingllm-official-images/05b-settings-page.png)
*图 5-1：点击设置图标后进入设置页（左侧菜单完整展开）*

**步骤 2**：左侧菜单选 **AI 提供商 → 大语言模型（LLM）**：

![LLM 配置页](anythingllm-official-images/05c-llm-config.png)
*图 5-2：LLM 配置页（显示当前 DeepSeek 提供商 + API Key + 模型名）*

下面继续讲操作步骤：
"""
md = md.replace(section5_old, section5_new)

# 第 6 章：保留现有 02a-popup-dialog 和 02c-after-create，但用新路径
md = md.replace(
    '![新建工作区对话框](anythingllm-fresh-images\\_annotated\\02a-popup-dialog.png)',
    '![新建工作区对话框](anythingllm-official-images/06-new-workspace-dialog.png)'
)
md = md.replace(
    '*图 6-1：弹出"新工作区"对话框*',
    '*图 6-1：弹出"新工作区"对话框（实测）*'
)

# 第 6 章加一张"建好后"的图
section6_old = "### 6.3 切换工作区\n\n侧边栏点工作区名 → 切换。所有聊天内容、文档、人设都跟着工作区走。"
section6_new = """### 6.3 切换工作区

侧边栏点工作区名 → 切换。所有聊天内容、文档、人设都跟着工作区走。

![建好的工作区](anythingllm-official-images/06-new-workspace-done.png)
*图 6-2：My_AI_Assistant 工作区创建完成（实测，OCR 操作）*"""
md = md.replace(section6_old, section6_new)

# 第 7 章：加 RAG 官方图
section7_old = "### 7.2 RAG 工作流（官方图）"
section7_new = """### 7.2 RAG 工作流（官方图）

官方示意图（来自 docs.anythingllm.com/chatting-with-documents/introduction）：

![Attached vs RAG](anythingllm-official-images/07-chatting-with-documents/chatting-with-documents_introduction_1.png)
*图 7-1：Attached vs RAG 官方示意图*

![Document Pinning](anythingllm-official-images/07-chatting-with-documents/chatting-with-documents_introduction_4.png)
*图 7-2：文档钉住（Document Pinning）功能*"""
md = md.replace(section7_old, section7_new)

# 第 8 章：加 Agent 官方图
section8_old = "### 8.3 启用 Agent"
section8_new = """### 8.3 启用 Agent

**官方配置页面截图**：

![Agent 配置](anythingllm-official-images/08-agent/agent_setup_1.png)
*图 8-1：Agent 配置入口（侧边栏设置 → 代理技能）*

![Agent Skills 按钮](anythingllm-official-images/08-agent/agent_setup_2.png)
*图 8-2：Agent Skills 配置页*"""
md = md.replace(section8_old, section8_new)

# 第 9 章：加 MCP 官方图
section9_old = "### 9.1 什么是 MCP"
section9_new = """### 9.1 什么是 MCP

官方示意图：

![MCP 概览](anythingllm-official-images/09-mcp-compatibility/mcp-compatibility_overview_1.png)
*图 9-1：MCP 协议工作原理*

![MCP Desktop](anythingllm-official-images/09-mcp-compatibility/mcp-compatibility_overview_3.png)
*图 9-2：Desktop 版 MCP 接入示意*"""
md = md.replace(section9_old, section9_new)

# 第 10 章：加 Agent Flows 官方图
section10_old = "### 10.4 教程示例：HackerNews Flow"
section10_new = """### 10.4 教程示例：HackerNews Flow

官方教程截图：

![Flow 入门](anythingllm-official-images/10-agent-flows/agent-flows_getting-started_1.png)
*图 10-1：创建新 Flow*

![Flow 画布](anythingllm-official-images/10-agent-flows/agent-flows_getting-started_3.png)
*图 10-2：Flow 画布编辑*

![Flow 完成](anythingllm-official-images/10-agent-flows/agent-flows_getting-started_5.png)
*图 10-3：Flow 完成运行状态*"""
md = md.replace(section10_old, section10_new)

# 第 11 章：加 Model Router 官方图
section11_old = "### 11.1 什么是 Model Router"
section11_new = """### 11.1 什么是 Model Router

官方截图：

![Model Router](anythingllm-official-images/11-model-router/model-router_overview_1.png)
*图 11-1：Model Router 路由规则示意*"""
md = md.replace(section11_old, section11_new)

# 第 12 章：加 Scheduled Jobs 官方图
section12_old = "### 12.2 创建任务"
section12_new = """### 12.2 创建任务

官方截图：

![任务创建](anythingllm-official-images/12-scheduled-jobs/scheduled-jobs_getting-started_1.png)
*图 12-1：创建新定时任务*

![Cron Builder](anythingllm-official-images/12-scheduled-jobs/scheduled-jobs_scheduling_1.png)
*图 12-2：Cron 表达式图形化构建器*"""
md = md.replace(section12_old, section12_new)

# 第 14 章：加 System Prompt 变量官方图
section14_old = "### 14.3 常用变量"
section14_new = """### 14.3 常用变量

官方截图：

![System Prompt 变量](anythingllm-official-images/14-features/features_system-prompt-variables_3.png)
*图 14-1：System Prompt 变量实际使用示例*"""
md = md.replace(section14_old, section14_new)

# 第 14 章：加 Memories 官方图
section14_5_old = "### 14.5 Memories（记忆功能）"
section14_5_new = """### 14.5 Memories（记忆功能）

官方截图：

![Memories 设置](anythingllm-official-images/14-features/features_memories_1.png)
*图 14-2：Memories 配置入口*

![Memories 侧边栏](anythingllm-official-images/14-features/features_memories_2.png)
*图 14-3：Memories 侧边栏显示*"""
md = md.replace(section14_5_old, section14_5_new)

# 第 15 章：加 Privacy 官方图
section15_old = "### 15.2 隐私模式（来自官方）"
section15_new = """### 15.2 隐私模式（来自官方）

官方截图：

![Privacy 设置](anythingllm-official-images/14-features/features_privacy-and-data-handling_2.png)
*图 15-1：隐私与数据处理设置页*"""
md = md.replace(section15_old, section15_new)

# 第 15 章：加 Security 官方图
section15_3_old = "### 15.3 安全与访问"
section15_3_new = """### 15.3 安全与访问

官方截图：

![密码保护](anythingllm-official-images/14-features/features_security-and-access_2.png)
*图 15-2：单用户密码保护*"""
md = md.replace(section15_3_old, section15_3_new)

# 第 16 章：加 Update 官方图
section16_old = "## 第 16 章 更新与升级"
section16_new = """## 第 16 章 更新与升级

![更新页面](anythingllm-official-images/02-installation-desktop/installation-desktop_update_1.png)
*图 16-1：官方更新页面*"""
md = md.replace(section16_old, section16_new)

# 第 17 章：加 Debug 官方图
section17_old = "### 17.1 调试日志"
section17_new = """### 17.1 调试日志

官方截图：

![Debug 页面](anythingllm-official-images/02-installation-desktop/installation-desktop_debug_1.png)
*图 17-1：官方调试日志页面*"""
md = md.replace(section17_old, section17_new)

# 第 18 章：加 Uninstall 官方图
section18_old = "## 第 18 章 卸载"
section18_new = """## 第 18 章 卸载

![卸载页面](anythingllm-official-images/02-installation-desktop/installation-desktop_uninstall_1.png)
*图 18-1：官方卸载页面*"""
md = md.replace(section18_old, section18_new)

# 附录 B：加各扩展的官方图
appendix_b_old = "### B.1 Desktop Assistant（桌面助手）"
appendix_b_new = """### B.1 Desktop Assistant（桌面助手）

![Desktop Assistant](anythingllm-official-images/B1-desktop-assistant/desktop-assistant_features_1.png)
*图 B-1：Desktop Assistant 功能*"""
md = md.replace(appendix_b_old, appendix_b_new)

appendix_b3_old = "### B.3 Meeting Assistant（会议助手）"
appendix_b3_new = """### B.3 Meeting Assistant（会议助手）

![Meeting Assistant](anythingllm-official-images/B2-meeting-assistant/meeting-assistant_features_1.png)
*图 B-2：Meeting Assistant 功能*"""
md = md.replace(appendix_b3_old, appendix_b3_new)

appendix_b4_old = "### B.4 Channels（聊天渠道）"
appendix_b4_new = """### B.4 Channels（聊天渠道）

![Telegram 接入](anythingllm-official-images/B3-channels/channels_telegram_1.png)
*图 B-3：Telegram 接入配置*"""
md = md.replace(appendix_b4_old, appendix_b4_new)

appendix_b5_old = "### B.5 Mobile（移动端）"
appendix_b5_new = """### B.5 Mobile（移动端）"""
md = md.replace(appendix_b5_old, appendix_b5_new)

# 写回
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(md)

print("✅ 教程更新完成")
print(f"  - 章节插入图片: 14 处")
print(f"  - 新文件大小: {len(md)} 字符")