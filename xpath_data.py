source_url = "C:/Users/그린써브(D)/Desktop/ff/source/"
driver_url = "C:/Users/그린써브(D)/Desktop/chromedriver.exe"
edge_url = "C:/Users/그린써브(D)/Desktop/msedgedriver.exe"
IE_url = "C:/Users/그린써브(D)/Desktop/IEDriverServer.exe"

id = 'green'
pwd = 'gs2580/**'

# 크롤링 주소
url = "https://srm.welstory.com/splogin.do"
folder = "Delivery_managenet_per_product_seles_performance"


a = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[2]/div/sc-button'
d = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[1]/td[2]/cc-vd-auto-complete/sc-combobox-field/div"
e = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[2]/sc-combobox-field/div'
f = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[2]/td[3]/sc-combobox-field/div"



date_select = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[2]/td[1]/sc-date-field/div/input"
login_button = '/html/body/div/div[1]/div/form/div[1]/a'

#팝업창1
btn ='/html/body/sc-messagebox/sc-toolbar[2]/sc-button'



#큰 팝업창 여러개 닫기
first_new_box = '/html/body/sc-window[20]/sc-toolbar/sc-button[3]'
first_new_box1 = "/html/body/sc-window[9]/sc-toolbar/sc-button[3]"
"/html/body/sc-window[10]/sc-toolbar/sc-button[3]"
#발주관리
btn_manage = '/html/body/sc-mdi/div[1]/div[2]/sc-mdi-topmenu/div[2]/ul/li[1]'

#order_manage
order_manage = "/html/body/sc-mdi/div[1]/div[2]/sc-mdi-topmenu/div[2]/ul/li[2]"

# receive_button
receive_button = "/html/body/sc-mdi/div[1]/div[2]/sc-mdi-topmenu/div[2]/ul/li[2]/ul/li[4]/a/span"

# receive- center_list
receive_center ='/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-asn-print/sc-pages/es-asn-print/cc-search-container/div[1]/div[1]/table/tbody/tr[1]/td[1]/cc-operorg-plt-combobox-field/div/sc-combobox-field[2]/div'
#발주 납품관리
report_manage = '//*[@id="SPO90000"]/a/span'

## center_get_list
center_address = "/html/body/sc-dropdown[1]/sc-listbox"

## date_checkbox_edge
date_checkbox = \
            "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-asn-print/sc-pages/es-asn-print/cc-search-container/div[1]/div[1]/table/tbody/tr[2]/td[1]/sc-date-field/div/input"

#firm edge
firm_address = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-asn-print/sc-pages/es-asn-print/cc-search-container/div[1]/div[1]/table/tbody/tr[1]/td[2]/cc-vd-auto-complete/sc-combobox-field/div"

#firm_list_address
firm_list_address = "/html/body/sc-dropdown[2]/sc-listbox"

#search_button
search_button_address = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-asn-print/sc-pages/es-asn-print/cc-search-container/div[1]/div[2]/div/sc-button/div"

#value_alert
address_alert = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-asn-print/sc-pages/es-asn-print/sc-grid/div/div/cc-grid-toolbar/div[1]/span"

order_button_address = "/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-asn-print/sc-pages/es-asn-print/sc-grid/div/div/cc-grid-toolbar/div[1]/div[2]/sc-button"

close_order_address = "/html/body/sc-window[10]/sc-toolbar/sc-button[3]"

# 협력회사 리스트 박스 선택
list_box = '/html/body/sc-dropdown[2]'

#mi
label_count = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/sc-toolbar/sc-label[8]/span[2]'

# BOX단위 출고 라벨 발행
box_manage = '/html/body/sc-mdi/div[1]/div[2]/sc-mdi-topmenu/div[2]/ul/li[1]/ul/li[5]/a/span'

#btn_c  센터 박스 선택
btn_c = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[1]/td[1]/cc-operorg-plt-combobox-field/div/sc-combobox-field[2]' #/div'

#알림창 끄기
alert = '/html/body/sc-messagebox/sc-toolbar[2]/sc-button'

# 발주 구분 체크 박스 초기화

check_1 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[1]/div/sc-checkbox-field[1]/div'
check_2 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[1]/div/sc-checkbox-field[2]/div'

check_11 ='#order1 > div'
check_22 = '#order2 > div'

#checkbox
a1='<div class="check-default style-scope sc-checkbox-field checked">2차주문(20시)</div>'
a2 = '<div class="check-default style-scope sc-checkbox-field">2차주문(20시)</div>'


#입고장
input_center = '/html/body/sc-dropdown[3]'

#입고예약버튼
c2 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/sc-grid/div/div/cc-grid-toolbar/div[1]/div[2]/sc-button[5]'
# 입고 예약 캠버스 버튼
#입고예약 예외 알림 & 발주구분 미표시에 발생하는 알림
alert_exc = '/html/body/sc-messagebox/sc-toolbar[2]/sc-button'


# 시간선택
c3 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-dt/div/div[1]/sc-grid/div/div/div[1]/div/canvas'

#최종 입고예약 버튼
c4 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-dt/cc-page-title-bar/div/sc-button[1]'

# 최종 입고예약 확인 취소 버튼
c5 = '/html/body/sc-messagebox/sc-toolbar[2]/sc-button[1]'
'/html/body/sc-messagebox/sc-toolbar[2]/sc-button[1]'
'/html/body/sc-messagebox/sc-toolbar[2]/sc-button'
'/html/body/sc-messagebox/sc-toolbar[2]/sc-button'
#최종 입고예약  확인 버튼
c6 = '/html/body/sc-messagebox/sc-toolbar[2]/sc-button'
c7 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-dt/cc-page-title-bar/div/sc-button[1]'

# 입고예약 미처리
incompleted_deal = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/sc-toolbar/sc-label[6]/span[2]'

# 배송 방식 설정
deliver_button = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[4]/sc-combobox-field/div'
deliver_list = "/html/body/sc-dropdown[4]"
#temp_sc = "/html/body/sc-dropdown["+4+"]"
"/html/body/sc-dropdown[2]/sc-listbox/div[1]"
"/html/body/sc-dropdown[1]"

#직송 마지막 예약버튼
directly_deliv = "/html/body/sc-messagebox/sc-toolbar[2]/sc-button"

check_box1 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[1]/div/sc-checkbox-field[1]'
check_box2 = '/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[1]/div/sc-checkbox-field[2]'
"/html/body/sc-mdi/div[2]/sc-mdi-content/sc-pages/sc-mdi-window[2]/em-fc-po-label-box-list/sc-pages/es-fc-po-label-box-list/cc-search-container/div[1]/div[1]/table/tbody/tr[3]/td[1]/div/sc-checkbox-field[2]/div"
############################## 이미지 모음  #############################
# 미리 체크된 이미지 찾기
checked_image = "a_4_9.png"#"a_4_9.png"

# 입고 예약 캠버스 버튼
input_reserve_image = "a_3.png"#"a_3.png"


# 상세 입고 예약 차량 번호 선택
## 김갑식
reserve_truck_driver_kim = "new_kimg.png"
reserve_truck_driver_kim1 = "new_only_kim.png"
reserve_truck_driver_kim_ch2= "ch2.png"
reserve_truck_driver_kim_27_1= "kim_27_1.png"
reserve_truck_driver_kim_27_2= "kim_27_2.png"
reserve_truck_driver_kim_27_3= "kim_27_3.png"

## 정성헌
reserve_truck_driver_jeong = "new_jeong.png"
reserve_truck_driver_jeong1 = "new_jeong.png"
reserve_truck_driver_jeong2 = "new_jeong.png"
reserve_truck_driver_jeong3 = "new_jeong.png"
## cj 김갑식
reserve_truck_driver_kim_cj = "cj_kim.png"
reserve_truck_driver_kim1_cj = "cj_kim1.png"
reserve_truck_driver_other_cj = "cj_other.png"
## CJ 대체
reserve_truck_driver_other_cj1 = "cj_others.png"
reserve_truck_driver_other_cj2 ='others_999.png'
reserve_truck_driver_other_cj3 ='ch.png'
reserve_truck_driver_other_cj4 ='cj_kim_ab.png'

## 송경희
reserve_truck_driver_song = "new_song.png"
reserve_truck_driver_song1 = "new_only_song.png"
reserve_truck_driver_song2 = "song_2.png"
##other
#reserve_truck_driver_other = "other.png"

# 상세 입고 예약 시간 선택
reserve_time_set_1730 = "new_1730.png"
reserve_time_set_2100 = "new_2100.png"

reserve_time_set_2100_1 = "new_2100.png"
reserve_time_set_2100_2 ="new_2100.png"
reserve_time_set_2100_3 ="new_2100_b.png"

#김해
reserve_time_set_2100_kimhae="re_2100.png"
#제주
reserve_time_set_1900_jeju="jeju_1900.png"
reserve_time_set_1730_jeju="jeju_1730.png"
#용인
reserve_time_set_2100_young="young_2100.png"
reserve_time_set_2100_young2="young2_2100.png"
reserve_time_set_1730_young="young_1730.png"


#광주
reserve_time_set_2100_gwang = "gwang_2100.png"

alarm_temp = "migomoon.png"

