# match对象----使用match（）和search（）返回的对象就是match对象

import re
match_result = re.search(r"\d+","aasdas1236asd")
print(match_result)

# 1、group ()
print(match_result.group())
"""
疑问---group--分组---为何要使用group
如果在正则中没有做任何分组，默认整体就是一个分组，编号为0，group（0）返回整个匹配的结果
"""
# 案例
str01 = "my name is abc 123 afa22sd"
match_result01 = re.search(r"\b([a-z]+)([0-9]+)([a-z]+)\b",str01)
print(match_result01.group(0))
print(match_result01.group(1))
print(match_result01.group(2))
print(match_result01.group(3))

# 2、groups()--将所有分组匹配的结果存入元组中
print(match_result01.groups())

# 3、 start（）匹配开始索引
print(match_result01.start())

# 4、 end（） 匹配结束索引
print(match_result01.end())

# 5、 span() -- start  +  end
print(match_result01.span())

# 打印匹配结果
print(str01[match_result01.start():match_result01.end()])

