import math
"""
提示用户输入半径，计算出圆的周长面积，要求如下：
1、圆周率π取3.1415926
2、如果输入的是负数和0，提示半径不能让为负数或者零
3、计算结果保留两位小数

"""
# 方法01   常规做法
"""pi = 3.1415926
# 提醒输入半径
radius = input("请输入圆的半径：")
# 判断输入的是否符合要求
if radius.isdigit():
    radius_num = float(radius)
    # 输出
    print("圆的周长为：%.2f" % (2*pi*radius))
    print("圆的面积为：%.2f" % (pi*radius*radius))
else:
    print("输入半径不符合要求，要求大于0的数字")"""

# 方法02  函数封装
def check_input(number:str):
    """
    判断某一个字符是否是数字
    :param number: 要判断的字符
    :return: 如果是数字，返回True，如果不是数字，返回False
    """
    if number.replace(".", "").isdigit():
        return True
    else:
        return False

def get_perimeter(radius:float):
    """
    根据半径，获得圆的周长
    :param radius: 半径
    :return: 返回周长
    """
    pi = 3.1415926
    return 2*pi*radius
def get_area(radius:float):
    """
    根据半径，获得圆的面积
    :param radius: 半径
    :return: 返回面积
    """
    pi = 3.1415926
    return pi*radius*radius

if __name__ == "__main__":
    # 提醒输入半径
    radius = input("请输入圆的半径：")
    # 判断是否有效
    if check_input(radius):
        # 计算周长和面积
        print("圆的周长为：%.2f" % get_perimeter(float(radius)))
        print("圆的面积为：%.2f" % get_area(float(radius)))
    else:
        print("输入半径不符合要求，要求大于0的数字")
