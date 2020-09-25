import MySQLdb

# 接続する
conn = MySQLdb.connect(
 user='test',
 passwd='test',
 host='127.0.0.1',
 db='forge')

# カーソルを取得する
cur = conn.cursor()


# sql = "insert into new_table value(2, 'hello');"

# cur.execute(sql)

# SQL（データベースを操作するコマンド）を実行する
# userテーブルから、HostとUser列を取り出す
sql = "select * from new_table"
cur.execute(sql)



# 実行結果を取得する
rows = cur.fetchall()

# 一行ずつ表示する
for row in rows:
    print(row)


cur.close
conn.close

