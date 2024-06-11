# 模块
# import time
# print("hello")
# time.sleep(3)       # 睡眠3秒
# print("666")

# from...import         *代指全部
# from time import sleep
# print("hello")
# sleep(3)
# print("666")

# 练习
import my_utils_exercise.str_util
from my_utils_exercise import file_util

print(my_utils_exercise.str_util.str_reverse("蔡徐坤喜欢打篮球"))
print(my_utils_exercise.str_util.str_sub("蔡徐坤喜欢打篮球", 2, 6))

file_util.print_file_info("D:/file/python-exercise/test.txt")
file_util.append_to_file("D:/file/python-exercise/test.txt","及你太美")
file_util.print_file_info("D:/file/python-exercise/test.txt")

