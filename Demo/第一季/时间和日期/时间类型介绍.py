
import time  # 使用的是time模块
import datetime
print(time.time())
print(datetime.datetime.now())

# 使用time模块
# 获取当前的时间戳-------当前的时间相对于1970年-01-01,0分0秒经过了多少秒，结果fudianx
time.time()  # 获得当前的时间戳

# 案例  求某一个程序的执行时间
sum01 = 0
# 获取开始时间戳
start_time = time.time()
for i in range(100000):
    sum01 += i
# 获取结束时间
end_time = time.time()
print("循环执行了%f秒" % (end_time - start_time))

# 如何将一个浮点数的时间转为标准时间日期格式

# 通过时间元组进行转换
print(time.localtime(time.time()))  # 将获取的时间戳转为当地的时间元组
time_tuple = time.localtime(time.time())
print("当前日期为：%d年%d月%d日：%d:%d:%d" % (time_tuple[0], time_tuple[1],
                                     time_tuple[2], time_tuple[3], time_tuple[4], time_tuple[5]))
print(time.gmtime(time.time()))  # 把获取时间戳转为格林威治时间元组
print(time.localtime())  # 把获取时间转为时间戳的当地时间元组，简单写法
print(time.gmtime())  # 把获取的时间戳转为格林威治的时间元组


# 应用案例，  如何通过访问元组获取标准的时间
time_tuple = time.localtime()
print("当前时间：%d-%d-%d  %d:%d:%d" % (time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3],
                                   time_tuple[4], time_tuple[5]))

# 如何格式化时间
print("asctime()格式化：", time.asctime(time.localtime()))  # RPC  1123标准时间格式
print("asctime()简写：", time.asctime())  # RPC1123标准时间格式：获取当前的时间标准格式
print("ctime格式：", time.ctime(time.time()))
print("ctime格式：", time.ctime())

# 以上两种都是格式化RPC标准时间，asctime参数时：时间元组，ctime参数为：浮点数

# 重点：strftime（）方法
# 演示   2019-9-22  12:12:12
print("当前时间为：", time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))
print("当前时间为：", time.strftime("%Y/%m/%d  %H:%M:%S", time.localtime()))
# print("当前时间为：", time.strftime("%Y年%m月%d日  %H:%M:%S", time.localtime()))  # 中间不能有中文

# time模块案例演示
# 2008年8月8日，20.08.08往后88，888，888秒是哪天，星期几
# 日期--》时间戳（浮点数）--》可以做数学运算
print("==================================================")
# 构造日期元组
tuple01 = (2008, 8, 8, 20, 8, 8, 0, 0, 0)
chinese_time01 = time.mktime(tuple01)
# 把指定日期转化为时间戳
print(chinese_time01)
print(time.localtime(chinese_time01))
print(time.asctime(time.localtime(chinese_time01)))
# 往后88888888秒
chinese_time01 += 88888888.0
# 输出结果
print("结果：", time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(chinese_time01)), end=" ")
tuple02_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
print(tuple02_week[time.localtime(chinese_time01)[6]])

