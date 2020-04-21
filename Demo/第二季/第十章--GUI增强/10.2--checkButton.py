# checkButton----checkbox----复选框

from tkinter.ttk import *
from tkinter import *

root = Tk()
root.title("CheckButton控件")

Label01 = Label(root,text="请选择你去过的城市：")
Label01.grid(row = 0,column = 0,padx=10,pady=10)
city_list = ["上海", "北京","南京"]
check_list  = []
for city in city_list:
    check_list.append(IntVar())
    Checkbutton01 = Checkbutton(root,text = city, variable = check_list[-1])
    Checkbutton01.grid(row=0,column=len(check_list),padx=10,pady=10)
def sel():
    all_select=""
    Label02["text"]=""
    for i in range(0,len(check_list)):
        if check_list[i].get()==1:
            all_select +=city_list[i] + "  "
    print(all_select)
    Label02["text"] = "所选的城市：" + all_select
Button01 = Button(root,text="确认",command = sel)
Button01.grid(row=1,column=0,padx=10,pady=10)
# 添加一个标签。展示显示的结果
Label02 = Label(root,text="")
Label02.grid(row=1,column=2,columnspan = 5)
root.mainloop()



