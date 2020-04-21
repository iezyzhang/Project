
if __name__ == "__main__":
    """
    num01, num02, num03 = 12, 23, 9
    print(num01 // num03)
    print(num01 % num03)
    print(round(10 / 3))  # round函数
    print(round(10 / 3, 2))  #
    print("%.2f" % (10/3))  # 基本格式化输出
    print("{:.2f}".format(10/3))  # format格式化输出
    print(3**4)  """


    """
    输出一个三位数，输出每个位置的数字，
    比如719，显示如下
    百位数字：7  十位数字：1  各位数字：9 """
    # 方法01
    """ 
    num = int(input("请输入一个三位数："))
    bai = num // 100
    shi = num % 100 // 10
    ge = num % 100 % 10
    print("三位数{0}：百位数字：{1}, 十位数字:{2}, 个位数字：{3}".format(num, bai, shi, ge))
    """

    # 方法2
    # num = input("请输入一个三位数：")
    # print("三位数{0}：百位数字：{1}, 十位数字:{2}, 个位数字：{3}".format(num, num[0], num[1], num[2]))


    # 赋值运算符
    # 编程实现145893是几天几时几分几秒
    """
    total = 145893
    day = total // (24*60*60)
    hour = (total % (24*60*60)) // (60 * 60)
    minute = (total % (60*60)) // 60
    second = total % 60
    print("%d秒为 %d天 %d时 %d分 %d秒" % (total, day, hour, minute, second))"""

    # 用户 输入语文，数学，英语分数，输出总分和平均分
    """
    chinese = int(input("请输入语文分数："))
    math = int(input("请输入数学分数："))
    english = int(input("请输入英语分数："))
    print("本次考试总分：%.2f, 平均分:%.2f" % (chinese + math + english, (chinese+math+english)/3))"""

    # 输入三个互不相等的整数，按从小到大输出
    """num01, num02, num03 = eval(input("请输入三个整数，用逗号分隔："))
    if num01 > num02:
        if num02 > num03:
            print("从小到大输出：%d, %d, %d" % (num03, num02, num01))
        elif num01 > num03:
            print("从小到大输出：%d, %d, %d" % (num02, num03, num01))
        else:
            print("从小到大输出：%d, %d, %d" % (num02, num01, num03))
    else:
        if num03 < num01:
            print("从小到大输出：%d, %d, %d" % (num03, num01, num02))
        elif num03 > num02:
            print("从小到大输出：%d, %d, %d" % (num01, num02, num03))
        else:
            print("从小到大输出：%d, %d, %d" % (num01, num03, num02))"""

# 登录判断
    """
    提示输入用户名和密码
    如果用户名不等于admin，密码等于123.com,提示登录成功
    如果用户名不是admin，提示用户名不存在
    如果密码不等于123.com，提示密码错误
    """
    """username = input("请输入用户名：")
    password = input("请输入密码：")
    if username != "admin":
        print("用户名不存在")
    elif password != "123.com":
        print("密码错误")
    else:
        print("登录成功")"""

    # 逻辑运算符
    """print(True and False)
    print(True and True)
    print(True or False)
    print(not False)
    print(not True)"""

    """username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "admin" and password == "123.com":
        print("登录成功")
    else:print("用户名或密码错误")"""

    """chinese = int(input("请输入语文成绩："))
    math = int(input("请输入数学成绩："))
    print("老王的成绩是否大于90：", (chinese >= 90 and math >= 90))
    print("老王的成绩是否有一个大于90：", (chinese >= 90 or math >= 90))"""


    # 判断闰年
    # 判断条件： 能被400整除  or   能被4整数  但不能被400整除
    """year = int(input("请输入一个年份："))
    if (year % 400 ==0) or (year % 4 == 0 and year % 100 != 0):
        print("%d是闰年" % year)
    else:
        print("%d是平年" % year)"""


# 位运算符
    """print(102 & 210)  # & 位与  对应二进制都是1  才位1
    print(102 | 210)  # | 位或    对应二进制有一个位1   就为1
    print(102 ^ 210)  # ^ 异或运算   相同为0，不同为1
    print(~ 101)  # 位非运算，对应二进制数+1取反
    print(102 >> 2)  # 右移运算符：吧当前的数转为二进制后整体向右移动，左边用0补齐
    print(102 << 2)  # 右移运算符：吧当前的数转为二进制后整体向左移动，右边用0补齐"""

    # 成员运算符 ————是否包含，主要应用字符串或者集合里面
    # 字符串   字符串中是否包含另外一个字符串
    """ str01 = "my name is Steven, I come from china"
    if "come" in str01:
        print("包含")
    else:
        print("不包含")"""

    # 使用场景2：集合中是否包含另外一个元素
    """name_array = ["alice", "bob", "peter", "tomas"]
    name = input("请输入姓名：")
    if name in name_array:
        print("%s在集合中" % name)
    else:
        print("%s不在集合中" % name)"""

    # shuzi
    """data_array = [13, 11, 43, 66]
    data = int(input("请输入数字："))
    if data in data_array:
        print("%s在集合中" % data)
    else:
        print("%s不在集合中" % data)"""

    # 三元运算符
    # num01 = 100 if 100 > 200 else 200
    # print(num01)

    """if 100 > 200:
        num01 = 100
    else:
        num01 = 200
    print(num01)"""

    # 模拟登陆
    """username = input("请输入用户名：")
    password = input("请输入密码：")
    result = "登陆成功" if username == "admin" and password == "123" else "用户名或密码错误"
    print(result)"""

    # 输入两个不相等的数，判断大小
    """num01, num02 = eval(input("请输入两个不想等的数，以逗号分开："))
    print("num01大于num02" if num01 > num02 else "num01小于num02")"""


# 运算优先级
    # b = 9 > 7
    # print(b)
    # # > 运算符的优先级比  =高
    #
    # a = 4*2**3
    # print(a)  # **优先级大于*
    #
    # print(2 + 4 * -2)  # *优先级高于+
    #
    # print(2+4*2/4)  # * /的优先级高于+-
    # print(2*3+5<=5+1*2)  # *优先级最高，+其次，<=再次，=最次

    # 身份运算符
    num01 = 100
    num02 = 100
    num03 = num01
    print("num01和num02是不是同一个对象：", num01 is num03)

    list01 = [11, 22, 33, 44, 55]
    list02 = [11, 22, 33, 44, 55]
    list03 = list01
    print("list01是否是同一个对象：", list01 is list02)
    print("list01是否是同一个对象：", list01 is list03)