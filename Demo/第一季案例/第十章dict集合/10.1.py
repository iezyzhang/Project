
"""
有十名90后学生，【王一，胡二，张三，李四，赵武，马六，杨奇，刘八，孙久，陈氏】
为他们随即生成10个生日
1、数据存储格式（姓名：生日）
2、输出10个同学的姓名姓名生日
3、按季节统计同学的出生状况，包括学生个数和具体姓名
    春季【3月-5月】，夏季【6月-8月】，秋季【9月-11月】，冬季【12月-2月】
"""
import random
import datetime
def build_name_birthday(list_name:list):
    """
    生成10个姓名list
    :param list_name:
    :return:
    """
    # 定义一个字典集合
    name_birthday_dict = {}
    # 遍历list集合
    for item in list_name:
        name_birthday_dict[item] = get_birthday()
    return name_birthday_dict

def get_birthday():
    """
    获得生日
    :return:
    """
    year = random.randint(1990, 1999)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    # 异常处理
    while True:
        try:
            dt01 = datetime.datetime(year=year,month=month,day=day)
            return dt01
        except:
            continue

def birthday_statistics(dict01:dict, name_list01:list):
    """
    按季节统计人数和姓名
    :param dict01:
    :return:
    """

    # 遍历字典
    spring_list = []
    summer_list = []
    autumn_list = []
    winter_list = []
    for item in name_list01:
        if dict01[item].month in [3,4,5]:
            spring_list.append(item)
        elif dict01[item].month in [6,7,8]:
            summer_list.append(item)
        elif dict01[item].month in [9, 10, 11]:
            autumn_list.append(item)
        elif dict01[item].month in [12, 1, 2]:
            winter_list.append(item)
        # 构造字典
        birthday_dict = {}
        birthday_dict["春季"] = spring_list
        birthday_dict["夏季"] = summer_list
        birthday_dict["秋季"] = autumn_list
        birthday_dict["冬季"] = winter_list

    return birthday_dict


if __name__ == "__main__":
    name_list = ["王一", "胡二", "张三", "李四", "赵武", "马六", "杨奇", "刘八", "孙久", "陈氏"]

    name_birthday_dict01 = build_name_birthday(name_list)
    # 打印
    print("======================姓名生日============================")
    for item in name_list:
        birthday = "%s年%s月%s日" % (str(name_birthday_dict01[item].year),
                                  str(name_birthday_dict01[item].month),str(name_birthday_dict01[item].day))
        print("姓名：%s\t  生日：%s" % (item, birthday))

    season_dict = birthday_statistics(name_birthday_dict01, name_list)
    season_list01 = season_dict.keys()
    # 打印
    print("==========================季节统计====================")
    for item in season_list01:
        print("%s\t    共%d人\t    姓名为：%s" % (item, len(season_dict[item]), season_dict[item]))