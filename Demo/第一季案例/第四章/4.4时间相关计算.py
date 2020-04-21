
"""
提示输入一个时间（时分秒用冒号分开）
实现如下需求
1、对输入的时间进行有效判断
2、计算时分秒数字之和
3、把输入的时间时长转化为秒，并输出这个值
4、输入时间再过18888秒后的时间是多少
"""
# 方法01  数学运算

def check_time(input:str):
    """
    校验时间是否有效
    :param input: 输入的时间
    :return: 返回布尔类型值
    """
    # 判断是否是数字
    if input.strip().replace(":","").isdigit():
        # 分隔时分秒
        time = input.split(":")
        # 判断时
        if int(time[0]) < 0 or int(time[0]) >23:
            return False
        # 判断分
        if int(time[1]) < 0 or int(time[1]) >59:
            return False
        # 判断秒
        if int(time[2]) < 0 or int(time[2]) >59:
            return False
        # 如果前面没有满足 return  T
        return True

    else:
        return False

def get_time(input:str):
    """
    获取时分秒的数字
    :param input:
    :return:
    """
    time_list = []
    time = input.split(":")
    # 添加时分秒的数字
    time_list.append(int(time[0]))
    time_list.append(int(time[1]))
    time_list.append(int(time[2]))
    return time_list

def get_seconds(time:list):
    """
    把标准时间转换为秒
    :param time: 提供的时分秒
    :return: 秒
    """
    return time[0] * 60*60+time[1]*60+time[2]

def get_add_second(time01:int,time02:int):
    """
    某一个时间增加多少秒后的值
    :param time01: 当前时间
    :param time02: 增加描述
    :return: 返回结果
    """

    result_time = time01 + time02
    result_time_list = []
    # 获得时分秒的值
    hour_number = result_time // (60*60)
    minute_number = (result_time%(60*60)) // 60
    second_number = result_time % 60
    # 添加结果到list
    result_time_list.append(hour_number % 24)
    result_time_list.append(minute_number)
    result_time_list.append(second_number)

    # 返回
    return result_time_list



if __name__ == "__main__":
    input_time = input("请输入一个时间：")
    # 判断是否有效
    if check_time(input_time):
        # 获得时分秒时间
        time = get_time(input_time)
        # 打印时分秒之和
        print("时分秒之和为：%d" % sum(time))
        # 打印转化为秒的值
        print("当前时分秒转化为秒的值为：%d" % get_seconds(time))
        # 18888秒的时间
        result_list = get_add_second(get_seconds(time),18888)
        # 打印18888秒后的时间
        print("18888秒后的时间为:%02d:%02d:%02d" % (result_list[0],result_list[1],result_list[2]))
    else:
        print("输入时间无效")

