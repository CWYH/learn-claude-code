# -*- coding: utf-8 -*-
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding="utf-8")
t=Path(r"C:\\repos\\CWYH\\learn-claude-code\\chapter2_memory_extracted.txt").read_text(encoding="utf-8")
markers=["\u8bb0\u5fc6\u5206\u7c7b","\u77ed\u671f\u8bb0\u5fc6","\u957f\u671f\u8bb0\u5fc6","\u8bed\u4e49\u8bb0\u5fc6","\u60c5\u666f\u8bb0\u5fc6","\u7a0b\u5e8f\u8bb0\u5fc6","\u8bb0\u5fc6\u7cfb\u7edf","\u5b9e\u73b0","\u603b\u7ed3","\u5d4c\u5165","\u5411\u91cf","Memory Types","Memory"]
for marker in markers:
    print("###", marker)
    idx=t.find(marker)
    print(idx)
    if idx!=-1:
        print(t[max(0,idx-200):idx+800].replace("\n"," "))
