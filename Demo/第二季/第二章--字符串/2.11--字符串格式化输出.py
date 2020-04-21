# 格式化输出： center
print("asdf".center(10))  # 在10个空间中显示
print("asd".center(10, "*"))   # 在10个空间中显示    用*填充
print("asdf".center(10, "*"))

# 格式化输出   %s
name = "dddd"
number = "1503655"
print("姓名:%s   电话：%s" % (name, number))

print("学号    姓名   性别     邮箱")
print("----------------------------")
student_info = [["95001","张三", "男", "zhangsn@ccu.com"],
                ["95002","李四", "男", "zhangsn@ccu.com"],
                ["95003","杨思", "女", "zhangsn@ccu.com"]]
for i in student_info:
    print("%s  %s    %s  %s" % (i[0], i[1], i[2], i[3]))
