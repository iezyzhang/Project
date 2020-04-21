
def get_char(string:str):
    """

    :param string:
    :return:
    """
    # 定义两个集合
    char_list = []
    char_number = []
    # 初始化两个集合
    for char in range(ord("a"), ord("z") + 1):
        char_list.append(chr(char))
        char_number.append(0)

    for char in string.lower():
        if ord("a") <= ord(char) <= ord("z"):
            char_number[ord(char) - ord("a")] += 1   # 出现字母次数加1
    # print(char_number)
    # print(char_list)
    # print(char_number.index(max(char_number)))    # 索引
    return char_list[char_number.index(max(char_number))]  # 取值

if __name__ == "__main__":
    aa = get_char("asdaassssss")
    print(aa)
