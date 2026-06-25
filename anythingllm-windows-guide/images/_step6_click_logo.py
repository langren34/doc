"""点击 AnythingLLM logo 文字 (51, 86)"""
import pyautogui, time, subprocess, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

base = r"D:\Users\ZN34\.openclaw\workspace\docs\anythingllm-official-images"

# 激活
subprocess.run(['powershell', '-Command', '''
Add-Type @"
using System; using System.Runtime.InteropServices;
public class W { [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h); }
"@
$proc = Get-Process -Name "AnythingLLM" | Where-Object { $_.MainWindowHandle -ne 0 } | Select-Object -First 1
[W]::SetForegroundWindow($proc.MainWindowHandle) | Out-Null
'''], capture_output=True)
time.sleep(1)

# 点击 AnythingLLM logo 文字（屏幕 43, 78）
print("点击 logo: (43, 78)")
pyautogui.click(43, 78)
time.sleep(2)

out = f"{base}\\06c-after-logo-click.png"
pyautogui.screenshot(out)
print(f"截图: {out}")