
"""
输入红包金额，然后输入红包数量，结果显示那些人抢到了多少红包
"""
import random
def input_red_picket():
    """
    输入红包金额
    :return:
    """
    while True:
        money_string = input("请输入红包金额：")
        try:
            if money_string.startswith("-"):
                raise ValueError("金额不能为负数！")
            money = float(money_string)
            return money
        except ValueError as e:
            print(e)
            continue

def input_red_number():
    """
    输入红包数量
    :return:
    """
    while True:
        number_string = input("请输入红包数量：")
        try:
            if number_string.startswith("-"):
                raise ValueError("输入数值不符合要求！")
            number = int(number_string)
            return number
        except ValueError as e:
            print(e)
            continue

def distribution_red_picket(money:float,number:int):
    """
    按照金额分配固定红包
    :param money:
    :param number:
    :return:
    """
    list_number = []
    for item in range(number):
        list_number.append(random.randint(100,1000))
    # 分配红包
    red_list = []
    already_red_money = 0
    for index in  range(len(list_number)):
        if index == len(list_number) - 1:
            red_list.append(round(money - already_red_money,2))
        else:
            this_packet = round(money * list_number[index]/sum(list_number),2)
            red_list.append(this_packet)
            already_red_money += this_packet
        # 最后一个红包：总的-已经分配的
    return red_list

def get_names():
    """
    获取规定数量的姓名
    :return:
    """
    xin = ('张','王','李','赵','陈','钱','孙','周','吴','郑','冯','将','沈','韩','杨')
    ming = ('进','刚','鹏','兰','爱国','建华','青玉','花','杰','霞','强','丽丽','陈')
    name_list = []
    for item in range(number):
        temp_number = xin[random.randint(0,len(xin)-1)] + ming[random.randint(0,len(ming)-1)]
        name_list.append(temp_number)
    return name_list


if __name__ == "__main__":


    money = input_red_picket()
    number = input_red_number()

    # 获取分配的红包
    red_packet_list = distribution_red_picket(money,number)
    # print(red_packet_list)
    # print(sum(red_packet_list))

    # 获取规定的数量姓名

    name_list = get_names()
    # 打印红包获得
    print("====================================================================")
    for index in range(number):
        print("%s抢到了红包，红包金额为：%.2f" % (name_list[index],red_packet_list[index]))
    print("====================================================================")