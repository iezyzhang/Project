import os

path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
with open(path,mode="r+",encoding="utf-8") as fd:
    print(fd.tell())   # 打印当前指针的位置
    fd.read(5)    # 读取五个字符
    print(fd.tell())
    fd.seek(3)   # 绝对路径
    print(fd.tell())
    fd.seek(0,os.SEEK_END)
    print(fd.tell())
    fd.seek(0,os.SEEK_SET)
    print(fd.tell())

