# 分组----组 ---》捕获组   捕获正则表达式前面匹配的内容
# 案例  在前一段英文中，匹配这样的单词  5个字符--第一个字母和第五个一样--第二个  第四个一样
# 比如：abcba
# 1、如何捕获组  2、捕获后如何调用  --- （通过/+组的编号）
import re
str01 = " If a program needs 20 hours using a single processor core, and a particular portion of the" \
        " program which takes one hour to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then regardless of how many processors are devoted to a" \
        " parallelized execution of this program, the minimum " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
print(re.findall(r"\b([a-z])([a-z])[a-z]\2\1\b","abcba   dncnd"))

# 重点 ：如果对正则表达 式做分组，使用fingall方法，显示的是捕获组的内容
# 解决方法01; 如果不对捕获组内容调用，可以使用非捕获组 加[?:]
# 解决方法01: 使用迭代函数  finditer()
match_result = re.finditer(r"\b([a-z])([a-z])[a-z]\2\1\b","abcba   dncnd  dddsa  mioim")
match_list = []
print(match_result)
for i in match_result:
    match_list.append(i.group(0))
print(match_list)

# 命名捕获组 ?P<name>
print(re.findall(r"\b(?P<num01>[a-z])(?P<num02>[a-z])[a-z](?P=num02)(?P=num01)\b","abcba   dncnd  dddsa  mioim"))

