
# loc: ZF4060

## 多渠道

## codes

- format_jnbb.py
  source:       data/src/src.xlsx
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

- bak.xlsx
  This is the template of destination which can be uploaded.
