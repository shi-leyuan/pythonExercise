# 数据容器
# 列表list  元组tuple  字符串str   集合set  字典dict
# stu1 = ["张三",23]
# stu2 = ["李四",24]
# stu3 = ["王五",25]
# name_list = [stu1,stu2,stu3]
# for i in name_list:
#     print(i)
# print(type(name_list))
# print(name_list[0][0])


# index方法找索引
# stu_list = [["张三", 23], ["李四", 24], ["王五", 25]]
# print(stu_list.index(["李四", 24]))
# # 利用索引修改值
# stu_list[1] = ["李四四", 244]
# print(stu_list)
# # insert(下标，元素)插入
# stu_list.insert(1, ["马六", 26])
# print(stu_list)
# # append 追加到尾部
# stu_list.append(["周八", 28])
# print(stu_list)
# # extend 追加一批
# stu_list2 = [["000",33],["ppp",22]]
# stu_list.extend(stu_list2)
# print(stu_list)
# # del删除
# del stu_list[1]
# print(stu_list)
# # pop删除
# stu0 = stu_list.pop(0)
# print(stu0)     # pop返回删除下标的元素
# print(stu_list)
# # remove删除
# stu_list.remove(["ppp",22])
# print(stu_list)
# # clear清空列表
# stu_list.clear()
# print(stu_list)
# # count统计某元素出现的次数
# stu_list = [["张三", 23], ["李四", 24], ["张三", 23],["王五", 25]]
# print(stu_list.count(["张三", 23]))
# # len统计元素个数
# sum = len(stu_list)
# print(sum)


# 列表练习
# student_age = [21, 25, 21, 23, 22, 20]
# print(student_age)
# # 追加31到尾部
# student_age.append(31)
# print(student_age)
# # 追加新列表[22,23,25]到尾部
# student_age2 = [22, 23, 25]
# student_age.extend(student_age2)
# print(student_age)
# # 取出第一个元素
# num1 = student_age.pop(0)
# print(num1)
# # 取出最后一个元素
# length = len(student_age)
# num_end = student_age.pop(length - 1)
# print(num_end)
# # 查找31的位置
# print(student_age)
# print(student_age.index(31))


# while循环遍历列表
# student_age = [21, 25, 21, 23, 22, 20]
# i = 0
# while i < len(student_age):
#     print(student_age[i])
#     i += 1


# for循环遍历列表
# student_age = [21, 25, 21, 23, 22, 20]
# for i in student_age:
#     print(i)


# 定义一个列表[1,2,3,4,5,6,7,8,9,10]，将偶数存入到新列表
# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = []
# arr3 = []
# for i in arr1:
#     if i % 2 == 0:
#         arr2.append(i)
# print(arr2)

