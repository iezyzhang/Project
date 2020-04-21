# 主要两个方法  findall   finditer
# findall() 使用场景01  没有分组
import re
str01 = " If a program needs 20 hours 13483333479 using a single processor core, and a particular portion of the" \
        " program which takes 9926 one hour to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then 13412369993 regardless 13423534787 of how many processors are devoted to a" \
        " parallelized execution of this program, 3318 the minimum https://www.baidu.com " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
# 案例01  获取a开头的单词
print(re.findall(r"\b[aA][a-z]*\b", str01))

# 案例02  获得1或9开头的数字
print(re.findall(r"\b[19]\d*\b", str01))
# findall() 使用场景01  使用分组(使用非捕获的分组)，没有引用分组后neir

# 案例03 获取http  https开头，cn  com结束的域名
print(re.findall(r"\b(?:http|https)[\w.:/]*(?:cn|com)\b", str01))

# 案例04  获取前两个数字一样的四位数字
print(re.findall(r"\b(\d)\1\d{2}\b", str01))

match_result = re.finditer(r"\b(\d)\1\d{2}\b", str01)
match_list = []
for i in match_result:
    match_list.append(i.group(0))
print(match_list)

match_result = re.finditer(r"\b(?:http|https)[\w.:/]*(?:cn|com)\b", str01)
print(match_result)
match_list = []
for i in match_result:
    match_list.append(i.group(0))
print(match_list)
