from tkinter import *
from tkinter.ttk import *

# radioButton----单选框---多个值 选一个

root = Tk()

root.title("RadioButton")
root.geometry("400x200")

def sel_gender():
    if str(gender_check)== "0":
        Label01_select_gender["text"] = "男"
    else:
        Label01_select_gender["text"] = "女"

def sel_edu():
    Label01_select_edu["text"] = education_list[education_check.get()]


# 性别单选
Label_gender = Label(root, text = "性别：")
Label_gender.grid(row = 0, column = 0, padx = 20, pady = 20,sticky = "w")

gender_check = IntVar()
radio_boy = Radiobutton(root,text= "男",variable = gender_check, value = 0, command = sel_gender)
radio_boy.grid(row=0,column=1, padx = 20, pady = 20,sticky = "w")
radio_gril = Radiobutton(root,text= "女",variable = gender_check, value = 1, command = sel_gender)
radio_gril.grid(row=0,column=2, padx = 20, pady = 20,sticky = "w")
# 学历
education_list = ["高中", "本科", "硕士", "博士"]
Label_education = Label(root,text= "学历:")
Label_education.grid(row=2,column=0, padx = 20,sticky = "w")

education_check = IntVar
for i in range(0, len(education_list)):
    radio = Radiobutton(root, text = education_list[i], variable = education_check, value = i, command = sel_edu)
    radio.grid(row = 2, column = i + 1)
Label01 = Label(root, text="所选择的值为:")
Label01.grid(row=3,column=0, padx = 20, pady = 20,sticky = "w")
Label01_select_gender = Label(root, text="")
Label01_select_gender.grid(row=3,column=2, padx = 20, pady = 20)
Label01_select_edu = Label(root, text="")
Label01_select_edu.grid(row=3,column=3,padx = 20, pady = 20)
root.mainloop()





