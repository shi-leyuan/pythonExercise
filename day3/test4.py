# 字典dict:不允许key的重复
# my_dict = {"张三": 23, "李四": 24, "王五": 25}
# print(my_dict)
# print(my_dict["张三"])


# # 字典嵌套
# student_dict = {
#     "张三": {"语文": 23, "数学": 44, "英语": 63},
#     "李四": {"语文": 80, "数学": 93, "英语": 77},
#     "王五": {"语文": 99, "数学": 55, "英语": 35}
# }
# print(student_dict["李四"]["语文"])


# # 字典的新增和修改
# my_dict = {"张三": 23, "李四": 24, "王五": 25}
# my_dict["马六"] = 26
# print(my_dict)
# my_dict["张三"] = 55
# print(my_dict)
#
# # pop删除
# del_num = my_dict.pop("李四")
# print(del_num)
# print(my_dict)
#
# # clear清空
# my_dict.clear()
# print(my_dict)

# # keys获取全部key
# my_dict = {"张三": 23, "李四": 24, "王五": 25}
# print(my_dict.keys())
# # 通过keys进行遍历
# for i in my_dict.keys():
#     print(f"{i}:{my_dict[i]}")

# # 遍历 ,不支持while
# my_dict = {"张三": 23, "李四": 24, "王五": 25}
# for i in my_dict:
#     print(f"{i}:{my_dict[i]}")

# # len统计数量
# my_dict = {"张三": 23, "李四": 24, "王五": 25}
# print(len(my_dict))

# 字典练习
my_dict = {
    "张三": {
        "学校": "本科",
        "工资": 3000,
        "等级": 1
    },
    "李四": {
        "学校": "专科",
        "工资": 1000,
        "等级": 3
    },
    "王五": {
        "学校": "专科",
        "工资": 2000,
        "等级": 1
    },
    "马六": {
        "学校": "本科",
        "工资": 4000,
        "等级": 2
    }
}
for k in my_dict:
    print(f"{k} = {my_dict[k]}")
print("------------------------------")
for i in my_dict:
    if my_dict[i]["等级"] == 1:
        my_dict[i]["等级"] += 1
        my_dict[i]["工资"] += 1000
for j in my_dict:
    print(f"{j} = {my_dict[j]}")
