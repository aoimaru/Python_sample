import sqlite3

dbfile = sqlite3.connect('example.db')
c = dbfile.cursor()



sql = "select * from Test_table;"

for row in c.execute(sql):
    print(row)

sql="select name from sqlite_master where type='table';"

for table in c.execute(sql):
    print(table)

dbfile.close()
