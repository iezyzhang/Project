"""
输入一个北京的日期和时间，计算出其他城市的日期和时间
【1】时区提示：北京东八时区
	          纽约西五时区，比北京慢13个小时
	          伦敦零时区，比北京慢8个小时
              东京东九时区，比北京快1个小时
              悉尼东十时区，比北京快3个小时

默认情况下显示当前的时间

"""

from tkinter import *
from datetime import datetime, timedelta
import time


class TimeZoneWindow():
    def __init__(self):
        self.frame = Tk()
        self.frame.title("时间")
        self.frame.geometry("500x400+400+200")
        self.frame.resizable(0, 0)

        self.setup_UI()

        # 自动加载
        self.get_time()

    def setup_UI(self):
        self.Label_beijing = Label(self.frame, text="北京时间：", font=("微软雅黑", 12, "bold"))
        self.Label_beijing.place(x=50, y=50)
        self.var_time = StringVar()
        self.Entry_beijing = Entry(self.frame, textvariable=self.var_time, width=25, font=("微软雅黑", 12, "bold"))
        self.Entry_beijing.place(x=150, y=50)

        self.Label_london = Label(self.frame, text="伦敦时间：", font=("微软雅黑", 12, "bold"))
        self.Label_london.place(x=50, y=100)

        self.Label_london_time = Label(self.frame, text="当前的伦敦时间", fg="red", font=("微软雅黑", 12, "bold"))
        self.Label_london_time.place(x=150, y=100)

        self.Label_newyork = Label(self.frame, text="纽约时间：", font=("微软雅黑", 12, "bold"))
        self.Label_newyork.place(x=50, y=150)

        self.Label_newyork_time = Label(self.frame, text="当前的纽约时间", fg="red", font=("微软雅黑", 12, "bold"))
        self.Label_newyork_time.place(x=150, y=150)

        self.Label_tokyo = Label(self.frame, text="东京时间：", font=("微软雅黑", 12, "bold"))
        self.Label_tokyo.place(x=50, y=200)

        self.Label_tokyo_time = Label(self.frame, text="当前的东京时间", fg="red", font=("微软雅黑", 12, "bold"))
        self.Label_tokyo_time.place(x=150, y=200)

        self.Label_sydney = Label(self.frame, text="悉尼时间：", font=("微软雅黑", 12, "bold"))
        self.Label_sydney.place(x=50, y=250)

        self.Label_sydney_time = Label(self.frame, text="当前的悉尼时间", fg="red", font=("微软雅黑", 12, "bold"))
        self.Label_sydney_time.place(x=150, y=250)

    def show(self):
        self.frame.mainloop()

    def get_time(self):
        """
        获取当前的时间
        :return:
        """
        while True:
            # 获取当前时间
            bj_time = datetime.today()

            # 展示出来  2018-10-10 20:10:12
            self.var_time.set("%04d-%02d-%02d %02d:%02d:%02d" % (bj_time.year, bj_time.month, bj_time.day,
                                                                 bj_time.hour, bj_time.minute, bj_time.second))

            # 伦敦时间
            london_time = datetime.today() + timedelta(hours=-8)
            self.Label_london_time["text"] = (
                        "%04d-%02d-%02d %02d:%02d:%02d" % (london_time.year, london_time.month, london_time.day,
                                                           london_time.hour, london_time.minute, london_time.second))
            # 纽约时间
            newyork_time = datetime.today() + timedelta(hours=-13)
            self.Label_newyork_time["text"] = (
                        "%04d-%02d-%02d %02d:%02d:%02d" % (newyork_time.year, newyork_time.month, newyork_time.day,
                                                           newyork_time.hour, newyork_time.minute, newyork_time.second))

            # 东京时间
            tokyo_time = datetime.today() + timedelta(hours=1)
            self.Label_tokyo_time["text"] = (
                    "%04d-%02d-%02d %02d:%02d:%02d" % (tokyo_time.year, tokyo_time.month, tokyo_time.day,
                                                       tokyo_time.hour, tokyo_time.minute, tokyo_time.second))

            # 东京时间
            sydney_time = datetime.today() + timedelta(hours=3)
            self.Label_sydney_time["text"] = (
                    "%04d-%02d-%02d %02d:%02d:%02d" % (sydney_time.year, sydney_time.month, sydney_time.day,
                                                       sydney_time.hour, sydney_time.minute, sydney_time.second))

            # 让时间停1秒
            time.sleep(1)

            # 更新gui
            self.frame.update()


if __name__ == "__main__":
    time01 = TimeZoneWindow()
    time01.show()