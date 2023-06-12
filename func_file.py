import os
import subprocess
import sys


# 패키지 설치 시도
try:
    import module_file as mf
    import keyboard_code

    import xpath_data as xpath


except:
    libraries = ['selenium', 'bs4', 'pandas', 'datetime', 'html_table_parser', 'reguests', 'atlassian-python-api',
                 'pyautogui']
    for i in libraries:
        if i == 'pyautogui':
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
        else:
            print("expe")
            #subprocess.check_call([sys.executable, ' conda install - c conda - forge pyautogui', i])

    import module_file as mf
    import keyboard_code

    import xpath_data as xpath




#value값 가져오는 함수
def get_list_value(list):
    list_value = []
    for element in list:
        list_value.append(element.text)

    return list_value

def date_delete(object_t):
    for k in range(0, 8):
        object_t.send_keys(mf.Keys.BACKSPACE)

def today_input_format():
    today = str(mf.datetime.today().strftime("%Y/%m/%d"))
    return today

def sch_input_format():
    today = str((mf.datetime.now()+ mf.timedelta(minutes=1)).strftime("%H:%M"))
    return today

def sch_hour_format():
    today = str((mf.datetime.now()+ mf.timedelta(minutes=1)).strftime("%H"))
    return int(today)

def sch_day_format():
    today = str((mf.datetime.now()+ mf.timedelta(minutes=1)).strftime("%d"))
    return int(today)

def sch_year_format():
    today = str((mf.datetime.now()+ mf.timedelta(minutes=1)).strftime("%Y"))
    return int(today)

def sch_month_format():
    today = str((mf.datetime.now()+ mf.timedelta(minutes=1)).strftime("%m"))
    return int(today)

def log_input_format_tdoay():
    today = str(mf.datetime.today().strftime("%Y_%m_%d_%H_%M"))
    return  today

def today_input_format_detail():
    today = str(mf.datetime.now())
    return today

def today_input_format_check():
    week_idx = mf.datetime.today().weekday()
    return week_idx

def other_day_input_format(day):
    other_day = mf.datetime.today() + mf.timedelta(day)
    other_day = str(other_day.strftime("%Y/%m/%d"))
    return other_day

def is_make_folder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    print(os.getcwd())


class car_driver:
    def __init__(self, Kim, Jeong, Song, Park, An):
        #평택 김갑식, 정성헌
        self.Kim =  Kim
        self.Jeong = Jeong

        #용인 송경희, 정성헌
        self.Song = Song

        # 다른 차량 안승진, 박신수
        self.Park =Park
        self.An =  An

    def car_driver_count(self):
        # 평택 김갑식, 정성헌
        self.Kim = self.Kim+1
        self.Jeong = self.Jeong+1
        # 용인 송경희, 정성헌
        self.Song = self.Song+1
        # 다른 차량 안승진, 박신수
        self.Park = self.Park+1
        self.An =  self.An+1

