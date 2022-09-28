
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

## data

- [x] bak.xlsx
      This is the template of destination which can be uploaded.

- src
  - jnbb_src.xlsx
  - dh
  - sf

- dst
