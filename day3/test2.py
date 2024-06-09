# 元组，只可读
# t1 = (1, 2, 3, 4, 5)
# t2 = ("zyb",)        # 元组中只有一个元素时最后要加,
# t3 = ("zyb")
# print(t1)
# print(t2)
# print(type(t2))       # <class 'tuple'>
# print(type(t3))      # <class 'str'>


# 元组练习
# t = ("蔡徐坤", 11, ["football", "music"])
# # 查询年龄所在下标
# print(f"年龄所在下标为{t.index(11)}")
# # 查询姓名
# print(f"姓名为t[0]")
# # 删除football
# del t[2][0]
# print(t)


# 字符串(只读)
# my_str = "蔡徐坤 喜欢 打篮球"
# print(my_str[4])
# print(my_str.index("喜欢"))
# new_str = my_str.replace("打篮球", "唱歌")
# print(new_str)
# list1 = my_str.split(" ")       # 将字符串按照空格进行划分，得到列表
# print(list1)
# # 字符串规整strip
# str1 = "  蔡徐坤 喜欢 打篮球  "
# print(str1)
# print(str1.strip())        # 默认去除首尾空格
# str2 = "666蔡徐坤 喜欢 打篮球666"
# print(str2)
# print(str2.strip("66"))


# 字符串练习
# str1 = "caixukun xihuan dalanqiu"
# # 统计有多少个u
# sum = 0
# for i in str1:
#     if i == "u":
#         sum += 1
# print(sum)
# # 将空格换为|
# str2 = str1.replace(" ", "|")
# print(str2)
# # 将字符串用|分割为列表
# print(str2.split("|"))


# 系列切片练习
str1 = "球篮打 欢喜 坤徐蔡"
str2 = str1[::-1]  # 进行正确排序
print(str2)
str3 = str2[4:6:1]  # 找出"喜欢"
print(str3)
