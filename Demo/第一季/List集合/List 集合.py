
num01 = 100
str01 = "ilskj"

num_list = [12, 34, 345]
print(num_list[1])

# 集合的创建
# 方法01： 新建集合的时候直接初始化成员
num_list1 = [122, 344, 444]
# 方法02：新建空的集合，后期插入
list02 = []
list02.append(100)
list02.append(200)
print(list02)

# 输入学生的数量，依次输入学生的成绩，打印出所有的成绩
student_number = int(input("请输入学生的数量："))
student_result = []
for i in range(1, student_number+1):
    student_result.append(int(input("请输入第【%d】个学生成绩：" % i)))
print(student_result)
