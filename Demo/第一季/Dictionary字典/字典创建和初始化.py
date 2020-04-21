
# 在创建的时候直接初始化
student_result = {"张三": 341, "李四": 542, "王五": 421}
print(student_result["张三"])
# 创建一个空的，后期添加
student_result = {}
student_result["张三"] = 342
student_result["李四"] = 512
student_result["王五"] = 412
print(student_result)

# 删除字典元素  pop  删除指定key的元素
student_result.pop("张三")
print(student_result)

# 方法02  popitem   删除这个字典最后一个
print(student_result)
student_result.popitem()
print(student_result)

dict01 = {1: "A", 2: "B", 3: "C", 4: "D"}
print(dict01)
dict01.popitem()
print(dict01)
dict01.popitem()
print(dict01)

# 使用pop删除，key不存在，怎么办   key不存在  程序报错  需要异常处理
# dict01 = {1: "A", 2: "B", 3: "C", 4: "D"}
# dict01.pop(222)
# print(dict01)

dict01 = {1: "A", 2: "B", 3: "C", 4: "D"}
print(dict01)
dict01.clear()
print(dict01)