
from tkinter import *
from tkinter.messagebox import *

class NumberTransfer:
    # 构造函数-----定义界面的模样
    def __init__(self):
        self.frame = Tk()  # 新建一个窗体
        self.frame.title("进制转换")  # 添加标题
        self.frame.geometry("600x300+450+200")  # 定义窗体的大小和放置的位置
        self.frame.resizable(0,0)  # 固定窗体大小
        self.frame["bg"] = "lightgray"  # 设置背景颜色

        # 通过label放置图
        # self.Banner_image = PhotoImage(file="./img/timg.jpg")
        # self.Banner_Top = Label(self.frame, image=self.Banner_image)
        # self.Banner_Top.place(x=0, y=0)

        # 选择进制
        self.Label_select = Label(self.frame, text = "选择要输入的进制：", bg="lightgray", font=("微软雅黑",
                                                                                        10,"bold"))
        self.Label_select.place(x=40,y=20)

        self.var_number = IntVar()
        self.Radio_two = Radiobutton(self.frame, variable = self.var_number, value=2, text="二进制",bg="lightgray", font=("微软雅黑",10,"bold"))
        self.Radio_two.place(x=180,y=20)

        self.Radio_eight = Radiobutton(self.frame, variable = self.var_number,value=8,text="八进制", bg="lightgray", font=("微软雅黑",10, "bold"))
        self.Radio_eight.place(x=280, y=20)

        self.Radio_ten = Radiobutton(self.frame, variable = self.var_number,value=10,text="十进制", bg="lightgray", font=("微软雅黑",10, "bold"))
        self.Radio_ten.place(x=380, y=20)

        self.Radio_sixteen = Radiobutton(self.frame, variable = self.var_number,value=16,text="十六进制", bg="lightgray", font=("微软雅黑",10, "bold"))
        self.Radio_sixteen.place(x=480, y=20)

        # 输入区域
        self.Label_input = Label(self.frame, text="请输入具体的数值：", bg="lightgray", font=("微软雅黑",10, "bold"))
        self.Label_input.place(x=40,y=60)

        self.var_input = StringVar()
        self.Entry_input = Entry(self.frame, textvariable=self.var_input, font=("微软雅黑",10, "bold"), width = 30)
        self.Entry_input.place(x=180, y=60)

        self.Button_get = Button(self.frame, text="计算", command=self.get_number,font=("微软雅黑", 8, "bold"), width=8)
        self.Button_get.place(x=450, y=60)

        # 结果
        self.Label_result = Label(self.frame, text="结果：", bg="lightgray", font=("微软雅黑", 12, "bold"))
        self.Label_result.place(x=80, y=100)

        self.Label_two = Label(self.frame, text="二进制：", bg="lightgray", font=("微软雅黑", 10, "bold"))
        self.Label_two.place(x=100, y=140)
        self.var_two = StringVar()
        self.Label_two_result = Label(self.frame, textvariable = self.var_two, text="二进制结果", bg="lightgray", fg="red", font=("微软雅黑", 10, "bold"))
        self.Label_two_result.place(x=180, y=140)

        self.Label_eight = Label(self.frame, text="八进制：", bg="lightgray", font=("微软雅黑", 10, "bold"))
        self.Label_eight.place(x=100, y=180)
        self.var_eight = StringVar()
        self.Label_eight_result = Label(self.frame, textvariable = self.var_eight, text="八进制结果", bg="lightgray", fg="red", font=("微软雅黑", 10, "bold"))
        self.Label_eight_result.place(x=180, y=180)

        self.Label_ten = Label(self.frame, text="十进制：", bg="lightgray", font=("微软雅黑", 10, "bold"))
        self.Label_ten.place(x=100, y=220)
        self.var_ten = StringVar()
        self.Label_ten_result = Label(self.frame, textvariable = self.var_ten,text="十进制结果", bg="lightgray",fg="red",  font=("微软雅黑", 10, "bold"))
        self.Label_ten_result.place(x=180, y=220)

        self.Label_sixteen = Label(self.frame, text="十六进制：", bg="lightgray", font=("微软雅黑", 10, "bold"))
        self.Label_sixteen.place(x=86, y=260)
        self.var_sixteen = StringVar()
        self.Label_sixteen_result = Label(self.frame, textvariable = self.var_sixteen,text="十六进制结果", bg="lightgray",fg="red", font=("微软雅黑", 10, "bold"))
        self.Label_sixteen_result.place(x=180, y=260)

    def show(self):
        self.frame.mainloop()

    def check_input(self,type,number):
        """
        判断输入的值是否有效
        :param type: 进制
        :param number: 具体的值
        :return: 如果符合要求返回T  不符合F
        """
        type_two = ["0", "1"]
        type_eight = ["0","1","2","3","4","5","6","7"]
        type_ten = ["0","1","2","3","4","5","6","7","8","9"]
        type_sixteen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","A","B","C","D","E","F"]

        # 判断
        if type==2:  # 二进制
            if number.startswith("0b"):
                number=number.replace("0b","")
            for i in number:
                if i not in type_two:
                    return False
        elif type == 8:  # 八进制
            if number.startswith("0o"):
                number=number.replace("0o","")
            for i in number:
                if i not in type_eight:
                    return False

        elif type == 10:  # 十进制
            for i in number:
                if i not in type_ten:
                    return False
        elif type == 16:  # 十六进制
            if number.startswith("0x"):
                number=number.replace("0x","")
            number = number.upper()
            for i in number:
                if i not in type_sixteen:
                    return False
        # 最后只要没有return  F
        return True

    def get_type_ten_number(self,typer_number:int,number:str):
        if typer_number == 2:
            return int(number,2)
        if typer_number == 8:
            return int(number,8)
        if typer_number == 10:
            return int(number,10)
        if typer_number == 16:
            return int(number,16)

    def transfer_number(self,number:int):
        """
        把十进制的数字转为二进制  八进制  十进制  十六进制
        :param number: 要转换的进制字符串
        :return: 列表【二进制  八进制  十进制  十六进制】
        """
        number_list = []
        # 添加二进制的值
        number_list.append(bin(number))
        # 添加八进制
        number_list.append(oct(number))
        # 添加十进制
        number_list.append(number)
        # 添加十六进制
        number_list.append(hex(number))

        # 返回
        return number_list

    def get_number(self):
        # 获取文本框输入的值
        input_number = self.var_input.get()
        type_number = self.var_number.get()  # 进制整形

        # 判断输入是否符合要求
        if type_number == 0:
            showinfo("系统消息","请选择对应的进制")
        elif self.check_input(type_number, input_number):
            number_list = self.transfer_number(self.get_type_ten_number(type_number, input_number))
            # 展示
            self.var_two.set(number_list[0])
            self.var_eight.set(number_list[1])
            self.var_ten.set(number_list[2])
            self.var_sixteen.set([number_list[3]])
        else:
            showinfo("系统消息","输入不符合要求")

if __name__ == "__main__":
    this_gui = NumberTransfer()
    this_gui.show()
