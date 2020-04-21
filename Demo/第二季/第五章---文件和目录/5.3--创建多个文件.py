# 创建10个文件  自动生成三位数  问题：可能重复
import os
import random
# 方法01 ：每次创建文件时候判断是否存储，如果存在重新创建
def get_file_name():
    return "Text" +"%03d" % random.randint(0,999) + ".txt"
for i in range(10):
    print(get_file_name())
# 创建目录
dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "demo" + os.path.sep
"""if not os.path.exists(dir_path):
    try:
        os.mkdir(dir_path)
        print("目录创建成功")
    except:
        print("创建目录出现异常")
else:
    print("目录已存在")
# 通过循环创建文件
total_number = 10
current_number = 0
while current_number < total_number:
    # 构件文件名
    file_path = dir_path + get_file_name()
    # 判断是否存在
    if not os.path.exists(file_path):
        try:
            global fd
            fd = open(file_path, mode= "w", encoding="utf-8")
            print("文件创建成功")
            current_number += 1
        except:
            print("创建文件出现异常")
        finally:
            fd.close()
    else:
        print("创建文件已存在")"""
# 方法02 先构件好10个不同的名字，然后依次创建
def get_file_number(num:int):
    file_name_list = []
    current = 0
    while current < num:
        name = "Text" +"%03d" % random.randint(0,999) + ".txt"
        if name in file_name_list:
            pass
        else:
            file_name_list.append(name)
            current += 1
    return file_name_list

# 创建目录
if not os.path.exists(dir_path):
    try:
        os.mkdir(dir_path)
        print("目录创建成功")
    except:
        print("创建目录出现异常")
else:
    print("目录已存在")
# 构件10个文件名
name_list = get_file_number(10)

# 依次创建
for name in name_list:
    file_path = dir_path + name
    try:
        global fd
        fd = open(file_path, mode="w", encoding="utf-8")
        print("文件创建成功")
    except:
        print("文件创建出现异常")
    finally:
        fd.close()
