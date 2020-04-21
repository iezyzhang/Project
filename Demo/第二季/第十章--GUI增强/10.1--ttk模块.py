from tkinter import *
from tkinter.ttk import *
root = Tk()

style01 = Style()
style01.configure("commite.TButton",font = ("微软雅黑",16),background = "green",foreground = "blue")
Button01 = Button(root,text = "确定",width = 40, style ="commite.TButton").pack(padx = 10,pady =20)
Button02 = Button(root,text = "确定").pack(padx = 10,pady =20)
root.mainloop()

