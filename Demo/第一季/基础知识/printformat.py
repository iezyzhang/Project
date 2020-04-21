
if __name__ == "__main__":

    # num01, num02, = 200, 300
    # print("八进制输出：%0o, %0o" % (num01, num02))
    # print("十六进制输出：0x%x, 0x%x" % (num01, num02))
    # print("二进制", bin(num01), "二进制", bin(num02))
    #
    # num01 = 1234567.8912
    # print("标准的模式：%f" % num01)
    # print("保留两位有效数字：%.2f" % num01)
    # print("e的标准模式：%.2e" % num01)
    # print("g的标准模式：%g" % num01)
    # print("g保留两位有效数字：%.2g" % num01)

    # 字符串的格式化输出
    str01 = "www.jasdkl.com"
    print("s标准输出：%s" % str01)
    print("s固定空间中输出：%20s" % str01)  # 右对齐    默认
    print("s固定空间输出：%-20s" % str01)  # 左对齐
    print("s截取：%.3s" % str01)    # 截取前三个字符
    print("s截取：%10.3s" % str01)    # 在固定10个字符空间中   截取前三个字符输出，靠右对齐
    print("s截取：%-10.3s" % str01)


    # format输出
    name = "Alice"
    gender = "男"
    age = 23
    print("姓名：{}  性别:{}  年龄：{}" .format(name, gender, age))
    print("姓名：{0}  性别:{1}  年龄：{2}  学生姓名: {0}".format(name, gender, age))
    print("姓名：{name}  性别:{gender}  年龄：{age}  学生姓名: {name}".format(name=name, gender=gender, age=age))

    print("姓名： {:10}".format(name))   # 默认左对齐
    print("姓名： {:<10}".format(name))  # 左对齐
    print("姓名： {:>10}".format(name))  # 右对齐
    print("姓名： {:^10}".format(name))  # 中间对齐

    print("{:.2}".format(3.1415967))  # 保留两位有效数字    左对齐
    print("{:10.2}".format(3.1415967))  # 保留两位有效数字。在10 个字符空间中打印  ，默认右对齐
    print("{:<10.2}".format(3.1415967))
    print("{:^10.2}".format(3.1415967))

    num01, num02 = 100, 200
    print("十六进制打印： {0:x}  {1:x}".format(num01, num02))
    print("八进制打印： {0:o}  {1:o}".format(num01, num02))
    print("八进制打印： {0:b}  {1:b}".format(num01, num02))

    print("{:c}".format(76))    # 打印ASK码
    print(("{:e}".format(123456.666756)))
    print(("{:0.2e}".format(123456.666756)))  # 小数点后保留两位
    print("{:g}".format(12323.654))
    print("{:0.2g}".format(12323.654))     # 保留两位有效数字
    print("{:0.2%}".format(0.2))
    print("{:%}".format(0.2))
    print("{:0.0%}".format(0.2))

    # 千位分隔符
    print("{:,}".format(123456789))
