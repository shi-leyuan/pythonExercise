# 导包
from pyecharts.charts import Line
# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国","美国","日本"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])
# 使用render生成图像
line.render()
