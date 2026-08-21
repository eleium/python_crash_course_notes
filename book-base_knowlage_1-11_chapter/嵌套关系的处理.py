#嵌套关系的处理： 字典嵌套列表，或列表嵌套字典,或者字典套字典，列表套列表：

# 不论是字典嵌套列表，还是列表嵌套字典，都是先遍历外层，拿到内层的列表或字典，
# 然后再遍历内层的列表或字典，得到列表的元素，或字典的键和值。
# 再看要求，分别操作这些元素，或键和值。

# 📌 两种嵌套结构的遍历模式
# 1. 字典嵌套列表（外层是字典，内层是列表）

data = {
    "张三": ["大连", "哈尔滨", "长春"],
    "李四": ["洛阳", "开封", "许昌"],
}

for name, cities in data.items():    # 外层：遍历字典
    print(f"{name} 喜欢的城市：")
    for city in cities:              # 内层：遍历列表：cities就是列表     第一次循环时：   cities=["大连", "哈尔滨", "长春"]
                                                                         #第二次循环时：   cities=["洛阳", "开封", "许昌"] 
        print(f"  {city}")



# 2. 列表嵌套字典（外层是列表，内层是字典）

data = [
    {"name": "张三", "cities": ["大连", "哈尔滨", "长春"]},
    {"name": "李四", "cities": ["洛阳", "开封", "许昌"]},
]

for item in data:                    # 外层：遍历列表
    name = item["name"]
    cities = item["cities"]
    print(f"{name} 喜欢的城市：")
    for city in cities:              # 内层：遍历列表
        print(f"  {city}")

# 📌 核心规律
# 外层结构	        遍历方式	        内层结构	遍历方式
# 字典	            .items()	            列表	for item in list
# 字典	            .items()	            字典	.items()
# 列表	            for item in list	    字典	.items()
# 列表	            for item in list	    列表	for sub in list

# 📌 一句话总结
# 无论嵌套结构如何，遍历逻辑都是“先外层，再内层”：外层拿到内层容器，内层再遍历元素或键值对。
# 关键是搞清楚每一层是什么类型，用对应的遍历方式。


