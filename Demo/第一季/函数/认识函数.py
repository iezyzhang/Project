
def get_number(num01):  # num01 为形参
    """
    用来返回num01*num01 - num01 的值
    :param num01:参数
    :return:返回结果
    """
    return num01 * num01 - num01

def get_add_result(num01, num02):
    return num01+num02

def get_sub_result(num01, num02):
    return num01 - num02

def get_mul_result(num01, num02):
    return num01 * num02

def get_div_result(num01, num02):
    return num01 / num02


if __name__ == "__main__":
    print(get_number(10))  # 10是实参
    print("100和50进行运算")
    print("两数相加结果为：", get_add_result(100, 50))
    print("两数相减结果为：", get_sub_result(100, 50))
    print("两数相乘结果为：", get_mul_result(100, 50))
    print("两数相除结果为：", get_div_result(100, 50))