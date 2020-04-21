from tkinter import *

class login_GUI(object):
    def __init__(self):
        self.frame = Tk()
        self.frame.title("登录窗体")
        self.frame.geometry("800x400")
        self.photo = PhotoImage(file = "C:\\Users\\iezyzhang\\Desktop\\office\\11.gif")
        imgLabel = Label(self.frame,image = self.photo).grid(row=0,column=0,rowspan=2)
        Label_username = Label(self.frame, text="用户名：", font=("微软雅黑", 15)).grid(row=0, column=1)
        # 第一行第三列
        Entry_username = Entry(self.frame, font=("微软雅黑", 15), width=18).grid(row=0, column=2)
        # 第二行第二列
        Label_password = Label(self.frame, text="密  码：", font=("微软雅黑", 15)).grid(row=1, column=1)
        # 第二行第三列
        Entry_password = Entry(self.frame, font=("微软雅黑", 15), width=18).grid(row=1, column=2)
        # 第三行空着
        # 第四行第三列
        Button_login = Button(self.frame, text="登录", font=("微软雅黑", 15), width=5).grid(row=2, column=2, sticky="w")
        Button_cencel = Button(self.frame, text="取消", font=("微软雅黑", 15), width=5).grid(row=2, column=2, sticky="e")
    def run(self):
        self.frame.mainloop()

if __name__ == '__main__':
    # 由窗体模板实例化一个窗体
    this_gui = login_GUI()
    # 展示窗体
    this_gui.run()