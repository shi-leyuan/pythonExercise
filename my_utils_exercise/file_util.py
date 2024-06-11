"""
文件模块
"""


def print_file_info(file_name):
    """
    按路径将文件内容输出到控制台
    :param file_name:文件路径
    :return:None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:  # 报告异常
        print(e)  # 打印异常报告
    finally:
        f.close()  # 关闭文件


def append_to_file(file_name, date):
    """
    将数据添加到指定的文件
    :param file_name:文件名
    :param date:数据
    :return:None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(date)
    f.write("\n")
    f.close()
