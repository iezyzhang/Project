# split ---- 字符串切割
str01 = "steven,tomas,kike"
mane_list = str01.split(",")
print(mane_list)
# 注意，在str标准split方法中   只能按一个符号分隔
import re
str01 = "steven,tomas:kike;lile|wei"
name_list = re.split(",|;|:|\|",str01)
print(name_list)

# 切割后处理---去除空内容
str02 = "steven,,,tomas:::kike;;;lile|wei"
name_list01 = [i for i in re.split(",|;|:|\|",str02) if i]
print(name_list01)
