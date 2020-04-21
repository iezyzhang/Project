
"""
有10个学生，姓名自行添加，有三门考试，语文，数学，英语，随机为这10个学生生成分数50-100
需求：打印一张成绩表

"""
"""dict01 = {
    95001: {"姓名": "张三", "名次": 4, "总分": 234, "明细": [67, 89, 78]},
    95002: {"姓名": "李四", "名次": 3, "总分": 255, "明细": [67, 89, 89]},
    95003: {"姓名": "王五", "名次": 1, "总分": 298, "明细": [99, 92, 89]},
    95004: {"姓名": "赵柳", "名次": 2, "总分": 267, "明细": [89, 92, 89]}
}"""
# 格式：{SNO:{""  "" []}}
# 初始化学生的基本信息
import random
dict_student_info = {95001: "王一", 95002: "胡二", 95003: "张三", 95004: "李四",
                95005: "赵武", 95006: "马六", 95007: "杨奇", 95008: "刘八", 95009: "孙久", 95010: "陈氏"}
# 生成成绩
student_result = []
for i in range(len(dict_student_info)):
    temp_result = []
    for j in range(3):
        temp_result.append(random.randint(50, 100))
        # 添加到student_result中
    student_result.append(temp_result)
print(student_result)  # 打印生成的成绩

# 生成总分List
total_result = []
for i in student_result:
    total_result.append(sum(i))
# 吧总分倒序排列
total_result.sort(reverse=True)
print(total_result)


# 组合存储结构
total_student_result = {}
# 获得学生信息的key
student_sno = list(dict_student_info.keys())
# 遍历
index = 0
for i in student_sno:
    temp_total = {}
    temp_total["姓名"] = dict_student_info[i]
    temp_total["明细"] = list(student_result)[index]
    temp_total["总分"] = sum(list(student_result)[index])
    temp_total["名次"] = total_result.index(sum(student_result[index])) + 1
    total_student_result[i] = temp_total
    index += 1
for i in total_student_result:
    print(i, ":", total_student_result[i])

# 打印成绩单  倒序排名表
print()
print()
print("===========================成绩统计表=================================")
print("名次     学号        姓名       语文     数学    英语     总分     均分")
print("=====================================================================")
for i in range(len(dict_student_info)):
    for j in total_student_result:
        if total_student_result[j]["名次"] == i + 1:
            # 打印明细
            print(i + 1, end="\t\t")
            print(j, end="\t\t")
            print(total_student_result[j]["姓名"], end="\t\t")
            print(total_student_result[j]["明细"][0], end="\t\t")
            print(total_student_result[j]["明细"][1], end="\t\t")
            print(total_student_result[j]["明细"][2], end="\t\t")
            print(total_student_result[j]["总分"], end="\t\t")
            print("%.2f" % (total_student_result[j]["总分"] / 3), end="\t\t")
            print()
            break
        else:
            continue


print("=====================================================================")