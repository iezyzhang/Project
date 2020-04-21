

# ===========================计算（min，max,sum）==================
"""list01 = [11, 43, 54, 65, 76, 87, 98]
print("list01中最小值：", min(list01))
print("list01中最大值：", max(list01))
print("list01中所有元素和：%d" % sum(list01))


# sum求和只能用于数字元素
list02 = ["abby", "sdf", "trew", "fs"]
print("list02中最小值：", min(list02))
print("list02中最大值：", max(list02))
# print("list02中所有元素和：%d" % sum(list02))


# 对于max，min 只能用于所有元素要么都是数字，要么都是字符串
list02 = ["abby", "sdf", "trew", "fs", 324, 65]
print("list02中最小值：", min(list02))
print("list02中最大值：", max(list02))"""


# =========================排序和反转=============
"""list01 = [43, 54, 65, 65, 323, 98]
# 排序sort
list01.sort()  # 默认升序
print(list01)  # 使用sort排序，是更改存储的顺序

# 倒序排序方法01   先排序  在反转
list01.sort()
list01.reverse()
print(list01)


# sprted 不更改存储的顺序
list02 = [32, 54, 65, 7, 87]
print(sorted(list02))  # 临时排序   不影响元素的存储顺序
print(list02)

# =================查找index======================
# 如果能查到，返回该元素的索引值，如果查不到返回false
list03 = [43, 43, 54, 76, 77, 99, 333]
print(list03.index(77))
# print(list03.index(772))
print(list03.index(43))  # 相同的数查找第一个数的索引
print(list03.index(99, 2, 6))

# =============统计count===================
print("=======统计count=====")
list04 = [43, 43, 43, 65, 65, 66, 43]
print(list04.count(43))  # 获取元素出现的次数
print(list04.count(65))"""

# ================== list案例============
"""有五名学生，,五门课程，为五位同学随机生成五门课的成绩，
按要求打印成绩
"""
import random
# student_name存储的学生姓名
student_name = ["张三", "李四", "王五", "赵柳", "马奇"]
# student_result  存储所有学生的明细
student_result = []
# 为学生生成成绩
for i in range(len(student_name)):
    list_temp = []  # 每个人的成绩   临时存储在里面
    for j in range(5):
        list_temp.append(random.randint(50, 100))  # 每次一个成绩
    # 把5门课的成绩插入到student_result中
    student_result.append(list_temp)
# 统计出每个人的总分
student_total_result = []  # 存储每个人总分
for i in student_result:
    student_total_result.append(sum(i))
"""print(student_name)
print(student_result)
print(student_total_result)

max(student_total_result)  # 获取最高分
student_total_result.index(max(student_total_result))  # 获取最高分编号"""

# 输出成绩明细
print("名次    姓名       语文     数学     英语     物理    化学    总分    平均分")
print("==========================================================================")
for i in range(len(student_name)):
    max_result = max(student_total_result)  # 获取最高分
    max_insex = student_total_result.index(max_result)  # 获取最高分编号
    # 打印名次
    print(" ", i+1, end="\t\t")

    # 打印姓名
    print(student_name[max_insex], end="\t\t")
    # 打印成绩五门
    for i in range(5):
        print(student_result[max_insex][i], end="\t\t")
    # 打印总分
    print(max_result, end="\t\t")
    # 打印均分
    print(max_result/5)

    # 删除信息---总分
    student_total_result.pop(max_insex)

    # 删除信息成绩明细
    student_result.pop(max_insex)
    # 删除信息姓名
    student_name.pop(max_insex)
print("==========================================================================")