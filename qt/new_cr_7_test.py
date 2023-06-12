import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
#from html_table_parser import parser_functions as parser
import pandas as pd
import os
import rename_filename as rf



class cr_7:
    def __init__(self, driver: webdriver,url,folder)->None:
        self.driver = driver
        self.url = url
        self.folder= folder
        BACKSPACE = '/ue003'
        ENTER = '/ue007'
        TAB = '/ue004'

    def run(self)->str:

        if not os.path.isdir(self.folder):
            os.mkdir(self.folder)

        print(os.getcwd())

        self.driver.find_element_by_name('login_id').send_keys('green')
        self.driver.find_element_by_name('login_pwd').send_keys('green1234*')
        self.driver.find_element_by_xpath('//*[@id="contentsArea"]/div/div/img').click()


        #url00 = "http://wms.greenserve.co.kr/iworks_app/stock/iwst2055.jsp"
        #self.driver.get(url00)
        #self.driver.dismiss()


        #self.driver.switch_to_window(l[0])

        #self.driver.close()

        url01 = "http://wms.greenserve.co.kr/iWorks"
        self.driver.get(url01)
        self.driver.implicitly_wait(1)

        l = window_after = self.driver.window_handles
        print("length :", l)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.window(l[1])
        self.driver.close()


        self.driver.switch_to.window(l[0])

        self.driver.find_element_by_xpath('//*[@id="menu_stock"]').click()
        # driver.find_element_by_xpath('//*[@id="sub_tree"]')
        # //*[@id="menu_sales"]
        # /html/body/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[4]/div/a[3]
        time.sleep(3)
        # 구매발주등록
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div[2]/div[1]/div[2]/ul/li[2]/ul/li[6]').click()
        #  /html/body/table/tbody/tr[2]/td/div[2]/div[1]/div[2]/ul/li[2]/ul/li[9]
        self.driver.switch_to.frame('iwst3020')
        # iwsm4070



        time.sleep(1)
        selected_start_date = self.driver.find_element_by_id('io_dt_start')
        selected_end_date = self.driver.find_element_by_id('io_dt_end')



        today_until = datetime.date.today().toordinal()
        today_ymd = datetime.date.today()
        print(today_ymd)
        until = today_ymd
        days = today_until - until.toordinal() +1
        print("total :", days)

        for k in range(0, int(days)):
            for i in range(0, 10):
                selected_start_date.send_keys(Keys.BACKSPACE)

            if k > 0:
                start_date = today_ymd + datetime.timedelta(days=( k))
            else:
                start_date = today_ymd

            selected_start_date.send_keys(str(start_date))
            time.sleep(1)

            for i in range(0, 11):
                selected_end_date.send_keys(Keys.BACKSPACE)

            if k > 0:
                end_date = today_ymd + datetime.timedelta(days=( k))
            else:
                end_date = today_ymd

            selected_end_date.send_keys(str(end_date))
            print(start_date,end_date)

            time.sleep(1)

            self.driver.implicitly_wait(20)
            self.driver.find_element_by_xpath('/ html / body / div[2] / form / table / tbody / tr / td[2] / button[1]').click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr/td[2]/button[2]').click()

            #self.driver.implicitly_wait(20)
            #get_list = self.driver.find_element_by_xpath('//*[@id="grid"]/div[2]/table')

        time.sleep(10)
        self.driver.close()

        rf.getfiles(os.getcwd()+"\\"+ self.folder, self.folder)



