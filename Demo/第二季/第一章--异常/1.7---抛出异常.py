
# 输入两个0-1000的数，求和差积商

def sum01(num01:int, num02:int):
    """
    求两个数之和
    :param num01:第一个数
    :param num02:第二个数
    :return:两数之和
    """
    return num01 + num02
def sub01(num01:int, num02:int):
    """
    求两个数之和
    :param num01:第一个数
    :param num02:第二个数
    :return:两数之和
    """
    return num01 + num02
def c01(num01:int, num02:int):
    """
    求两个数之和
    :param num01:第一个数
    :param num02:第二个数
    :return:两数之和
    """
    return num01 + num02
def div01(num01:int, num02:int):
    """
    求两个数之和
    :param num01:第一个数
    :param num02:第二个数
    :return:两数之和
    """
    if num01 < 0 or num01>1000 or num02 < 0 or num02 >1000:
        raise Exception("输入的值不在有效范围内")
    try:
        return num01 / num02
    except ZeroDivisionError as e:
        raise e
if __name__ == "__main__":
    try:
        num01 = int(input("请输入第一个整数："))
        num02 = int(input("请输入第二个整数："))
        print("%d + %d = %d" %  (num01,num02, div01(num01, num02)))
    except ValueError as e:
        print("输入不是数字")
    except ZeroDivisionError as e:
        print("除数不为0")
    except Exception as e:
        print(e)


