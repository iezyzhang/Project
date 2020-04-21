
"""
输入一个数字，转换成中文数字

"""
def transfer_number(number):
    """
    数字转大写
    :param number:
    :return:
    """
    string_result=""
    for item in number:
        if "0" in item:
            string_result += "零"
        elif "1" in item:
            string_result += "壹"
        elif "2" in item:
            string_result += "贰"
        elif "3" in item:
            string_result += "叁"
        elif "4" in item:
            string_result += "肆"
        elif "5" in item:
            string_result += "伍"
        elif "6" in item:
            string_result += "陆"
        elif "7" in item:
            string_result += "柒"
        elif "8" in item:
            string_result += "捌"
        elif "9" in item:
            string_result += "玖"
    return string_result


if __name__ == "__main__":
    # 最佳方式    使用元组，主要防止被篡改
    chinese_number = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    # print(transfer_number("2130981240981"))
    number = input("请输入要转换的数字：")
    string_result = ""
    for item in number:
        string_result += chinese_number[int(item)]
    print(string_result)

