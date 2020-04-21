
# list集合的基本操作

"""list01 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
list02 = list01  # 吧list01赋值给list02
print(list02)

# copy
list03 = list01.copy()  # 使用copy吧list01的值给list03
print(list03)"""
# = 和 copy 有本质的区别
# + : 让两个集合合并
"""list01 = [1, 2, 3]
list02 = [4, 5, 6]
print(list01 + list02)

# * 让集合重复多少次、
list01 = ["aaa", "bbb", "ccc"]
print(list01 * 3)

# len 返回list集合元素的个数
list01 = [11, 22, 33, 44, 55, 66]
print("list01元素个数为：", len(list01))

# in: 成员运算符，判断某一个元素是否存在于list中
list01 = [11, 22, 33, 44, 55, 66]
print("44是否存在list01中", 44 in list01)"""

# ======================================元素添加===================================
# 方法1 使用append添加，添加到最后
"""list01 = [11, 22, 33, 44, 55, 66]
list02 = []
list02.append("aaa")
list02.append("bbb")
print(list02)

# 方法02：使用insert添加：添加到指定位置
list02.insert(1, "ccc")
print(list02)

# 方法03 使用enxtend添加    添加的是个集合
list02.extend(["ddd", "eee", "fff"])
print(list02)"""

# =================list删除=========================
list01 = [11, 22, 33, 33, 44, 55, 66]
# 删除方法01：remove（具体元素值）  如果有重复的删除第一个元素
list01.remove(33)
print(33)

# 删除的方法02：使用pop（元素索引值）
list02 = [111, 33, 54, 65, 76, 32]
list02.pop(1)
print(list02)
list02.pop()  # 默认删除最后一个
print(list02)

# 删除额外方法03：使用del删除
list03 = [11, 323, 44, 55, 66, 77, 88]
del list03[1]  # 删除第二个
print(list03)
del list03[1:5]  # 删除第二个到第五个
print(list03)

# 删除方法04： clear 清空
list04 = [12, 43, 54, 65, 87, 98]
list04.clear()
print(list04)