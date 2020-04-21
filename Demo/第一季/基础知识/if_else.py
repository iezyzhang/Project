

"""
在控制台输入小王的成绩（语文，数学，英语）
判断：
    如果平均分大于90，提醒你是个聪明的孩子
    如果平均分低于60，提醒你的成绩不理想以后好好努力
"""
# chinese = int(input("请输入语文成绩："))
# math = int(input("请输入数学成绩："))
# english = int(input("请输入英语成绩："))
# avg = (chinese + math + english) / 3
# if avg >= 90:
#     print("你的平均分%.2s,你真是个聪明的孩子。" % avg)
# if avg < 60:
#     print("你的平均分%.2f,你要好好努力了" % avg)

"""
在控制台输入小王成绩（语文，数学，英语）成绩
    判断：
        如果有一门是100分
        如果有两门大于90
        如果三门都大于80
    满足上述任一条件就奖励一朵小红花    
"""
# chinese = int(input("请输入语文成绩："))
# math = int(input("请输入数学成绩："))
# english = int(input("请输入英语成绩："))
# if (chinese == 100 or math == 100 or english == 100):
#     print("奖励一朵小红花！")
# if (chinese >= 90 and math >= 90) or (chinese>=90and english>=90) or (math>=90 and english >= 90):
#     print("奖励小红花")
# if (chinese>=80 and math>=80 and english >=80):
#     print("奖励小红花")

"""chinese = int(input("请输入语文成绩："))
math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))
get_course = ""
if (chinese == 100 or math == 100 or english == 100):
    if (chinese==100): get_course += "语文"
    if (math == 100): get_course += "数学"
    if (english == 100): get_course += "英语"
    print("你的%s得了100分，奖励一朵小红花！" % get_course)
if (chinese >= 90 and math >= 90) or (chinese>=90and english>=90) or (math>=90 and english >= 90):
    if (chinese>=90): get_course += "语文"
    if (math >= 90): get_course += "数学"
    if (english >= 90): get_course += "英语"
    print("你的%s大于等于90分，奖励一朵小红花！" % get_course)
if (chinese >=80 and math >=80 and english >= 80):
    print("你的语文，数学，英语都大于80分，奖励一朵小红花！")"""

# 输入用户名和密码，如果用户名admin，密码123，提示登录成功，否则用户名或密码错误

# lower()吧字符串转为小写      upper（）把字符串转为大写
# strip()去除字符串前后空格
"""username = input("请输入用户名：")
password = input("请输入密码：")
if username.lower().strip() == "admin" and password == "123":
    print("登陆成功")
else:
    print("用户名或密码错误")"""

"""chinese = int(input("请输入语文成绩："))
math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))
get_course = ""
if chinese>=60 and math>=60 and english>=60 :
    print("恭喜你所有科目都及格了")
else:
    if chinese < 60: get_course += "语文"
    if math < 60 :get_course += "数学"
    if english < 60: get_course += "英语"
    print("很遗憾，你没有全部通过考试，需要补考科目为：" + get_course)"""


"""chinese = int(input("请输入语文成绩："))
math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))
get_course = ""
if chinese == 100 or math == 100 or english == 100:
    if chinese == 100:
        get_course += "语文"
    if math == 100:
        get_course += "数学"
    if english == 100:
        get_course += "英语"
    print("你的%s得了100分，奖励一朵小红花！" % get_course)
else:
    if (chinese >= 90 and math >= 90) or (chinese >= 90and english >= 90) or (math >= 90 and english >= 90):
        if chinese >= 90:
            get_course += "语文"
        if math >= 90:
            get_course += "数学"
        if english >= 90:
            get_course += "英语"
        print("你的%s大于等于90分，奖励一朵小红花！" % get_course)
    else:
        if chinese >= 80 and math >= 80 and english >= 80:
            print("你的语文，数学，英语都大于80分，奖励一朵小红花！")"""

# elif
"""
输入小王成绩
评分标准：
    >=90 A
    80_90 B
    70-80 C
    60-70 D
    <60 E
"""
"""chinese = int(input("请输入语文成绩："))
math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))
avg = (chinese + math + english) / 3
if avg >= 90:
    print("你的平均成绩：%.2f,成绩评定为A" % avg)
elif avg >= 80 and avg <= 90:
    print("你的平均成绩：%.2f,成绩评定为B" % avg)
elif avg >= 70 and avg <=80:
    print("你的平均成绩：%.2f,成绩评定为C" % avg)
elif avg >= 60 and avg <= 70:
    print("你的平均成绩：%.2f,成绩评定为D" % avg)
else:
    print("你的平均成绩：%.2f,成绩评定为E" % avg)"""


"""chinese = int(input("请输入语文成绩："))
math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))
get_course = ""
if chinese == 100 or math == 100 or english == 100:
    if chinese == 100:
        get_course += "语文"
    if math == 100:
        get_course += "数学"
    if english == 100:
        get_course += "英语"
    print("你的%s得了100分，奖励一朵小红花！" % get_course)
elif(chinese >= 90 and math >= 90) or (chinese >= 90and english >= 90) or (math >= 90 and english >= 90):
    if chinese >= 90:
        get_course += "语文"
    if math >= 90:
        get_course += "数学"
    if english >= 90:
        get_course += "英语"
    print("你的%s大于等于90分，奖励一朵小红花！" % get_course)
elif chinese >= 80 and math >= 80 and english >= 80:
    print("你的语文，数学，英语都大于80分，奖励一朵小红花！")
else:
    print("没有奖励")"""


# 输入一个月份，判断属于哪个季节
month = int(input("请输入一个月份："))
if month == 12 or month == 1 or month == 2:
    print("%d月是冬季" % month)
elif month == 3 or month == 4 or month == 5:
    print("%d月是春季" % month)
elif month == 6 or month == 7 or month == 8:
    print("%d月是夏季" % month)
elif month == 9 or month == 10 or month == 11:
    print("%d月是秋季" % month)
else:
    print("输入错误，请重新输入。")


