import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
#from html_table_parser import parser_functions as parser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import rename_filename as rf

class cr_10:
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

        self.driver.find_element_by_xpath('//*[@id="main_menu"]')
        temp = self.driver.find_elements_by_xpath('//*[@id="menu_base"]')[0].get_attribute('class')
        print(temp)
        btn = self.driver.find_elements_by_xpath(
            '/html/body/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[4]/div/a[8]')[0]
        self.driver.execute_script("arguments[0].click();", btn)

        time.sleep(3)
        # 구매발주등록
        self.driver.find_element_by_xpath('//*[@id="sub_tree"]/ul/li[3]/div/span/img').click()
        #  /html/body/table/tbody/tr[2]/td/div[2]/div[1]/div[2]/ul/li[2]/ul/li[9]
        self.driver.switch_to.frame('iwbm3040')
        # iwsm4070



        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        self.driver.implicitly_wait(10)
        dropdown = self.driver.find_element_by_class_name('k-pager-numbers')
        li_element = dropdown.find_elements_by_tag_name('li')
        print(len(li_element))

        if len(li_element) == 1:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div[3]/div/ul/li')))
            element.click()
            self.driver.implicitly_wait(10)

            html = self.driver.page_source
            soup = BeautifulSoup(html)

            temp = soup.find_all('table')
            columns = parser.make2d(temp[4])
            content = parser.make2d(temp[5])
            print(columns)

            df = pd.DataFrame(content[:-1], columns=columns[0])

            print(df.head(10))
            df.to_csv("./" + self.folder + "./" + self.folder + "_" + str(datetime.date.today()) + ".csv", encoding='utf-8-sig')
            print("kkkk")


        elif len(li_element) > 1:

            content_total_list = []
            for count in range(1, len(li_element) + 1):
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[5]/div[2]/div[3]/div/ul/li[' + str(count) + ']')))
                element.click()

                self.driver.implicitly_wait(10)

                html = self.driver.page_source
                soup = BeautifulSoup(html)

                temp = soup.find_all('table')
                columns = parser.make2d(temp[4])
                content = parser.make2d(temp[5])
                print(content)
                content_total_list = content_total_list + content[:-1]
                print(columns)

            df = pd.DataFrame(content_total_list, columns=columns[0])

            print(df.head(10))
            df.to_csv("./" +self.folder + "./" + self.folder + "_" + str(datetime.date.today()) + ".csv", encoding='utf-8-sig')

            print("kkkk", count)

        print("execel 10")
        self.driver.implicitly_wait(10)
        self.driver.close()

        rf.getfiles(os.getcwd()+"\\"+ self.folder, self.folder)



