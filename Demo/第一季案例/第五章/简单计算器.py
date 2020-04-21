
# 实现一个简单地计算器

def input_number(str_number:str):
    while True:
        number_str = input("请输入第" + str_number + "个数：")
        try:
            # 判断是否有效，我直接转化为小数，如果成功，说明OK，不成功转到Except执行
            number = float(number_str)
            # 返回
            return number
        except:
            print("输入的不是有效的数字！")

def input_action():
    while True:
        action01 = input("请选择要执行的操作【+ - * / %】:")
        if action01.strip() in ["+","-","*","/","%"]:
            return action01
        else:
            print("选择操作运算符无效")

def get_result(num01,num02,action):
    if action == "+":
        return num01+num02
    elif action=="-":
        return num01 - num02
    elif action == "*":
        return num01 * num02
    elif action =="/":
        return num01 / num02
    elif action == "%":
        return num01 % num02
    else:
        pass


if __name__ == "__main__":
    num01 = input_number("一")
    action = input_action()
    num02 = input_number("二")
    # print("%.2f  %s  %.2f = %.2f" % (num01,action,num02,get_result(num01,num02,action)))
    print("{0:g} {1} {2:g} = {3:g}".format(num01,action,num02,get_result(num01,num02,action)))

