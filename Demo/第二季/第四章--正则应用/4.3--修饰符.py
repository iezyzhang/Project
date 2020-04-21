# re.I   --- 忽略大小写
# re.M ---  多行模式
import re
str01 = " If a program needs 20 hours Single 13483333479 using a single processor core, and a particular portion of the" \
        " program which takes one hour singLe to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then 13412369993 regardless 13423534787 of how many processors are devoted to a" \
        " parallelized execution of this program, the minimum " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
# 找出single  单词忽略大小写
print(re.findall(r"\bsingle\b",str01,re.I))  # 忽略大小写
print(re.findall(r"\b[sS][iI][nN][gG][lL][eE]\b",str01))  # 不用匹配修饰符

# 多行模式
str02 = "single\nsingle\nsingle\nsingle"
print(re.findall(r"^single",str02))
print(re.findall(r"^single",str02,re.M)) # 多行模式  每一行就是一个匹配的字符串

