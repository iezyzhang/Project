import os
import re
import time
# 统计某一个目录下的文件信息
# 分析： 信息  ：文件名称，类型，大小，创建时间，修改时间
def get_all_file(path):
    total_list = os.listdir(path)
    file_list= []
    # 筛选文件
    for current in total_list:
        abs_path = path + current
        if os.path.isfile(abs_path):
            file_list.append(current)
    return file_list
def get_file_type(filename, path):
    type_dic = {
    "文本文件":["txt"],
    "图片文件":["jpg","png"],
    "office文件":["docx","doc","xls","xlsx","ppt","pptx"]
}
    # 获取字典key的list
    name_list = list(type_dic.keys())
    # 获取字典key的value
    value_list = list(type_dic.values())

    # 获取文件的后缀
    current_type = os.path.splitext(path + filename)[1][1:]
    # 判断属于哪个类型
    for i in range(0, len(value_list)):
        if current_type in value_list[i]:
            return name_list[i]


def get_file_name(filename):
    pattern = re.compile("[\w]*(?=[.])")
    return pattern.search(filename).group()

def format_datetime(time_number:float):
    return time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time_number))



if __name__ == '__main__':
    # 1、获取指定目录下所有文件信息
    dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
               os.path.sep + "office" + os.path.sep
    file_list = get_all_file(dir_path)
    # 2、 遍历获取文件，依次获得类型，大小，创建时间，修改时间
    all_file_info = []
    for curren_file in file_list:
        temp_file_info = []
        # 添加文件信息
        temp_file_info.append(get_file_name(curren_file))
        # print(temp_file_info)
        # 添加类型
        temp_file_info.append(get_file_type(curren_file,dir_path))
        # 添加文件大小
        temp_file_info.append("%.2f" % (os.path.getsize(dir_path + curren_file)/1024))
        # 添加文件创建时间
        temp_file_info.append(format_datetime(os.path.getctime(dir_path + curren_file)))
        # 添加到all_file_list
        all_file_info.append(temp_file_info)
    # 打印
    print("文件名称         文件类型         文件大小（KB）         创建时间")
    print("===============================================================")
    for i in all_file_info:
        print("%-10s" % i[0], end="\t")
        print("%-6s" %i[1], end="\t")
        print("%10s" % i[2], end="\t\t")
        print("%-30s" % i[3])


