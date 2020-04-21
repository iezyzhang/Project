# \d---数字    \w---数字  字母下划线     \s---空白字符
# \D--非数字    \W---非数字  字母  下划线   \S---非空白字符
# 案例  非数字开头   +两个空格 +数字/字母/_结尾
import re
print(re.findall(r"\D\s{2}\w", "a sf 22d  s22__"))

# 案例 自定义字符集  ---[]
# 匹配a--f开头，不区分大小写，后面三个小写字母   后面以偶数结尾
print(re.findall(r"[a-fA-F][a-z]{3}[02468]", "asss2 swww6   ___dddda8"))
print(re.findall(r"[a-fA-F][.]{3}[02468]", "a...2 swww6   ___dddda8"))

