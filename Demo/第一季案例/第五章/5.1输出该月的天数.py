
# 输入一个年份  在输入一个月份  输出该月的天数

def check_year_month(year, month):
    """
    校验月份年份是否有效
    :return: 正整数  1-12   满足返回T  不满足  返回F
    """
    # 判断年份
    if year.isdigit() and month.isdigit():
        # 判断月份是否是1-12
        month_number = int(month)
        if month_number < 1 or month_number >12:
            return False
        else:
            return True
    else:
        return False

def get_days(year, month):
    """
    获得该月的天数 ，
    :param year: 年份
    :param month: 月份
    :return: 该月的天数
    """
    # 判断年份和月份是否符合要求
    if check_year_month(year, month):
        if month in ["1","3","5","7","8","10","12"]:
            return 31
        elif month in ["4","6","9","11"]:
            return 30
        else:
            # 判断闰年还是平年
            year_number = int(year)
            if year_number % 400 ==0 or (year_number%4==0 and year_number%100 !=0):
                return 29
            else:
                return 28
    else:
        return 0

if __name__ == "__main__":
    year = input("请输入年份：")
    month = input("请输入月份[1-12]：")
    # 获得days
    days = get_days(year, month)
    # 判断
    if days == 0:
        print("输入的年份或月份不符合要求！")
    else:
        print("%s年%s月有%d天" % (year,month,days))
