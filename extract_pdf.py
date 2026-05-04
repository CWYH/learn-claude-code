import fitz
p = r'C:\Users\qianxue\Downloads\KubeCon_EU_2022_Volcano_Intro-v2.0.pdf'
doc = fitz.open(p)
out = []
out.append(f'PAGES {len(doc)}')
out.append(f'METADATA {doc.metadata}')
for i, page in enumerate(doc):
    out.append(f'--- PAGE {i+1} ---')
    out.append(page.get_text('text'))
open('volcano_extract.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written', len(doc), 'pages')
