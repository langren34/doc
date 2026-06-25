with open(r'D:\Users\ZN34\.openclaw\workspace\docs\AnythingLLM官方教程.md', 'rb') as f:
    raw = f.read()

# 找 "推荐后续" UTF-8 字节
idx = raw.find('推荐后续'.encode('utf-8'))
print(f'位置: {idx}')
if idx > 0:
    # 显示前后 50 字节
    start = max(0, idx - 50)
    chunk = raw[start:idx + 100]
    print('原文 (UTF-8 decode):')
    print(chunk.decode('utf-8', errors='replace'))