
# * 和 + 不支持
dict01 = {93001: 32, 98002: 43, 97004: 54}
dict02 = {95002: 43, 87003: 33}
# print(dict01 + dict02)  报错不支持
# print(dict01*3)  报错不支持

# 2 update   让两个字典合并    类似于  +
dict01.update(dict02)
print(dict01)
dict03 = dict01
print(dict03)

# 问题： 如果改变dic01   那么dic03会变吗
dict01[93001] = 100
print(dict03[93001])

# 使用copy
dict04 = dict01.copy()
print(dict01)
print(dict04)
dict01[93001] = 200
print(dict01)
print(dict04)
# 使用钱复制， 把存储的每个值得索引复制一份，改变一个，另外一个不变

# 3 len----元素长度
dict01 = {93001: 32, 98002: 43, 97004: 54}
print(len(dict01))

# in---判断key是否包含
print(93001 in dict01)  # 值判断key

# sorted ------按照key排序
print(sorted(dict01))
list_key = sorted(dict01)
for i in list_key:
    print(i, ":", dict01[i], end=" ")

# 计算   min   max   sum     针对key
print()
dict01 = {93001: 32, 98002: 43, 97004: 54}
print(min(dict01))
print(max(dict01))
print(sum(dict01))

# fromkeys ------  创建新字典
student_sno = [95001, 95002, 94003, 95005, 95006]
student_result = {}.fromkeys(student_sno)
print(student_result)
student_result[95001] = 234
student_result[95002] = 318
student_result[94003] = 345

print(student_result)