
from tkinter import *
from tkinter.messagebox import *
class Window_q:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("键盘响应事件测试")
        self.frame.geometry("800x500+300+200")
        self.frame.resizable(0, 0)

        # 绑定键盘事件
        self.frame.bind("<KeyPress>", self.key_method)

    def show(self):
        self.frame.mainloop()

    def key_method(self,event):
        """
        根据按键响应的方法
        :param event:
        :return:
        """
        if event.keysym == "Return":
            showinfo("系统消息","你按了回车键")
        if event.keysym in["A","a"]:
            showinfo("系统消息","你按了A键")
        if event.keysym in["1"]:
            showinfo("系统消息","你按了数字1键")

if __name__ == "__main__":
    this_windows = Window_q()
    this_windows.show()

