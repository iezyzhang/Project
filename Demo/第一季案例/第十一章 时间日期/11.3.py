"""
输入一个年份，打印当年和未来四年父亲节和母亲节日期，并分别打印出是该年多少天
"""
import time
import datetime
def get_years():
    """
    输入一个年份
    :return:
    """
    while True:
        year = input("请输出一个年份：")
        if year.startswith("-"):
            print("年份不能为负数")
            continue
        elif not year.isdigit():
            print("年份必须为数字")
            continue
        else:
            year_number = int(year)
            year_list = []
            year_list.append(year_number)
            year_list.append(year_number + 1)
            year_list.append(year_number + 2)
            year_list.append(year_number + 3)
            year_list.append(year_number + 4)
            return year_list

def get_mother_day(number:int):
    """

    :param year_list:
    :return:
    """
    list_day = [13,12,11,10,9,8,7]

    # 构建5月1日
    tuple01 = (number, 5, 1, 0, 0, 0, 0, 0, 0)
    # 将日期转换为时间戳
    time01 = time.mktime(tuple01)
    return datetime.datetime(number,5,1,0,0,0) + datetime.timedelta(days=list_day[time.localtime(time01)[6]])
def get_father_day(number:int):
    """

    :param year_list:
    :return:
    """
    list_day = [20,19,18,17,16,15,14]

    # 构建6月1日
    tuple01 = (number, 6, 1, 0, 0, 0, 0, 0, 0)
    # 将日期转换为时间戳
    time01 = time.mktime(tuple01)
    return datetime.datetime(number,6,1,0,0,0) + datetime.timedelta(days=list_day[time.localtime(time01)[6]])

def get_mother_and_father_day(year_list:list):
    """
    计算年份中的母亲节和父亲节
    :param year_list:
    :return:
    """
    for year in year_list:
        mother_day = get_mother_day(year)
        father_day = get_father_day(year)
        print("%d年母亲节为：%d年%d月%d日" % (year, mother_day.year, mother_day.month, mother_day.day), end="\t")
        print("父亲节为：%d年%d月%d日" % (father_day.year, father_day.month, father_day.day), end="\t")
        print()

if __name__ == "__main__":
    # 获取年份列表
    list_year = get_years()
    # print(list_year)
    # print(get_mother_day(2018))
    # print(get_father_day(2018))
    get_mother_and_father_day(list_year)
