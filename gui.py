import tkinter
import MySQLdb

from tkinter import ttk
from PIL import Image, ImageTk



# from tkinter import *



root = tkinter.Tk()

root.title(u"Software Title")
root.geometry("400x300")




Static1 = tkinter.Label(text=u'test')
Static1.pack()

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


for row in rows:
    Static1 = tkinter.Label(text=row[1])
    Static1.pack()



root.mainloop()

