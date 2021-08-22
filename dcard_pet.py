import sys
import requests
import json
import os
import wget
import time


def text_cleanup(text):
    new = ""
    for i in text:
        if i not in '\?.!/;:"':
            new += i
    return new


url = "https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true"
reqs = requests.get(url)
reqsjson = json.loads(reqs.text)

total_num = len(reqsjson)
for i in range(0, total_num):

    if not os.path.isdir('Figure'):  # 檢查是否已經有了
        os.mkdir('Figure')  # 沒有的用標題建立資料夾

    title = reqsjson[i]["title"]  # 取得每篇標題
    title = text_cleanup(title)  # 標題會有非法字原要幫她去掉

    media_num = len(reqsjson[i]['media'])  # 判斷這文章圖的數量
    print(title+"檢查有沒有圖檔")
    if media_num != 0:

        path = title
        print("狀態:有圖喔!")

        for i_m in range(0, media_num):
            image_url = reqsjson[i]['media'][i_m]['url']

            filepath = 'Figure' + '/' + title + '_' + str(i_m) + '.jpg'
            if not os.path.isfile(filepath):  # 檢查是否下載過圖片，沒有就下載
                wget.download(image_url, filepath)
                # print(image_url)
    else:
        print("狀態:沒有圖QQ")

    time.sleep(3)
