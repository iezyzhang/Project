# 量词    ---  控制某一个元素重复的次数
import re
# 1、[*]  重复0次或无限次
# 案例   输入一段英文，以na开头以e结尾
print(re.findall("na[a-z]*e", "my name  ie   nae"))  # 匹配name重复1次    nae 重复0次

# 2、[+]  重复1次或无限次
print(re.findall("na[a-z]+e", "my name  ie   nafasfasfsade"))

# 3、[?]  重复1次或0次
print(re.findall("na[a-z]?e", "my name  ie nae  nafasfasfsade"))

# 4、[m]  重复m次
print(re.findall("na[a-z]{5}e", "my name  ie nae  nafasfae"))

# 案例  判断身份证号码是否有效   1、长度 18 为15    前17位数字   最后一位x
print(re.match(r"(\d{14}[0-9x])|(\d{17}[0-9x])", "12365412365555x"))

# 5、[m,n]  重复m-n次
print(re.findall("na[a-z]{3,10}e", "nafasfae"))

# 6、[m,]  重复m次到无限次
print(re.findall("na[a-z]{3,}e", "nafasfae  nafasdfhksadfjkladshfkle"))

# 7、贪婪模式或非贪婪模式  【+】【*】【m,n】[m,]
# 贪婪模式：默认情况下尽可能多的匹配，Python默认贪婪模式
# 非贪婪模式：默认情况下尽可能少的匹配
print(re.findall("\d+", "23465164655assa"))  # 尽可能多匹配
print(re.findall("\d*", "234651646156455assa"))
print(re.findall("\d{3,8}", "23465164655assa"))
print(re.findall("\d{3,}", "23465164655assa"))

# 非贪婪模式   加？
print(re.findall("\d+?", "23465164655assa"))
print(re.findall("\d{3,}?", "23465164655assa"))