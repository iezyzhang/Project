import traceback
# 输入两个整数，求两个数之商

#  实现方式01  通用异常类 ----exception
# try:
#     num01 = int(input("请输入第一个整数："))
#     num02 = int(input("请输入第二个整数："))
#
#     print("%d / %d = %.2f" % (num01, num02, num01/num02))
# except Exception as e:
#     # 01基本异常处理
#     # print("代码出现了异常")
#     # 02给用户一个提示，然后将详细信息写入日志
#     # print("代码出现异常，请联系管理员")
#     # traceback.print_exc(file= open("C:\\applicationSoft\\Systemlogerror.txt", "w", encoding= "utf-8"))
#     # 方式03  展示错误信息
#     print("程序出现异常：", str(e))  # 异常基本信息
#     print(repr(e))           # 异常基本信息和类型
#     print(traceback.format_exc())   # 异常详细信息


# 实现方式02 具体化异常
try:
    num01 = int(input("请输入第一个整数："))
    num02 = int(input("请输入第二个整数："))

    print("%d / %d = %.2f" % (num01, num02, num01/num02))
except ValueError as e:
    print("输入的值不是整数")
except ZeroDivisionError as e:
    print("除数不能为0")
except Exception as e:
    print("代码出现异常，请联系管理员")
    traceback.print_exc(file = open("C:\\applicationSoft\\Systemlogerror.txt", "w", encoding= "utf-8"))
else:
    print("程序正常运行，没有出现异常")

"""
关于try--except
try:
    可能出现异常的代码
except:
    如果出现异常执行的代码
else:
    如果没有异常执行的代码
"""
