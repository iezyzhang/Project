# match()   search()
# 提醒输入手机号码，判断手机号码是否有效
#   11位----第二位【3578】----1开头
import re
input_phone = "15083333479"
# 做法01  简单
if re.match(r"^1[3578]\d{9}$", input_phone):
    print("手机号码有效！号码为：",input_phone)
else:
    print("手机号码无效")

# 做法02  标准
pattren = re.compile(r"^1[3578]\d{9}$")
result = pattren.match(input_phone)
print(result)
if result is not None:
    print("手机号码有效！号码为：", input_phone)
else:
    print("手机号码无效")

# 案例02  判断是否包含134开头的手机号码
str01 = " If a program needs 20 hours 13483333479 using a single processor core, and a particular portion of the" \
        " program which takes one hour to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then 13412369993 regardless 13423534787 of how many processors are devoted to a" \
        " parallelized execution of this program, the minimum " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
pattren01 = re.compile(r"134\d{8}")
match_result = pattren01.search(str01)
print(match_result)
if match_result:
    print("包含134的手机号码，具体为：", match_result.group(0))
else:
    print("不包含134的手机号码")