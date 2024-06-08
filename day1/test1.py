# 占位符
"""
name = "周蕴博"
age = "18"
print("名字为：%s,年龄为:%s" % (name, age))
"""

"""
a = 11
b = 11.125
print("a=%d" % a)
print("a=%2d" % a)
print("b=%d" % b)
print("b=%f" % b)
print("b=%.2f" % b)
print("b=%5f" % b)
print("b=%7.1f" % b)
print("b=%-7.1f" % b)    # 左对齐
"""
"""
name = "周蕴博"
age = "18"
print(f"我是{name},年龄为{age}岁.")    
print(bool(3>=5))
"""

"""
name = "小米"
now_price = 19.99
name_id = "000001"
growth = 1.2
grow_days = 7
print(f"公司:{name},股票代码:{name_id},当前股价:{now_price}")
print("每日增长系数:%.2f,经过%d天的增长，股价达到了%.2f" % (growth, grow_days, now_price * growth ** grow_days))
"""

"""
# input用法
print("你是鸡哥吗？")
print("请输入你的名字")
name = input()
print("我的名字是%s" % name)
"""

"""
# if语句
age = 10
if age > 18:
    print("我已经成年了")
    print("666")
print("999")          # 注意对齐，不对其不属于
"""

# print("欢迎来到小米游乐场，18岁以下免费")
# print("请输入您的年龄：")
# age = int(input())             # input输出的是字符串
# if age > 18:
#     print("交钱")
# else:
#     print("免费")

# age = input("请输入")
# print(age)


# age = int(input("请输入年龄："))
# if age<=10:
#     print("小学生")
# elif age<=20:
#     print("中学生")
# else:
#     print("666")


# 简单猜数字
# answer = 10
# if int (input("请输入您要猜的数字：")) == answer:
#     print("猜对了")
# elif int(input("再猜")) == answer:
#     print("猜对了")


# if int(input("请输入您的年龄")) > 18:
#     print("年龄过大")
#     if int(input("请输入会员：")) > 2:
#         print("可以")
#     else:
#         print("不可以")
# else:
#     print("可以")


# 猜数字游戏：3次机会，会提示大了还是小了
import random

num = random.randint(1, 10)
print(num)

print("请猜：")
guess_num = int(input())
if (guess_num == num):
    print("猜对了")
else:
    if (guess_num < num):
        print("小了")
    else:
        print("大了")
    guess_num2 = int(input("请猜第二次："))
    if(guess_num2 == num):
        print("猜对了老弟")
    else:
        if (guess_num2 < num):
            print("小了")
        else:
            print("大了")
        guess_num3 = int(input("请猜第三次："))
        if (guess_num3 == num):
            print("猜对了老弟")
        else:
            print("你输了")
