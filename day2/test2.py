# 函数 （必须先定义，后使用）
# 统计字符串长度 ,不使用len()
# arr1 = "zybs432"
# arr2 = "143423"
# arr3 = "     "
# count = 0
# for i in arr1:
#     if i != None:
#         count += 1
# print(count)
#
# def my_len(str):
#     count = 0
#     for i in str:
#         count += 1
#     return count
# print(my_len(arr1))
# print(my_len(arr2))
# print(my_len(arr3))


# 加法函数
# def add(x, y):
#     """
#     add函数，用于两数求和
#     :param x:第一个参数
#     :param y:第二个参数
#     :return:相加的结果
#     """
#     return x + y
#
#
# print("请输入第一个数：")
# x = int(input())
# print("请输入第二个数：")
# y = int(input())
# print(add(x, y))


# 核酸检测函数
# print("请输入您的体温：")
#
#
# def check(x):
#     if x > 37.5:
#         print("发烧了，去做核酸")
#     else:
#         print("健康")
#
#
# temp = int(input())
#
# check(temp)


# global关键字
# num = 100
# def test1():
#     print(f"test1 = {num}")
# def test2():
#     global num              # global设置为全局变量
#     num = 200
#     print(f"test2 = {num}")
# test1()
# test2()
# print(f"num = {num}")


# 简单ATM取钱：主菜单，余额查询，存款，取款
def menu():
    print("欢迎来到中原银行，请选择：")
    print("1.查询余额        2.存款")
    print("3.取款           4.退出")


def watch_money():
    print("---余额查询---")
    print("10000")


def in_money():
    print("存款成功")


def out_money():
    print("取款成功")


while 1:
    menu()
    x = int(input())
    if x == 1:
        watch_money()
    elif x == 2:
        in_money()
    elif x == 3:
        out_money()
    else:
        print("退出")
        break
