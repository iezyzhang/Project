import math
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


def get_list_prime(small_number,big_number,number):
    """
    从大到小取五个质数
    :param small_number:较小的数
    :param big_number: 较大的数
    :param number: 取得数量
    :return: 取得五个列表
    """
    # 定义存储取到的质数
    prime_list = []
    for i in range(big_number,small_number,-1):
        # 判断是不是质数
        if prime_number(i):
            prime_list.append(i)
            if len(prime_list) == number:
                return prime_list
        else:
            pass


if __name__ == "__main__":
    # 调用
    get_list = get_list_prime(1,100,5)
    print("1-100后五个质数为：",get_list)
    print("5个质数之和为：", sum(get_list))
