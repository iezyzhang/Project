# 提取手机号码，写到mobile.txt中
import os
import re

def get_mobile(path):
    """
    提取指定文件中的手机号
    :param path: 指定文件路径
    :return: 返回手机号码集合
    """
    # 实例化正则表达式对象
    pattern = re.compile(r"[1][35678]\d{9}")
    # 判断是不是文件
    if not os.path.isfile(path):
        raise Exception("提供文件不存在")
    else:
        # 读取内容
        try:
            with open(path, mode="r", encoding="utf-8") as fd:
                return pattern.findall(fd.read())
        except Exception as e:
            raise e



if __name__ == '__main__':
    # 读取文件中手机号码
    path01 = "C:\\Users\\iezyzhang\\Desktop\\office\\Student.txt"
    mobile_list = []
    try:
        mobile_list = get_mobile(path01)
    except Exception as e:
        print(e)
    # 处理list  去重 换行
    for i in range(0,len(mobile_list)):
        mobile_list[i] = mobile_list[i] + "\n"
    set01 = set(mobile_list)  # 转化为set集合   直接去重
    # 输出到文件
    new_path = "C:\\Users\\iezyzhang\\Desktop\\office\\mobile.txt"
    try:
        with open(new_path, mode="w", encoding="utf-8") as ft:
            ft.writelines(set01)
    except:
        print("写入文件出现异常")
    else:
        print("写入成功")



