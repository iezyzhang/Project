from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

root= Tk()
root.title("LabelFrame控件")
root.geometry("800x150")

# 在窗体加入LabelFrame
LabelFrame_quary = Labelframe(root,text="学生信息系查询")
LabelFrame_quary.pack(padx=10,pady=20)
# 在 Labelframe装控件
Label01 = Label(LabelFrame_quary, text = "学号：").pack(side = LEFT,padx=10,pady=5)
Entry01 = Entry(LabelFrame_quary, width = 15).pack(side = LEFT,padx=5,pady=5)

Label02 = Label(LabelFrame_quary, text = "姓名：").pack(side = LEFT,padx=10,pady=5)
Entry02 = Entry(LabelFrame_quary, width = 15).pack(side = LEFT,padx=5,pady=5)

Label03 = Label(LabelFrame_quary, text = "班级：").pack(side = LEFT,padx=10,pady=5)
Entry03 = Entry(LabelFrame_quary, width = 15).pack(side = LEFT,padx=5,pady=5)

Button01 = Button(LabelFrame_quary, text="查询").pack(side = LEFT,padx=10,pady=10)

root.mainloop()