import random
"""
有十名学生，【王一，胡二，张三，李四，赵武，马六，杨奇，刘八，孙久，陈氏】
每个学生五门科目【语文，数学，英语，物理，化学】
为这5位同学随机生成5门考试的成绩【50-100】
要求输出，第一名和最后一名学生的姓名，总分，均分，没门科目的成绩
"""
def get_result_detail(person:int,course:int,start:int,end:int):
    """
    为一些人生成一些科目，分数在某一个范围
    :param person: 学生数量
    :param course: 科目数量
    :param start: 分数的其实范围
    :param end: 分数的结束范围
    :return: 分数明细
    """
    # 定义一个list存储量
    detail_list = []
    # 生成
    for person_number in range(person):
        # 定义一个list存储一个人的分数
        one_person_result = []
        for course_number in range(course):
            one_person_result.append(random.randint(start,end))
        # 所有科目成绩生成完后，添加到detail_list
        detail_list.append(one_person_result)
    return detail_list

def get_result_total(result_detail:list):
    """
    根据成绩明细，计算出总分
    :param result_detail: 提供的成绩明细
    :return: 返回list
    """
    # 定义一个存储总分集合
    result_total = []
    # 遍历明细分数
    for i in result_detail:
        result_total.append(sum(i))
    return result_total

def print_first_total(name:list,detail:list,total:list):
    """
    输出第一名的明细
    :param name: 姓名集合
    :param detail: 明细集合
    :param total: 总分集合
    :return:
    """
    # 获得第一名分数
    first_total = max(total)
    # 遍历total的集合  看那些人的分数最高
    for index in range(len(total)):
        if total[index] == first_total:
            # 打印姓名和总分  均分 明细
            print("第一名：  \t姓名:%s\t总分：%d\t均分：%.2f" % (name[index], first_total,first_total/5))
            print("成绩明细：\t语文：%d\t数学：%d\t英语：%d\t物理：%d\t化学：%d" % (detail[index][0],detail[index][1],
                                                                detail[index][2],detail[index][3],detail[index][4]))

def print_last_total(name:list,detail:list,total:list):
    """
    输出第一名的明细
    :param name: 姓名集合
    :param detail: 明细集合
    :param total: 总分集合
    :return:
    """
    # 获得最后一名分数
    last_total = min(total)
    # 遍历total的集合  看那些人的分数最高
    for index in range(len(total)):
        if total[index] == last_total:
            # 打印姓名和总分  均分 明细
            print("最后一名：\t姓名:%s\t总分：%d\t均分：%.2f" % (name[index], last_total,last_total/5))
            print("成绩明细：\t语文：%d\t数学：%d\t英语：%d\t物理：%d\t化学：%d" % (detail[index][0],detail[index][1],
                                                                detail[index][2],detail[index][3],detail[index][4]))

if __name__ == "__main__":
    name_list = ["王一", "胡二", "张三", "李四", "赵武", "马六", "杨奇", "刘八", "孙久", "陈氏"]
    result_detail_list = get_result_detail(10,5,50,100)
    # print(result_detail_list)
    result_total_list = get_result_total(result_detail_list)
    # print(result_total_list)

    # 输出 第一名 最后一名   总分均分
    print("=======================================================================")
    print_first_total(name_list,result_detail_list,result_total_list)
    print("=======================================================================")

    print_last_total(name_list, result_detail_list, result_total_list)
    print("=======================================================================")

