
if __name__ == "__main__":
    # # 输姓名，输入性别，并打印
    # print("请输入姓名：", end= "")
    # name = input()
    # print("请输入性别：", end= "")
    # gender = input()
    # print("姓名：%s  性别：%s" %(name, gender))

    # # 简化
    # name = input("请输入姓名：")
    # gender = input("请输入性别：")
    # print("姓名：%s  性别：%s" % (name, gender))

    """
    # 题目：输入两个数，求两数之和
    num01 = input("请输入一个数：")
    num02 = input("请输入一个数：")
    print(type(num02))
    # print("%d + %d = %d" % (num01, num02, num01 + num02))
    # 所有输入的字符都会被系统当做字符串
    # print("%s + %s = %s" % (num01, num02, num01 + num02))  # 字符串连接
    print("%d + %d = %d" % (int(num01), int(num02), int(num01) + int(num02)))
    """


    """ 
       eval特点：只能一次输入多个整数，不能是字符串
       输入后自动转为int类型
    """
    # num01, num02 = eval(input("请输入两个数，逗号分开："))
    # print("%d + %d = %d" % (num01, num02, num01 + num02))


    # 数据类型转换
    """
    数据类型转换：要转换的类型（数据）
    1、num01转换为整数   int（num01）
    1、num01转换为浮点数   float（num01）
    1、num01转换为字符串   str（num01）
    1、num01转换为bool   bool（num01）
    1、num01转换为整数   int（num01）
    """
    print(int("12344") + 1)
    print(float("12.345") + 1.187)
    print(str(123) + "456")
    print(bool(1))  # 如果转为bool类型，非0结果为true，0结果为false

    print(int(12.98))  # 去除小数点后的值
    # print(int("abby"))
    # 在做数据类型转换的时候，不是所有的转换都能成功，需要做异常处理

    # 数值——————字符
    print(ord("X"))
    print(chr(88))
    # 进制
    print(hex(200))
    print(bin(200))
    print(oct(200))