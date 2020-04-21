
"""
计算出100-1000内所有质数之和并输出结果，并计算出整个程序执行花了多长时间

"""
import time
import math
def get_result(start:int,end:int):
    """
    计算两个数范围内的质数
    :param start:
    :param end:
    :return:
    """
    print("从%d到%d的质数有：")
    for item in range(start, end + 1):
        for index in range(2, int(math.sqrt(item)) + 1):
            if item % index == 0:
                break
            if index == int(math.sqrt(item)):
                print(item, end="  ")


if __name__ == "__main__":
    # 计算当前时间
    time01 = time.time()
    # 开始计算
    get_result(100, 10000)
    # 获取计算后时间
    time02 = time.time()
    # 打印结果
    print("\n计算用时为：%.2f" % (time02 - time01))
