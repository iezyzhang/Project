import os
# 读取文件内容   并打印   使用三种方法
dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
               os.path.sep + "office" + os.path.sep + "student01.txt"
# 方法01   通过read读取
print("==========read==============")
fd = open(dir_path, mode="r", encoding="UTF-8")
content = fd.read()
print(content)
# 方法02   通过readlines读取
print("==========readlines==============")
fd = open(dir_path, mode="r", encoding="UTF-8")
content_list = fd.readlines()     # 读取存储 list集合
for i in content_list:
    print(i, end="")
# 方法03   通过readline读取
print("==========readline==============")
fd = open(dir_path, mode="r", encoding="UTF-8")
content = fd.readline()  # 读取一行
while content:     # 如果有内容  循环执行，如果没有结束循环
    print(content,end="")
    content = fd.readline()

