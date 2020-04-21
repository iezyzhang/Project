
"""
准备10个人的姓名。然后为这10个人随机生成生日 都90后
1 统计那些人是那些季节出生
2 谁的生日最早  最晚
3 最大 比最小大多少天
"""
import datetime
import random

def build_birthday(list01_person_name:list):
    # 初始化存储   "姓名: 生日"  字典
    name_birthday = {}.fromkeys(list01_person_name)
    # print(name_birthday)
    # 生成生日
    for key in name_birthday:
        temp_year = random.randint(1990, 1999)
        temp_month = random.randint(1, 12)
        temp_day = random.randint(1, 30)
        name_birthday[key] = datetime.date(temp_year, temp_month, temp_day)
    return name_birthday

def person_birthday_summer(name_birthday: dict):
    # 用户存储夏天出生的key
    list_person = []
    for key in name_birthday:
        # print(name_birthday[key])
        if name_birthday[key].month >= 6 and name_birthday[key].month <= 8:
            list_person.append(key)
    # 返回
    return list_person

# 获取最大年龄
def get_person_max_min(name_birthday: dict):
    person_birth = list(name_birthday.values())
    # 获取最大的生日
    max_birthday = sorted(person_birth)[len(person_birth) - 1]
    # 遍历
    for key in name_birthday:
        if (name_birthday[key] == max_birthday):
           return key

# 获取最小年龄
def get_person_min(name_birthday: dict):
    person_birth = list(name_birthday.values())
    # 获取最大的生日
    min_birthday = sorted(person_birth)[0]
    # 遍历
    for key in name_birthday:
        if (name_birthday[key] == min_birthday):
           return key

# 获取年龄 差距
def get_person_days(name_birthday: dict):
    person_birth = list(name_birthday.values())
    # 获取最大的生日
    max_birthday = sorted(person_birth)[len(person_birth) - 1]
    min_birthday = sorted(person_birth)[0]
    # 返回天数
    return (max_birthday - min_birthday).days

# 生日最小的
def get_person_early_birthday(name_birthday: dict):
    for key in name_birthday:
        name_birthday[key] = name_birthday[key].replace(year=1990)
    person_birth = list(name_birthday.values())
    return (sorted(person_birth)[0])


# 生日最大的
def get_person_later_birthday(name_birthday: dict):
    for key in name_birthday:
        name_birthday[key] = name_birthday[key].replace(year=1990)
    person_birth = list(name_birthday.values())
    return (sorted(person_birth)[len(person_birth)-1])


if __name__ == "__main__":
    list_name = ["王一", "胡二", "张三", "李四", "赵武", "马六", "杨奇", "刘八", "孙久", "陈氏"]
    # 为list_name中所有学员生成生日
    name_birthday = build_birthday(list_name)
    print(name_birthday)
    # 调用功能模块
    birthday_summer_list = person_birthday_summer(name_birthday)
    if (len(birthday_summer_list) == 0):
        print("没有人的生日在夏天")
    else:
        print("生日为夏天的有：", birthday_summer_list)
    # 调用最大
    print("年龄最大的", get_person_max_min(name_birthday))
    print("年龄最小的", get_person_min(name_birthday))

    print("最大的比最小的大的天数", get_person_days(name_birthday))

    # 调用
    date_early = get_person_early_birthday(name_birthday)
    print("生日最大的为：%d月%d日" % (date_early.month, date_early.day))

    date_later = get_person_later_birthday(name_birthday)
    print("生日最大的为：%d月%d日" % (date_later.month, date_later.day))