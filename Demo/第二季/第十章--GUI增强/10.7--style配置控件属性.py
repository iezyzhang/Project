from tkinter import *
from tkinter.ttk import *

root= Tk()
root.title("Style控件")
root.geometry("400x300")
style01 = Style()
style01.configure("TLabel",font = ("微软雅黑",16),background = "green",foreground = "blue")

Label01 = Label(root, text = "用户名", style ="TLabel")
Label01.pack(padx= 20,pady=20)
Label02 = Label(root, text = "用户名")
Label02.pack(padx= 20,pady=20)
Button01 = Button(root,text = "确定",width = 40, style ="TLabel").pack(padx = 10,pady =20)
Button02 = Button(root,text = "确定").pack(padx = 10,pady =20)
root.mainloop()

# 总结：1、如果在配置style的时候紧紧填写标准的style 名字，那么生效的是stylename对应的控件，无论是否绑定控件
# 2、如果只想对某类中的某些控件生效，必须使用自定义的名称，加标准style名字--自定义名字.stylename