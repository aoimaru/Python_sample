import MySQLdb

class CREATE:
    conn = MySQLdb.connect(
    user='test',
    passwd='test',
    host='127.0.0.1',
    db='forge')

    cur = conn.cursor()
    sql = "select * from new_table"
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close
    conn.close


