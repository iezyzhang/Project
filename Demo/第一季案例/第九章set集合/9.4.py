
"""
=================通讯录管理=================
实现一个通讯录管理系统，要求有添加、修改、删除、查询功能。并且能够退出通讯录管理系统。
具体要求：
【1】根据相应的字母提示完成相应的操作
【2】添加的时候，提醒用户输入姓名，然后输入手机号码；修改的时候只能修改电话号码；删除的时候通过姓名删除；查询的时候可以通过电话查人，也可以通过人查电话
【3】执行界面参考右边截图
"""

def add_person(person_list:list):
    """
    执行添加操作
    :param person_list:
    :return:
    """
    name = input("请输出姓名：")
    mobile = input("请输入手机号码：")
    if is_exist_name(person_list,name):
        print("姓名已存在")
    elif is_exist_mobile(person_list, name):
        print("手机号已存在")
    else:
        # 添加到临时list中
        temp_list = []
        temp_list.append(name)
        temp_list.append(mobile + "\n")
        # 添加到person——list中
        person_list.append(temp_list)
    return person_list
def is_exist_name(person_list:list,name:str):
    """
    查询姓名是否存在
    :param person_list:
    :param name:
    :return:
    """
    for item in person_list:
        if str(item[0]) == name:
            return True
    return False
def is_exist_mobile(person_list:list,mobile:str):
    """
    查询电话是否存在
    :param person_list:
    :param name:
    :return:
    """
    for item in person_list:
        if str(item[1]).replace("\n", "") == mobile:
            return True
    return False
def update_person(person_list):
    """
    修改电话号码
    :return:
    """
    name = input("请输入要修改的姓名：")
    if is_exist_name(person_list,name):
        mobile = input("请输入修改后的电话号码：")
        for index in range(len(person_list)):
            if person_list[index][0] == name:
                person_list[index][1] = mobile + "\n"
                print("修改成功！")

    else:
        print("没有找到%s的任何信息！" % name)
    return person_list
def delete_person(person_list:list):
    """
    删除一个人
    :return:
    """
    name = input("请输入要删除的姓名：")

    if is_exist_name(person_list, name):

        for index in range(len(person_list)):
            if person_list[index][0] == name:
                person_list.pop(index)
                print("删除成功！")
                break
    else:
        print("没有找到%s的任何信息！" % name)
    return person_list
def quary_person(person_list:list):
    """
    可以人查电话，也可以电话查人
    :return:
    """
    select = input("请选择要查询的条件【姓名-A  电话-B】：")
    if select.upper().strip() == "A":
        name = input("请输入要查询的姓名：")
        for index in range(len(person_list)):
            if person_list[index][0] == name.strip():
                print("查询结果：姓名：%s   手机号码：%s" % (name, person_list[index][1]))
                break
            if index == len(person_list) - 1:
                print("查询结果：没有查到%s的信息" % name)

    elif select.upper().strip() == "B":
        mobile = input("请输入要查询的电话：")

        for index in range(len(person_list)):
            if str(person_list[index][1]).replace("\n","") == mobile.strip():
                print("查询结果：姓名：%s   手机号码：%s" % (person_list[index][0], mobile))
                break
            if index == len(person_list) - 1:
                print("查询结果：没有查到%s的信息" % mobile)
def print_person(person_list:list):
    """
    输出通讯录
    :return:
    """
    print("============欢迎使用通讯录管理系统=============")
    print("        姓名       手机号码    ")
    print("-------------------------------------------")
    for item in person_list:
        print("\t\t%s\t%s" % (item[0], item[1]), end="")
    print("\n============================================")
    print("请选择要执行的操作【添加-A  修改-M  删除-D  查找-Q  退出-E】：", end="")
def read_from_file():

    file_path = 'C:\\Users\\iezyzhang\\Desktop\\office\\person.txt'
    # 读取文件
    person_list = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as fd:
            # 捉行读取
            current_line = fd.readline()
            # 判断是否有数据
            while current_line:
                # 把读取的一行数据通过逗号分开
                temp_list = current_line.split(",")
                # 添加到集合
                person_list.append(temp_list)
                # 读取下一行
                current_line = fd.readline()
    except:
        print("读取文件出现异常")
    return person_list
def write_to_file(person_list:list):
    """
    写入文件  1、清空  2、捉行写
    :return:
    """
    file_path = 'C:\\Users\\iezyzhang\\Desktop\\office\\person.txt'
    # 读取文件
    try:
        # 先清空
        with open(file_path,mode="w") as fd:
            fd.write("")
            # 在捉行写
        with open(file_path, mode="a") as fd:
            for item in person_list:
                temp = ",".join(item)
                temp = temp.replace("\n","") + "\n"
                fd.write(temp)
        print("写入完成！")

    except:
        print("写入文件异常！")
if __name__ == "__main__":
    # 读取为间信息
    contact_list = read_from_file()
    print(contact_list)

    while True:

        # 输出
        print_person(contact_list)
        input_char = input()
        # 根据输入的字符执行操作
        if input_char.upper().strip() == "A":
            # 添加
            contact_list = add_person(contact_list)
        elif input_char.upper().strip() == "M":
            # 修改
            contact_list = update_person(contact_list)
        elif input_char.upper().strip() == "D":
            # 删除
            contact_list = delete_person(contact_list)
        elif input_char.upper().strip() == "Q":
            # 查询
            quary_person(contact_list)

        elif input_char.upper().strip() == "E":
            # 退出
            write_to_file(contact_list)
            break
