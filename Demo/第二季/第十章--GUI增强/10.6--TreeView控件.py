from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("学生信息")
root.geometry("500x300+500+200")

# frame容易放置表格
frame01 = Frame(root)
frame01.place(x=10, y=10, width = 480, height = 380)

# 加载滚动条
scrollBar = Scrollbar(frame01)
scrollBar.pack(side = RIGHT, fill = Y)

# 准备表格
tree =  Treeview(frame01, columns= ("学号", "姓名", "性别", "年龄", "手机号码"), show = "headings", yscrollcommand = scrollBar.set)

# 设置每一列的宽度和对齐方式
tree.column("学号", width = 80, anchor = "center")
tree.column("姓名", width = 90, anchor = "center")
tree.column("性别", width = 60, anchor = "center")
tree.column("年龄", width = 60, anchor = "center")
tree.column("手机号码", width = 180, anchor = "center")

# 设置表头的标题文本
tree.heading("学号", text= "学号")
tree.heading("姓名", text= "姓名")
tree.heading("性别", text= "性别")
tree.heading("年龄", text= "年龄")
tree.heading("手机号码", text= "手机号码")

# 设置关联
scrollBar.config(command = tree.yview)

# 插入数据
for i in range(100):
    tree.insert("", i, values = ["95001" ,"张三","男","23","15083333479"])

# 加载表格信息
tree.pack()

root.mainloop()



