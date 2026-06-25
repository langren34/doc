"""
实操：点击设置入口
"""
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

# 点击设置入口（原图坐标 92, 1278 → 屏幕 84, 1270）
print("点击设置入口: (84, 1270)")
pyautogui.click(84, 1270)
time.sleep(2)

# 截图看是否进入设置页
out = f"{base}\\05b-settings-page.png"
pyautogui.screenshot(out)
print(f"截图: {out}")