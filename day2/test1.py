# break和continue用法
# for x in range(10):
#     print(666)
#     if x == 5:
#         continue
#     print("看看我执行了吗")
#     if x == 6:
#         break


# 发工资：1w员给20个员工，每人1000.绩效随机1-10，低于5，不发，发完了就不发了
import random

i = 1           # i代表员工编号
money_sum = 10000        # 总钱数
while money_sum >= 0:
    grade = random.randint(1, 10)        # 员工绩效
    if grade >= 5:
        money_sum -= 1000
        print(f"员工{i}的绩效为{grade}，发了1000元，还有{money_sum}元")
        i += 1
        if i > 20:                    # 不能超过20人
            break
        if money_sum == 0:
            print("发完了，下个月再来")
            break
    else:
        print(f"员工{i}的绩效为{grade}，没有工资，还有{money_sum}元")
        i += 1
        if i > 20:
            break
        if money_sum == 0:
            print("发完了，下个月再来")
            break
