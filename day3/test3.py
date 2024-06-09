# set集合:无序，不重复
# set1 = {"蔡徐坤", "唱", "喜欢", "唱", "跳", "rap", "唱", "篮球"}
# print(set1)

# # 添加元素
# set1.add("哥哥")
# print(set1)

# # 移除元素
# set1.remove("哥哥")
# print(set1)

# # pop随机取出一个元素
# s1 = set1.pop()
# print(s1)
# print(set1)

# # 清空集合
# set1.clear()
# print(set1)

# # difference取差集
# set1 = {"蔡徐坤", "唱", "喜欢", "唱", "跳", "rap", "唱", "篮球"}
# set2 = {"666", "喜欢", "跳", "rap", "唱", "篮球"}
# set3 = set1.difference(set2)
# print(set3)

# # difference_update消除差集，删除1中和2相同的元素
# set1 = {"蔡徐坤", "唱", "喜欢", "唱", "跳", "rap", "唱", "篮球"}
# set2 = {"666", "喜欢", "跳", "rap", "唱", "篮球"}
# set1.difference_update(set2)
# print(set1)
# print(set2)        # 2不变

# # union集合合并
# set1 = {"蔡徐坤", "唱", "喜欢", "唱", "跳", "rap", "唱", "篮球"}
# set2 = {"666", "喜欢", "跳", "rap", "唱", "篮球"}
# set3 = set1.union(set2)
# print(set3)
# print(set1)
# print(set2)

# # len统计集合中元素个数
# set1 = {"蔡徐坤", "唱", "喜欢", "唱", "跳", "rap", "唱", "篮球"}
# sum = len(set1)
# print(sum)

# # 集合只能用for遍历，不能用while
# set1 = {"蔡徐坤", "唱", "喜欢", "唱", "跳", "rap", "唱", "篮球"}
# for i in set1:
#     print(i)

# # 集合练习:将列表中的元素添加到集合
my_list = ['蔡徐坤', '唱', '喜欢', '唱', '跳', 'rap', '唱', '篮球']  # 列表
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_set)