
# 1 访问一个元素
dict01 = {95001: 56, 95002: 54, 95005: 99}
print(dict01[95001])

# 如果给出的key不存在怎么办
# print(dict01[99889])  # 出现异常
# 解决办法：  setdefault  get
print(dict01.setdefault(950012, "Nome"))
print(dict01.pop(950052, "Nome"))
print(dict01.pop(95005, "Nome"))
print(dict01.get(95001, "none"))
# 解释： 使用setdefault和get是避免获取一个key不存在的时候的初始值
# 解释： 使用pop后面的参数，是避免删除一个key不存在的时候的初始值

# 遍历
dict01 = {95001: 56, 95002: 54, 95005: 99, 98001: 231}
# 方式01 标准遍历
for i in dict01:
    print(i, ":", dict01[i])

# 3 item
dict01 = {95001: 56, 95002: 54, 95005: 99, 98001: 231}
print(dict01.items())
print(list(dict01.items())[0])

# 方法02 使用items遍历
list01 = list(dict01.items())
for i in list01:
    print(list(i)[0], list(i)[1])

# 方式03 使用keys遍历
print("=======================================================")
dict01 = {95001: 56, 95002: 54, 95005: 99, 98001: 231}
keys_list = list(dict01.keys())
for i in keys_list:
    print(i, ":", dict01[i])

# 方式04  使用keys和values
print("==========================")
keys_list = list(dict01.keys())
values_list = list(dict01.values())
for i in range(len(keys_list)):
    print(keys_list[i], ":", values_list[i])