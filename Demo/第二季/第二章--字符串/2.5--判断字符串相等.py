
# 判断字符串相等   ==   is

str01 = "acsd"
str02 = "acsd"
print(str01 == str02)
print(str01 is str02)

# 总结 ==   ----两个字符串内容是否相等
     #  is   ----判断俩个字符创是否是同一个对象（存储的内存地址是否是同一个）
print(id(str01))
print(id(str02))

# 通常情况下，比较字符串是否一致，主要指内容是否一致   常用  ==
# 案例  默写静夜思
tuple01 = ("静夜思", "李白", "床前明月光", "疑是地上霜", "举头望明月", "低头思故乡")
total_number = len(tuple01) - 2
this_time = 0    # 当前默写到第几句
right_total = 0   # 总共正确多少句
wrong_time = 0    # 当前错误了几句
print("当前默写：" + tuple01[1] + "的《" + tuple01[0] + "》，总共" + str(total_number) + "句：")
# 通过循环完成默写
while this_time < total_number:
    this_time += 1
    current = input("请默写第" + str(this_time) + "句：")
    if current.strip() == tuple01[this_time + 1]:
        print("恭喜你！第" + str(this_time) + "句默写正确！")
        right_total += 1
        wrong_time = 0
    else:
        wrong_time += 1
        if wrong_time == 3:
            print("很遗憾！第" + str(this_time) + "句默写错误已达三次！正确答案为：" + tuple01[this_time + 1])
            wrong_time = 0
            continue
        else:
            print("第" + str(this_time) + "句默写错误，请重新默写")
            this_time -= 1
            continue
print("本次默写总共：%d句, 其中正确%d句，正确率%.2f" % (total_number, right_total , right_total/total_number))