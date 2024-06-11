# 函数的多返回值
# def my_return():
#     return 1, 6.6, "hello"
#
# a, b, c = my_return()
# print(a)
# print(b)
# print(c)

# 位置参数
# def my_test(name, age, hobby):
#     print(f"我叫{name},今年{age}岁，喜欢{hobby}")
#
# my_test("蔡徐坤", 23, "打篮球")

# 关键字参数
# def my_test(name, age, hobby):
#     print(f"我叫{name},今年{age}岁，喜欢{hobby}")
#
# my_test(name="蔡徐坤", age=23, hobby="打篮球")
# my_test(age=23, name="蔡徐坤", hobby="打篮球")
# my_test(hobby="打篮球", name="蔡徐坤", age=23)

# 缺省参数
# def my_test(name, age, hobby="打篮球"):
#     print(f"我叫{name},今年{age}岁，喜欢{hobby}")
#
# my_test("蔡徐坤", 23)
# my_test("蔡徐坤", 23, "rap")

# 位置不定长
# def my_test1(*args):
#     print(f"my_test1类型为{type(args)},内容是{args}")
#
# my_test1(1, 1.1, "蔡徐坤")
#
#
# # 关键字不定长
# def my_test2(**kwargs):
#     print(f"my_test2类型为{type(kwargs)},内容是{kwargs}")
#
# my_test2(name="蔡徐坤", age=23)

# 函数作为参数
def my_test(my_add):
    result = my_add(1, 2)
    print(result)

def my_add(x, y):
    return x + y

my_test(my_add)

# lambda匿名函数       (只有一行,不能重复调用)
def my_test2(my_add2):
    result = my_add2(1, 2)
    print(result)

my_test2(lambda x, y: x + y)
