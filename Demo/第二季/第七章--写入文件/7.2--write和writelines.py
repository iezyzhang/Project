import os

# 1、写入文件时候，可以写入整数，小数么
path = "C:\\Users\\iezyzhang\\Desktop\\office\\stu03.txt"
try:
    with open(path, mode="w", encoding="utf-8") as fd:
        # fd.write("1000")  # 写入多行
        # 写入多行需要借助于集合
        list01 = ["list1000","list2000","list3000"]  # list 可以作为多行写入的参数
        tuple01 = ("tuple1000","tuple2000","tuple3000")  # 元组 可以作为多行写入的参数
        set01 = {"set1000","set2000","set3000"}   # set 可以作为多行写入的参数
        dict01 = {"上海":3000,"北京":6000,"南京":9000}  # 字典集合 可以作为多行写入的参数  但是只写入key
        # 处理list  写完一行后换行
        for i in range(0, len(list01)):
            list01[i] = "第" + str(i + 1) + "个元素" + list01[i] + "\n"
        fd.writelines(list01)
except TypeError:
    print("写入文件出现异常, 只能写入字符类型")
except Exception as e:
    print("写入文件出现异常, 未知错误")
    print(repr(e))
else:
    print("with写入成功")

# 使用mode=w 在文件写入前。先清空文件内容

# 2、write() 写入单行  和  writelines（）写入多行

