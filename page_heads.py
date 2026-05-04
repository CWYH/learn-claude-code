from pathlib import Path
import sys
sys.stdout.reconfigure(encoding="utf-8")
t=Path(r"C:\\repos\\CWYH\\learn-claude-code\\chapter2_memory_extracted.txt").read_text(encoding="utf-8")
for i in range(1,50):
    m=f"--- PAGE {i} ---"
    idx=t.find(m)
    nxt=t.find(f"--- PAGE {i+1} ---") if i<49 else len(t)
    page=t[idx+len(m):nxt]
    first=" ".join([line.strip() for line in page.splitlines() if line.strip()][:4])
    print(f"{i}: {first[:200]}")
