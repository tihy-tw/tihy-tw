import os
import re

base_dir = r"C:\Users\pamir\Desktop\CLAUDE\code-projects\titanium-h2"
base_href = "/tihy-tw/"

html_files = []
for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d != '.git']
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 加入 base tag（若還沒有）
    if '<base href=' not in content:
        content = content.replace('<head>', f'<head>\n  <base href="{base_href}">', 1)

    # 2. 首頁連結 href="/" → href="/tihy-tw/"
    content = re.sub(r'href="/"', f'href="{base_href}"', content)

    # 3. 移除內部絕對路徑開頭的 / (排除 http/https)
    # src="/xxx" → src="xxx"
    content = re.sub(r'src="/(?!/)(?!http)', 'src="', content)
    # href="/xxx" → href="xxx" (排除 http/https 和錨點 #)
    content = re.sub(r'href="/(?![/#]|http)', 'href="', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"OK {filepath.replace(base_dir, '')}")

print(f"\nDone: {len(html_files)} files")
