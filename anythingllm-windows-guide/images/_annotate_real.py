"""给实操截图加 6 个功能按钮标注（参考用户给的红色椭圆风格）"""
from PIL import Image, ImageDraw, ImageFont
import math

RED = (220, 38, 38)

def font(size):
    for p in [r"C:\Windows\Fonts\msyhbd.ttc", r"C:\Windows\Fonts\msyh.ttc"]:
        try:
            return ImageFont.truetype(p, size)
        except:
            continue
    return ImageFont.load_default()

src = r"D:\Users\ZN34\.openclaw\workspace\docs\anythingllm-official-images\06-current-workspace.png"
img = Image.open(src).convert("RGB")
W, H = img.size
print(f"图: {W}x{H}")

# OCR 已知锚点（原图 2560x1400）：AnythingLLM logo (49, 85), + 新建工作区 (241, 158), +NewThread (94, 483)
# deepseek-v4-flash (314, 94), 今天欢迎语 (~1410, 624), +工具 (1076, 775)

# 计算缩放比（如果是 1280x720 或 2560x1400）
S_x = W / 2560
S_y = H / 1400
S = (S_x + S_y) / 2

f = font(int(16 * S))

draw = ImageDraw.Draw(img, "RGBA")

# 6 个功能按钮（原图坐标）
elements = [
    ("新建工作区", 241, 158, 40, 40),    # 侧边栏 + 号
    ("切换模型",   370, 100, 140, 28),   # 顶部 deepseek-v4-flash
    ("新建对话",   94, 483, 130, 32),    # 侧边栏底部 + New Thread
    ("输入问题",   1000, 720, 700, 70),  # 输入框
    ("发送",       1735, 730, 50, 50),   # 发送按钮
    ("上传文件",   850, 945, 140, 32),   # 快捷按钮
]

print(f"缩放比 S={S:.3f}")
for name, xf, yf, wf, hf in elements:
    xs = int(xf * S); ys = int(yf * S)
    ws = int(wf * S); hs = int(hf * S)
    pad = int(8 * S)
    line_w = max(2, int(3 * S))
    # 红圈
    draw.ellipse((xs - ws//2 - pad, ys - hs//2 - pad,
                  xs + ws//2 + pad, ys + hs//2 + pad),
                 outline=RED + (220,), width=line_w)
    # 红色标签（无背景，纯红字）
    # 放在按钮右下方
    lx = xs + ws//2 + pad + int(10 * S)
    ly = ys + hs//2 + pad
    draw.text((lx, ly), name, fill=RED + (255,), font=f)

out = r"D:\Users\ZN34\.openclaw\workspace\docs\anythingllm-official-images\06-current-workspace-annotated.png"
img.save(out, "PNG", optimize=True)
import os
print(f"已保存: {out} ({os.path.getsize(out)//1024} KB)")