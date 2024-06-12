# 导包
from pyecharts.charts import Map

# 准备对象
my_map = Map()
# 准备数据
data = [
    ("北京", 99),
    ("湖南", 199),
    ("河北", 299),
    ("台湾", 399),
    ("广东", 499),
    ("内蒙古", 599),
    ("河南", 699)
]
# 添加数据
my_map.add("地图", data, "china")
# 生成地图
my_map.render()
