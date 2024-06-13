# 魔术方法
# __str__魔术方法
class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student1("张三", 23)
print(stu1)
print(str(stu1))
print("---------------------------------------")


class Student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name = {self.name},age = {self.age}"


stu2 = Student2("张三", 23)
print(stu2)
print(str(stu2))
print("---------------------------------------")


# __lt__魔术方法,比较>或<
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age


stu1 = Student("张三", 23)
stu2 = Student("李四", 24)
print(stu1 > stu2)
print(stu1 < stu2)

print("---------------------------------------")

# __le__魔术方法,比较>=或<=
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age <= other.age


stu1 = Student("张三", 23)
stu2 = Student("李四", 23)
print(stu1 >= stu2)
print(stu1 <= stu2)