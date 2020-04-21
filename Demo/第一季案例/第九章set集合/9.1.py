

# list: 可编辑
# tuple   不可编辑
# set    无序不可重复
"""list01 = [11, 33, 44, 55, 66, 77]
set01 = {11, 33, 44, 55, 66, 77, 77}

print(list01[1])
print(set01)"""

"""
生成20个50-100之间互不相等的数，统计有多少个质数，并输出。
"""
import random
import math
def get_numbers(start:int, end:int, number:int):
    """
    生成某个范围多个数
    :param start:开始值
    :param end:结束值
    :param number:个数
    :return:生成数字的集合
    """
    # 定义一个空的集合
    number_set = set()
    # 生成数字
    while len(number_set)<number:
        number_set.add(random.randint(start,end))
    return number_set

def prime_number(number):
    """
    判断某一个数是不是质数
    :param number: 要判断的整数
    :return: 是T  不是 F
    """
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            # 如果在求余过程中有一个被整除了，那么这个数不是质数
            return False
        if i == int(math.sqrt(number)):
            # 所有的都没有被整除
            return True

def get_prime(set01:set):
    """
    获得集合中的质数
    :param set01: 集合
    :return: 质数
    """
    primes_set = set()
    for item in set01:
        if prime_number(item):
           primes_set.add(item)
    return primes_set

if __name__ == "__main__":
    # 获得集合
    numbers = get_numbers(50, 100, 20)
    print(numbers)
    # 获得质数
    prime_number_set = get_prime(numbers)
    print("生成的质数个数为：", len(prime_number_set))
    print("质数有：", prime_number_set)
