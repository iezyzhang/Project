import os
# 读取大文件
# 情况一：如果有分行   用readline 读取
dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
               os.path.sep + "office" + os.path.sep + "student01.txt"
print("========== 有分行==readline==============")
fd = open(dir_path, mode="r", encoding="UTF-8")
content = fd.readline()  # 读取一行
while content:     # 如果有内容  循环执行，如果没有结束循环
    print(content,end="")
    content = fd.readline()
# 情况02  文本没有分行
print("========== 没有分行==readlines==============")
fd = open(dir_path, mode="r", encoding="UTF-8")
content = fd.read(1024)  # 读取一行
while True:     # 如果有内容  循环执行，如果没有结束循环
    print(content,end="")
    content = fd.read(1024)
    if not content:
        break

# 情况03  使用with迭代器
print("==========使用with迭代器============================")
with open(dir_path, mode="r", encoding="UTF-8") as fd:
    for line in fd:
        print(line, end="")