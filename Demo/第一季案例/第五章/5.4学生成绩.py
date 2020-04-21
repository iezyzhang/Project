import random
"""
依次输入十个学生的姓名，随机为每个学生生成语文，数学，外语的分数（分数介于50-100）
根据均分来综合判定等级
1、均分85以上，A
2、均分70-85，B
3、均分70以下，C
统计综合评定ABC的数量及学生姓名
"""
def get_name(number:int):
    """
    输入指定数量的学生的姓名
    :param number: 学生数量
    :return: 返回姓名的列表
    """
    # 定义一个集合  存储学生的列表
    name_list = []
    # 循环判断依次输入
    for i in range(10):
        temp = input("请输入第"+ str(i+1) +"个学生姓名:")
        name_list.append(temp)
    return name_list

def get_result(name:list):
    """
    根据提供的姓名，生成分数
    :param name: 姓名列表
    :return: 返回分数
    """
    # 定义一个分数列表
    result_list = []
    # 遍历姓名  依次生成分数
    for index in range(len(name)):
        # 生成三门分数
        chinese_result = random.randint(50,100)  # 随机数[50-100]
        math_result = random.randint(50,100)
        english_result = random.randint(50, 100)
        # 计算平均值
        avg_result = (chinese_result + math_result + english_result) / 3
        # 添加到list
        result_list.append(avg_result)
    return  result_list

def student_count(name:list,result:list):
    """
    统计出学生的成绩的等级
    :param name: 姓名列表
    :param result: 成绩列表
    :return: 结果list
    """

    name_a_list = []
    name_b_list = []
    name_c_list = []
    # 遍历成绩列表
    for index in range(len(result)):
        if result[index] >= 85:

            name_a_list.append(name[index])
        elif result[index] >= 70:

            name_b_list.append(name[index])
        else:

            name_c_list.append(name[index])
    # 把结果凭借成一个list
    final_result_list = []
    final_result_list.append(name_a_list)
    final_result_list.append(name_b_list)
    final_result_list.append(name_c_list)
    return final_result_list

def print_result(level_name:str,level:int):
    """
    打印统计的结果
    :param level:等级  0-A  1-B   2-C
    :return:
    """
    print("综合评定%s:\t" % level_name, end=" ")
    print("学生人数：\t" + str(len(final_result[level])), end="")
    print("\t学生姓名：", end="")
    for i in final_result[level]:
        print(i, end=" ")
    print()
    


if __name__ == "__main__":
    # 输入学生列表
    name_list01 = get_name(10)
    # 获得十个学生三门科目的平均值
    result_list = get_result(name_list01)
    # print(name_list01)
    # print(result_list)
    # 获得统计的最终结果
    final_result = student_count(name_list01,result_list)
    # 打印
    print("===========================本次统计如下=====================")
    # 打印综合评定A的
    # print("综合评定A：\t",end=" ")
    # print("学生人数：\t" + str(len(final_result[0])),end="")
    # print("\t学生姓名：",end="")
    # for i in final_result[0]:
    #     print(i,end=" ")
    #
    # print("\n综合评定B：\t", end=" ")
    # print("学生人数：\t"+ str(len(final_result[1])),end="")
    # print("\t学生姓名：", end="")
    # for i in final_result[1]:
    #     print(i, end=" ")
    #
    # print("\n综合评定C：\t", end=" ")
    # print("学生人数：\t" + str(len(final_result[2])),end="")
    # print("\t学生姓名：", end="")
    # for i in final_result[2]:
    #     print(i, end=" ")

    print_result("A",0)
    print_result("B",1)
    print_result("C",2)

    print("\n===========================================================")
