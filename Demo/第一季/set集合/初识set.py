
"""list01 = [11, 22, 33, 44, 55, 66, 77]
print(list01[0])
print(list01[2])
list01.append(88)
print(list01)"""

set01 = {11, 22, 22, 33, 44, 55, 66, 77}
print(set01)   # set存储是无序的   不支持索引访问   初始化的顺序和打印出来的顺序是不一样的
# 一组无序不重复的集合
# set集合在存储时会消除重复值
set02 = {"steven", "abboy", "alice", "steven"}
print(set02)

# ==============创建set集合================
# 创建直接初始化
set01 = {11, 22, 22, 33, 44, 55, 66, 77}
for i in set01:
    print(i, end=" ")

# 创建空的set集合，往里面加入值
set02 = set()
print(type(set02))
set02.add("steven")
set02.add("abby")
print(set02)
