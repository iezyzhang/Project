# 零宽断言----匹配一个位置
import re
print(re.findall(r"\b(?<=name=)[a-z]+\b","dfsad  name=bob   name = lij   name=kitee"))

"""
(?<=exp)---在自身位置后面
(?=exp)----在自身位置前面
"""
