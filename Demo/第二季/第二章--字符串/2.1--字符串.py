
# 1、字符串，使用单引号和双引号都可以
str01 = "abc"
str02 = 'aaa'

# 取字符串中的字符,第一个字符下标为0
str03 = "assafsaaggkllk"
print(str03[0]) # 第一个
print(str03[-1]) # 最后一个
print(str03[1:5]) # 第二个到第五个
print(str03[1:8:2]) # 从第一个到第九个，间隔为 2

# 3、长字符串  续行符    和注释符号
str04 = "dsjfhuewiofkjvdsklhg" \
        "lkgjsdjfiowejpofklnvjkvj;" \
        "slajfioeiwoajkljkdfklnkjfdagqw" \
        "egfwgergag"
print(str04)
str05 = """asdfafagd
       fdsafsdafs
        sdafdasga
"""
print(str05)

# 4、转义字符\ 和 取消转移r
str11 = "fksdal;jas\ngkl;ajg;"
print(str11)

# 5、求字符串的长度
str12  = "12556933555555"
print(len(str12))
# 6、去除空格   strip(去除前后)   lstrip(去除前面空格)   rstrip(去除后面空格)

str22 = "   我  是  中   国   "
print(str22.strip())
print(str22.lstrip())
print(str22.rstrip())
# 7、字符串的大小写
str14 = "asafRETERdadfWEEEEE"
print(str14.upper())  # 转大写
print(str14.lower())   # 转小写
# 8、大小写转换补充功能
str15 = "aAAsssFFFzzz"
print(str15.swapcase())  # 大小写互换
print(str15.capitalize())   # 转小写  首字符大写
print(str15.title())  # 首字符大写，其他小写

# 9、判断字符串为空
str111 = "  "
print("是否为空:" ,len(str111.strip()) == 0)
print("是否为空:" ,str111.strip() == "")

# 10、字符串运算符  +   *
str01 = "absjf"
str02 = "eeeee"
print(str01+ str02)  # 连接字符串
print("%s%s" % (str01, str02))
print(str02 * 3)  # 把字符串输出  3遍

