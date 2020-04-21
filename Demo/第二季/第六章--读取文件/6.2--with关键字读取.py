import re
import os
# with---使用with读取的好处在于不用手工关闭资源，读取后系统自定关闭
# 1、基本语法
# dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
#            os.path.sep + "office" + os.path.sep + "Student.txt"
# with open(dir_path, mode="r", encoding="utf-8") as fd:
#     print(fd.read())

# 使用with关键字读取
def get_mobile(text):
    """
    在文本中找出手机号码
    :param text:提供的文本
    :return:返回手机号码的list
    """
    # 实例化一个正则表达式对象
    pattern = re.compile(r"[1][3578]\d{9}")
    # 获取匹配结果
    mobile_list = pattern.findall(text)
    return mobile_list

if __name__ == '__main__':
    dir_path = "C:" + os.path.sep + "Users" + os.path.sep + "iezyzhang" + os.path.sep + "Desktop" + \
               os.path.sep + "office" + os.path.sep + "Student.txt"
    try:
        with open(dir_path, mode="r", encoding="utf-8") as fd:
            # 步骤02 读取文件内容
            content = fd.read()  # 把所有内容存储到内存中
    except IOError as e:
        print(repr(e))
        print("打开文件出现异常")
    except UnicodeDecodeError as e:
        print(repr(e))
        print("文件编码错误")
    except Exception as e:
        print(repr(e))
        print("未知异常")

    # 步骤03 处理内容
    mobile_list01 = get_mobile(content)
    # 输出
    print("获取的手机号码有：")
    for i in mobile_list01:
        print(i)


