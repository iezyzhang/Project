
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

def get_result_01(list01:list):
    result_list = [] # 第一个元素就是最大值，第二个最小值， 第三个求和
    max_result = list01[0]
    min_result = list01[0]
    sum_result = 0
    # 求最大值  最小值   求和
    for i in list01:
        if i > max_result:
            max_result = i
        if i < min_result:
            min_result = i
        sum_result += i
    result_list.append(max_result)
    result_list.append(min_result)
    result_list.append(sum_result)

    # 返回一个集合
    return result_list

def get_result_02(list01:list):
    result_list01 = []  # 第一个元素就是最大值，第二个最小值， 第三个求和
    max_result01 = list01[0]
    min_result01 = list01[0]
    sum_result01 = 0
    # 求最大值  最小值   求和
    for i in list01:
        if i > max_result01:
            max_result01 = i
        if i < min_result01:
            min_result01 = i
        sum_result01 += i
    return (max_result01, min_result01, sum_result01)


if __name__ == "__main__":
    # 生成集合
    list_number = build_array(100, 200, 10)
    print("生成的集合为：", list_number)

    # 方法01：最大值， 最小值， 求和
    result_list01 = get_result_01(list_number)
    print("最大值：", result_list01[0])
    print("最小值：", result_list01[1])
    print("所有元素之和：", result_list01[2])

    # 方法02 最大值， 最小值， 求和
    max_result, min_result, sum_result = get_result_02(list_number)
    print("最大值：", max_result)
    print("最小值：", min_result)
    print("所有元素之和：", sum_result)
