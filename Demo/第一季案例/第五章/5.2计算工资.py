
"""
公司给员工占工资  涨工资规则
  工资<=4000 张20%  工资在4000-6000，长15%
  工资在6000-8000 涨10%  工资在8000-12000 涨5%
  12000以上涨500
  输入一个金额，输出涨工资后的金额
"""
def input_salary():
    """
    输入工资的金额
    :return:
    """
    while True:
        salary = input("请输入工资的金额：")
        if salary.replace(".", "").isdigit():
            return float(salary)
        else:
            print("输入的工资金额不符合要求[大于0的数字]")

def get_new_salary(salary:float):
    """
    获取占工资后的金额
    :param salary: 元工资
    :return: 涨完后的金额
    """
    if salary <=4000:
        return salary * 1.20
    elif salary <= 6000:
        return salary * 1.15
    elif salary <= 8000:
        return salary * 1.10
    elif salary <= 12000:
        return salary * 1.05
    else:
        return salary + 500


if __name__ == "__main__":
    # salary01 = input_salary()
    # print("原工资为：%.2f\t涨完后的工资为：%.2f" % (salary01, get_new_salary(salary01)))

    name_list = ["张三", "李四", "王五", "赵柳","马奇","陈八","露酒"]
    salary_list = [4500, 5612, 5123, 8901, 14000, 11910, 6091]
    for index in range(len(salary_list)):
        print("【%s: 原工资:%.2f  涨后的工资：%.2f】" % (name_list[index], salary_list[index], get_new_salary(salary_list[index])))

