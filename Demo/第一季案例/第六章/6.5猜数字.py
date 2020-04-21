
"""
随机生成一个1-100的数字，用户有五次猜数字的机会
要求如下：
    1、如果猜小了，系统提示 你猜的数字笑了
    2、如果才打了，系统提示 你猜的数字打了
    3、如果在五次之内猜到，系统提示  恭喜您猜对了
    4、如果五次之内没猜到，系统提示  很遗憾 没有猜对，并显示正确的数字
"""
import random

if __name__ == "__main__":
    # 随机生成一个整数
    private_number = random.randint(1,100)
    # 猜数字
    for time in range(1,6):
        number = int(input("请猜数字【1-100】第%d次猜：" % time))
        if private_number == number:
            print("恭喜你，猜对了！")
        elif private_number > number:
            if time == 5:
                print("很遗憾，没有猜对。\t正确的数字为%s" % private_number)
            else:
                print("您猜的数字小了")
        elif private_number < number:
            if time == 5:
                print("很遗憾，没有猜对。\t正确的数字为%s" % private_number)
            else:
                print("您猜的数字大了")
        else:
            pass
