# 正则表达式   通过re模块
import re
input_number = input("请输入一个手机号码：")
if re.match(r"1[3578]\d{9}", input_number) is not None:
    print("有效")
else:
    print("无效")

