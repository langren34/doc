"""
点击"大语言模型 (LLM)"菜单进入 LLM 配置页
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

# 用 OCR 找 "大语言模型 (LLM)" 位置
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img_path = f"{base}\\05b-settings-page.png"
img = Image.open(img_path)
# 裁剪左侧菜单（x=0-285, y=100-700）
crop = img.crop((0, 100, 285, 700))
crop = crop.resize((crop.width*3, crop.height*3))
data = pytesseract.image_to_data(crop, lang='chi_sim+eng', config='--psm 11', output_type=pytesseract.Output.DICT)
print("=== 左侧菜单 OCR ===")
for i, t in enumerate(data['text']):
    t = t.strip()
    if not t: continue
    try: c = int(float(data['conf'][i]))
    except: continue
    if c < 30: continue
    x = data['left'][i] // 3
    y = data['top'][i] // 3 + 100
    print(f"  ({x},{y}) [{c}%] '{t}'")