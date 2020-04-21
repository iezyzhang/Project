import os
# 案例  删除文件名为奇数的文件，显示删除前综述，删除后总数，删除了那些文件
import re
dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
           os.path.sep + "office" + os.path.sep + "demo" + os.path.sep

def get_file_number(path):
    """
    统计出文件的数量
    :param path: 提供目录
    :return: 返回文件数量
    """
    total_file = os.listdir(path=dir_path)
    file_number = 0
    for i in total_file:
        abs_path = dir_path + i
        if os.path.isfile(abs_path):
            file_number += 1
    return file_number

def get_file_name(path):
    """
    找出文件名为奇数的文件
    :return:返回文件名称的集合
    """
    total_file = os.listdir(path=dir_path)
    # 实例化一个正则表达式对象
    pattern = re.compile("[\w]+[13579][.][\w]+")
    # 新建一个list  存储匹配的文件名
    name_list = []
    # 遍历
    for i in total_file:
        if pattern.search(i):
            name_list.append(i)
    return name_list

def delete_file(file_list01, path):
    """
    删除指定文件下的路径
    :param file_list: 删除文件的集合
    :param path:删除文件路径
    :return:
    """
    for current in file_list01:
        abs_path = dir_path + current
        try:
            os.remove(abs_path)
        except Exception as e:
            raise e

if __name__ == '__main__':
    # 1、打印删除前的文件数量
    print("删除前文件数量：%s" % get_file_number(dir_path))
    # 2、找出文件名中为奇数的文件
    file_list = get_file_name(dir_path)
    print(file_list)
    # 3、删除符合条件的文件
    try:
        delete_file(file_list,dir_path)
    except:
        print("删除出现异常！")
    else:
        print("删除成功")

    # 4、删除后的文件数量统计
    print("删除后文件数量：%s" % get_file_number(dir_path))

    # 5、打印删除了那些文件
    print("删除文件名如下：")
    for i in file_list:
        print(i, end="\t")


