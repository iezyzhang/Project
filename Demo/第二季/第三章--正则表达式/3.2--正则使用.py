# 三个基本方法函数:   match   search   findall

import re
# 1、match  -----从头开始匹配
print(re.match("\d{3}", "123aaa"))  # 以三个数字开始   能匹配
print(re.match("\d{3}", "eda123aaa"))  # 不是三个数字开始  不 能匹配

# 2、search--- 从任意位置匹配
print(re.search("\d{3}", "123aaa"))  # 可以匹配
print(re.search("\d{3}", "aaa123aaa"))  # 可以匹配
print(re.search("\d{3}", "asc123aaa123"))  # 可以匹配  匹配满足条件的第一个

# 3、findall-----获得匹配的结果，存储在列表中
print(re.findall("\d{3}", "asc123aaa123, 999, # 354"))
list01 = re.findall("\d{3}", "asc123aaa123, 999, # 354")
for i in list01:
    print(i)

# 4、正则的两种写法：
# 方法01 简单地写法   re.match(正则语法，要匹配的文本)
print(re.search("\d{3}", "123aaa"))

# 方法02  标准写法：步骤一：实例化正则的对象   步骤二：用正则对象匹配字符串
patten = re.compile("\d{3}")
result = patten.match("123asd")
print(result)
if result is None:
    print("不匹配")
else:
    print("匹配")

