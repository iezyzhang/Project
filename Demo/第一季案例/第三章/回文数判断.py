import math
"""
正读和反读都一样的数字
平方回文数：是一个回文数，并且是某个数的平方
1、输入一个数，至少三位数，判断是不是回文数
2、打印所有三位平方回文数
"""
def check_input(input_number):
    """
    判断是不是大于三位的整数
    :param input_number:
    :return:
    """
    if input_number.isdigit() and len(input_number) >= 3:
        return True
    else:
        return False

def input_number():
    while True:
        number = input("请输入一个大于100的数字：")
        if check_input(number):
            return number
        else:
            print("输入数字不符合要求！【要求大于100的整数】")

def palindrome_number(input_number: str):
    len_number = len(input_number)
    # 循环
    for i in range(len_number // 2):
        # 判断是否相等
        if input_number[i] == input_number[len_number-i-1]:
            # pass
            if i==(len_number//2) - 1:
                return True
        else:
            return False
        # 循环结束都没有return  false
    # return True

def palindrome_number02(input_number: str):
    """
    判断回文数的第二种方法
    :param input_number:提供的参数
    :return: 如果是 返回T   不是 返回F
    """
    new_number = ""
    for i in range(1, len(input_number) + 1):
        new_number += input_number[-i]

    # 判断两个是否相等
    if new_number == input_number:
        return True
    else:
        return False


def is_square_number(number:int):
    for i in range(10, 33):
        if i * i == number:
            return True
        if i == number:
            return False



if __name__ == "__main__":
    # 提醒输入一个至少三位数的整数
    """number = input_number()

    # 判断是否是回文数
    if palindrome_number02(number):
        print("%s是回文数" % number)
    else:
        print("%s不是回文数" % number)"""

    # print("123456789"[::-1])
    # if number == number[::-1]:
    #     print("%s是回文数" % number)
    # else:
    #     print("%s不是回文数" % number)

    print("所有三位回文数如下：")
    for i in range(100, 1000):
        if palindrome_number02(str(i)):
            # 回文数
            if math.sqrt(i) == int(math.sqrt(i)):
                print(i, end="  ")
        else:
            pass



