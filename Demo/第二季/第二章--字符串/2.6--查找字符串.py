
# 查找字符串使用的函数：find     index
str01 = "wwww.000.dd33"
print(str01.find("000"))  # 如果查到  返回包含字符串起始位置索引
print(str01.find("sss"))  # 如果查不到 返回是-1

print(str01.index("000"))  # 如果查到返回字符串起始位置索引
try:
    print(str01.index("sss"))  # 如果index查找，找不到报错
except ValueError as e:
    print("无法查到结果")


# 查询常见的使用
str02 = "jeujwfijowhgjahvjkahsfeaw"
print(str02.find("j"))   # 返回第一个 结果索引
print(str02.rfind("j"))   # 返回最后一个结果索引
print(str02.find("j", 3))  # 返回从指定索引开始的第一个结果索引
print(str02.find("j", 6, 10))  # 返回从指定索引开始 到某个结束索引的第一个结果索引
print(str02.count("j"))  # 统计查询结果的个数

# 案例  生成500个数字的字符串，判断88出现的次数，并打印出现位置
import random
str_total = ""
for i in range(500):
    str_total += str(random.randint(0, 9))
# 打印每行显示100个
num01 = 0
for i in str_total:
    num01 += 1
    print(i, end="")
    if num01 % 100 == 0:
        print()
# 出现88的次数
print("出现88的次数：%d" % str_total.count("88"))
# 打印具体的值
strat = 0
current = 0
while True:
    current_index = str_total.find("88", strat)
    if current_index == -1:
        break
    else:
        current += 1

        print("第" + str(current) + "个88的位置：", current_index)
        strat = current_index + 1
print("出现88的次数：%d" % current)
