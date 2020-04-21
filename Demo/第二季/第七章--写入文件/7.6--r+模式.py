import os
# r+模式
# 1、基本功能认识
"""print("==========r+=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
with open(path,mode="r+",encoding="utf-8") as fd:
    # print(fd.read())   # 正常读
    fd.write("abcd")   # 可以写，从头写，覆盖相应位置内容，不覆盖所有内容"""
# 2、先读在写
"""print("==========r+先读在写=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
with open(path,mode="r+",encoding="utf-8") as fd:
    print(fd.read())   # 正常读
    fd.write("abcd")"""   # 可以写，从头写，覆盖相应位置内容，不覆盖所有内容
# 3、先写后读
print("==========r+先读在写=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
with open(path,mode="r+",encoding="utf-8") as fd:
    fd.write("abcd")   # 可以写，从头写，覆盖相应位置内容，不覆盖所有内容
    print(fd.read())  # 正常读
# r+模式  先写后读，先覆盖文档相应位置的字符，然后接着指针往下读