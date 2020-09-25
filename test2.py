import http.client
import json
import pandas as pd
import math

h = {'Authorization': 'Bearer <############################################>'}
conn = http.client.HTTPSConnection("qiita.com")
url = "/api/v2/items?"

# この期間に作成されたQiitaの記事情報を取得
start = '2019-04-15'
end = '2019-06-30'

# 半月ごとの日付をリスト化
date_list = [d.strftime('%Y-%m-%d') for d in pd.date_range(start, end, freq='SM')]
start_list = date_list[:-1]
end_list = date_list[1:]

# カウント用変数
num = 0
p = 0

# start_listの配列の数だけ繰り返し処理
for i in start_list:
    num += 1
    # 日付のリストから検索の開始日と終了日を取り出す
    start_date =  start_list[num - 1]
    end_date = end_list[num - 1]
    query = "&query=created:>" + start_date  + "+created:<" + end_date
    # 検索で指定した期間内に作成された記事数を取得
    conn.request("GET",  url + query, headers=h)
    res = conn.getresponse()
    res.read()
    print(res.status, res.reason)
    total_count = int(res.headers['Total-Count'])
    # 取得した記事数をもとにリクエスト回数を算出
    page_count = math.ceil(total_count / 100)
    print(start_date + "から" + end_date + "までのデータを取得します...")
    print("この期間に作成されたデータを取得するのに必要なリクエスト回数は" + str(page_count) + "回です")
    # データを取得しCSVに書き出す
    for p in range(page_count):
        p += 1
        page = "page=" + str(p)
        conn.request("GET", url + page + query, headers=h)
        res = conn.getresponse()
        print(res.status, res.reason)
        data = res.read().decode("utf-8")
        df = pd.read_json(data)
        df.to_csv("qiita2.csv", columns=[
            'likes_count', 
            'created_at',
            'title',
            'url'
            ], mode='a', header=False, index=False)
        print(str(p) + "/" + str(page_count) + "完了")
