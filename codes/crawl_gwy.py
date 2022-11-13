#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect
import re


MAX_PAGES = 100
NUM_BUTTONS = 9

browser = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
browser.get('https://bmfw.www.gov.cn/yqfxdjcx/risk.html')
browser.implicitly_wait(60)
#Wait(browser, 60).until(
#    Expect.presence_of_element_located((By.CLASS_NAME, "risk-info-table"))
#)

risk_levels_list = [ '中风险', '中风险' ]

for level in risk_levels_list:
    # 等待加载

    # eg.中风险区 （2155）
    level_pattern = ' %s区 （\d+）' %(level)
    risk_levels = browser.find_elements(By.CLASS_NAME, 'tabs-header-tab')
    find_level = False
    for lid in range( len(risk_levels) ):
        risk_level = risk_levels[lid].get_attribute('textContent')
        if re.search(level_pattern, risk_level):
            find_level = True
            risk_levels[lid].click()
            #Wait(browser, 60).until(
            #    Expect.presence_of_element_located((By.CLASS_NAME, "loading"))
            #)
            print('%s has found.\t Click it.' %(level))
            break

    if not find_level:
        print('Level %s doesnot have found.' %(level) )
        continue


    # visit all pages
    for pid in range(1, MAX_PAGES):
    
        btn = browser.find_elements(By.CSS_SELECTOR, 'div.pages-box > button')
        # find pid in 9 buttons
        # bid: 0 is 首页, 1 is 上一页
        find_flag = False
        for bid in range( 2, NUM_BUTTONS-2 ):
            page_info = btn[bid].get_attribute('textContent')
            if int(page_info) == pid:
                find_flag = True
                print( 'Page %02d:\t crawl info.' %(pid) )
                break
    
        if not find_flag:
            print('Total pages is %02d.' %(pid-1) )
            break
    
        # next page
        btn[bid].click()
        
        risk_table = browser.find_elements(By.CLASS_NAME, "risk-info-table")
        for risk_title in risk_table:
            flight_price_row = risk_title.find_element(By.CLASS_NAME, "risk-info-table-title")
            print(flight_price_row.get_attribute("textContent"))
            # single page
    
    
    if pid == MAX_PAGES:
        print('MAX_PAGES is smaller.')
