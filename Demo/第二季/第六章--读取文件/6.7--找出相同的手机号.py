# 找出手机号相同的号码
import os
import re

def get_mobile(path):
    pattern= re.compile(r"[1][3578]\d{9}")
    if not os.path.isfile(path):
        raise Exception
    else:
        with open(path, mode="r", encoding="utf-8") as fd:
            content = fd.read()
            mobile_list = pattern.findall(content)
    return mobile_list


if __name__ == '__main__':
    path01 = "C:\\Users\\iezyzhang\\Desktop\\office\\Student.txt"
    path02 = "C:\\Users\\iezyzhang\\Desktop\\office\\stu01.txt"
    try:
        file_moble01 = get_mobile(path01)
        file_moble02 = get_mobile(path02)
    except:
        print("获取手机号异常！")
    print("两个文件中相同的手机号码：")
    # set01 = set()
    for mobile in file_moble01:
        if mobile in file_moble02:
            print(mobile, end="\t")
            # set01.add(mobile)
# 放法02
    print("\n两个文件中相同的手机号码：")
    # 去除重复手机号
    # 做交集
    print(set(file_moble01) & set(file_moble02))
    print(set(file_moble01).intersection(set(file_moble02)))