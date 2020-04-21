
"""list01 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 第一种遍历的方法
# 基础支持：len（list01）---返回集合的元素
print("===第一种while循环=====")
i = 0  # 循环的变量
while i < len(list01):
    print("第%i个元素为" % (i+1), list01[i])
    i += 1

print("===第一种for循环=====")
for i in range(0, len(list01)):
    print("第%i个元素为" % (i + 1), list01[i])

print("===第一种for循环=====")
num = 1
for i in list01:
    print("第%i个元素为" % num, i)
    num += 1"""

# list集合案例演示
import  random
# 生成10个三位数
list01 = []
for i in range(10):
    list01.append(random.randint(100, 999))
# 第二部打印
print("集合中的元素为：", list01)
print("大于500的元素为：", end=" ")
for j in list01:
    if j > 500:
        print(j, end=" ")

# 反序显示结果
print("\n反序大于500的元素为：", end=" ")
for num in range(-1, -11, -1):
    if list01[num] > 500:
        print(list01[num], end=" ")
