
list01 = [123, 456, 789]
tuple01 = (123, 456, 789)
set01 = {123, 456, 789}
# item

dict01 = {9801: "张三", 94403: "李四", 2343: "王五"}
# 字典元素：key  ，value   键值对   冒号连接
# 冒号前面成为key  冒号后面:value
# 通过key可以访问到value，反之不可以
print(dict01[2343])

# 2  字典的元素不重复
dict01 = {9801: "张三", 94403: "李四", 2343: "王五", 9801: "张三"}
print(dict01[9801])

# 3 字典的无序   不能通过下标访问
dict01 = {9801: "张三", 94403: "李四", 2343: "王五"}
# print(dict01[0])

# 4 什么情况下能用到字典
# 比如：  学号 + 姓名
list01 = {"张三", "李四"}
dict01 = {9801: "张三", 94403: "李四", 2343: "王五"}

# 比如  姓名加成绩
dict02 = {"张三": [23, 54, 66], "李四": [65, 99, 32]}
print(dict02["李四"])
# 比如科目成绩
dict03 = {"语文": 95, "数学": 54, "英语": 88}

# 5  key不能重复   重复情况下最后一个生效，后面覆盖前面
dict01 = {67001: 200, 98001: 789, 67001: 423}
print(dict01)

# 6 value可以重复
dict01 = {67001: 200, 98001: 789, 67003: 200}
print(dict01)

# key必须是不可变的类型， int  str  float  bool  tuple
dict01 = {1.11: "AAA", 2.22: "BBB", 3.33: "CCC"}
print(dict01)
dict01 = {True: "AAA", False: "BBB"}
print(dict01)
dict01 = {(11.22, 33.11): "徐家汇", (12.43, 55.21): "东方明珠"}
print(dict01)

# value类型可以存储任一类型的Python数据
dict01 = {(11.22, 33.21): ["徐家汇", "人民广场", "东方明珠"], (11.43, 55.31): {"AAA", "BBB"}, (32.33, 66.21): (111, 22, 444)}
print(dict01)
