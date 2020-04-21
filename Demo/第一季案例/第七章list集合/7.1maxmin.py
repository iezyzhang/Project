
"""
生成20个50-100中互不相等的数，打印出这20个数，求最大值，最小值，平均数
"""
import random
def geta_nimbers(start:int,end:int,number:int):
    """
    获得随机number个数
    :param start: 开始
    :param end: 结束
    :param number: 数量
    :return: 返回20个数
    """
    # 定义一个集合用来储存生成的数字
    number_list = []
    # 生成随机数
    while len(number_list) < number:
        temp = random.randint(start,end)
        # 判断是否在集合中已经存在
        if temp not in number_list:
            # 如果集合中不存在 就添加
            number_list.append(temp)
        else:
            pass

    return number_list


if __name__ =="__main__":
    number_result = geta_nimbers(50,100,20)
    print("生成的集合为:", number_result)
    print("生成集合的最大值为：",max(number_result))
    print("生成集合的最小值为：", min(number_result))
    print("生成集合的和为：", sum(number_result))
    print("生成集合的平均值为：%.2f" % (sum(number_result) / len(number_result)))

