# python中演示mysql
from pymysql import Connection

# 连接到mysql
conn = Connection(
    host="localhost",  # 主机名
    port=3306,  # 端口
    user="root",  # 用户
    password="123456"  # 密码
)

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("test")

# 执行sql (创建表)
cursor.execute("create table test_pymysql(id int)")