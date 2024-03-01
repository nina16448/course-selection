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
URL1 = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class/Add_Course01.cgi?session_id=rjjddYhAZFYodqmz5c0RksbQAUS1EeT3Y086&use_cge_new_cate=1&m=0&dept=4106&grade=1&page=1"
URL2 = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class/Add_Course01.cgi?session_id=rjjddYhAZFYodqmz5c0RksbQAUS1EeT3Y086&use_cge_new_cate=1&m=0&dept=4106&grade=1&page=2"
driver.get(URL1)

while check == False:
    now = datetime.now()
    wait_time = random.uniform(0.1, 2)
    time.sleep(wait_time)

    if state == 1:
        check = selection_class(1, 4105004)  # 課程是該頁的第幾個，以及課程代碼
        state = 2
        driver.get(URL2)
        if check == True:
            break

    elif state == 2:
        state = 1
        driver.get(URL1)
        if check == True:
            break

input("選到了!!!!")
