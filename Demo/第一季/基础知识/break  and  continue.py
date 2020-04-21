# break  continue  跳出循环

"""
break  跳出整个循环，后边的都不知道，包括else  都不执行

continue  跳出当次循环，后面的继续执行，else 也执行
"""
"""print("====break===")
num = 10
i = 0
while i <= num:
    i += 1
    if i == 5:
        break
    else:
        print(i, end=" ")
else:
    print("测试结束")



print("\n ====continue===")
num = 10
i = 0
while i <= num:
    i += 1
    if i == 5:
        continue
    else:
        print(i, end=" ")
else:
    print("测试结束")"""

# 2006年学校80000人，每年增长25%，请问按此增长数据，到哪年学生人数达到20万人
# 不知道循环次数
"""student_number = 80000
years = 0
while student_number < 200000:
    student_number *= 1.25
    years += 1
print("到%d年后人数超过20万" % (2006 + years))

# 方法二
student_number = 80000
years = 0
while True:
    student_number *= 1.25
    years += 1
    if student_number > 200000:
        break
print("到%d年后人数超过20万" % (2006 + years))"""

# 求 1-100间和7（含7的数字，7的倍数，）相关的数之和
"""sum_of_number = 0
i = 1
while i <= 100:
    if i % 7 == 0:
        sum_of_number += i
    elif "7" in str(i):
        sum_of_number += i
    else:
        pass   # pass 和 continue区别   pass为空语句
    i += 1
print("1-100间和7（含7的数字，7的倍数，）相关的数之和为：%d" % sum_of_number)"""


"""# for 循环
# 求从1-100之和
sum_of_number = 0
for i in range(1, 101):
    sum_of_number += i
else:
    print("==循环结束==")
print(sum_of_number)

# for i in 范围
# 范围的表示
# 表示方法01：
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=" ")
# 使用中括号表示一个范围，中括号的所有成员都从头到尾依次取到，没有range关键
print()
for i in ["Alice", "Bob", "Tomas", 123, 456, 789]:
    print(i, end=" ")

# 表示方法2：range（单个数字: 从0开始到这个数字-1）
print("\n============")
for i in range(10):
    print(i, end=" ")

# 表示方法3：range(两个数字：从第一个数字开始，到第二个数字-1结束，每次增1)
print("\n========")
for i in range(2, 10):
    print(i, end=" ")

# 表示方法4：range(三个数字：从第一个数字开始，到第二个数字-1结束，每次按第三个数递增)
print("\n=============")
for i in range(2, 10, 2):
    print(i, end=" ")"""


# 求1-100间5和7的倍数之和
"""sum_of_number = 0
for i in range(1, 101):
    if i % 5 == 0:
        sum_of_number += i
    elif i % 7 == 0:
        sum_of_number += i
    else:
        pass
print("1-100间5和7的背数之和为：%d" % sum_of_number)

# 求水仙花数（三位数）
# 比如： 153=1^3+5^3+3^3
for i in range(100, 1000):
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        print(i, end=",")
    else:
        pass"""

# 循环嵌套
# 乘法口诀表
"""for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (i, j, i*j), end=" ")
    print()  # 每过一个数字循环 就换行"""

# 100元买2元的铅笔、5元的铅笔盒、10元的文件夹、15元的彩笔
# 刚好画完，每样物品至少一种，一共有多少种可能，打印出每一种组合
"""times = 0
for i in range(1, 50):  # 铅笔
    for j in range(1, 20):  # 铅笔盒
        for l in range(1, 10):  # 文件夹
            for m in range(1, 7):  # 彩笔
                if 2*i + 5*j + 10*l + 15*m == 100:
                    times += 1
                    print("第【%d】种情况【铅笔：%d个, 铅笔盒：%d个, 文件夹：%d个, 彩笔：%d个】" % (times, i, j, l, m))"""

# 输入行数，打印三角形
"""
1-----1
2-----3
3-----5
4-----7
5-----9
行数和星的数量 2n-1
行数空格关系
1-----行数-1
2-----行数-2
3-----行数-3

"""

rows = int(input("请输入要打印的行数："))
# 行数
for i in range(1, rows+1):
    # 空格
    for l in range(1, rows-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()