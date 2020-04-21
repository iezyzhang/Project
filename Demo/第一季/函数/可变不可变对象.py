
def number_update(num01:int, list01:list):
    num01 = num01 + 100
    list01[0] += 100
    return num01
"""
int float  bool  string tuple  不可变类型

list  dict  可变类型
"""
if __name__ == "__main__":
    num01 = 100
    num_result = [11, 33, 44, 55, 55, 7]
    # 调用函数
    num01 = number_update(num01, num_result)
    # 输出结果
    print(num01)
    print(num_result[0])

"""
总结： 按值传递，在函数值的修改不影响调用的实参，按地址传递，修改值影响调用实参
"""

