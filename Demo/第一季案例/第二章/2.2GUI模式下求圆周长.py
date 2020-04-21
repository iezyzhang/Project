from tkinter import *
from tkinter.messagebox import *
class Calaulator:

    def __init__(self):  # 构造函数  初始化GUI界面
        # 先创建一个窗体    self.frame
        self.frame = Tk()

        # 为窗体添加标题
        self.frame.title("计算圆的周长和面积")
        # 指定窗体大小
        self.frame.geometry("600x400+200+100")
        # 不允许改变窗体大小
        self.frame.resizable(0, 0)
        # 为窗体指定背景
        self.frame["bg"] = "gray"

        # 添加一个lable标签
        self.Label_input = Label(self.frame, text="请输入圆的半径：", bg = "gray", foreground="black",
                                 font = ("微软雅黑",12, "bold"))
        self.Label_input.place(x=50, y=50)

        # 添加输入文本框
        self.var_radius = StringVar()
        self.Entry_input = Entry(self.frame, textvariable=self.var_radius, font = ("微软雅黑",12, "bold"), width = 20)
        self.Entry_input.place(x=180, y=50)

        # 添加一个计算按钮
        self.Button_cel = Button(self.frame, text = "计算", font = ("微软雅黑", 9, "bold"), width = 8, command = self.get_result)
        self.Button_cel.place(x=400, y=50)

        # 添加圆的周长label
        self.Label_perimeter = Label(self.frame, text = "圆的周长：", bg = "gray", font = ("微软雅黑",12, "bold"))
        self.Label_perimeter.place(x=100, y=110)


        self.var_perimeter = StringVar()
        self.Label_perimeter_result = Label(self.frame, textvariable=self.var_perimeter,text = "圆的周长结果", bg = "gray", fg="red", font = ("微软雅黑",12, "bold"))
        self.Label_perimeter_result.place(x=200, y=110)

        # 添加圆的面积的Label
        self.Label_area = Label(self.frame, text="圆的面积：", bg = "gray", font=("微软雅黑", 12, "bold"))
        self.Label_area.place(x=100, y=150)

        self.var_area = StringVar()
        self.Label_area_result = Label(self.frame, textvariable=self.var_area,text="圆的面积结果", bg = "gray",fg="red", font=("微软雅黑", 12, "bold"))
        self.Label_area_result.place(x=200, y=150)

    def show(self):
        """
        在屏幕中显示窗体
        :return:
        """
        self.frame.mainloop()

    def get_perimeter(self, radius: float):
        """
        根据半径，获得圆的周长
        :param radius: 半径
        :return: 返回周长
        """
        pi = 3.1415926
        return 2 * pi * radius

    def get_area(self, radius: float):
        """
        根据半径，获得圆的面积
        :param radius: 半径
        :return: 返回面积
        """
        pi = 3.1415926
        return pi * radius * radius

    def check_input(self, number: str):
        """
        判断某一个字符是否是数字
        :param number: 要判断的字符
        :return: 如果是数字，返回True，如果不是数字，返回False
        """
        if number.replace(".", "").isdigit():
            return True
        else:
            return False

    # 点击计算触发事件
    def get_result(self):
        # 获得文本框填写的半径
        radius = self.var_radius.get()


        # 校验半径是否符合要求
        if self.check_input(radius):
            primeter = self.get_perimeter(float(radius))
            area = self.get_area(float(radius))
            # 赋值
            self.var_perimeter.set("%.2f" % primeter)
            self.var_area.set("%.2f" % area)
        else:
            showinfo("系统消息", "输入半径不符合要求，要求大于0的数字")

if __name__ == "__main__":
    # 根据类实例化一个对象
    this_gui = Calaulator()
    # 展示窗体
    this_gui.show()