from tkinter import *

class count_char:
    def __init__(self):  # 构造方法
        self.frame = Tk()
        self.frame.title("统计字符")
        self.frame.geometry("600x300+400+200")
        self.frame.resizable(0,0)
        self.frame["bg"] = "lightgray"

        # 添加文本框
        # self.var_input = StringVar()
        self.Text_input = Text(self.frame,height=6,width=35,font=("微软雅黑",14,"bold"))
        self.Text_input.place(x=20,y=20)

        # 添加按钮
        self.Button_get = Button(self.frame,text="统计字符",font=("微软雅黑",13,"bold"),height=6, command=self.get_result)
        self.Button_get.place(x=460,y=20)

        # 添加label标签
        self.Label_all = Label(self.frame,text="字符总数：",font=("微软雅黑",12,"bold"),bg="lightgray")
        self.Label_all.place(x=20, y=200)

        self.Label_all_result = Label(self.frame, text="结果", font=("微软雅黑", 12, "bold"), bg="lightgray",fg="red")
        self.Label_all_result.place(x=100, y=200)

        # 添加label标签
        self.Label_upper = Label(self.frame, text="大写字母:", font=("微软雅黑", 12, "bold"), bg="lightgray")
        self.Label_upper.place(x=170, y=200)

        self.Label_upper_result = Label(self.frame, text="大写字母结果", font=("微软雅黑", 12, "bold"), bg="lightgray", fg="red")
        self.Label_upper_result.place(x=250, y=200)

        # 添加label标签
        self.Label_lower = Label(self.frame, text="小写字母:", font=("微软雅黑", 12, "bold"), bg="lightgray")
        self.Label_lower.place(x=380, y=200)

        self.Label_lower_result = Label(self.frame, text="小写字母结果", font=("微软雅黑", 12, "bold"), bg="lightgray", fg="red")
        self.Label_lower_result.place(x=460, y=200)

        # 添加label标签
        self.Label_number = Label(self.frame, text="数字总数：", font=("微软雅黑", 12, "bold"), bg="lightgray")
        self.Label_number.place(x=20, y=240)

        self.Label_number_result = Label(self.frame, text="结果", font=("微软雅黑", 12, "bold"), bg="lightgray", fg="red")
        self.Label_number_result.place(x=100, y=240)

        # 添加label标签
        self.Label_Chinese = Label(self.frame, text="中文字符:", font=("微软雅黑", 12, "bold"), bg="lightgray")
        self.Label_Chinese.place(x=170, y=240)

        self.Label_Chinese_result = Label(self.frame, text="中文字符结果", font=("微软雅黑", 12, "bold"), bg="lightgray", fg="red")
        self.Label_Chinese_result.place(x=250, y=240)

        # 添加label标签
        self.Label_other = Label(self.frame, text="其他字符:", font=("微软雅黑", 12, "bold"), bg="lightgray")
        self.Label_other.place(x=380, y=240)

        self.Label_other_result = Label(self.frame, text="其他字符结果", font=("微软雅黑", 12, "bold"), bg="lightgray", fg="red")
        self.Label_other_result.place(x=460, y=240)

    def show(self):
        self.frame.mainloop()

    def get_result(self):
        """
        获取文本框中相应字符的数量
        :return:
        """
        # 获取文本框的内容
        all_string = self.Text_input.get("0.0","end")
        # 定义多个变量，用来统计大写字母，小写字母，字母，中文，其他
        upper = 0
        lower = 0
        number = 0
        chinese = 0
        other = 0
        # 遍历字符
        for i in all_string:
            # 大写字母
            if (i >= "A") and (i <= "Z"):
                upper += 1
            elif (i >= "a") and (i <= "z"):
                lower += 1  # 小写字母
            elif (i >= "0") and (i <= "9"):
                number += 1  # 数字字符
            elif (i >= "\u4e00") and (i <= "\u9FA5"):
                chinese += 1  # 中文字符
            else:
                other += 1
        # 赋值
        self.Label_all_result["text"] = len(all_string)  # 所有字符长度
        self.Label_upper_result["text"] = upper
        self.Label_lower_result["text"] = lower
        self.Label_number_result["text"] = number
        self.Label_Chinese_result["text"] = chinese
        self.Label_other_result["text"] = other

if __name__ == "__main__":
    this_gui = count_char()
    this_gui.show()
