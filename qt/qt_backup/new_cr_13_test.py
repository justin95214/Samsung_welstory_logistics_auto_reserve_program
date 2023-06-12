import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from html_table_parser import parser_functions as parser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import rename_filename as rf

class cr_13:
    def __init__(self, driver: webdriver,url,folder)->None:
        self.driver = driver
        self.url = url
        self.folder= folder
        BACKSPACE = '/ue003'
        ENTER = '/ue007'
        TAB = '/ue004'

    def run(self)->None:

        if not os.path.isdir(self.folder):
            os.mkdir(self.folder)

        print(os.getcwd())

        self.driver.find_element_by_name('login_id').send_keys('green')
        self.driver.find_element_by_name('login_pwd').send_keys('green1234*')
        self.driver.find_element_by_xpath('//*[@id="contentsArea"]/div/div/img').click()


        url01 = "http://wms.greenserve.co.kr/iWorks"
        self.driver.get(url01)
        self.driver.implicitly_wait(1)

        l = window_after = self.driver.window_handles
        print("length :", l)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.window(l[1])
        self.driver.close()
        self.driver.implicitly_wait(2)

        self.driver.switch_to.window(l[0])

        self.driver.find_element_by_xpath('//*[@id="main_menu"]')
        temp = self.driver.find_elements_by_xpath('//*[@id="menu_base"]')[0].get_attribute('class')
        print(temp)
        btn = self.driver.find_elements_by_xpath(
            '/html/body/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[4]/div/a[8]')[0]
        self.driver.execute_script("arguments[0].click();", btn)

        # driver.find_element_by_xpath('//*[@id="sub_tree"]')
        # //*[@id="menu_base"]
        self.driver.find_element_by_xpath('//*[@id="sub_tree"]/ul')
        time.sleep(3)
        # 구매발주등록
        self.driver.find_element_by_xpath('//*[@id="sub_tree"]/ul/li[6]/div/span/img').click()
        self.driver.switch_to.frame('iwbm2010')

        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="btnExcel"]').click()

        time.sleep(3)
        print("execel problem")
        time.sleep(5)
        self.driver.close()

        rf.getfiles(os.getcwd()+"\\"+ self.folder, self.folder)





"""
url = "http://wms.greenserve.co.kr/"
folder = "base_info_mster_client_info_manage"
options = webdriver.ChromeOptions()


profile = {
    "download.default_directory": os.getcwd() + "\\" + folder,
    "download.prompt_for_download": False,
    # "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "profile.default_content_setting_values.automatic_downloads": 1
    #"profile.default_content_setting_values.notifications": 1
}

options.add_experimental_option("prefs", profile)
# D:\chromedriver.exe
driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
driver.get(url)

cr_0 = cr_13(driver,url,folder)
cr_0.run()
"""