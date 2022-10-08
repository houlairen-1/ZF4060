#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

import openpyxl
import os
import re

fn_path = '../data/src/fxq/test.txt'
fn_list = []
pattern = r'(.+)\(\d+\)个'
with open(fn_path, 'r') as f:
    fn_list = f.readlines()

    #print(fn_list)
    
for value in fn_list:
    ret = re.search(pattern, value)
    if ret:
        print(ret.group(1))
    #print(value)
