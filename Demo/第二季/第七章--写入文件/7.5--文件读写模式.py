# 常见的读写模式---r, w, a ,r+,w+,a+
import os
# 1、r ---只读不写，标准文本文件，默认就是r模式
print("==========r=============")
new_path = "C:\\Users\\iezyzhang\\Desktop\\office\\mobile.txt"
with open(new_path,mode="r",encoding="utf-8") as fd:
    print(fd.read())

# 2、w----只写不读，  如果文件不存在，创建文件。如果文件存在，打开前清空文件内容
print("==========w=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
# with open(path,mode="w",encoding="utf-8") as fd:
    # print(fd.read())   # 报错  不能读

# 3、a-----追加写   如果文件不存在，创建文件。如果文件存在，打开前不清空文件内容
print("==========a=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
# with open(path,mode="a",encoding="utf-8") as fd:
#     print(fd.read())   # 报错  不能读
# 总结：r模式只读不写，W 模式只写不读

# 4、r+ ---可读可写   不会创建文件， 不清空所有内容，顶部覆盖写
print("==========r+=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
# with open(path,mode="r+",encoding="utf-8") as fd:
     # print(fd.read())
    # fd.write("11oopkopaf")   # 可以写，从头写，覆盖相应位置内容，不覆盖所有内容

# 5、w+ ---可读可写   如果文件存在，则覆盖整个文件，不存在则创建
print("==========w+=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
with open(path,mode="w+",encoding="utf-8") as fd:
     # print(fd.read())
    fd.write("WWW.ccti.com")   # 可以写，如果文件存在，则覆盖整个文件，不存在则创建
    fd.seek(0,os.SEEK_SET)  # 把指针移到头部
    print(fd.read())

# 6、a+ ---可读可写   从文件顶部读取内容，从文件底部添加内容，不存在则创建
print("==========a+=============")
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
with open(path,mode="a+",encoding="utf-8") as fd:
     # print(fd.read())
    fd.write("11oopkopaf")