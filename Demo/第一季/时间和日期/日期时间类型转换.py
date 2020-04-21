
# time-----------datetime
import time
import datetime
#  time--->>>datetime
time01 = time.time()
print(time01)
print(datetime.datetime.fromtimestamp(time01))

# 2 datetime--->>>time
dt01 = datetime.datetime.today()
print("转化前", dt01)
print("转换后  时间戳", dt01.timestamp())
print("转换成时间元组", dt01.timetuple())


# =====================时间日期计算==================
print("===============================================================")
from datetime import datetime, timedelta
dt03 = datetime(2012, 12, 12, 12, 12, 12, 121212)
dt04 = datetime(2011, 11, 11, 12, 11, 11, 111111)
print(dt03 - dt04)
print((dt03 - dt04).days)
print(abs((dt03 - dt04).days))  # 相差多少天
print(abs((dt03 - dt04).seconds))  # 相差多少秒
print(abs((dt03 - dt04).microseconds))  # 相差多少微妙

print(dt03.strftime("%Y-%m-%d  %H:%M:%S"), end=" 和 ")
print(dt03.strftime("%Y-%m-%d  %H:%M:%S"), end=" 相差：")
print(abs((dt03 - dt04).days), "天", abs((dt03 - dt04).seconds), "秒")

# 对某一个时间增加或者减少
print(dt03 + timedelta(days=100))  # 100天之前
print(dt03 + timedelta(days=-100))  # 100天之后
print(dt03 - timedelta(days=-100))  # 100天之后
print(dt03 + timedelta(seconds=9999))
print(dt03 + timedelta(hours=88))
print(dt03 + timedelta(microseconds=999999999))
print(dt03 + timedelta(milliseconds=8989898989))
print(dt03 + timedelta(weeks=88))
