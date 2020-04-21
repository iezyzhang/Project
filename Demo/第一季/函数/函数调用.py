import random
# 生成若干个整数的集合   求最大值  最小值  元素之和   平均数

def build_array(start_number:int = 10, end_number:int = 100, number:int = 10):
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



if __name__ == "__main__":
    # 调用方法01：调用的标准做法实参和形参必须一一对应
    print(build_array(10, 50, 20))
    # 调用的方法02：调用时候指明参数名称, 这种情况下，调用的顺序可以不一致
    print(build_array(number=10, end_number=99, start_number=10))
    # 调用方法：按照形参的默认值
    print(build_array())

