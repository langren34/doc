"""
第 6 章实操：上传文档
步骤：
1. 从设置页回到聊天页（点击侧边栏工作区名）
2. 准备测试文档
3. 拖拽文档到聊天区
4. 截图上传后状态
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

# 步骤 1: 回到聊天页（OCR 找侧边栏工作区名"人工智能"位置）
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img_path = f"{base}\\05c-llm-config.png"
img = Image.open(img_path)
# 找侧边栏工作区名（在侧边栏顶部，OCR 之前找过）
crop = img.crop((0, 100, 285, 250))
crop = crop.resize((crop.width*4, crop.height*4))
data = pytesseract.image_to_data(crop, lang='chi_sim+eng', config='--psm 11', output_type=pytesseract.Output.DICT)
print("=== 侧边栏顶部 OCR（找工作区名）===")
for i, t in enumerate(data['text']):
    t = t.strip()
    if not t: continue
    try: c = int(float(data['conf'][i]))
    except: continue
    if c < 30: continue
    x = data['left'][i] // 4
    y = data['top'][i] // 4 + 100
    print(f"  ({x},{y}) [{c}%] '{t}'")