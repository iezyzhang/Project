
"""
输入两个数  求最大公约数和最小公倍数
"""
def get_gcd(num01,num02):
    """
    求最大公约数
    :param num01:第一个数
    :param num02: 第二个数
    :return: 返回最大公约数
    """
    if num01 > num02:
        for i in range(num02,0,-1):
            if num01 % i == 0 and num02 % i == 0:
                return i
    else:
        # get_gcd(num02,num01)
        for i in range(num01,0,-1):
            if num01 % i == 0 and num02 % i == 0:
                return i

def get_mcm(num01,num02):
    """
    求最小公倍数
    :param num01:
    :param num02:
    :return: 返回最小公倍数
    """
    if num01 > num02:
        for i in range(num01, num01*num02+1):
            if i % num01 == 0 and i % num02 == 0:
                return i
    else:
        # get_gcd(num02,num01)
        for i in range(num02, num01 * num02 + 1):
            if i % num01 == 0 and i % num02 == 0:
                return i


if __name__ =="__main__":
    print(get_gcd(12,36))
    print(get_mcm(12,36))
    print(12*36/get_gcd(12,36))


