# 文件
# 打开文件open

# f = open("D:/file/python-exercise/test.txt","r",encoding="UTF-8")

# # read读取文件   read(x)表示读取x字节
# r1 = f.read()
# print(r1)

# # readlines读取全部行,封装到列表
# r2 = f.readlines()
# print(r2)

# # readline读取一行
# r1 = f.readline()
# print(r1)

# # for循环读取文件
# for i in f:
#     print(i)

# close关闭文件
# f.close()

# with open 执行完自动关闭文件
# with open("D:/file/python-exercise/test.txt","r",encoding="UTF-8") as f:
#     for i in f:
#         print(i)

# # write写入
# f = open("D:/file/python-exercise/test2.txt","w",encoding="UTF-8")
# f.write("蔡徐坤是鸡哥")
# f.flush()         # flush刷新,将内容推送到硬盘
# f.close()

# # a追加
# f = open("D:/file/python-exercise/test2.txt","a",encoding="UTF-8")
# f.write("\n及你太美")
# f.close()

# 文件操作练习
f = open("D:/file//python-exercise/test.txt", "w", encoding="UTF-8")
f.write("张三 23 男 0\n"
          "李四 24 男 4\n"
          "王五 23 男 0\n"
          "马六 25 女 5\n"
          "孙七 26 男 2\n"
          "周八 28 女 1\n")

f1 = open("D:/file//python-exercise/test1.txt", "r", encoding="UTF-8")

f2 = open("D:/file//python-exercise/test2.txt", "a", encoding="UTF-8")
for line in f1:
    line = line.strip()    # strip去掉首尾空格
    if line.split(" ")[3] >= "2":
        f2.write(line)
        f2.write("\n")
f1.close()
f2.close()