
str01 = input("请输入第一个数：")
str02 = input("请输入第二个数：")
num01 = 0
num02 = 0
if str01.isdigit() and str02.isdigit():
    num01 = int(str01)
    num02 = int(str02)
    if num02 == 0:
        print("除数不能为0")
    else:
        print("%d / %d = %d" % (num01, num02, num01/num02))
else:
    print("输入两个数不是整数")