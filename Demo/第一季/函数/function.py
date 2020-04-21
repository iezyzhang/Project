#
# def print_text(text):
#     """
#     功能描述： 用来打印指定的文本
#     :param text:  print_text  要打印的wenb
#     :return: 没返回值
#     """
#     print(text)
#
# def print_start():
#     print("=========cehgnxu执行的开始===============")
#
# def print_end():
#     print("=============程序执行结束===================")
#
# def connect_str(str01, str02):
#     """
#     功能描述： 连接两个字符串
#     :param str01:  第一个字符串
#     :param str02:  第二个周四付出
#     :return:    返回连接后的字符串
#     """
#     str_num = str01 + str02
#     return str_num
#
#
# if __name__ == "__main__":
#     # 打印程序开始
#     print_start()
#     print_text("欢迎学习PythonPython")
#
#     # 打印具体文本
#     str_num = connect_str("我是", "中国人")
#     print_text(str_num)
#     print_end()
#

import random
# 生成若干个整数的集合   求最大值  最小值  元素之和   平均数

def build_array(start_number:int, end_number:int, number:int):
    """
    功能描述： 生成若干个固定范围内的整数集合
    :param start_number: 指定范围的起始值
    :param end_number: 指定范围结束值
    :param number: 生成数量
    :return: 整数集合
    """
    number_list = []
    for i in range(number):
        number_list.append(random.randint(start_number, end_number))
    return number_list

def sum_of_list(list01:list):
    """
    功能描述：求所有元素之和
    :param list01: 要求list的名称
    :return: 返回所有元素之和
    """
    sum01 = 0
    for i in list01:
        sum01 += i
    return sum01

def max_of_list(list01:list):
    max_number = list01[0]
    for i in list01:
        if i > max_number:
            max_number = i
    # 返回
    return max_number


def min_of_list(list01:list):
    min_number = list01[0]
    for i in list01:
        if i < min_number:
            min_number = i
    # 返回
    return min_number


if __name__ == "__main__":
    # 生成集合
    list_number = build_array(100, 200, 10)
    print("生成的集合为：", list_number)

    # 求最大值
    print("生成元素的最大值为：", max_of_list(list_number))
    # 求最小值
    print("生成元素的最小值为：", min_of_list(list_number))
    # 求和
    print("所有的元素之和为：", sum_of_list(list_number))
    # 平均值
    print("所有的元素的平均值为：", sum_of_list(list_number) / 10)