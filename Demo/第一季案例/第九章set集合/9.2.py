"""
随机生成6个姓名，每个姓名5个字母，小写
输出  6个名字中没有包含的字母

"""
import random

def get_name_list(number:int):
    """
    生成50-100个姓名   名字组成   一个大写字母 + 四个小写字母
                       大写字母Ask吗的范围65--90  小写字母97--122
                       大写字母list=【A，B  】
    :return: 名字的list
    """
    # 定义一个list存储生成的姓名
    name_list = []
    # 生成
    for number in range(number):
        # 定义一个temp_name
        temp_name = ""

        # 添加名字的5个小写字母
        for index in range(5):
            temp_name += chr(random.randint(97,122))
        name_list.append(temp_name)
    return name_list

def get_all_lower_char():
    """
    获得所有的小写字母
    :return:
    """
    lower_char = []
    for index in range(97, 123):
        lower_char.append(chr(index))
    return  lower_char

def get_all_char(number_set:list):
    """
    获得所有的set集合的字母
    :param number_set:
    :return:
    """
    # 拼接所有字母
    char_list = set()
    # 遍历集合
    for item in number_set:
        char_list.update(item)
    return char_list





if __name__ == "__main__":
    name_list01 = get_name_list(6)
    print("生成的名字：", name_list01)

    # 所有小写字母
    all_lower_list = get_all_lower_char()
    print("所有小写字母：", all_lower_list)

    # 当前字母
    current_set_char = get_all_char(name_list01)
    print("当前名字中出现的小写字母：", current_set_char)

    # 判断哪些字母没有
    print("以下字母没有出现：", set(all_lower_list) - current_set_char)
    print("以下字母没有出现：", set(all_lower_list).difference(current_set_char))
