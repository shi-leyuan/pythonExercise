# 时间线柱状图
# 导包
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 第一段
bar1 = Bar()
# 添加x轴数据
bar1.add_xaxis(["中国", "美国", "日本"])
# 添加y轴数据
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转x，y轴
bar1.reversal_axis()

# 第二段
bar2 = Bar()
# 添加x轴数据
bar2.add_xaxis(["中国", "美国", "日本"])
# 添加y轴数据
bar2.add_yaxis("GDP", [60, 50, 60], label_opts=LabelOpts(position="right"))
# 反转x，y轴
bar2.reversal_axis()

# 第三段
bar3 = Bar()
# 添加x轴数据
bar3.add_xaxis(["中国", "美国", "日本"])
# 添加y轴数据
bar3.add_yaxis("GDP", [100, 80, 60], label_opts=LabelOpts(position="right"))
# 反转x，y轴
bar3.reversal_axis()

# 创建时间线对象
timeline = Timeline()

# 在时间线上添加对象
timeline.add(bar1, "19世纪")
timeline.add(bar2, "20世纪")
timeline.add(bar3, "21世纪")

# 设置自动播放
timeline.add_schema(
    play_interval=1000,  # 时间间隔（毫秒）
    is_timeline_show=True,  # 时间线
    is_auto_play=True,  # 自动播放
    is_loop_play=True  # 循环播放
)

# 绘图
timeline.render("时间线柱状图.html")
