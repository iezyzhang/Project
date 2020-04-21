import traceback
# try---except---finally
# try:
#     num01 = int(input("请输入第一个整数："))
#     num02 = int(input("请输入第二个整数："))
#
#     print("%d / %d = %.2f" % (num01, num02, num01/num02))
# except:
#     print("代码出现异常")
# finally:
#     print("fianlly的应用代码")
# 无论try中的代码是否异常，finally中的代码都会执行
# 重要：finally代码主要对资源进行回收：打开文件的关闭，或者打开数据库关闭连接

# 案例   读取文件
# try:
#     global fd
#     fd = open("C:\\Users\\iezyzhang\\Desktop\\aaa.csv","r", encoding= "utf-8")
#     print(fd.read())
#     fd.close()
# except FileNotFoundError as  e:
#     print("文件路径错误")
# except UnicodeDecodeError as e:
#     print("编码错误")
# except Exception as e:
#     print("未知错误")
# finally:
#     fd.close()


# try---except---else---finally
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
else:  # 没有异常。执行代码
    print("程序正常运行，没有出现异常")
finally:     #  无论是否异常都执行
    print("finally============")

