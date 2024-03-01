from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# 初始化 Chrome 選項
chrome_options = webdriver.ChromeOptions()

# 設置自定義 User-Agent
chrome_options.add_argument("")

# 啟動瀏覽器並應用選項
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(
    "https://inline.app/booking/-Na9q9G8SpXEYDXFblzD:inline-live-3/-Na9q9_wOPo_MMbJ-fqj"
)
input("選到了!!!!")
# 選擇3位大人
adult_picker = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[1]/div/div/main/div[3]/div[1]/div[1]/div/select/option[4]",
        )
    )
)
adult_picker.click()

# 展開日期選擇器
date_picker = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/div/div/main/div[3]/div[1]/div[2]/div")
    )
)
date_picker.click()

# 檢查8月13日是否可選，如果不可選則隨機時間重整網頁
while True:
    try:
        date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/main/div[3]/div[1]/div[3]/div[2]/div[3]/div[3]/div[1]",
                )
            )
        )
        date.click()
        break
    except:
        time.sleep(random.randint(5, 10))  # 隨機等待5到10秒
        driver.refresh()  # 重整網頁

# 進行後續的訂位操作...
