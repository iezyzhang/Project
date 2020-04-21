# 逻辑或----或者
# 案例：匹配身份证号----18或15位----前面全是数字----最后一位是数字或x
import re
# 整体或
print(re.match(r"\d{17}[0-9x]","41138119960510791x"))

# 部分或
# 案例  找出es或ing  ion结尾的单词
str01 = " If a program needs 20 hours using a single processor core, and a particular portion of the" \
        " program which takes one hour to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then regardless of how many processors are devoted to a" \
        " parallelized execution of this program, the minimum " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
pattren = re.compile(r"\b[a-z]*(?:es|ing|ion)\b")
print(pattren.findall(str01))

