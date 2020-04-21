
"""
题目
提醒输入学生的学号，然后输入学生姓名，然后依次输入学生的语文，数学，英语成绩，需求如下
1、计算学院的总分和平均分
2、所有的成绩都是浮点数，保留两位小数
3、运行过程参考如下

"""
# 提醒输入学号，提醒输入姓名，输入语文成绩，输入数学成绩，输入外语成绩 打印结果

def check_input(result):
    """
    校验成绩是否在0-100之间

    :param result: 提供的成绩
    :return: 返回的结果，如果是  返回true  不是 返回false
    """
    # 如果不是数字
    if result.startswith("-"):
        return False # 是否包含负数
    if result.replace(".", "").isdigit():
        result_number = float(result)
        if result_number>=0 and result_number<=100:
            return True
        else:
            return False

def get_result(sno, name, chinese, math, english):
    print("============================================================")
    print("学号：%s\t\t姓名：%s" % (sno, name))
    total = float(chinese) + float(math) + float(english)
    print("总分：%.2f\t均分：%.2f" % (total, total / 3))
    print("成绩明细:【语文：%.2f\t数学：%.2f\t英语：%.2f\t】" % (float(chinese), float(math), float(english)))
    print("============================================================")

def input_result(sno, name, subject):
    while True:
        result = input("请输入【学号：%s  姓名：%s】的%s成绩：" % (stu_sno, stu_name, subject))
        if check_input(result):
            return result
        else:
            print("输入成绩不符合要求,请重新输入【所有成绩介于0-100】！")
            continue

if __name__ == "__main__":
    # 主函数负责录入和展示
    # 提醒输入学号
    stu_sno = input("请输入学号：")
    stu_name = input("请输入姓名：")
    # chinese_result = input("请输入【学号："+ stu_sno +" 姓名: "+ stu_name +" 】的语文成绩：")
    # chinese_result = input("请输入【学号：%s  姓名：%s】的语文成绩：" % (stu_sno, stu_name))
    # math_result = input("请输入【学号：%s  姓名：%s】的数学成绩：" % (stu_sno, stu_name))
    # english_result = input("请输入【学号：%s  姓名：%s】的英语成绩：" % (stu_sno, stu_name))
    chinese_result = input_result(stu_sno, stu_name, "语文")
    math_result = input_result(stu_sno, stu_name, "数学")
    english_result = input_result(stu_sno, stu_name, "英语")

    # 判断成绩是否符合要求
    # if check_input(chinese_result) and check_input(math_result) and check_input(english_result):
    #     # 打印结果
    #     get_result(stu_sno, stu_name, chinese_result, math_result, english_result)
    # else:
    #     print("输入成绩不符合要求【所有成绩介于0-100】！")
    get_result(stu_sno, stu_name, chinese_result, math_result, english_result)
