"""
计算三角形的三边，然后计算三角形的周长和面积，
需要些两个函数
    1、校验三条边是否满足条件   check_input
    2、计算三角形周长面积    get_perimeter_area
"""
import math
def input_number():
    """
    输入三角形的遍
    :return:
    """
    while True:
        number_str = input("请输入三角形的边：")
        # 判断是否是数字
        try:
            number = float(number_str)
            if number <= 0:
                print("输入的数必须为整数")
                continue
            return number
        except:
            print("输入的必须为数字")

def check_edge(num01, num02, num03):
    """
    校验三条边能否构成三角形
    :param num01:
    :param num02:
    :param num03:
    :return:
    """
    if num01 + num02 < num03:
        return False
    if num01 + num03 < num02:
        return False
    if num03 + num02 < num01:
        return False
    return True

def get_perimeter_area(num01, num02, num03):
    """
    计算三角形周长面积
    :param num01:
    :param num02:
    :param num03:
    :return:
    """
    perimeter = num01 + num02 + num03
    area = math.sqrt((perimeter/2) * (perimeter/2 - num01)* (perimeter/2 - num02)* (perimeter/2 - num03))
    return perimeter, area

if __name__ == "__main__":
    # 输入三角形的三条边
    edge01 = input_number()
    edge02 = input_number()
    edge03 = input_number()
    if check_edge(edge01, edge02, edge03) == False:
        print("三条边不能构成三角形")
    else:
        permetre, area = get_perimeter_area(edge01, edge02, edge03)
        print("三角形的周长为：%.2f  面积为：%.2f" % (permetre, area))

