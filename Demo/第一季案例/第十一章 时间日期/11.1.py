
"""# 时间日期   time和datetime[date,time,datetime,timedetla]
# 时间戳-----time
import time
import datetime
print(time.time())  # 返回值 是一个小数，差值。1970-01-01 0.00.00
print(time.asctime())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

print(datetime.datetime.today())"""

"""
需求01：获取当前系统时间，计算出当前的时间距离北京奥运会开幕式【2008-08-08  20：08:08】
相差多少天，多少时，多少分
"""
from datetime import *
import time
def get_time():
    """
    求两个时间差
    :return:
    """
    # 获取当前时间
    today = datetime.today()
    # 北京奥运会开幕时间
    time_2008 = datetime(year=2008,month=8,day=8,hour=20,minute=8,second=8)
    # 求差额
    datla = today-time_2008
    return datla
def get_time01():
    # 获得现在时间戳
    today = time.time()
    # 指定日期
    tuple01 = (2008, 8, 8, 20, 8, 8, 0, 0, 0)
    # 将日期转换为时间戳
    chinese_time = time.mktime(tuple01)

    return today - chinese_time

if __name__ == "__main__":
    """time_date = get_time()
    hour = (time_date.seconds)/3600
    minute = ((time_date.seconds)%3600)/60
    seconds = time_date.seconds % 60
    print("当前时间离2008年开幕式过了：%d天%d时%d分%d秒" % (time_date.days, hour, minute, seconds))"""
    time = get_time01()
    day = time / (60*60*24)
    hour = time % 86400 / 3600
    minute = (time%3600)/60
    second = time % 60
    print("当前时间离2008年开幕式过了：%d天%d时%d分%d秒" % (day, hour, minute, second))


