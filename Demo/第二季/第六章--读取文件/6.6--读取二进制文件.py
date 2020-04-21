import os
import base64
# 读取二进制文件
path = "C:\\Users\\iezyzhang\\Desktop\\office\\11.txt"
with open(path, mode="rb", encoding="utf-8") as fd:
    base64_data = fd.read()   # 读取二进制文件
    image_data = base64.b64decode(base64_data)  # 将二进制转码
    # 将图片转储到磁盘
    wriate_image = open("C:\\Users\\iezyzhang\\Desktop\\office\\11.jpg", mode="wb")
    wriate_image.write(image_data)
    wriate_image.close()

# 通过GUI展示图片
from tkinter import *
root = Tk()
photo = PhotoImage(file = "C:\\Users\\iezyzhang\\Desktop\\office\\11.jpg")
lal = Label(root, image = photo)
lal.pack()
mainloop()



