
"""
输入5个100-200间的整数
打印出5个数中最大的数和最小的数
"""
# 判断是不是整数  是不是100-200

def input_numbers(number:int):
    """
    输入多个整数
    :param number:输入的数量
    :return: 返回的集合
    """
    # 定义一个集合
    list_number = []
    # 输入五个
    for i in range(number):
        while True:
            temp = input("请输入第" + str(i+1) + "个整数：")
            # 判断是不是整数   是不是100-200
            if check_input(temp):
                list_number.append(int(temp))
                break
            else:
                print("输入不符合要求，请重新输入，", end=" ")
    # 返回集合
    return list_number


def check_input(input:str):
    """
    判断是不是100-200间的整数
    :param input: 输入的值
    :return: 返回布尔类型
    """
    if input.strip().isdigit() and int(input) >= 100 and int(input) <= 200:
        return True
    else:
        return False



if __name__ == "__main__":
    # 获得输入的数字
    get_number = input_numbers(5)
    # 输出最大值 最小值
    print("最大值为：%d" % max(get_number))
    print("最小值为：%d" % min(get_number))
    print("平均值为：%.2f" % (sum(get_number) / len(get_number)))

