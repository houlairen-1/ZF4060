#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

import openpyxl
import os
import re

xlsx_path = r'../data/src/fxq_src.xlsx'
fn_path = '../data/dst/fxq.txt'


# open file
municipality = {'北京市', '天津市', '上海市', '重庆市'}

wb = openpyxl.load_workbook(xlsx_path)
sheet = wb['Sheet1']

with open(fn_path, 'w') as f:
    rows = sheet.max_row
    
    for rid in range(2,rows+1):
        province = sheet.cell(rid,1).value
        city = sheet.cell(rid,2).value
        county = sheet.cell(rid,3).value
        if province in municipality:
            city = province
            county = sheet.cell(rid,2).value
        # split column
        county = county.replace('；','\n\t\t\t')
        print('中风险\t%s\t%s\t%s\n' 
              %( province, city, county ) )

        f.write('中风险\t%s\t%s\t%s\n' 
                %( province, city, county ) )

