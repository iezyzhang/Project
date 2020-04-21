import os
# 分析：1、读出内容   2、编辑内容   3、写入文件

def get_mobile(path):
    """
    读取指定路径下所有手机号码
    :param path: 提供路径
    :return: 返回号码集合
    """
    try:
        with open(path, mode="r", encoding="utf-8") as fd:
            content = fd.read()
            if len(content) == 0:
                raise Exception("没有任何内容！")
            else:
                return content.split("\n")
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 读取指定路径下的手机号码
    path = "C:\\Users\\iezyzhang\\Desktop\\office\\mobile.txt"
    mobile_list = []
    try:
        mobile_list = get_mobile(path)
        print(mobile_list)
    except Exception as e:
        print(e)

    # 处理
    for i in range(len(mobile_list)):
        mobile_list[i] = str(i+1) + ") " +  +mobile_list[i]
    print(mobile_list)
    try:
        with open(path, mode="w", encoding="utf-8") as fd:
            fd.writelines(mobile_list)
    except:
        print("写入出现异常")
    else:
        print("写入成功")