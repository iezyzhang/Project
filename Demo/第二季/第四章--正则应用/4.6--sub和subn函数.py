# sub  subn  文本内容的替换

str01 = " If a program needs 20 hours Single M:13483333479 using a single processor core, and a particular portion of the" \
        " program which takes one hour singLe to execute cannot be parallelized, while the remaining 19 hours of " \
        "execution time can be parallelized, then m:13412369993 regardless 13423534787 of how many processors are devoted to a" \
        " parallelized execution of this program, the minimum " \
        "execution time cannot be less than that critical one hour. Hence the speedup is limited to at most 20×."
# 1 需求 把str01中M开头的 号码的后四位替换成****
# sub 文本内容替换  返回替换后的文本
import re
print(re.findall(r"(?<=M:[1][3578]\d{5})\d{4}",str01))
# 替换
print(re.sub(r"(?<=M:[1][3578]\d{5})\d{4}","****",str01,flags=re.I))

# 2、 subn  返回替换后的文本 和  替换次数
tuple01 = re.subn(r"(?<=M:[1][3578]\d{5})\d{4}","****",str01,flags=re.I)
print(tuple01)
print("替换的文本为：",tuple01[0])
print("替换次数为：",tuple01[1])