import os
import subprocess
import sys


# 패키지 설치 시도
try:
    import module_file as mf
    import keyboard_code
    import func_file as ff
    import xpath_data as xpath
    import sel_option as s_option


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
    import func_file as ff
    import xpath_data as xpath
    import sel_option as s_option


today_date = ff.today_input_format(),
tomorrow = ff.other_day_input_format(2)

# 크롤링 주소
url = xpath.url
folder = xpath.folder
source_url = xpath.source_url

# 폴더 생성
ff.is_make_folder(folder)

options = mf.webdriver.ChromeOptions()
profile = s_option.profile

options.add_experimental_option("prefs", profile)
driver = mf.webdriver.Chrome(xpath.driver_url, options=options)
driver.get(url)

### login
# Id
driver.find_element_by_name('username').send_keys(xpath.id)
# pwd
driver.find_element_by_name('password').send_keys(xpath.pwd)
# login button
login_button = xpath.login_button
driver.find_element_by_xpath(login_button).click()
mf.time.sleep(2)

#팝업창1 닫기
btn = driver.find_element_by_xpath(xpath.btn)
driver.execute_script("arguments[0].click();", btn)
mf.time.sleep(2)

#큰 팝업창 여러개 닫기
# /html/body/sc-window[10]/sc-toolbar/sc-button[3]
first_new_box = xpath.first_new_box
front = '/html/body/sc-window['
count = first_new_box[len(front):len(front) + 1]
print("new box count : ", count)


for i in range(int(count) * 10, 0, -1):
    try:
        name = '/html/body/sc-window[' + str(i) + ']/sc-toolbar/sc-button[3]'
        print(name)
        btn1 = driver.find_element_by_xpath(name)
        driver.execute_script("arguments[0].click();", btn1)
        mf.time.sleep(0.1)
    except:
        print("not notice pages index :", i)

#발주 납품관리
btn = driver.find_element_by_xpath(xpath.report_manage)
driver.execute_script("arguments[0].click();", btn)
mf.time.sleep(0.5)

# 발주 관리
btn_manage = xpath.btn_manage
driver.find_element_by_xpath(btn_manage).click()
mf.time.sleep(0.5)

# BOX단위 출고 라벨 발행
box_manage = xpath.box_manage
driver.find_element_by_xpath(box_manage).click()
mf.time.sleep(0.5)

#btn_c  센터 박스 선택
btn_c = xpath.btn_c
mf.time.sleep(1)
driver.find_element_by_xpath(btn_c).click()
mf.time.sleep(0.5)

dropdown = driver.find_element_by_xpath('/html/body/sc-dropdown')
li_element = dropdown.find_elements_by_tag_name('div')
print(len(li_element))

#Center List
center_list = ff.get_list_value(li_element)
print(center_list)
#center_김해, 왜관 제외 list
execept_list = center_list[1:3]
print(center_list[1:3])
mf.time.sleep(1)


# 협력회사 박스
a = xpath.a
d = xpath.d
e = xpath.e
date_select = xpath.date_select


for count in range(1, len(li_element) + 1):
    print(center_list[count-1])
    if not center_list[count-1] in execept_list:
    #if center_list[count - 1] == center_list[4]:

        print(center_list[count-1])
        list_element_name = '/html/body/sc-dropdown/sc-listbox/div[' + str(count) + ']'
        print(list_element_name)
        btn_b = driver.find_element_by_xpath(list_element_name)
        # 물류센터 선택
        driver.execute_script("arguments[0].click();", btn_b)

        if  center_list[count - 1] == center_list[4]:
            # date option
            input_date = driver.find_element_by_xpath(date_select)
            driver.execute_script("arguments[0].click();", input_date)
            ff.date_delete(input_date)
            mf.time.sleep(1)
            input_date.send_keys(tomorrow)


        # 협력회사 리스트 박스 선택
        driver.find_element_by_xpath(d).click()
        list_box = xpath.list_box
        dropdown_client = driver.find_element_by_xpath(list_box)
        li_element_client = dropdown_client.find_elements_by_tag_name('div')

        #Client firm list & Client firm Option
        client_list = ff.get_list_value(li_element_client)
        CJ_food = client_list[8]


        print("client : ", len(li_element_client))
        for count_client in range(1, len(li_element_client) + 1):
            if client_list[count_client-1] != CJ_food:
                print(client_list[count_client-1])

                driver.find_element_by_xpath(d).click()
                count_client_name = '/html/body/sc-dropdown[2]/sc-listbox/div[' + str(count_client) + ']'
                driver.find_element_by_xpath(count_client_name).click()
                mf.time.sleep(0.5)

                # 발주 구분 체크 박스 초기화
                check_box_list = []
                print("check box inited")
                check_1 = xpath.check_1
                check_2 = xpath.check_2
                check_box_list.append(check_1)
                check_box_list.append(check_2)
                driver.find_element_by_xpath(check_1).click()
                driver.find_element_by_xpath(check_2).click()
                mf.time.sleep(1)

                for check_box_i in check_box_list:
                    print("check box :", check_box_i)
                    # 체크박스 1번
                    driver.find_element_by_xpath(check_box_i).click()

                    # 입고장
                    driver.find_element_by_xpath(e).click()
                    mf.time.sleep(1)

                    dropdown_place = driver.find_element_by_xpath(xpath.input_center)
                    li_element_place = dropdown_place.find_elements_by_tag_name('div')

                    print("place :", len(li_element_place))
                    for check_p in range(1, len(li_element_place) + 1):
                        driver.find_element_by_xpath(e).click()
                        count_place_name = '/html/body/sc-dropdown[3]/sc-listbox/div[' + str(check_p) + ']'
                        #print(count_place_name)
                        driver.find_element_by_xpath(count_place_name).click()
                        mf.time.sleep(1)

                        driver.find_element_by_xpath(e).click()

                        # 조회 버튼 클릭
                        driver.find_element_by_xpath(a).click()
                        mf.time.sleep(2)

                        # 알림창 끄기

                        try:
                            b = driver.find_element_by_xpath(xpath.alert)
                            driver.execute_script("arguments[0].click();", b)
                            print("Alert")
                            mf.time.sleep(1)
                        except:
                            print("Not Alert")

                        try:
                            #연결파트
                            driver.maximize_window()
                            print("이미지 찾기")
                            mf.time.sleep(2)


                            img_capture2 = mf.pyautogui.locateOnScreen(source_url+"a11.png")
                            mf.time.sleep(0.2)
                            print(img_capture2,type(img_capture2))
                            mf.pyautogui.click(img_capture2)

                            c2 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/sc-grid/div/div/cc-grid-toolbar/div[1]/div[2]/sc-button[5]'
                            mf.time.sleep(0.2)
                            driver.find_element_by_xpath(c2).click()
                            mf.time.sleep(2)
                            # pip install opencv-python region = (100,500,100,500)
                            print("예약 시간 선택")
                            img_capture3 = mf.pyautogui.locateOnScreen(source_url+"12qq.png")
                            print(img_capture3)
                            mf.pyautogui.click(img_capture3)
                            mf.time.sleep(0.5)

                            c3 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-dt/div/div[1]/sc-grid/div/div/cc-grid-toolbar/div[1]/div[2]/sc-button'
                            mf.time.sleep(0.2)
                            driver.find_element_by_xpath(c3).click()
                            mf.time.sleep(2)

                            # code070 print("기사 선택 김갑식 007")
                            # qw12 print("기사 선택 송경희 009")
                            # qqq12 print("기사 선택 정선헌 010")qqq12
                            print("기사 선택 김갑식 070")
                            img_capture4 = mf.pyautogui.locateOnScreen(source_url+"qqq12.png")
                            print(img_capture4)
                            mf.pyautogui.click(img_capture4)
                        except:
                            mf.time.sleep(0.2)
                            alert_exc = driver.find_element_by_xpath(xpath.alert_exc)
                            driver.execute_script("arguments[0].click();", alert_exc)
                            print("alert_exc")
                            print("예약 항목 없음\n")


                    # 이전 check 박스 해제
                    driver.find_element_by_xpath(check_box_i).click()

            else :
                print("CJ foodbill",client_list[count_client-1])

            # 물류 선택을 위해 리스트 박스 재선택
            driver.find_element_by_xpath(btn_c).click()
            mf.time.sleep(0.2)

    else:
        print("except list : ",center_list[count - 1])
# driver.close()