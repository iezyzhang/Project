"""
在一次电视综艺节目中，观众通过手机拨打电话参与综艺节目，奖品是0-9的数字对应的奖品(奖品自行定义) ,用户拨通电话后，在事先准备的题目中随意抽3道进行电话答题(题目和答案自行准备，题目为选择题或判断题)。
【1】如果只答对一道，在用户手机号码包含的数字中随机抽取一个数字，奖品就是获取对应数字的奖品
【2】如果答对两道题，在用户手机号码包含的数字中随机抽取两个数字，奖品就是这两个数字对应的奖品
【3】如果三道题都答对，手机号码中所有数字对应的奖品都可以带走
【4】程序运行后，输入自己的手机号码然后开始答题，三道题目答完后，显示你获得的奖品。
"""
import random
import time

def input_name_moble():
    """
    输入姓名和电话
    :return:
    """
    name = input("请输入参赛选手姓名：")
    moble = input("请输入参赛选手电话：")
    # 对输入进行检验

    return name, moble

def start_answer(name:str):
    """
    开始答题
    :param name:
    :return:
    """
    # 准备题目，随机选择三道题
    current_question_list = []
    current_answer_list = []
    current_question_list, current_answer_list = prepare_question(3)
    # 开始答题
    print(name + "，请开始答题！")

    # 记录答对的数量
    right_number = 0

    for index in range(3):
        time.sleep(1)
        print("第" + str(index + 1) + "题, " + current_question_list[index] + "请回答：")
        answer = input()
        # 判断是否正确
        if answer.strip() == current_answer_list[index]:
            print("恭喜你！回答正确！")
            right_number += 1
        else:
            print("回答错误！")
    # 返回回答正确的题目数量
    return right_number


def prepare_question(number:int):
    """
    准备答题的题目
    :param number:
    :return:
    """

    question_tuple = ("世界上国土面积最大的国家？", "世界上人口最多的国家？", "世界上最长的河是那条河？", "澳大利亚的首都？",
                      "中国最大的湖泊？", "2006年世界杯冠军是哪个国家？", "2012年NBA总冠军是哪个队？",
                      "枸杞是中国哪个地方的特产？")
    answer_tuple = ("俄罗斯", "中国", "尼罗河", "堪培拉", "鄱阳湖", "意大利", "迈阿密热火", "宁夏")

    # 准备题目的序号   保证抽不到相同的题目
    current_question_index = []
    while True:
        current_index = random.randint(0, len(question_tuple) - 1)
        if current_index not in current_question_index:
            current_question_index.append(current_index)
        if len(current_question_index) == number:
            break

    # 准备题目
    current_question_list = []
    current_answer_list = []
    for index in current_question_index:
        current_question_list.append(question_tuple[index])
        current_answer_list.append(answer_tuple[index])
    #返回
    return current_question_list, current_answer_list

def get_random_number(list_all:list, number:int):
    """
    在一个集合随机找到几个
    :param list_all:
    :param number:
    :return:
    """
    current_list = []
    while True:
        temp = list_all[random.randint(0, len(list_all))]
        if temp not in current_list:
            current_list.append(temp)
        if len(current_list) == number:
            break
    return current_list

def get_lucky(right_number:int, mobile:str):
    """
    获得奖品
    :param right_number:
    :return:
    """
    lucky_tuple = ["iPhoneX手机", "PPTV 50寸高清电视", "iPad平板", "1000元红包", "64G U盘", "100元话费",
                   "海尔空调", "美的豪华电饭煲", "Dell品牌电脑", "新马泰豪华7日游"]
    # 准备手机号码集合
    mobile_set = set()
    mobile_set.update(mobile)
    # 判断获得的奖品
    lucky_list = []
    if right_number == 1:
        lucky_list.append(lucky_tuple[int(list(mobile_set)[random.randint(0, len(list(mobile_set)))])])
    elif right_number == 2:
        # 随机抽两个
        two_lucky_list = get_random_number(list(mobile_set), 2)
        for item in two_lucky_list:
            lucky_list.append(lucky_tuple[int(item)])


    elif right_number == 3:
        for index in list(mobile_set):
            lucky_list.append(lucky_tuple[int(index)])
    return lucky_list

if __name__ == "__main__":

    name, moble = input_name_moble()
    # print(name, moble)

    # 开始答题，并返回正确的数量
    number = start_answer(name)



    if number == 0:
        print("很遗憾，没有获奖。")
    else:
        lucky_list = get_lucky(number, moble)
        print("=============答题结果====================")
        print("恭喜你获奖了！ 姓名：%s 手机号码：%s" % (name, moble))
        print("你回答正确%d道题目！" % number)
        print("奖品为：%s" % lucky_list)



    #lucky_tuple = ["iPhoneX手机", "PPTV 50寸高清电视", "iPad平板", "1000元红包", "64G U盘", "100元话费",
    #              "海尔空调", "美的豪华电饭煲", "Dell品牌电脑", "新马泰豪华7日游"]

