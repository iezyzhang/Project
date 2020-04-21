
"""
随机生成10个农历的年龄，依次输入农历年份的生肖属相
年份  %  12  =  result
"""
import random

def get_years(number:int,start:int,end:int):
    """
    生成多少个年份
    :param number:
    :return:
    """
    list_years = []
    for index in range(number):
        list_years.append(random.randint(start,end))

    # 返回
    return list_years

def print_years_zodiac(list):
    zodiac_tuple = ("猴","鸡","狗","猪","鼠","牛","虎","兔","龙","蛇","马","羊")
    for item in list:
        print("农历年份：%d\t属相：%s" % (item, zodiac_tuple[item % 12]))


if __name__ == "__main__":
    list_years1 = get_years(10,1900,2019)
    print(list_years1)
    print_years_zodiac(list_years1)

