import tkinter as tk

# 新建一个窗体
root = tk.Tk()
# 为窗体添加标题
root.title("Python窗体")
photo = tk.PhotoImage(file = "C:\\Users\\iezyzhang\\Desktop\\office\\11.jpg")
# 添加标签
Label01 = tk.Label(root, text = "第一个Label标签",width = 30, height = 5, fg = "red", bg = "blue",
                   font = ("微软雅黑", 20), anchor = "w")
Label01.pack()

Label02 = tk.Label(root, text = "第一个Label标签")
Label02.pack()

Buutton01 = tk.Button(root, text = "确定")
Buutton01.pack()
# 显示
root.mainloop()

# pack()布局把控件一个个放在容器中
