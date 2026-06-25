"""点击 LLM 菜单项"""
import pyautogui, time, subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base = r"D:\Users\ZN34\.openclaw\workspace\docs\anythingllm-official-images"

# 激活窗口
subprocess.run(['powershell', '-Command', '''
Add-Type @"
using System; using System.Runtime.InteropServices;
public class W { [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h); }
"@
$proc = Get-Process -Name "AnythingLLM" | Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -First 1
[W]::SetForegroundWindow($proc.MainWindowHandle) | Out-Null
'''], capture_output=True)
time.sleep(1)

# 点击 LLM 菜单（屏幕坐标 94, 208）
print("点击 LLM 菜单: (94, 208)")
pyautogui.click(94, 208)
time.sleep(2)

# 截图 LLM 配置页
out = f"{base}\\05c-llm-config.png"
pyautogui.screenshot(out)
print(f"截图: {out}")