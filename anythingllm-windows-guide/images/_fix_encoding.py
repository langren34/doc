"""修复文件编码：前 UTF-8，后 GBK → 统一 UTF-8"""
import os, sys, io

file_path = r"D:\Users\ZN34\.openclaw\workspace\docs\AnythingLLM官方教程.md"

# 强制 UTF-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

with open(file_path, 'rb') as f:
    raw = f.read()

# 找 UTF-8 失败的边界
try:
    full_text = raw.decode('utf-8')
    print('整个文件 UTF-8 正常，无乱码')
except UnicodeDecodeError as e:
    print(f'UTF-8 边界: byte {e.start}')
    utf8_part = raw[:e.start].decode('utf-8')
    # 后面用 GBK 解码（用 replace 避免失败）
    gbk_part = raw[e.start:].decode('gbk', errors='replace')
    full_text = utf8_part + gbk_part
    print(f'UTF-8 部分: {len(utf8_part)} chars')
    print(f'GBK 部分: {len(gbk_part)} chars')

# 备份原文件
backup = file_path + '.bak'
with open(backup, 'wb') as f:
    f.write(raw)
print(f'备份: {backup}')

# 重新写入 UTF-8
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
print(f'已修复: {file_path}')
print(f'新文件大小: {os.path.getsize(file_path)} bytes')