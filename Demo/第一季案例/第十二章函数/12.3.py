
"""
加密解密
1、加密函数str_encpyption   解密函数为str_decryption
2、加密过程，先将字符串反序，，每个位置转换成ask吗  然后 -10
3、解密算法相反
4、输入一个字符要求只能输入字符和数字，输出加密后的字符，并对加密后的密文解密
"""

def str_encpyption(string:str):
    """
    对字符串加密
    :param string:
    :return:
    """
    string01 = string[::-1]
    en_string = ""
    # 遍历整个字符串
    for char in string01:
        en_string = en_string + chr(ord(char) - 10)
    return en_string



def str_decryption(string:str):
    """
    对字符串解密,
    :param string:
    :return:
    """
    de_string = ""
    for char in string:

        de_string = de_string + chr(ord(char) + 10)

    return de_string[::-1]

def string_check(string:str):
    """
    要求字符和数字
    :param string:
    :return:
    """
    for char in string:
        if char.isdigit() or char.isupper() or char.islower():
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    string = input("请输入要加密的字符串：")
    if string_check(string):
        en__string = str_encpyption(string)
        print("原字符串为：", string)
        print("加密后字符串为：", en__string)
        print("解密后字符串为：", str_decryption(en__string))
    else:
        print("加密的字符必须为数字和字母")
