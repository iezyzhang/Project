
"""
提示输入一个时间（时分秒用冒号分开）
实现如下需求
1、对输入的时间进行有效判断
2、计算时分秒数字之和
3、把输入的时间时长转化为秒，并输出这个值
4、输入时间再过18888秒后的时间是多少
"""
import datetime
# 方法02 时间运算

def check_time(input:str):
    """
    时间基本判断
    :param input:输入时间
    :return: 如果符合要求 返回F  如果符合 返回T
    """
    # 定义一个数组 如果符合要求返回时分秒
    time01 = []
    # 判断是否是数字
    if not input.strip().replace(":","").isdigit():
        return False
    else:
        time_list = input.split(":")
        if len(time_list) != 3:
            return False
        else:
            time01.append(int(time_list[0]))
            time01.append(int(time_list[1]))
            time01.append(int(time_list[2]))
            return time01

if __name__ == "__main__":
    input_time = input("请输入时间【12:12:12】：")
    # 判断输入是否有效
    time_list = check_time(input_time)
    if time_list == False:
        print("输入的时间无效！")
    else:
        # 把时分秒组合成时间
        try:
            time02 = datetime.time(time_list[0],time_list[1],time_list[2],0)
            print("时分秒值和为：%d" % sum(time_list))
            # 打印转换成秒的时间
            print("转换成秒的时间为：%d" % (time_list[0]*3600+time_list[1]*60+time_list[2]))

            # 18888秒后的时间
            datetime01 = datetime.datetime(2000,12,12,time02.hour,time02.minute,time02.second,0)
            datetime02 = datetime01 + datetime.timedelta(seconds=18888)
            print("18888秒是时间为：%02d:%02d:%02d" % (datetime02.hour, datetime02.minute, datetime02.second))
        except:
            print("输入时间无效！")

