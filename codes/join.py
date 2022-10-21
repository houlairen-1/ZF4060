#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

import openpyxl
import os
import re

xlsx_path = r'../data/template_risk.xlsx'
fn_path = '../data/src/fxq/test.txt'

fn_list = []
stack = [] #风险区栈 拼接省-市-县
pattern = r'(.+)\(\d+\)个'

# 23 + 5 + 4 + 2
province = [ '河北省', '山西省', '辽宁省', '吉林省', 
             '黑龙江省', '江苏省', '浙江省', '安徽省',
             '福建省', '江西省', '山东省', '河南省', 
             '湖北省', '湖南省', '广东省', '海南省', 
             '四川省', '贵州省', '云南省', '陕西省', 
             '甘肃省', '青海省', '台湾省',
             '内蒙古自治区', '广西壮族自治区', 
             '西藏自治区', '宁夏回族自治区', 
             '新疆维吾尔自治区',
             '香港特别行政区', '澳门特别行政区',
             '北京市' ]

municipality = {'天津市', '上海市', '重庆市'}
# 当前是重庆郊县发生疫情，重庆市暂时不用判断

# open file

wb = openpyxl.load_workbook(xlsx_path)
sheet = wb['Sheet1']
rid = 2 # sheet record id

with open(fn_path, 'r') as f:
    fn_list = f.readlines()

    #print(fn_list)
    
for value in fn_list:
    value = value.strip('\n')
    ret = re.search(pattern, value)
    if ret:
        # 判断省和市
        key = ret.group(1)
        if key in province:
            if len(stack)==0:
                #print(key)
                stack.append(key)
            else:
                #到了下一省份
                if len(stack) != 2:
                    print('stack Error!%s' %(stack) )
                    break
                stack.pop() #弹出市
                stack.pop() #弹出省
                stack.append(key) #new province in stack
        elif key in municipality:
            if len(stack)==0:
                #print(key)
                stack.append(key)
                stack.append(key)
            else:
                #到了下一省份
                if len(stack) != 2:
                    print('stack Error!%s' %(stack) )
                    break
                stack.pop() #弹出市
                stack.pop() #弹出省
                stack.append(key) #new province in stack
                stack.append(key) #new province in stack
            
        else:
            if len(stack) == 2:
                stack.pop()
            #print('\t%s' %(key) )
            stack.append(key)
        continue
    #print(value)
    
    print('%s\t%s\t%s' %(stack[-2], stack[-1], value) )
    rid = rid+1
    sheet.cell(rid, 2).value = stack[-2] # col B
    sheet.cell(rid, 3).value = stack[-1] # col C
    sheet.cell(rid, 4).value = value # col D

wb.save('../data/dst/risk.xlsx')
