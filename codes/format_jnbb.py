#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

import openpyxl

src_xlsx_path = r'../data/src/jnbb_src.xlsx'
dst_xlsx_path = r'../data/bak.xlsx'

wb_src = openpyxl.load_workbook(src_xlsx_path)
sheet_src = wb_src.active
wb_dst = openpyxl.load_workbook(dst_xlsx_path)
sheet_dst = wb_dst.active

# get shape of src
# start from 4th row
rows = sheet_src.max_row
#print(rows)

for rid in range(4,rows+1):
    for cid in range(1, 13): #col: A-L
        sheet_dst.cell(rid,cid).value = sheet_src.cell(rid,cid).value
        #print('%d\t%s' %(rid, sheet_src.cell(rid,cid).value))
    for cid in range(13, 24): #col: A-L
        sheet_dst.cell(rid,cid+1).value = sheet_src.cell(rid,cid).value

#cells = sheet_src[4]

# for cell in cells:
#     print(cell.value)

wb_dst.save('../data/dst/jnbb.xlsx')
