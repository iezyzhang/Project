
# 基本判断：大写字母，小写字母，数字，汉字等

# 案例01：输入密码，字母或数字   大于等于6位
# str_password = input("请输入密码：")
# if str_password.isalnum() and len(str_password) >= 6:
#     print("密码符合要求")
# else:
#     print("不符合要求")

# 案例02; 输入手机号   必须为数字
# str_num = input("请输入手机号码：")
# if str_num.isdigit() and len(str_num) == 11:
#     print("手机号码符合要求")
# else:
#     print("手机号码不符合要求")

# 案例03 输入一段话，判断统计字符大写字母，小写字母，数字，汉字，其他字符
str01 = input("请输入一段话：")
upper_char = 0
lower_char = 0
number_char = 0
chinese_char = 0
other_char = 0
for i in str01:
    if i.islower():   # 小写字母
        lower_char += 1
    elif i.isupper():
        upper_char +=1   # 大写字母
    elif i.isdigit():    # 数字
        number_char += 1
    elif "\u4e00" <= i <= "\u9fa5":   # 汉字
        chinese_char += 1
    else:
        other_char += 1
print("字符串总数：%d  大写字母：%d  小写字符：%d  数字字符：%d  汉字字符：%d  其他字符：%d" %
      (len(str01), upper_char, lower_char, number_char, chinese_char, other_char))

