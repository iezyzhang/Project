
"""
输入1到20得数，求阶乘的和
"""

def get_factorial(number:int):
    """
    返回这个数的阶乘和
    :param number:
    :return:
    """
    # 传统做法
    result = 1
    for number in range(2, number + 1):
        result = result * number
    return result
def get_factorial02(number:int):
    """
    返回这个数的阶乘
    :param number:
    :return:
    """
    if number == 1:
        return 1
    else:
        return number * get_factorial02(number - 1)
def get_total_factorial(number:int):
    """
    计算阶乘总和
    :param number:
    :return:
    """
    sum01 = 0
    for number in range(1, number + 1):
        sum01 += get_factorial02(number)
    return sum01

if __name__ == "__main__":
    total = get_total_factorial(10)
    print(total)
