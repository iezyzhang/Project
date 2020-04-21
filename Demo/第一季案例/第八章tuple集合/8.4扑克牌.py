"""
一副扑克牌52张，4个玩家在玩，模拟系统发牌，洗牌，整理牌，需求如下：
1、先按照顺序打印一副扑克牌
2、在没有洗牌的情况下，输出发到玩家的扑克牌
3、实现洗牌，然后发到四个玩家的扑克牌
4、对洗牌后的四个玩家的扑克牌进行整理
整理规则1、 数字从小到大
            （3 4 5 6 7 8 9 10 j q k A 2）
整理规则2、 在数字相同的情况下，按照花色（黑红梅方）
"""

import random

def get_poker(number:int = 1):
    """
    获得几幅扑克牌
    :param number:
    :return:
    """
    # 数字：3、4、5、6、7、8、9、10、J、Q、K、A、2
    # 花色：黑红梅方----------♠♥♣♦
    # 数字：03、04、05、06、07、08、09、10、11、12、13、14、15
    # 花色：01、02、03、04
    # 组合：
    poker_number = []
    for item in range(0,13):
        poker_number.append("%02d" % item)
    # 生成花色
    poker_type = ("00","01","02","03")
    # 构件扑克牌
    poker_list = []
    for pair in range(number):
        for number in poker_number:
            for type in poker_type:

                poker_list.append(str(number) + str(type))
    return poker_list

def print_poker(poker_list:list):
    """
    打印扑克牌
    :param poker_list:
    :return:
    """
    poker_number = ("3","4","5","6","7","8","9","10","J","Q","K","A","2")
    poker_type = ("♠","♥","♣","♦")
    # 遍历集合
    for item in poker_list:
        print("%s%s" % (poker_type[int(item[2:])],poker_number[int(item[0:2])]),end=" ")


def deal_poker(poker_list:list,person:int = 4):
    """
    模拟发牌，默认四个玩家
    :param poker_list:
    :param person:
    :return:
    """
    # 定义一个集合包含n个玩家的牌
    deal_poker_list = []
    for number in range(person):
        # 一个玩家
        temp_list = []
        # 遍历牌
        for index in range(len(poker_list)):
            if index % person == number:
                temp_list.append(poker_list[index])
        # 添加到list
        deal_poker_list.append(temp_list)
    return deal_poker_list

def print_all_poker(poker_list:list):
    # 打印四家的牌
    for index in range(len(poker_list)):
        print("第%d家的牌" % (index + 1), end=" ")
        print_poker(poker_list[index])
        print()
def sort_poker(poker_list:list):
    """
    整理牌
    :param poker_list:
    :return:整理的牌
    """
    sorted_poker_list=[]
    for item in poker_list:
        sorted_poker_list.append(sorted(item))
    return sorted_poker_list
if __name__ == "__main__":
    # 获得扑克牌列表
    poker_all = get_poker(1)
    print("==============所有扑克牌=============")
    # 打印
    print_poker(poker_all)
    print("\n==============洗牌前所有扑克牌=============")
    deal_list = deal_poker(poker_all)
    print_all_poker(deal_list)
    # 洗牌
    print("==============洗牌后所有扑克牌=============")
    random.shuffle(poker_all)
    # 发牌
    deal_list = deal_poker(poker_all)
    print_all_poker(deal_list)
    print("==============整理后所有扑克牌=============")
    sorted_list = sort_poker(deal_list)
    print_all_poker(sorted_list)



