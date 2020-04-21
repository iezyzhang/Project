import os
# os模块下常用操作方法
# 1、getcwd()----获取当前工作路径
print(os.getcwd())

# 2、chdir(path) --- 修改当前工作路径

# 3、listdir()----列出某一个目录下所有文件和子文件夹，返回list集合
list01 = os.listdir(r"C:\Users\iezyzhang\Desktop\office")
print(list01)
for i in list01:
    file = "C:\\Users\\iezyzhang\\Desktop\\office\\" + i
    if os.path.isfile(file):
        print("文件", i)
    else:
        print("目录", i)

# 4、mkdir ---- 创建单层目录
dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "Demo01" + os.path.sep
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    print("创建成功")
else:
    print("目录已存在")

# 5、makedirs()---创建多层目录
dir_path01 = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "Demo01" + os.path.sep + "AAA" + os.path.sep
if not os.path.exists(dir_path01):
    os.makedirs(dir_path01)
    print("创建成功")
else:
    print("目录已存在")
# 6、 remove()---删除文件
dir_path02 = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "Demo01" + os.path.sep + "111.txt"
if os.path.exists(dir_path02):
    os.remove(dir_path02)
    print("删除成功")
else:
    print("文件不存在")

# 7、 rmdir---删除单层目录
if os.path.exists(dir_path01):
    os.rmdir(dir_path01)
    print("删除成功")
else:
    print("目录不存在")

# 8、removedirs(path)--删除多层目录
# 9、remove() --- 重命名文件或目录
dir_path04 = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "Demo01" + os.path.sep
os.chdir(dir_path04)
# os.rename("","")
# 10、walk(top) --- 遍历top路径下所有子目录，返回一个三元组，（路径，[包含目录],[包含文件]）
tuple01 = os.walk("C:\\Users\\iezyzhang\\Desktop\\office\\demo\\")
print(tuple01)
for root, dir, files in tuple01:
    print(root)
    print(dir)
    print(files)