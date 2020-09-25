import tkinter

import http.client
import json
import math

CONN = http.client.HTTPSConnection('qiita.com', 443)
USER_ID = 'riekure'
PER_PAGE = 100



class Api:
    # リクエスト結果をJSON形式で返す
    @staticmethod
    def request(http, url) :
        CONN.request(http, url)
        res = CONN.getresponse()
        data = res.read().decode('utf-8')
        return json.loads(data)

    # 投稿数とからページ番号を計算する
    @staticmethod
    def page_count(items_count) :
        return math.floor(items_count / PER_PAGE) + 1

# 投稿数を取得
items_count = Api.request('GET', '/api/v2/users/' + USER_ID)['items_count']
page = Api.page_count(items_count)

# 投稿記事を全て取得
for i in range(page) :
     article = Api.request('GET', '/api/v2/users/' + USER_ID + '/items?page=' + str(i+1) + '&per_page=' + str(PER_PAGE))

     root = tkinter.Tk()

     root.title(u"Software Title")
     root.geometry("400x300")
     for j in range(PER_PAGE) :
         try :
             Static1 = tkinter.Label(text=article[j]['title'])
             Static1.pack()
             
         except IndexError :
             print("ok")
             break