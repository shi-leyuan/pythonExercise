def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner


def sleep():
    import time
    import random
    print("睡眠中.....")
    time.sleep(random.randint(1, 5))


fn = outer(sleep)
fn()
print("-------------------------------------")


# 装饰器的语法糖写法
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner


@outer
def sleep():
    import time
    import random
    print("睡眠中.....")
    time.sleep(random.randint(1, 5))


sleep()
