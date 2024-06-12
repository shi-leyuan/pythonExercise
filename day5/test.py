# 类
# class Student:
#     name = None
#     gender = None
#     age = None
#     id = None
#     hobby = None
#     address = None
#
#
# # 创建对象
# stu1 = Student()
# # 赋值
# stu1.name = "张三"
# stu1.gender = "男"
# stu1.age = 23
# stu1.id = "2024"
# stu1.hobby = "打篮球"
# stu1.address = "河南"
# print(stu1.name)
# print(stu1.gender)
# print(stu1.age)
# print(stu1.id)
# print(stu1.hobby)
# print(stu1.address)


# 带有成员方法的类
class Student:
    name = None

    def act(self):
        print(f"我是{self.name},我喜欢打篮球")

    def act2(self, msg):
        print(f"{self.name},{msg}")


stu1 = Student()
stu1.name = "张三"
stu1.act()

stu2 = Student()
stu2.name = "蔡徐坤"
stu2.act2("哎哟，你干嘛")
print("---------------------------------")


# init构造方法
class People:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("鸡哥")
        print(f"{self.name},{self.gender},及你太美{self.age}")


p1 = People(name="蔡徐坤", gender="男", age=23)
p2 = People("张三", "女", 22)
print(p1.name)