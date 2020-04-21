"""
从文件中导入学生信息, 在Python的控制台中展示学生信息
【1】文本的格式如下图，信息依次为：学号、姓名、性别、出生日期、手机号码、邮箱地址.
【2】存储格式要求：
{
    95001:{ 姓名:张三, 性别:男, 出生日期:1995/12/24, 手机号码:13562311342,邮箱地址 : zhangsan@iLync.cn },
    95002:{ 姓名: 李四,….}……..
 }

"""

def read_from_file_to_list():
    """
    在文件读取信息
    :return:
    """
    # 定义文件路径
    file_path = "C:\\Users\\iezyzhang\\Desktop\\office\\Student.txt"
    # 定义list集合存储信息
    student_list = []
    # 读取文件   捉行读取
    try:
        with open(file_path, mode="r", encoding="utf-8") as fd:
            # 读取第一行
            current_line = fd.readline()
            # 判断是否有数据
            while current_line:
                # 用逗号把属性分开
                one_line_list = current_line.split(",")
                # 添加到student——list
                student_list.append(one_line_list)
                # 处理下一行
                current_line = fd.readline()
            return student_list

    except Exception as e:
        raise e

def read_from_file_to_dict():
    """
    读取文件存储到字典中
    :return:
    """
    # 定义文件路径
    file_path = "C:\\Users\\iezyzhang\\Desktop\\office\\Student.txt"
    # 定义一个字典集合
    student_dict = {}
    try:
        with open(file_path, mode="r", encoding="utf-8") as fd:
            # 读取第一行
            current_line = fd.readline()
            # 判断是否有内容
            while current_line:
                # 使用逗号分开
                one_line_list = current_line.split(",")
                # 获取最外层字典的key--sno
                sno = one_line_list[0]
                # 拼接定义内层字典
                one_line_dict = {}
                # 初始化内层字典
                one_line_dict["姓名"] = one_line_list[1]
                one_line_dict["性别"] = one_line_list[2]
                one_line_dict["出生日期"] = one_line_list[3]
                one_line_dict["手机号码"] = one_line_list[4]
                one_line_dict["邮箱地址"] = one_line_list[5]
                one_line_dict["家庭住址"] = one_line_list[6]
                # 添加到最外层的字典中
                student_dict[sno] = one_line_dict
                # 处理下一行
                current_line = fd.readline()
            return student_dict

    except Exception as e:
        raise e

def print_student_info(student_dict:dict):
    """
    以表格输出信息
    :param student_dict:
    :return:
    """
    sno_list = list(student_dict.keys())
    print("===============================================学生信息表=============================================")
    print("学号\t姓名\t性别\t出生日期\t\t手机号码\t\t\t\t邮箱地址\t\t\t\t\t\t家庭地址")
    print("-----------------------------------------------------------------------------------------------------")
    for item in student_dict:
        print(item,end="\t")
        print(student_dict[item]["姓名"],end="\t")
        print(student_dict[item]["性别"],end="\t\t")
        print(student_dict[item]["出生日期"],end="\t")
        print(student_dict[item]["手机号码"],end="\t\t")
        print("%-22s" % student_dict[item]["邮箱地址"],end="\t\t")
        print(student_dict[item]["家庭住址"].replace("\n",""),end="")
        print()
    print("=============================================输出完毕====================================================")


if __name__ == "__main__":
    # 加载信息
    student_dict = read_from_file_to_dict()

    print_student_info(student_dict)

