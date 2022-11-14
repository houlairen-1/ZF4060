#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

################################################
#
# 2022-10-28 transfer docx to text
#
################################################


import sys
import os
import re
import docx
import datetime


def docx2txt():
    today = datetime.datetime.now()
    today_pattern = '.*{}年{}月{}日.*\.docx'.format(today.year,
                                                    today.month,
                                                    today.day)
    # find goal: today's docx
    docx_dir = '../data/src/fxq/docx/'
    txt_dir = '../data/src/fxq/'
    
    txt_fn = 'today.txt'
    
    docx_list = [x for x in os.listdir(docx_dir) if os.path.splitext(x)[1] == '.docx' and re.search(today_pattern, x) ] # 罗列目录内所有xlsx文件
    if len(docx_list) == 0:
        print('Error:\tdocx donot exit.')
        sys.exit(1)
    print('Transfer %s to text' %(docx_list[0]) )
    
    docx_path = docx_dir+docx_list[0]
    
    file_h = docx.Document(docx_path)
    
    txt_path = txt_dir+txt_fn
    with open(txt_path, 'w') as f:
        duplicate = ''
        duplicate_id = 0
        for p in file_h.paragraphs:
            #print(p.text)
            # 根据空格切割
            ret = p.text.split(' ')
            value = ret[0]
    
            # 去重
            if len(value) == 0 or value == duplicate:
                duplicate_id = duplicate_id+1
                continue
            duplicate = value
            f.write('%s\n' %(value) )
        print('Have writen to %s\n \t delete-duplicate-lines:\t%04d lines'
              %(txt_path, duplicate_id) )
    
    
    # 将中高风险区分开
    txt_arr = [ ['高风险', 'high.txt'],
                ['中风险', 'mid.txt'],
                ['低风险', 'low.txt'] ]
    
    with open(txt_path, 'r') as f:
        contents = f.readlines()
    
    for tid in range(len(txt_arr)-1):
        txt_start_pattern = '^%s区\(\d+\)个' %txt_arr[tid][0]
        txt_end_pattern = '^%s区\(\d+\)个' %txt_arr[tid+1][0]
        txt_sub_path = txt_dir + txt_arr[tid][1]
        with open(txt_sub_path, 'w') as f:
            start_f = False
            for value in contents:
                ret = re.search(txt_start_pattern, value)
                if ret:
                    start_f = True
                    continue
                ret = re.search(txt_end_pattern, value)
                if ret:
                    end_f = True
                    break
                if not start_f: # 找到起点
                    continue
    
                f.write('%s' %(value) )
                
        print('%s has generated.' %(txt_sub_path))
