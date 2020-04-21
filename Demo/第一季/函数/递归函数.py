"""
# 输入一个数， 计算这个数的阶层并输出

def get_result_01(num01):  # 常规方法
    result = 1
    for i in range(1, num01+1):
        result *= i
    return result

def get_result_02(num01):  # 递归方法
    if num01 == 1:
        return 1
    else:
        return num01 * get_result_02(num01 - 1)


if __name__ == "__main__":
    print(get_result_01(10))
    print(get_result_02(10))
"""

# 求所有元素之和
def sum_of_result(*args):
    sum01 = 0
    for i in args:
        if isinstance(i, (int, float, bool)):
            sum01 += i
        elif isinstance(i, (list, tuple)):
            sum01 += sum_of_result(*i)
    return sum01


if __name__ == "__main__":
    result = sum_of_result(10, [10, 10, [10]], (10, 10, [10, 10, [10, 10, 10]]))
    print(result)