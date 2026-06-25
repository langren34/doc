import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open(r'D:\Users\ZN34\.openclaw\workspace\docs\anythingllm-official-images\05c-llm-config.png')
crop = img.crop((0, 0, 2560, 100))
data = pytesseract.image_to_data(crop, lang='eng', config='--psm 11', output_type=pytesseract.Output.DICT)
print('=== 顶部栏 OCR ===')
for i, t in enumerate(data['text']):
    t = t.strip()
    if not t: continue
    try: c = int(float(data['conf'][i]))
    except: continue
    if c < 30: continue
    x = data['left'][i]; y = data['top'][i]
    print(f'  ({x},{y}) [{c}%] "{t}"')