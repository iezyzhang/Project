
# num = int(input("请输入一个大于1的数："))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print(sum)

"""num = int(input("请输入一个大于1的数："))
i, sum01 = 1, 0
while i <= num:
    sum01 += i
    i += 1
print("从1加到%d的和为:%d" % (num, sum01))"""

# 输入一个整数，求从1开始到这个数中所有包含3的数字和3的倍数的和
"""
3的倍数  num02 % 3 == 0  求余后为0  就是3的倍数
包含3的数字， 3  in  str（num）  成员运算符
"""
"""num01 = int(input("请输入一个大于1的整数："))
i, sum01 = 1, 0
while i <= num01:
    if i % 3 == 0:
        sum01 += i
    elif "3" in str(i):
        sum01 += i
    i += 1
print("从1开始到%d中所有包含3的数字和3的倍数的和为:%d" % (num01, sum01))"""


# 输入班级人数，然后依次输入所有学员的成绩，计算该班级学员的平均成绩和总成绩
"""
循环变量：i=1
"""
"""student_number = int(input("请输入学生人数："))
i = 1
total_result = 0
while i <= student_number:
    total_result += int(input("请输入第%d个学生成绩：" % i))
    i += 1
print("该班级考试总分：%d 平均分：%.2f" % (total_result, total_result / student_number))"""

"""
2083>>>8302
方法1： 去数字字符，转化为字符串，从前往后取

"""

num01 = input("请输入一个数字：")
i = 0
new_num = ""
while i < len(num01):
    new_num = num01[i] + new_num
    i += 1
else:
    print("循环结束！")  # 当循环条件为false时候执行语句
print(new_num)
print("%s + %s = %d" %(num01, new_num, int(num01) + int(new_num)))