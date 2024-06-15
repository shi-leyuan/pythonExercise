# 闭包

def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn1 = outer("$")
fn1("蔡徐坤")
fn1("gege")
print("-------------------------")
fn2 = outer("^")
fn2("蔡徐坤")
print("-------------------------")


# nonlocal修改外部变量
def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner


fn3 = outer(10)
fn3(20)
print("-------------------------")


# 闭包练习
def account_create(initial_money=0):
    def atm(num, deposit=True):
        nonlocal initial_money
        if deposit:
            initial_money += num
            print(f"存钱{num},余额{initial_money}")
        else:
            initial_money -= num
            print(f"取钱{num},余额{initial_money}")

    return atm


atm = account_create()

atm(1000)
atm(2000)
atm(500, False)
