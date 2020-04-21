# 目录 文件名  扩展名 操作
import os
import time
# 1、basename(path) --- 返回文件名
path03 = "C:\\Users\\iezyzhang\\Desktop\\office\\student01.txt"
print(os.path.basename(path03))

# 案例 返回某一个文件夹下面 所有的文件名  listdir
path = "C:\\Users\\iezyzhang\\Desktop\\office\\"
list01 = os.listdir(path)
print(list01)
# 方法01
# file_list = []
# for i in list01:
#     if "." in i:
#         file_list.append(i)
# print(file_list)

# 方法02
for i in list01:
    abc_path = path + i
    if os.path.isfile(abc_path):
        print(i)

# 2、 dirname(path) --- 返回路径（去掉文件名）
print(os.path.dirname(path03))

# 3、split(path)---分隔文件名和路径，返回元组
tuple01= os.path.split(path03)
print(tuple01)

# 4、splitext(path)--分离文件名和扩展名 返回元组
tuple02 = os.path.splitext(path03)
print(tuple02)

# 案例
all_file = os.listdir(path)
print("路径" + path + "下所有文件名字：")
for i in all_file:
    abs_path = path + i
    if os.path.isfile(abc_path):
        tuple03 = os.path.splitext(abc_path)
        if tuple03[1] == ".txt":
            print("文件名：",os.path.basename(abc_path),"文件类型：","普通文本")
        if tuple03[1] == ".jpg":
            print("文件名：",os.path.basename(abc_path),"文件类型：","图片文本")
# 5、 getsize(file)---获得文件大小
print("文件",path03,"大小为：",os.path.getsize(path03),"B")

# 6、关于文件时间   返回时间戳
# getatime(file)---上次访问的时间
# getmtime(file)--- 上次修改时间
# # getctime(file)--- 创建时间
print("文件上次访问时间：",time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(os.path.getatime(path03))))
print("文件创建时间：",time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(os.path.getctime(path03))))
