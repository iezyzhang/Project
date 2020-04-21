
if __name__ == "__main__":
    # num01, num02, num03 = 12, 32, 34
    # print("10" + "20")
    # # float类型精度有17位
    # num06 = 1.23435436576574234325435
    # print(num01)
    # is_small = False
    # str01 = "asdfjklsd"
    # print(str01[-1])
    # print(type(num01))
    # print(type(is_small))
    #
    # if isinstance(str01, str):
    #     print("字符型")


    # str02 = "jake"
    # str02 = '''这是一个dome
    # 今天天气真好'''
    # print(str02)
    # print("my name is Alice")
    # print(r"我的资料在D:\python\ ")


    # # 运算符
    # name = "Alice"
    # print("我是" + name)
    # print("我的年龄：", 14)
    #
    # # 索引方式
    # str03 = "asdfhsdajkfjdsaklj"
    # str01 = "asd"
    # print(str03[0])  # 第一个字符
    # print(str03[-1])  # 最后一个字符
    # print(str03[4])  # 第五个字符
    # print(str03[-5])  # 倒数第五个
    # print(str03[5:])  # 从第六个开始到结束
    # print(str03[-5:])  # 从倒数第五个开始到结束
    # print(str03[3:10])  # 从第四个来时到第十个
    #
    # # 求长度
    # print("字符串长度：", len(str03))
    # # 是否包含
    # print(str01 in str03)
    # # 判断是否相等
    # print(str03 == str01)
    # print(str01 is str03)

    # num01 = 100
    # print(id(num01))
    # # 对于数值类型相同的值只存储一份

    # str01 = "www.icyu.com"
    # str02 = "steven"
    # str03 = "steven"
    # print(id(str01))
    # print("str02的内存地址", id(str02))
    # print(id(str03))
    # print(id(str02[-1]))

    # print打印
    # print(str02, str03)  # 先print（str02）,后print(str03)
    # # 一般来说是打印换行，如果打印不换行，需要修改end
    # print("hello", end="  ")
    # print("hello")
    # print("alace", "bob", "tomas", sep="=|=")
    # money = 121
    # print("本次消费金额为：", money, sep="$")

    # 输出文件
    str01 = "aaasdkajflasddsfksdal"
    f = open("C:\\lse.txt", 'w')  # write
    print(str01, file=f)

