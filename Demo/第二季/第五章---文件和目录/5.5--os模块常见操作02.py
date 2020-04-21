# 路径操作
# 相对路径和绝对路径
# 绝对路径  C:\aaa\www.txt
# 相对路径   \11\ss.txt
import os
print(os.getcwd())
# 1、abspath()---获取绝对路径
path = "111.txt"   # 相对路径
print(os.path.abspath(path))

# 2、curdir---当前目录
dir_path04 = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "Demo01" + os.path.sep
new_path = dir_path04 + os.curdir
print(os.path.abspath(new_path))

# 3、pardir---上一级目录
new_path01 = dir_path04 + os.pardir
print(os.path.abspath(new_path01))

# 4、name -- 获得操作系统名称
print(os.name)

# 5、exists()---判断某一个文件或路径是否存在
if os.path.exists(dir_path04):
    print("存在")
else:
    print("不存在")

# 6、isabs()---判断是不是绝对路径
path01 = "111.txt"
if os.path.isabs(path01):
    print("shi ")
else:
    print("bushi ")

# 7、ispath()  --- 是不是目录
# 8、isfile() --- 是不是文件
if os.path.isfile(dir_path04):
    print("文件")
else:
    print("目录")

# 9、samefile(path1,path2)---判断两个目录或文件是不是同一个
path03 = "C:\\Users\\iezyzhang\\Desktop\\office\\student01.txt"
path05 = "C:\\Users\\iezyzhang\\Desktop\\office\\person.txt"
if os.path.samefile(path03,path05) and os.path.isfile(path03) and os.path.isfile(path05):
    print("是同一个")
else:
    print("不是同一个")
