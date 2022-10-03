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

key_dict = { '赵固堆派出所':'赵堌堆乡', 
             '馆驿派出所':'馆驿镇' }

for rid in range(4,rows+1):
    for cid in range(1, 13): #col: A-L
        sheet_dst.cell(rid,cid).value = sheet_src.cell(rid,cid).value
        #print('%d\t%s' %(rid, sheet_src.cell(rid,cid).value))
    for cid in range(13, 20): #col: A-L
        sheet_dst.cell(rid,cid+1).value = sheet_src.cell(rid,cid).value
    
    # 判断管控措施 T20 ==> U21
    find_flag = False
    value = sheet_src.cell(rid,17).value

    for k, v in key_dict.items():
        if k in value:
            tid = tid+1
            find_flag = True
            sheet_dst.cell(tid,1).value = v
            break
    
    if not find_flag:
        continue


    for cid in range(20, 24): #col: A-L
        sheet_dst.cell(rid,cid+1).value = sheet_src.cell(rid,cid).value


#cells = sheet_src[4]

# for cell in cells:
#     print(cell.value)

wb_dst.save('../data/dst/jnbb.xlsx')
