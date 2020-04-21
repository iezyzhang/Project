from tkinter import *
from  tkinter.messagebox import *
# 写一个类  实现两数相加的功能
class get_sum(object):
    def __init__(self):
        # 创建一个窗体
        self.frame = Tk()
        # 为窗体加标题
        self.frame.title("实现两数相加")
        # root.geometry("600x100")
        # 第一个数字文本框
        self.Entry_num01 = Entry(self.frame, font=("微软雅黑", 16), width=10)
        self.Entry_num01.pack(side=LEFT, padx=20, pady=20)
        # +
        self.Label01 = Label(self.frame, text="+", font=("微软雅黑", 16), width=10).pack(side=LEFT)

        # 第二个数字文本框
        self.Entry_num02 = Entry(self.frame, font=("微软雅黑", 16), width=10)
        self.Entry_num02.pack(side=LEFT)
        # =
        self.Label02 = Label(self.frame, text="=", font=("微软雅黑", 16), width=10).pack(side=LEFT)
        # 结果
        self.var = StringVar()
        self.Entry_num03 = Entry(self.frame, font=("微软雅黑", 16), width=10,textvariable = self.var).pack(side=LEFT)
        # 按钮
        self.Button01 = Button(self.frame, text="计算", font=("微软雅黑", 16), width=6, command = self.cal_sum).pack(side=LEFT, padx=20, pady=20)

    def run(self):
        self.frame.mainloop()

    # 实现两数相加
    def cal_sum(self):
        num01 = str(self.Entry_num01.get())
        num02 = str(self.Entry_num02.get())
        if num01.isdigit() and num02.isdigit():
            self.var.set(str(int(num01)+int(num02)))
        else:
            showinfo("系统消息！","输入的数值不是数字，无法计算")


if __name__ == '__main__':
    this_gui = get_sum()
    this_gui.run()