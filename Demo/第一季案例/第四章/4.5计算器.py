
from tkinter import *
class Calculator:
    def __init__(self):
        # 新建GUI窗体
        self.frame = Tk()
        # 窗体标题
        self.frame.title("我的计算器")
        # 指定窗体大小和放置位置
        self.frame.geometry("320x500+500+200")
        # 不允许窗体变化
        self.frame.resizable(0, 0)


        # 添加顶部Label标签
        self.var_detail = StringVar()
        self.Label_detail = Label(self.frame, textvariable = self.var_detail,bg="lightgray", font=("微软雅黑", 16), fg="Dimgray", anchor = "se")
        self.Label_detail.place(x=0, y=0, width = 320, height = 200)

        # 添加结果标签
        self.var_result = StringVar()
        self.Label_result = Label(self.frame, textvariable = self.var_result, bg="lightgray", font=("微软雅黑", 24), anchor = "e")
        self.Label_result.place(x=0, y=200, width=320, height = 50)

        # 添加按钮 AC  清除
        self.Button_ac = Button(self.frame, text = "AC", font=("微软雅黑", 18), fg = "black", command = self.ac)
        self.Button_ac.place(x=0,y=250,width=80,height= 50)

        # 添加按钮 删除
        self.Button_del = Button(self.frame, text="<-", font=("微软雅黑", 18), fg="black",command = self.delete)
        self.Button_del.place(x=80, y=250, width=80, height=50)

        # 添加按钮 乘除 × ÷
        self.Button_mul = Button(self.frame, text="×", font=("微软雅黑", 18), fg="black",command=self.mul)
        self.Button_mul.place(x=160, y=250, width=80, height=50)
        self.Button_div = Button(self.frame, text="÷", font=("微软雅黑", 18), fg="black",command=self.div)
        self.Button_div.place(x=240, y=250, width=80, height=50)

        # 添加按钮 7
        self.Button_seven = Button(self.frame, text="7", font=("微软雅黑", 18), fg="black",command=self.get_seven)
        self.Button_seven.place(x=0, y=300, width=80, height=50)

        # 添加按钮 8
        self.Button_eight = Button(self.frame, text="8", font=("微软雅黑", 18), fg="black",command=self.get_eight)
        self.Button_eight.place(x=80, y=300, width=80, height=50)

        # 添加按钮 9
        self.Button_nine = Button(self.frame, text="9", font=("微软雅黑", 18), fg="black",command=self.get_nine)
        self.Button_nine.place(x=160, y=300, width=80, height=50)
        # 添加按钮 -
        self.Button_sub = Button(self.frame, text="-", font=("微软雅黑", 18), fg="black",command=self.sub)
        self.Button_sub.place(x=240, y=300, width=80, height=50)

        # 添加按钮 4
        self.Button_four = Button(self.frame, text="4", font=("微软雅黑", 18), fg="black",command=self.get_four)
        self.Button_four.place(x=0, y=350, width=80, height=50)

        # 添加按钮 5
        self.Button_five = Button(self.frame, text="5", font=("微软雅黑", 18), fg="black",command=self.get_five)
        self.Button_five.place(x=80, y=350, width=80, height=50)

        # 添加按钮 6
        self.Button_six = Button(self.frame, text="6", font=("微软雅黑", 18), fg="black",command=self.get_six)
        self.Button_six.place(x=160, y=350, width=80, height=50)
        # 添加按钮 +
        self.Button_add = Button(self.frame, text="+", font=("微软雅黑", 18), fg="black", command = self.add)
        self.Button_add.place(x=240, y=350, width=80, height=50)

        # 添加按钮 1
        self.Button_one = Button(self.frame, text="1", font=("微软雅黑", 18), fg="black", command = self.get_one)
        self.Button_one.place(x=0, y=400, width=80, height=50)

        # 添加按钮 2
        self.Button_two = Button(self.frame, text="2", font=("微软雅黑", 18), fg="black",command=self.get_two)
        self.Button_two.place(x=80, y=400, width=80, height=50)

        # 添加按钮 3
        self.Button_three = Button(self.frame, text="3", font=("微软雅黑", 18), fg="black",command=self.get_three)
        self.Button_three.place(x=160, y=400, width=80, height=50)

        # 添加按钮 %
        self.Button_percent = Button(self.frame, text="%", font=("微软雅黑", 18), fg="black", command=self.yu)
        self.Button_percent.place(x=0, y=450, width=80, height=50)

        # 添加按钮 0
        self.Button_zero = Button(self.frame, text="0", font=("微软雅黑", 18), fg="black",command=self.get_zero)
        self.Button_zero.place(x=80, y=450, width=80, height=50)

        # 添加按钮 .
        self.Button_point = Button(self.frame, text=".", font=("微软雅黑", 18), fg="black", command=self.get_point)
        self.Button_point.place(x=160, y=450, width=80, height=50)
        # 添加按钮 =
        self.Button_result = Button(self.frame, text="=", font=("微软雅黑", 18), fg="black", bg= "lightgray", command = self.get_result)
        self.Button_result.place(x=240, y=400, width=80, height=100)

    def show(self):
        self.frame.mainloop()

    def ac(self):
        self.var_result.set("0")
    def delete(self):
        content = self.var_result.get()
        self.var_result.set(content[0:len(content)-1])
    def add(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " + ")
        # result归0
        self.var_result.set("0")
    def sub(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " - ")
        # result归0
        self.var_result.set("0")
    def mul(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " × ")
        # result归0
        self.var_result.set("0")
    def div(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " ÷ ")
        # result归0
        self.var_result.set("0")
    def yu(self):
        content = self.var_result.get()
        # 为明细赋值
        self.var_detail.set(content + " % ")
        # result归0
        self.var_result.set("0")
    def get_result(self):
        detail = self.var_detail.get()
        num01 = detail.replace(" ","")[0:len(detail.replace(" ",""))-1]
        action = detail.replace(" ","")[-1]
        num02 = self.var_result.get()
        # 操作符执行操作
        if action == "+":
            result = float(num01) + float(num02)
            # 修改明细
            self.var_detail.set("{0} + {1} = ".format(num01,num02))
            # 修改结果
            self.var_result.set("{:g}".format(result))
        if action == "-":
            result = float(num01) - float(num02)
            # 修改明细
            self.var_detail.set("{0} - {1} = ".format(num01,num02))
            # 修改结果
            self.var_result.set("{:g}".format(result))
        if action == "×":
            result = float(num01) * float(num02)
            # 修改明细
            self.var_detail.set("{0} × {1} = ".format(num01,num02))
            # 修改结果
            self.var_result.set("{:g}".format(result))
        if action == "÷":
            result = float(num01) / float(num02)
            # 修改明细
            self.var_detail.set("{0} ÷ {1} = ".format(num01,num02))
            # 修改结果
            self.var_result.set("{:g}".format(result))
        if action == "%":
            result = float(num01) % float(num02)
            # 修改明细
            self.var_detail.set("{0} % {1} = ".format(num01,num02))
            # 修改结果
            self.var_result.set("{:g}".format(result))
    def get_one(self):  # 获得1
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("1")
        else:
            self.var_result.set(content + "1")
    def get_two(self):  # 获得2
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("2")
        else:
            self.var_result.set(content + "2")
    def get_three(self):  # 获得3
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("3")
        else:
            self.var_result.set(content + "3")
    def get_four(self):  # 获得4
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("4")
        else:
            self.var_result.set(content + "4")
    def get_five(self):  # 获得5
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("5")
        else:
            self.var_result.set(content + "5")
    def get_six(self):  # 获得6
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("6")
        else:
            self.var_result.set(content + "6")
    def get_seven(self):  # 获得7
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("7")
        else:
            self.var_result.set(content + "7")
    def get_eight(self):  # 获得8
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("8")
        else:
            self.var_result.set(content + "8")
    def get_nine(self):  # 获得9
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("9")
        else:
            self.var_result.set(content + "9")
    def get_zero(self):  # 获得0
        content = self.var_result.get()
        if content == "0":
            self.var_result.set("0")
        else:
            self.var_result.set(content + "0")
    def get_point(self):  # 获得.
        content = self.var_result.get()
        self.var_result.set(content + ".")
if __name__ == "__main__":
    my_cal = Calculator()
    my_cal.show()

