
# ======================案例1====================
# 生成0-10之间五个不想等的数
import random
"""list01 = []
for i in range(5):
    num01 = random.randint(0, 10)
    if num01 not in list01:
        list01.append(num01)
    if len(list01) == 5:
        break
print(list01)

# 方法2  使用set集合  消除重复
number_set = set()
while len(number_set) < 5:
    number_set.add(random.randint(0, 10))
print(number_set)"""


# 案例2
"""
有10个学生，姓名自行添加，有三门考试，语文，数学，英语，随机为这10个学生生成分数50-100
要求没一门科目中所有学生分数不能重复
要求：
  统计没门科目的前三名和后三名，包括姓名和具体分数
  统计出总分的前三名和后三名
  在50-100的数字中，那些数字没有在三门分数中出现过
"""
# 考虑什么问题：用什么集合存储
# 姓名和成绩  有序  名次》》》成绩   list
# 语文数学外语    随机值：10个随机    无序》》绑定

def get_result(result:set):
    while True:
        temp = random.randint(50, 100)
        if temp not in result:
            result.add(temp)
            break
        else:
            continue
    return result

student_name = ["王一", "胡二", "张三", "李四", "赵武", "马六", "杨奇", "刘八", "孙久", "陈氏"]
student_result = []  # 存储所有学生成绩明细
chinese_result = set()  # 存储语文分数
math_result = set()  # 存储数学
english_result = set()  # 存储英语

# 开始生成分数
for i in range(len(student_name)):
    # 生成语文分数
    chinese_result = get_result(chinese_result)

    # 生成数学分数

    math_result = get_result(math_result)
    # 生成英语分数

    english_result = get_result(english_result)

# 把三个set集合转为list
chinese_result = list(chinese_result)
math_result = list(math_result)
english_result = list(english_result)
# 生成成绩明细
for i in range(len(student_name)):
    temp_list = []
    temp_list.append(chinese_result[i])
    temp_list.append(math_result[i])
    temp_list.append(english_result[i])
    student_result.append(temp_list)
print(chinese_result)
print(math_result)
print(english_result)
print(student_result)

# 需求1：统计每门科目前三名和后三名
chinese_one = max(chinese_result)
print("语文第一名：[姓名：%s  分数：%d]" % (student_name[chinese_result.index(chinese_one)], chinese_one))
chinese_two = sorted(chinese_result)[8]
print("语文第二名：[姓名：%s  分数：%d]" % (student_name[chinese_result.index(chinese_two)], chinese_two))
chinese_three = sorted(chinese_result)[7]
print("语文第三名：[姓名：%s  分数：%d]" % (student_name[chinese_result.index(chinese_three)], chinese_three))

chinese_last_one = sorted(chinese_result)[0]
print("语文倒数第一名：[姓名：%s  分数：%d]" % (student_name[chinese_result.index(chinese_last_one)], chinese_last_one))
chinese_last_two = sorted(chinese_result)[1]
print("语文倒数第二名：[姓名：%s  分数：%d]" % (student_name[chinese_result.index(chinese_last_two)], chinese_last_two))
chinese_last_three = sorted(chinese_result)[2]
print("语文倒数第三名：[姓名：%s  分数：%d]" % (student_name[chinese_result.index(chinese_last_three)], chinese_last_three))

# 统计出总分的前三名和后三名
student_total_result = []
for i in student_result:

    student_total_result.append(sum(i))
print(student_total_result)
# 打印前三名
total_one = sorted(student_total_result)[9]
print("总分第一名：[姓名：%s  总分：%d   均分：%.2f]" % (student_name[student_total_result.index(total_one)], total_one, total_one / 3))
total_two = sorted(student_total_result)[8]
print("总分第二名：[姓名：%s  分数：%d   均分：%.2f]" % (student_name[student_total_result.index(total_two)], total_two, total_two / 3))
total_three = sorted(student_total_result)[7]
print("总分第二名：[姓名：%s  分数：%d   均分：%.2f]" % (student_name[student_total_result.index(total_three)], total_three, total_three / 3))


# 在50-100，的数字钟，那些数字没有在三门的分数中出现过-----逻辑运算
total_number = set()
for i in range(50, 101):
    total_number.add(i)
had_number = (set(chinese_result) | set(math_result) | set(english_result))
print("未出现的数字有：", (total_number - had_number))

