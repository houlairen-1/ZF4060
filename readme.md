
# loc: ZF4060

## 多渠道

## codes

@2022-09-28 已转换为 windows `exe`可执行程序。
不再需要 windows 和 linux 虚拟机之间文件互传。

- format_jnbb.py
  source:       data/src/jnbb_src.xlsx
  temporary:    NULL
  destination:  data/dst/jnbb.xlsx

- format_dh.py
  source:       data/src/dh/*.xlsx
  temporary:    data/tmp_dh.xlsx
  destination:  data/dst/dh.xlsx

- format_sf.py
  source:       data/src/sf/*.xlsx
  temporary:    data/tmp_sf.xlsx
  destination:  data/dst/sf.xlsx

- format_fxq.py
  source:       data/src/fxq_src.xlsx
  destination:  data/dst/fxq.xlsx

- format_fxq_gwy.py
  source:       data/src/fxq/docx/*.docx [unique]
  temporary:    data/src/fxq/today.txt
                data/src/fxq/high.txt   # 高风险区
                data/src/fxq/mid.txt    # 中风险区
  destination:  data/dst/高风险_<now()>.xlsx
                data/dst/中风险_<now()>.xlsx

- docx2txt.py
  source:       data/src/fxq/docx/*.docx [unique]
  temporary:    data/src/fxq/today.txt
  destination:  data/src/fxq/high.txt   # 高风险区
                data/src/fxq/mid.txt    # 中风险区

- join.py 
  拼接省市县
  source:       data/src/fxq/high.txt   # 高风险区
                data/src/fxq/mid.txt    # 中风险区
  destination:  data/dst/高风险_<now()>.xlsx
                data/dst/中风险_<now()>.xlsx

## data

- [x] bak.xlsx
      This is the template of destination which can be uploaded.

- src
  - jnbb_src.xlsx
  - dh
  - sf
  - fxq
    - docx
      fn2022年10月29日.docx
    - high.txt
    - mid.txt

- dst
