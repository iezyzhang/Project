
import os
# 创建目录
# file_path = r"C:\Users\iezyzhang\Desktop\office\demo"
# if not os.path.exists(file_path):
#     os.mkdir(file_path)
# else:
#     print("目录已存在")
# 案例：1、创建一个文件夹demo，demo里面创建一个文件 text01.txt
#   2、删除  demo和text01
# 1、 准备文件和目录的路径
dir_path = "C:\\Users\\iezyzhang\\Desktop\\office\\demo\\"
file_path = dir_path + "Text.txt"
print(dir_path)
print(file_path)
# 2、创建目录
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    print("目录创建成功")
else:
    print("目录已存在")
# 创建文件
if not os.path.exists(file_path):
    fd = open(file_path,mode="w",encoding="utf-8")   #  os.mknod() window下不能使用  创建文件
    print("文件创建成功")
    fd.close()
else:
    print("文件已存在")
# 4、 删除文件
if os.path.exists(file_path):
    os.remove(file_path)
    print("文件删除成功")
else:
    print("要删除的文件不存在")

# 5、删除 目录
if os.path.exists(dir_path):
    os.rmdir(dir_path)
    print("目录删除成功")
else:
    print("要删除的目录不存在")