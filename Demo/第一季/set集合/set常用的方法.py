
# + 和* 无法使用
"""list01 = [1, 2, 3]
print(list01 + [4, 5, 6])
print(list01 * 3)

set01 = {11, 22, 33}
set02 = {44, 55, 66}"""
# print(set01+set02)  不支持
# print(set01 * 3)  不支持

# 赋值运算 =
set01 = {11, 22, 33}
set02 = set01
print(set02)

# len 返回元素长度
set03 = {33, 44, 66}
print(len(set03))

# 判断是否包含元素
set04 = {66, 99, 90}
print("是否包含22：", (22 in set04))

# 排序和反转   sort和reverse不支持，仅支持sorted
set05 = {11, 0, 65, 43, 88}
print(sorted(set05))

# 添加元素：add
set07 = {11, 55, 33}
print(set07)
set07.add(54)
set07.add(234)
print(set07)

# 删除元素  discsrd  remove  pop
set01 = {11, 43, 65, 76, 87}
set01.discard(76)
print(set01)
set01.discard(736)
print(set01)

# 总结 discard在删除的时候，根据元素值删除，如果元素值不存在不报错


print("删除11钱", set01)
set01.remove(11)
print("删除11后", set01)
# set01.remove(122)
print("删除一个不存在的122", set01)
# 总结 remove在删除的时候，根据元素的值删除，如果删除不存在会报错

# pop
set01 = {11, 43, 65, 76, 87}
print("删除前", set01)
num = set01.pop()

print("删除后", set01)
# pop 在删除的时候，不允许加参数，他删除的是按照hash值存储的第一个元素


# max min sum    数值元素
print(min(set01))
print(max(set01))
print(sum(set01))

# 逻辑运算： 交集  并集   差集   对等差集  是否是子集  是否是父集
set02 = {11, 22, 33, 44, 44, 55}
set01 = {11, 33, 55, 87, 98}
# 交集
print(set01 & set02)
print(set01.intersection(set02))
# 并集
print(set01 | set02)
print(set01.union(set02))
# 差集
print(set01 - set02)
print(set01.difference(set02))
# 对等差集
print(set01 ^ set02)
print(set01.symmetric_difference(set02))
# print((set01 - set02) + (set02 - set01))

# 判断是否是子集    set02是否是set01的子集
print(set01 >= set02)
print(set02.issubset(set01))

# 判断付集
print(set01 <= set02)
print(set02.issuperset(set01))

# 类型转换
set02 = {11, 22, 33, 44, 44, 55}
list01 = list(set02)
print(type(list01))
tuple01 = tuple(set02)
print(type(tuple01))
str01 = str(set02)
print(type(str01))
print(list01)
print(tuple01)
print(str01)