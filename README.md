# 搶課機器人

## 1. 下載程式碼
` git clone https://github.com/nina16448/course-selection.git`

## 2. 要下載符合自己版本的 chrome dtiver
https://googlechromelabs.github.io/chrome-for-testing/

## 3. 使用方法

### 打開程式碼 class_auto.py

### 假設說要選的課是 **漫遊聲樂的世界** ，這堂課在第1頁中
![](https://i.imgur.com/yoecc1P.png)

### 那就先點進其他頁（示範點進第2頁）
![](https://i.imgur.com/Hhg9BJQ.png)

### 接著右鍵點擊 **第1頁** 選 **複製連結網址**
![](https://i.imgur.com/8iaxSSd.jpeg)

###  **漫遊聲樂的世界** 是在第 $3$ 格，且課程代碼為 $7304012$
![](https://i.imgur.com/Xcr6HCI.png)


### 接著就將上述資訊貼到程式碼的清單中（網址太長截圖放不下）
![](https://i.imgur.com/tyi9cmj.png)

### 有幾堂要搶的就重複上述過程，如下
![](https://i.imgur.com/oQUM2mK.png)



### 最後最重要的步驟，加上一個終止條件，隨便複製一頁剛剛沒用到的網址
![](https://i.imgur.com/TfRfON8.jpeg)

### 加在清單中最後一項，後面兩個參數設為 $0$
![](https://i.imgur.com/CeGjFD0.png)

### 最後就可以執行程式了:D

## 4. 執行程式
`python class_auto.py`