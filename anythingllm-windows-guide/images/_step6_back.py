"""点击 AnythingLLM logo 回到主页"""
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

# 点击 AnythingLLM logo（原图 24, 64 → 屏幕 16, 56）
print("点击 logo: (16, 56)")
pyautogui.click(16, 56)
time.sleep(2)

# 截图看是否回到聊天页
out = f"{base}\\06a-back-to-chat.png"
pyautogui.screenshot(out)
print(f"截图: {out}")