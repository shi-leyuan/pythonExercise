"""
字符串模块
"""


def str_reverse(s):
    """
    字符串反转返回
    :param s:要反转的字符串
    :return:返回结果字符串
    """
    return s[::-1]  # 切片反转


def str_sub(s, x, y):
    """
    对字符串进行切片
    :param s: 被切片的字符串
    :param x: 切片开始下标
    :param y:切片结束下标
    :return:返回切片完成的字符串
    """
    return s[x:y:1]


# 包内测试
if __name__ == '__main__':
    print(str_reverse("蔡徐坤"))
    print(str_sub("caixukun", 2, 6))
