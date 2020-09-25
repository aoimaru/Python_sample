import sqlite3
 
dbfile = sqlite3.connect('example.db')
c = dbfile.cursor()
 
# sql = 'create table Test_table(atai1,atai2,atai3);'
# c.execute(sql)
 
sql = "insert into Test_table values(3,'Second value',0.56);"
c.execute(sql)

sql2 = "insert into Test_table values(4,'Third value',0.67);"
c.execute(sql2)
 
dbfile.commit()
dbfile.close()

