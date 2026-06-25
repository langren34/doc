"""
实操：导航到 LLM 配置页
步骤：
1. 截图当前聊天页（用作对比）
2. 点侧边栏底部 ⚙️（设置）
3. 在设置页找 "AI 提供商" → "LLM" 菜单
4. 截图 LLM 配置页
"""
import pyautogui, time, subprocess
import pytesseract
from PIL import Image
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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

# 步骤 1: 截图当前聊天页
shot1 = f"{base}\\05a-chat-page-before.png"
pyautogui.screenshot(shot1)
print(f"[1] 截图: {shot1}")

# 步骤 2: 点侧边栏底部 ⚙️ 设置
# OCR 找 ⚙️ 位置（侧边栏底部，约 y=1370）
# 已知：AnythingLLM 侧边栏底部 4 图标在 y=1370, x=40,75,110,145
# 第 4 个图标是返回箭头（向左），不是设置
# 设置可能在侧边栏底部其他位置，或者工作区名右侧

# 截图侧边栏底部找设置图标
img = Image.open(shot1)
# 裁剪侧边栏底部（y=1300-1400）
crop = img.crop((0, 1300, 285, 1400))
crop = crop.resize((crop.width*3, crop.height*3))
data = pytesseract.image_to_data(crop, lang='chi_sim+eng', config='--psm 11', output_type=pytesseract.Output.DICT)
print("\n=== 侧边栏底部 OCR ===")
for i, t in enumerate(data['text']):
    t = t.strip()
    if not t: continue
    try: c = int(float(data['conf'][i]))
    except: continue
    if c < 30: continue
    x = data['left'][i] // 3
    y = data['top'][i] // 3 + 1300
    print(f"  ({x},{y}) [{c}%] '{t}'")

# 用 image 工具看右侧的"设置"图标位置
# 实际上从之前的 OCR 知道侧边栏底部 4 图标位置
# 让我用 image 工具问
import subprocess as sp
print("\n[手动] 用 image 工具问设置图标位置")