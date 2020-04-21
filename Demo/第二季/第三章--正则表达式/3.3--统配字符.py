
import re

# ^+3个数字
print(re.findall("\^\d{3}", "^123dsafdsa465"))

# 统配字符----【.】-------------
# a 开头 后面3个任意字符
print(re.findall("a.{3}", "a1s2d12adfdsfs2aee2"))

