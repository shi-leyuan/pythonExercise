# JSON和python字典相互转换
import json

# 将列表中的字典转化为json
date = [{"name": "张三", "age": 23}, {"name": "李四", "age": 24}, {"name": "王五", "age": 25}, ]
json_date1 = json.dumps(date, ensure_ascii=False)  # ensure_ascii=False可以输出中文
print(type(json_date1))
print(json_date1)
print("------------------------------------")

# 将字典转化为json
d = {"name": "张三", "age": 23}
json_date2 = json.dumps(d, ensure_ascii=False)
print(type(json_date2))
print(json_date2)
print("------------------------------------")

# 将json转化为python类型
p = '[{"name": "张三", "age": 23}, {"name": "李四", "age": 24}, {"name": "王五", "age": 25}]'
python_date = json.loads(p)
print(type(python_date))
print(python_date)
print("------------------------------------")

# 将json转化为python类型
d = '{"name": "张三", "age": 23}'
python_date2 = json.loads(d)
print(type(python_date2))
print(python_date2)
print("------------------------------------")
