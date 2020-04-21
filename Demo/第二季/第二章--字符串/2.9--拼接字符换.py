# 拼接字符串   +    %s
list_name = ["lice", "tomas", "kike"]
# 方法01 +
num01 = ""
for i in list_name:
    num01 += i + ","
print(num01)
# 方法02 %s
num02 = "%s,%s,%s" % (list_name[0], list_name[1], list_name[2])
print(num02)

# 方法03 join
str02 = "123"
str01 = "asdf"
print(str01.join(str02))  # 基本功能

sep = ","
num03 = sep.join(list_name)
print(num03)

# 案例  将多个学生的信息 d\student.txt   用逗号分开学生属性
student_info = [["95001","张三", "男", "zhangsn@ccu.com"],
                ["95002","李四", "男", "zhangsn@ccu.com"],
                ["95003","杨思", "女", "zhangsn@ccu.com"]]

sep = ","
# 循环读取每一条记录
try:
    global fd
    fd = open(r"C:\Users\iezyzhang\Desktop\student.txt", "a", encoding="utf-8")
    for i in student_info:
        fd.write(sep.join(i) + "\n")
    print("写入成功")
except Exception as e:
    print(repr(e))
    print("写入文件出错")
finally:
    fd.close()
