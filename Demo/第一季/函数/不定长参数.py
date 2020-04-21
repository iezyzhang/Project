# """"""
# def sum_of_number(*args):
#     # print(type(args))
#     """
#     # 功能介绍：求一组数字之和
#     # :param args: 提供的数字的元组
#     # :return: 返回结果为所有数字之和
#     """
#     sum01 = 0
#     for i in args:
#         sum01 += i
#     return sum01
#
# def sum_number(num01, num02, *args):
#     print("num01:", num01)
#     print("num01", num02)
#     print("args", args)
#
#
# if __name__ == "__main__":
#     print(sum_of_number(11))
#     print(sum_of_number(11, 22, 33))
#     print(sum_of_number(11, 33, 44, 55, 66))
#
#     tuple01 = (11, 33)
#     print(sum_of_number(*tuple01))
#     list01 = (11, 33)
#     print(sum_of_number(*list01))
#
#     # 多参数
#     sum_number(11, 22, 33)
#
# # 总结：如和函数的方法中有普通参数和不定长参数的时候，不定长参数一定要放在最后
# # 在调用的时候，先把实参匹配普通的参数，普通参数全部匹配后，再匹配不定长参数
# """"""

"""def sum_of_result(**kwargs):
    # print(type(kwargs))
    sum02 = 0
    for key in kwargs:
        sum02 += kwargs[key]
    return sum02

if __name__ == "__main__":
    print(sum_of_result(语文=89, 数学=90, 英语=77))

    dict01 = {"语文": 89, "数学": 90, "英语": 77}
    print(sum_of_result(**dict01))"""
# 不定长的字典类型使用两个星号  **kwargs


def sum_of_result(num01, *args, **kwargs):
    print(num01)
    print(args)
    print(kwargs)

# 如果有普通参数，不定长的元组，不定长字典，顺序：先普通参数，然后不定长元组，最后不定长字典
print(sum_of_result(100, 200, 300, 500, 语文=89, 数学=90, 英语=77))
