import os
# open(path,mode="w", encoding = )
# 方法01  传统方法
print("传统方式====================")
path02 = "C:\\Users\\iezyzhang\\Desktop\\office\\stu02.txt"
try:
    global fd
    fd = open(path02, mode="w", encoding="utf-8")
    fd.write("Hello World!")
except:
    print("写入文件出现异常")
else:
    print("写入成功")
finally:
    fd.close()
# 第一个关键点  mode ="w" ---如果指定路径中文件不存在，会创建文件
# 第二个关键点  写入函数 write

# 方法02 --使用with关键字
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
try:
    with open(path, mode="w", encoding="utf-8") as fd:
        fd.write("Hello Hello Hello")
except:
    print("写入文件出现异常")
else:
    print("with写入成功")

# 重点：如果mode=w,如果写入文件已存在，并且文件中有数据，在写入前清空文件内容
