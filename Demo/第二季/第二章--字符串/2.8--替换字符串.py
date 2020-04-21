
# 替换字符串---replace
str01 = "www.cctv.com"
print(str01.replace("com", "cn"))

# 去除空格
str02 = "  我  是  中  过  人  "
print(str02.strip())
print(str02.replace(" ", ""))

# 如果多处匹配  如何替换
str03 = "abddabjjabllab"
print(str03.replace("ab", "12"))  # 默认全部替换
print(str03.replace("ab", "12", 2))  # 替换前两个匹配的

# 如果实现第偶数个 替换，怎么做

# 模拟聊天窗口，设定一些关键字，如果发送信息包含关键字，把信息中关键字用*替换
tuple01 = ("我爱你", "我恨你","我想你")
send_message = input("请输入信息：")

for i in tuple01:
    if i in send_message:
        send_message = send_message.replace(i, "*")
print("你要发送的信息为：", send_message)

