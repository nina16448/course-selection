from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import random
import time


def selection_class(index, id):
    index_c = str(index + 1)
    id_c = str(id) + "_01"
    font_name = driver.find_element(
        By.XPATH,
        f"//table[@border='0' and @width='100%']/tbody/tr[1]/th[@colspan='2']/table[@border='1' and @width='100%']/tbody/tr[{index_c}]/th[4]",
    )
    font_elem1 = driver.find_element(
        By.XPATH,
        f"//table[@border='0' and @width='100%']/tbody/tr[1]/th[@colspan='2']/table[@border='1' and @width='100%']/tbody/tr[{index_c}]/th[3]",
    )
    print(now.strftime("%H:%M:%S"), " ", font_name.text, " ", font_elem1.text)
    if int(font_elem1.text) > 0:
        button = driver.find_element(
            By.CSS_SELECTOR, f"input[type='checkbox'][name='course'][value='{id_c}']"
        )
        button.click()
        button = driver.find_element(
            By.CSS_SELECTOR, "input[type='submit'][value='加選以上標記科目']"
        )
        button.click()
        return True
    return False


driver = webdriver.Chrome()

state = 1
check = False
my_list = [0, 0, 0]

# [那頁的網址, 課程是該頁的第幾個，以及課程代碼]
URL_list = [
    [
        "http://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class/Add_Course01.cgi?session_id=AbULubSjXpg4NFeiNAxuwIDhWoE82Ac0E134&use_cge_new_cate=1&m=0&dept=I001&grade=1&page=1&cge_cate=2&cge_subcate=5",
        8,
        7403008,
    ],  # 電影與國際關係
    [
        "http://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class/Add_Course01.cgi?session_id=AbULubSjXpg4NFeiNAxuwIDhWoE82Ac0E134&use_cge_new_cate=1&m=0&dept=I001&grade=1&page=2&cge_cate=2&cge_subcate=5",
        0,
        0,
    ],  # 空
]

while len(URL_list) >= 2:
    for Class in URL_list:
        if len(URL_list) > 2 and Class[1] == 0:
            continue

        wait_time2 = random.uniform(0.1, 2)
        time.sleep(wait_time2)
        driver.get(Class[0])

        if Class[1] == 0:
            continue
        now = datetime.now()
        check = selection_class(Class[1], Class[2])

        if check == True:  # 選到了
            print("======================= 選到了 =======================")
            URL_list.remove(Class)
            time.sleep(10)


input("選到了!!!!")
