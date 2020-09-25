import tkinter

from tkinter import ttk
from PIL import Image, ImageTk


root = tkinter.Tk()

root.title(u"Software Title")
root.geometry("400x300")



# 画像を表示するための準備
image = Image.open('image/sample.png')
img = ImageTk.PhotoImage(image)
# 画像を表示するためのキャンバスの作成（黒で表示）
canvas = tkinter.Canvas(bg = "red", width=400, height=300, img)
canvas.place(x=100, y=50) # 左上の座標を指定
# キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
# canvas.create_image(30, 30, image=img, anchor=tkinter.NW)
canvas.create_image(30, 30, image=img )

root.mainloop()

