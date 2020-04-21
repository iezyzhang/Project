
"""# tuple 是一组有序的不可变的集合
list01 = [11, 22, 33, 44, 545]
print(list01)
list01.append(55)
print(list01)
list01.remove(44)
print(list01)
list01[0] = 99
print(list01)

# tuple
tuple01 = (11, 22, 33, 44, 55)
print(tuple01[2])
# tuple01[1] = 99
# print(tuple01)
print(tuple01[1:5])

# 元组创建    因为不可变，所以在创建的时候直接初始化
tuple02 = (11, 33, 44, 55, 566)
tuple01 = ()  # 空元素元组
tuple03 = (22,)  # 如果只有一个元素元组，元素必须要有逗号
print(type(tuple03))

tuple04 = tuple02 + tuple03   # 元组虽然不可修改，但是支持多个元组的拼接
print(tuple04)

# 元组的元素访问
tuple01 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print(tuple01[1])
print(tuple01[-1])
print(tuple01[2:4])
print(tuple01[-4:-2])
print(tuple01[3:7:2])
print(tuple01[1::2])

# 遍历
tuple01 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
for i in tuple01:
    print(i, end=" ")
print()
for i in range(len(tuple01)+1):
    print(tuple01[i], end=" ")"""

# 元组常用的方法
"""tuple01 = (11, 22, 33, 44)
tuple02 = tuple01
print(tuple01)
print(tuple02)

# + 拼接元组
tuple03 = (11, 22, 33)
tuple04 = (55, 66)
tuple05 = tuple04 + tuple03
print(tuple05)

# * 打印多少遍
print(tuple04 * 3)

# len 求元组个数
print(len(tuple03))
# in 判断是否包含元素
print(33 in tuple03)

# 添加修改    ----如果元组中嵌套list  list可以修改
tuple01 = (11, 22, 33, [44, 55, 66])
tuple01[3].append(77)
tuple01[3].remove(55)
tuple01[3][2] = 666

# 元组的删除
tuple01 = (11, 22, 33, 44)
# del tuple01[2]  # 不可以修改元素
# del tuple01
# print(tuple01[1])

# 元组的计算  ---  max  min   sum
tuple01 = (11, 22, 99, 33, 44)
print(max(tuple01))
print(min(tuple01))
print(sum(tuple01))


# ======排序sort=============反转reverse
tuple01 = (11, -10, 22, 999, 44, 33, 22)
# tuple01.s     # sort改变了元素的位置，修改了元组，所以不可以
print(sorted(tuple01))  # sorted 不改变元素位置，临时排序

#  index
print(tuple01.index(22))

# 统计出现的次数  count
print(tuple01.count(22))"""


# ================元组案例演示====================
"""
输入一个数字，转换成中文
"""

# 方法1
"""number = input("请输入一个数字：")
for i in range(len(number)):
    if "0" in number[i]:
        print("零", end="")
    if "1" in number[i]:
        print("壹", end="")
    if "2" in number[i]:
        print("贰", end="")
    if "3" in number[i]:
        print("叁", end="")
    if "4" in number[i]:
        print("肆", end="")
    if "5" in number[i]:
        print("伍", end="")
    if "6" in number[i]:
        print("陆", end="")
    if "7" in number[i]:
        print("柒", end="")
    if "8" in number[i]:
        print("捌", end="")
    if "9" in number[i]:
        print("玖", end="")
    if "." in number[i]:
        print("点", end="")"""

# 方法2  使用元组
"""chinese_number = ("零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖")
number = input("请输入一个数字：")
for i in range(len(number)):
    if "." in number[i]:
        print("点", end="")
    else:
        print(chinese_number[int(number[i])], end="")"""

# 第二题  根据花色和数字，生成一副扑克牌
poker_type = ("♠", "♥", "♦", "♣")
poker_number = ("3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2")
poker_list = []
for i in poker_number:
    for j in poker_type:
        poker_list.append(j+i)

print(len(poker_list))
print(poker_list)

# 洗牌  发牌  整理牌