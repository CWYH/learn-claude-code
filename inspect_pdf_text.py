import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
s=Path(r'C:\repos\CWYH\learn-claude-code\KubeCon_EU_2022_Volcano_Intro-v2.0.extracted.txt').read_text(encoding='utf-8')
pages=s.split(chr(12))
print('pages', len(pages))
for i,p in enumerate(pages,1):
    print(f'--- PAGE {i} ---')
    print(p[:1800].replace('\r',''))
