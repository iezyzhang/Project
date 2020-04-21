import copy
"""list01 = [11, 22, 33, 44, 55]
print(list01)
print("list01变量内存地址", id(list01))  # list的地址
print("list01第一个变量内存地址", id(list01[0]))

list02 = list01
print(list02)
print("list02变量内存地址", id(list02))
print("list02第一个变量内存地址", id(list02[0]))

list03 = [11, 22]
print(list03)
print("list03变量内存地址", id(list03))
print("list03第一个变量内存地址", id(list03[0]))

list01.append(66)
print(list01)
print(list02)

list01[0] = 99
print(list01)
print(list02)
print(list03)

list01.remove(55)
print(list01)
print(list02)
print(list03)"""


# =================copy===============
list01 = [44, 55, 66]
list02 = [11, 22, 33, list01]
list03 = list02  # 直接赋值
list04 = list02.copy()  # 浅拷贝
list05 = copy.copy(list02)  # 浅拷贝
list06 = copy.deepcopy(list02)  # 深拷贝

# 修改list01
list01[0] = 88
list02[0] = 99

print(list01)
print(list02)
print(list03)
print(list04)
print(list05)
print(list06)




