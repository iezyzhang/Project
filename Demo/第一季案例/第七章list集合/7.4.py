
"""
输入货币金额，转换为金额中文大写，具体要求如下：
1、输入的金额不能小于等于0，金额最大到千亿单位
2、如果没有小数，最后加一个整

"""
from tkinter import *
from tkinter.messagebox import *
class RMBTransferGUI:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("人命币金额转换")
        self.frame.geometry("600x200+600+200")
        self.frame.resizable(0,0)

        # 添加金额输入框
        self.Label_input = Label(self.frame,text="请输入要转换的金额：", font=("微软雅黑",12,"bold"))
        self.Label_input.place(x=30,y=40)

        self.var_input=StringVar()
        self.Entry_input = Entry(self.frame,font=("微软雅黑",12,"bold"),width=20,textvariable=self.var_input)
        self.Entry_input.place(x=200,y=40)

        # 添加按钮
        self.Button_transfer = Button(self.frame,text="转换",font=("微软雅黑",12,"bold"),width=6,command=self.transfer)
        self.Button_transfer.place(x=420,y=32)

        # 添加转换结果
        self.Label_result_info = Label(self.frame, text="金额大写：", font=("微软雅黑", 12, "bold"))
        self.Label_result_info.place(x=100, y=110)

        self.Label_result = Label(self.frame, text="结果", font=("微软雅黑", 12, "bold"),fg="red")
        self.Label_result.place(x=200, y=110)

    def show(self):
        self.frame.mainloop()

    def transfer(self):
        # 获取金额
        input_number = self.var_input.get()
        # 判断
        try:
            # 校验
            MoneyTransfer.check_number(input_number)
            input_number = "%.2f" % float(input_number)
            # 转换
            transfer_result = MoneyTransfer.build_chinese_money(input_number)
            # 优化
            transfer_result = MoneyTransfer.optimize_chinese_money(transfer_result)

            # 输出
            self.Label_result["text"] = transfer_result

        except ValueError as e:
            showinfo("系统消息","e")

class MoneyTransfer:
    @staticmethod
    def check_number(money_string:str):
        """
        校验输入的金额是否有效
        :return:
        """
        if money_string.startswith("-"):
            raise ValueError("金额不能为负数！！")
        try:
            money_number = float(money_string)
            return money_number
        except:
            raise ValueError("货币的金额必须为数字！")

    @staticmethod
    def input_money():
        """
        输入人命币金额，并做校验
        :return:
        """
        while True:
            RMB_string = input("请输入要转换的金额：")
            RMB_number = 0.0
            # 条用校验
            try:
                RMB_number = MoneyTransfer.check_number(RMB_string)
                return RMB_number
            except ValueError as e:
                print(e)
                continue
    @staticmethod
    def build_chinese_money(money:str):
        """
        实现数字转换为大写
        :param money:
        :return:
        """
        chinese_money = ["分","角","圆","拾","佰","仟","万","拾","佰","仟","亿","拾","佰","仟"]
        chinese_number = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
        # 把数字倒序
        re_number = money[::-1].replace(".","")
        # 把数字转换为大写
        re_number_upper = ""
        for item in re_number:
            re_number_upper += chinese_number[int(item)]

        total_string = ""
        # 和单位拼接
        for index in range(len(re_number_upper)):
            total_string += chinese_money[index]
            total_string += re_number_upper[index]
        return total_string[::-1]
    @staticmethod
    def optimize_chinese_money(money:str):
        """
        优化金额的表示
        :param money:
        :return:
        """
        if "零角零分" in money:
            money = money.replace("零角零分", "整")
        if "零分" in money:
            money = money.replace("零分", "")
        if "零仟零佰零拾" in money:
            money = money.replace("零仟零佰零拾", "零")
        if "零佰零拾" in money:
            money = money.replace("零佰零拾", "零")
        if "零仟零佰" in money:
            money = money.replace("零仟零佰", "零")
        if "零仟" in money:
            money = money.replace("零仟", "零")
        if "零佰" in money:
            money = money.replace("零佰", "零")
        if "零拾" in money:
            money = money.replace("零拾", "零")
        if "零零" in money:
            money = money.replace("零零", "零")
        if "零万" in money:
            money = money.replace("零万", "万")
        if "零亿" in money:
            money = money.replace("零仟亿", "亿")
        if "亿万" in money:
            money = money.replace("亿万", "亿")
        if "零圆" in money:
            money = money.replace("零圆", "圆")
        return money


if __name__ == "__main__":
    gui = RMBTransferGUI()
    gui.show()

