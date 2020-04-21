
"""
随机生成50-100个姓名（每个名字5个英文字母，首字母大写）
具体需求：
1、输出生成所有姓名，每行10个
2、输出7的倍数或者包含7的索引位上的名字
3、获取所有H开头的姓名
4、删除所有带4的索引号的姓名
5、把首字母A改成B
"""
import random
def get_name_list():
    """
    生成50-100个姓名   名字组成   一个大写字母 + 四个小写字母
                       大写字母Ask吗的范围65--90  小写字母97--122
                       大写字母list=【A，B  】
    :return: 名字的list
    """
    # 定义一个list存储生成的姓名
    name_list = []
    # 生成
    for number in range(random.randint(50,100)):
        # 定义一个temp_name
        temp_name = ""
        # 添加名字的第一个大写字母
        temp_name += chr(random.randint(65,90))
        # 添加名字的四个小写字母
        for index in range(4):
            temp_name += chr(random.randint(97,122))
        name_list.append(temp_name)
    return name_list

def print_name(name:list):
    """
    打印list的姓名，一行10个
    :param name:
    :return:
    """
    for index in range(len(name)):
        # 一行10个换行
        print(name[index], end="   ")
        if (index + 1) % 10 == 0:
            print()

def print_name_contain_seven(name:list):
    """

    :param name:
    :return:
    """
    for index in range(len(name)):
        if "7" in str(index) or index % 7 ==0:
            print(name[index],end="   ")

def print_name_start_h(name:list):
    """
    输出以h开头的姓名
      :param name:
      :return:
      """
    for index in range(len(name)):
        if str(name[index]).startswith("H"):
            print(name[index], end="   ")

def delete_name_index_contain_four(name:list):
    """
    删除索引号为包含4的元素
    :param name:
    :return:
    """
    new_name_list = []
    for index in range(len(name)):
        if "4" not in str(index):
            new_name_list.append(name[index])

    return new_name_list

def rename_a_to_b(name:list):
    """
    把字母A--》B
    :param name:
    :return:
    """
    for index in range(len(name)):
        if str(name[index]).startswith("A"):
            name[index] = "B" + str(name[index])[1:]

if __name__ == "__main__":
    name_list = get_name_list()
    print("姓名数量：", len(name_list))
    print("========================================================================")
    print_name(name_list)
    print("\n========================================================================")
    # 需求2  输出7的倍数或者包含7的索引位上的名字
    print("===========================输出含7的索引的名字==============================")
    print_name_contain_seven(name_list)
    print("\n========================================================================")
    # 需求3  输出h开头的名字
    print("===========================输出含7的索引的名字==============================")
    print_name_start_h(name_list)
    print("\n========================================================================")
    # 需求4  删除所有带4的索引名字
    print("===========================删除所有带4的索引名字==============================")
    name_list = delete_name_index_contain_four(name_list)
    print_name(name_list)
    print("\n========================================================================")
    # 需求5  把首字母A改成B
    print("===========================把首字母A改成B==============================")
    rename_a_to_b(name_list)
    print_name(name_list)
    print("\n========================================================================")
