
# 实现字符串反转

str01 = "www.iezyahng.2222.dasf"

# 方法1--使用循环，反着取
# range(初始值， 结束值， 渐变值)      渐变值默认+1
print("第一种方法：")
for i in range(-1, -len(str01) - 1, -1):
    print(str01[i], end="")

# 方法2
print("\n第二种方法：")
for i in range(1, len(str01) + 1):
    print(str01[-i], end="")

# 方法3  把字符串转为list   在转为字符串
print("\n第三种方法：")
list01 = []
# 字符串----list
for i in str01:
    list01.append(i)
print(list01)
# 反转
list01.reverse()
print(list01)
# 打印字符串
for i in list01:
    print(i, end="")

# 第四种
print("\n第四种方法：", str01[::-1])   # str01[-1, -len(str01) - 1, -1]
