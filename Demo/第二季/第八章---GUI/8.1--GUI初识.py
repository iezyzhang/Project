import tkinter as tk

# 添加窗体
root = tk.Tk()
# 为窗体添加标题
root.title("Python窗体")
# 指定窗体大小
root.geometry("400x300")
# 添加一个标签
Label01 = tk.Label(root, text = "第一个Label标签")
Label01.pack()
# 添加一个按钮
Buutton01 = tk.Button(root, text = "确定")
Buutton01.pack()
# 添加单行文本框
Entry01 = tk.Entry(root)
Entry01.pack()

# 展示窗体
root.mainloop()


