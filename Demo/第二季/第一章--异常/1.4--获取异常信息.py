
"""

"""
import traceback
list01 = [11, 22, 33, 55]
try:
    print(list01[5])
except Exception as e:
    print("出现异常")
    print(e)
    print(e.args[0]) # 反馈异常基本信息
    print(repr(e))  # 反馈异常基本信息和异常类型
    print(traceback.format_exc())  # 反馈异常详细信息
    # 将异常信息写入日志文本
    traceback.print_exc(file= open("C:\\applicationSoft\\Systemlogerror.txt", "w", encoding= "utf-8"))
