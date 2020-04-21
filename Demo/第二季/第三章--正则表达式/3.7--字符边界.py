import re
# 1、--[^]---开始位置
# 以95开头的数字
print(re.findall("^95\d*","95654dsfdsfs9523"))

# 2、--[$]---结束位置
# 以95开头的数字
print(re.findall(r"[a-z]{3}95$","95654dsfdsfs95"))

# 输入一个6位数，必须以95开头，8结尾
print(re.findall(r"^95\d{3}8$","950008"))

# 需求  找出 a b c 开头的单词
str01 = " If a program needs 20 hours using a single processor core, and a particular portion of the" \
        " program which takes one hour to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then regardless of how many processors are devoted to a" \
        " parallelized execution of this program, the minimum " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
pattern = re.compile(r"[abcABC][a-z]*")
print(pattern.findall(str01))

# \b  单词边界
# 某一个位置前后不都是\w(数字字母下划线)
pattern = re.compile(r"\b[abcABC][a-z]*")
print(pattern.findall(str01))

# \B  不是什么什么的边界  和\b相反