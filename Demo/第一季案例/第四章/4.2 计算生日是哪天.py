
"""
输入自己生日  计算这天是当年的多少天
"""
# 日期时间：1989-10-23   如何获得年月    闰年和平年
import datetime

if __name__ == "__main__":
    input_number = input("请输入你的生日【比如1988-10-10】:")
    # 判断是否有效
    if input_number.replace("-", "").strip().isdigit():
        # 分隔年月日
        date = input_number.strip().split("-")
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        # 由年月日  异常类型的日期
        try:
            birthday = datetime.date(year, month, day)
            print(birthday)
            # 生成前一年的最后一天
            last_year = datetime.date(year-1, 12, 31)
            # 两个日期相减
            result = (birthday - last_year).days
            print("您的生日是%d年的第%d天" % (year, result))
        except:
            print("输入的生日格式不符合日期规范")
