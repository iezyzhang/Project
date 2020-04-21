import sys
import math
if __name__ == "__main__":
    num01 = 100
    num02 = 112300000000
    num03 = 0x123214
    num04 = 0o12321
    num05 = 1e20

    print("num01占用空间：", sys.getsizeof(num01))
    print("num02占用空间：", sys.getsizeof(num02))
    print(abs(100))
    print(abs(-100))      # 绝对值
    print(math.fabs((-100)))  # 绝对值
    print(math.sqrt(100))   # 平方根
    print((pow(3, 4)))    # a的b次方
    print(max(12, 43, 67, 87))
    print(min(12, 43, 11, 87))
    # round
    num01 = 12.234
    print(round(num01))  # 获取整数位
    # 保留两位有效数字   类似四舍五入
    print(round(num01, 2))
    # ceil  向上取整,返回上入整数
    print(math.ceil(num01))
    print(math.ceil(-1.3424))
    # floor 返回下舍整数
    print(math.floor(num01))
    print(math.floor(-12.893443))

    # modf  分别返回整数部分和小数部分
    print(math.modf(num01))
    print(math.modf(num01)[0])
    print(math.modf(num01)[1])
    print(math.modf(-12.3456))

    is_small = True  # 1
    is_first = False  # 0
    print(is_small+100)
    #  所有非0整数在True
    if 0:
        print("真")
    else:
        print("假")
