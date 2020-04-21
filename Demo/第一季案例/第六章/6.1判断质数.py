import math
"""
判断一个数是不是质数
"""
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

if __name__ == "__main__":
    num01 = int(input("请输入一个整数："))
    if prime_number(num01):
        print("%d是质数！" % num01)
    else:
        print("%d不是质数！" % num01)

