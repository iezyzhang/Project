
# 判断包含字符串   in
str01 = "www.cctv.com"
print("str01是否包含com:" , ("com" in str01))

# 使用查找实现
print("str01是否包含com:" , str01.find("com") >= 0)
print("str01是否包含com:" , str01.find("aaa") >= 0)

# 判断以什么开头   startwith
# 判断以什么结尾    endwith
print(str01.startswith("s"))
print(str01.endswith("m"))

# 案例  发送消息，判断是否有敏感信息
tuple01 = ("我爱你", "我恨你","我想你")
send_message = input("请输入信息：")
is_con_keyword = False
for i in tuple01:
    if i in send_message:
        is_con_keyword = True
if is_con_keyword:
    print("发送的信息包含敏感信息")
else:
    print("消息发送成功")