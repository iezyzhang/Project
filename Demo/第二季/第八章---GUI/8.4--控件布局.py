from tkinter import *


root = Tk()
root.title("登录")
root.geometry("400x300+600+200")

Label_username = Label(root, text = "用户名：", font = ("微软雅黑", 15)).place(x=30,y=30)
Entry_username = Entry(root,font = ("微软雅黑", 15), width = 15).place(x=120,y=30)

Label_password = Label(root, text = "密  码：", font = ("微软雅黑", 15)).place(x=30,y=100)
Entry_password = Entry(root,font = ("微软雅黑", 15), width = 15).place(x=120,y=100)
Button_login = Button(root,text = "登录",font = ("微软雅黑", 15), width = 6).place(x=50,y=160)
Button_cencel = Button(root,text = "取消",font = ("微软雅黑", 15), width = 6).place(x=240,y=160)
root.mainloop()



