from tkinter import *

# 创建一个窗体
root = Tk()
# 为窗体加标题
root.title("求两数之和")
# root.geometry("600x100")
# 第一个数字文本框
Entry_num01 = Entry(root, font = ("微软雅黑", 20), width = 10).pack(side = LEFT, padx = 20, pady = 20)

# +
Label01 = Label(root, text = "+", font = ("微软雅黑", 20), width = 10).pack(side = LEFT, padx = 20, pady = 20)

# 第二个数字文本框
Entry_num02 = Entry(root, font = ("微软雅黑", 20), width = 10).pack(side = LEFT, padx = 20, pady = 20)
# =
Label02 = Label(root, text = "=", font = ("微软雅黑", 20), width = 10).pack(side = LEFT, padx = 20, pady = 20)
# 结果
Entry_num03 = Entry(root, font = ("微软雅黑", 20), width = 10).pack(side = LEFT, padx = 20, pady = 20)
# 按钮
Button01 = Button(root, text = "计算", font = ("微软雅黑", 20) ,width = 10).pack(side = LEFT, padx = 20, pady = 20)
# 展示
root.mainloop()



