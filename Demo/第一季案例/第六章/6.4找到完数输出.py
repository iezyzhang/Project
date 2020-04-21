
"""
一个数如果恰好等于它的因子之和，之个数被称为完数
如  6的因子 1、2、3 而6=1+2+3  6是完数
找到1000内所有完数并输出
"""
def perfect_number(number):
    """
    获取某个数的因子
    :param number: 要获取因子得数
    :return: 因子集合
    """
    # 定义一个集合，存储因子
    perfect_list = []
    # 取出所有的因子
    for i in range(1,number):
        if number % i == 0:
            perfect_list.append(i)
        else:
            pass
    return perfect_list

if __name__ == "__main__":
    # 打印
    print("从1-1000内所有的完数：")
    # 1-1000遍历
    for i in range(1,1001):
        if i == sum(perfect_number(i)):
            print("完数：%-10s该完数的因子为：%s" % (i,perfect_number(i)))


