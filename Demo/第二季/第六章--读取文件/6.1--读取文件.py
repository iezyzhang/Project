import os
import re
# 读取文件  Student   筛选手机号码
# 步骤01

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
        global fd, content
        fd = open(dir_path, mode="r", encoding="utf-8")
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
    finally:
        # 步骤四 关闭资源
        fd.close()
    # 步骤03 处理内容
    mobile_list01 = get_mobile(content)
    # 输出
    print("获取的手机号码有：")
    for i in mobile_list01:
        print(i)



