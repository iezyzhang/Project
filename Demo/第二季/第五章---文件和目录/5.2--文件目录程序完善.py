import os
# 程序完善01  路径分隔符
# 程序完善02   异常处理
# file_path = r"C:\Users\iezyzhang\Desktop\office\demo"
dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "demo" + os.path.sep
file_path = dir_path + "Text.txt"
print(dir_path)
print(file_path)

# 2、创建目录
if not os.path.exists(dir_path):
    try:
        os.mkdir(dir_path)
        print("目录创建成功")
    except:
        print("创建目录出现异常")
else:
    print("目录已存在")
# 创建文件
if not os.path.exists(file_path):
    try:
        global fd
        fd = open(file_path,mode="w",encoding="utf-8")   #  os.mknod() window下不能使用  创建文件
        print("文件创建成功")
    except:
        print("创建文件出现异常")
    finally:
        fd.close()
else:
    print("文件已存在")
# 4、 删除文件
if os.path.exists(file_path):
    try:
        os.remove(file_path)
        print("文件删除成功")
    except:
        print("删除文件出现异常")
else:
    print("要删除的文件不存在")

# 5、删除 目录
if os.path.exists(dir_path):
    try:
        os.rmdir(dir_path)
        print("目录删除成功")
    except:
        print("删除目录出现异常")
else:
    print("要删除的目录不存在")
