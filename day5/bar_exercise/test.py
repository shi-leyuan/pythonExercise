"""
柱状图
"""

# 导包
from pyecharts.charts import Bar

bar = Bar()
# 添加x轴数据
bar.add_xaxis(["中国", "美国", "日本"])
# 添加y轴数据
bar.add_yaxis("GDP", [30, 20, 10])
# 反转x，y轴
bar.reversal_axis()
# 绘图
bar.render()
