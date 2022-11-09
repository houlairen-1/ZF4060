
# loc: ZF4060

## 多渠道

## codes

@2022-09-28 已转换为 windows `exe`可执行程序。
不再需要 windows 和 linux 虚拟机之间文件互传。
@2022-11-09 风险区：前期已经实现将国务院每日更新的docx文档，整理成表格。
现进行后期处理——去除重复项。

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

- join.py 
  拼接省市县
  
## data

- [x] bak.xlsx
      This is the template of destination which can be uploaded.

- src
  - jnbb_src.xlsx
  - dh
  - sf

- dst
  - 县级行政区划
    可参照 [卫生健康委-疫情风险等级查询](http://bmfw.www.gov.cn/yqfxdjcx/index.html)

    但是，不可尽信。行政区划依旧不全。eg. 德州市 - 天衢新区 lack


