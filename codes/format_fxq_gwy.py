#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

from docx2txt import docx2txt
from join import join


if __name__=='__main__':
    
    print('\n\n开始切割docx文件\n---\n')
    docx2txt()
    print('\n\n\n开始拼接风险等级-省-市-县\n---\n')
    join()
