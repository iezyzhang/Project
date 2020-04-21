
import datetime
# 1 日期类型
date01 = datetime.date.today()
print(date01)
print("年份：", date01.year)
print("月份：", date01.month)
print("日期：", date01.day)

# 2 时间（时 分 秒 微秒  时区）
time01 = datetime.time(12, 12, 12, 121212)
print(time01)
print("时：", time01.hour)
print("分：", time01.minute)
print("秒：", time01.second)
print("微妙", time01.microsecond)

# 3 datetime  时间日期  （年份 月份  日期  时  分  秒  微妙  时区）
datetime01 = datetime.datetime.now()
print(datetime01)
print("年份：", datetime01.year)
print("月份：", datetime01.month)
print("日期：", datetime01.day)
print("时：", datetime01.hour)
print("分：", datetime01.minute)
print("秒：", datetime01.second)
print("微妙", datetime01.microsecond)

# 4 三种转换类型
print("datetime中取date：", datetime01.date())
print("datetime中取time:", datetime.time())
print("date和time组合datetime:", datetime.datetime.combine(date01, time01))

# 5 timeDelta----时间间隔
date03 = datetime.date(2012, 12, 12)
date04 = datetime.date(2008, 5, 27)
print(date03 - date04)
print((date03 - date04).days)

# =======================================
# datetime基本引用
# 1 获取当前日期
from datetime import datetime
print(datetime.now())  # 获取当前日期时间， 可以加时区
print(datetime.today())  # 获取当前日期时间
print(datetime.utcnow())  # 获取当前日期时间

# 2 获取当前日期时间
dt01 = datetime.today()
print(dt01.date())
print(dt01.time())

# 3 获取日期时间的年 月 日  时  分  秒  微妙

print(dt01.year)
print(dt01.month)
print(dt01.day)
print(dt01.hour)
print(dt01.minute)
print(dt01.second)
print(dt01.microsecond)

# 4 构造时间datetime
dt02 = datetime(2008, 8, 8, 20, 8, 8, 888888)
print(dt02)

# 5 格式化时间   ctime
print(dt01.ctime())

# 自定义方法格式化   strftime()
# 2016/8/2
print(dt02.strftime("%Y/%m/%d"))
# 20:56:46
print(dt02.strftime("%H:%M:%S"))
# 2016-8-2  20:56
print(dt01.strftime("%Y/%m/%d  %H:%M"))
# 2016年8月2日  20:56:46
print("%d年%d月%d日" % (dt01.year, dt01.month, dt01.day), dt01.strftime("%H:%M:%S"))
# 2016/8/2  20:56:46
print(dt01.strftime("%Y/%m/%d  %H:%M:%S"))
# 8月2日
print("%d月%d日" % (dt01.month, dt01.day))
# Tue, 02 Aug  2016    20:56:46
print(dt01.ctime())

