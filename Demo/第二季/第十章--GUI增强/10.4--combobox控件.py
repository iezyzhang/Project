from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
# Combobox控件----下拉框

def sel_gender(*args):
    showinfo("系统提示！","你选择的性别：" + combo_gender.get())

def sel_edu(*args):
    showinfo("系统提示！","你选择的性别：" + combo_edu.get())

root= Tk()
root.title("Combobox控件")
root.geometry("400x300")

# 性别单选
Label_gender = Label(root, text = "性别：")
Label_gender.grid(row = 0, column = 0, padx = 20, pady = 20,sticky = "w")

gender = StringVar()
combo_gender = Combobox(root, textvariable = gender)
combo_gender["values"] = ["男", "女"]
combo_gender["state"] = "readonly"
combo_gender.current(0)
combo_gender.grid(row=0,column=1,padx=10,pady=10)

# 绑定选择性别事件
combo_gender.bind("<<ComboboxSelected>>", sel_gender)

Label_edu = Label(root, text = "学历：")
Label_edu.grid(row = 1, column = 0, padx = 20, pady = 20,sticky = "w")

education = StringVar()
combo_edu = Combobox(root, textvariable = education)
combo_edu["values"] = ["专科","本科","硕士","博士"]
combo_edu["state"] = "readonly"
combo_edu.current(2)   # 默认选择
combo_edu.grid(row = 1, column = 1,padx=10,pady=10)
combo_edu.bind("<<ComboboxSelected>>", sel_edu)
root.mainloop()
