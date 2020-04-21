
"""
输入一个五位数整数，求所有未上数值之和
12345    1+2+3+4+5
"""
# 方法01  数值运算
def check_input(input:str):
    """
    校验输入的是否是5位数字
    :param input: 输入字符串
    :return: 如果是 返回T   不是 返回 F
    """
    if input.isdigit() and len(input) == 5:
        return True
    else:
        return False

def sum_of_number(input:str):
    """
    计算所有数值之和
    :param input: 输入字符串
    :return: 返回所有数值之和
    """
    input_number = int(number)
    # 万位
    wan_number = input_number // 10000
    # 千位
    qian_number = (input_number % 10000) // 1000
    # 百位
    bai_number = (input_number % 1000) // 100
    # 十位
    shi_number = (input_number % 100) // 10
    # 各位
    ge_number = input_number % 10

    return wan_number + qian_number + bai_number + shi_number + ge_number

# 方法02 字符串操作
def sum_of_number02(input:str):
    """
    第二种方法  作为字符串处理
    :param input:
    :return:
    """
    # return int(input[0]) + int(input[1]) + int(input[2]) + int(input[3]) + int(input[4])
    sum01 = 0
    for i in range(len(input)):
        sum01 += int(input[i])
    return sum01

if __name__ == "__main__":
    number = input("请输入一个五位数整数：")
    # 判断是否符合要求
    if check_input(number):
        print("所有数值为之和为：%d" % sum_of_number02(number))
    else:
        print("输入的字符串不符合要求")
