from tkinter import *
from tkinter.messagebox import *
class login_GUI(object):
    def __init__(self):
        self.frame = Tk()
        self.frame.title("登录窗体")
        self.frame.geometry("800x400")
        self.photo = PhotoImage(file = "C:\\Users\\iezyzhang\\Desktop\\office\\11.gif")
        self.imgLabel = Label(self.frame,image = self.photo)
        self.imgLabel.grid(row=0,column=0,rowspan=2)
        self.Label_username = Label(self.frame, text="用户名：", font=("微软雅黑", 15))
        self.Label_username.grid(row=0, column=1)
        # 第一行第三列
        self.Entry_username = Entry(self.frame, font=("微软雅黑", 15), width=18)
        self.Entry_username.grid(row=0, column=2)
        # 第二行第二列
        self.Label_password = Label(self.frame, text="密  码：", font=("微软雅黑", 15))
        self.Label_password.grid(row=1, column=1)
        # 第二行第三列
        self.Entry_password = Entry(self.frame, font=("微软雅黑", 15), width=18)
        self.Entry_password.grid(row=1, column=2)
        # 第三行空着
        # 第四行第三列
        self.Button_login = Button(self.frame, text="登录", font=("微软雅黑", 15), width=5,command = self.login)
        self.Button_login.grid(row=2, column=2, sticky="w")
        self.Button_cencel = Button(self.frame, text="取消", font=("微软雅黑", 15), width=5,command = self.exit)
        self.Button_cencel.grid(row=2, column=2, sticky="e")

        # 定义全局变量
        self.error_times = 0
        self.is_diable=False
    def run(self):
        self.frame.mainloop()
    def login(self):
        """
        实现登录
        :return:
        """

        # 先获取用户名和密码
        username = str(self.Entry_username.get())
        password = str(self.Entry_password.get())
        # 验证
        if username.strip().lower() != "admin":
            showinfo("系统消息","用户名不存在，请核实")
        elif password != "123.com":

            self.error_times += 1
            if self.error_times > 3:
                self.is_diable = True
            if self.is_diable:
                showinfo("系统消息", "密码错误三次，账号锁定，请联系管理员")
            else:
                showinfo("系统消息", "密码错误，请核实")
        else:
            showinfo("系统消息", "登录成功")
            self.error_times = 0
    def exit(self):
        self.frame.destroy()  # 关闭窗体
if __name__ == '__main__':
    # 由窗体模板实例化一个窗体
    this_gui = login_GUI()
    # 展示窗体
    this_gui.run()


