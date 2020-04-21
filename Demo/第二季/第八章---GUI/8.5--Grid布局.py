from tkinter import *

# 新建一个窗体
root = Tk()
# 为窗体添加标题
root.title("Python窗体")
root.geometry("800x400")
photo = PhotoImage(file = "C:\\Users\\iezyzhang\\Desktop\\office\\11.gif")
img_Label = Label(root, image = photo).grid(row = 0,column = 0,rowspan = 2)
# 第一行第二列
Label_username = Label(root, text = "用户名：", font = ("微软雅黑", 15)).grid(row=0,column=1)
# 第一行第三列
Entry_username = Entry(root,font = ("微软雅黑", 15), width = 16).grid(row=0,column=2)
# 第二行第二列
Label_password = Label(root, text = "密  码：", font = ("微软雅黑", 15)).grid(row=1,column=1)
# 第二行第三列
Entry_password = Entry(root,font = ("微软雅黑", 15), width = 16).grid(row=1,column=2)
# 第三行空着
# 第四行第三列
Button_login = Button(root,text = "登录",font = ("微软雅黑", 15), width = 5).grid(row=2,column=2,sticky = "w")
Button_cencel = Button(root,text = "取消",font = ("微软雅黑", 15), width = 5).grid(row=2,column=2,sticky = "e")
root.mainloop()

