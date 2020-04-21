# 分隔字符串   把一个大字符串分隔多个小字符串，和拼接想对应
list_name = "lice, tomas, kike"
name_list = list_name.split(",")
print(name_list)

# 案例01 在文件中读出所有男生的学号和姓名
# 方法01--每次读一行
print("================方法01===========================")
try:
    global fd
    fd = open(r"C:\Users\iezyzhang\Desktop\student.txt", "r", encoding="utf-8")
    current_line = fd.readline()  # 把当前读的这行数据赋值给变量
    while current_line:  # 如果没读完一直循环，如果读完  curent-line为null
        student_list = current_line.split(",")
        if student_list[2] == "男":
            print("学号：%s  姓名:%s" % (student_list[0], student_list[1]))
        # 读取下一行
        current_line = fd.readline()
except Exception as e:
    print("出错")
    print(repr(e))
finally:
    fd.close()

# 方法02  把整个数据读到变量里面，慢慢处理（区分学生，区分属性）
print("================方法02===========================")
all_line = ""
try:
    global fa
    fa = open(r"C:\Users\iezyzhang\Desktop\student.txt", "r", encoding="utf-8")
    all_line = fa.read()  # 把读的所有数据赋值给变量
except Exception as e:
    print(repr(e))
    print("出错")
finally:
    fa.close()

# 01 区分学生
student_list01 = all_line.split("\n")
# 02 使用循环读出每个学生的属性
try:
    for current_student in student_list01:
        detal_list = current_student.split(",")
        if detal_list[2] == "男":
            print("学号：%s  姓名:%s" % (detal_list[0], detal_list[1]))
except Exception as e:
    print(repr(e))
    print("出错")
