import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from multiprocessing import Process, Queue
import multiprocessing as mp
import datetime
import time
import os
from selenium import webdriver
from PyQt5 import uic
import new_cr_3_test as cr
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import schedule

def producer(q):
    proc = mp.current_process()
    print(proc.name)

    while True:
        now = datetime.datetime.now()
        data = str(now)
        q.put(data)
        time.sleep(1)

def producer1(q):
    proc = mp.current_process()
    print(proc.name)

    url = "http://wms.greenserve.co.kr/"
    folder = "Order_Manage_Per_client_order_details_schedule"
    options = webdriver.ChromeOptions()

    profile = {
        "download.default_directory": os.getcwd() + "\\" + folder,
        "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.automatic_downloads": 1
        # "profile.default_content_setting_values.notifications": 1
    }

    options.add_experimental_option("prefs", profile)
    # D:\chromedriver.exe
    print("1")
    driver = webdriver.Chrome('F:\chromedriver_win32\chromedriver.exe', options=options)
    print("2")
    driver.get(url)
    print("3")

    now = cr.cr_0(driver,url,folder).run()
    print("4")
    q.put(now)


class Consumer(QThread):
    poped = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            if not self.q.empty():
                data = q.get()
                self.poped.emit(data)


class Consumer1(QThread):
    poped1 = pyqtSignal(str)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if not self.q.empty():
            data1 = q.get()
            self.poped1.emit(data1)


class MyWindow(QMainWindow):
    def __init__(self, q,qq):
        super().__init__()


        self.setGeometry(200, 200, 300, 200)

        # thread for data consumer
        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.print_data)
        self.consumer.start()
        self.consumer1 = Consumer1(qq)
        self.consumer1.poped1.connect(self.print_data1)
        self.consumer1.start()
        btn1  = QPushButton("button",self)
        btn1.move(20,20)
        btn1.clicked.connect(self.button_clicked1)

    @pyqtSlot()
    def button_clicked1(self):
        pp = Process(name="producer1", target=producer1, args=(qq,), daemon=True)
        pp.start()

    @pyqtSlot(str)
    def print_data(self, data):
        self.statusBar().showMessage(data)

    @pyqtSlot(str)
    def print_data1(self, data1):
        print(data1)



if __name__ == "__main__":
    q = Queue()
    qq = Queue()


    # producer process
    p = Process(name="producer", target=producer, args=(q, ), daemon=True)
    p.start()

    # Main process
    app = QApplication(sys.argv)
    mywindow = MyWindow(q,qq)
    mywindow.show()
    app.exec_()