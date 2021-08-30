list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[2:-2])#  从第二个开始（包含），到倒数第二个（不包含）

length = len(list)  # 容量
max_data = max(list)  # 最大值
min_data = min(list)  # 最小值
# list(tuple)
print(list)
list.append(11)  # 添加元素
print(list)
print(list.count(3))  # 计算元素出现次数
list.extend([12, 13, 14, 15])  # 添加列表
print(list)
list.insert(8, 89)  # insert(idex, element) 在指定位置添加元素
print(list)
list.pop(-1)  # pop(index) 移除指定位置元素，默认最后一个，
print(list)
list.remove(12)  # 移除指定元素
print(list)
list.reverse()  # 反转
print(list)
list.sort()  # 排序
print(list)
new_list = list.copy()
list.clear()  # 清空
print(list)
print("""--------------------------dictionary----------------------------------""")
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict2 = dict.copy()  # 复制
del dict["Name"]
print(f"删除Name元素之后是{dict}")
dict.clear()
print(f"清空所有元素之后是{dict}")
print(f"字典的元素数量为{len(dict2)}")
print(f"将字段转换为字符串{str(dict2)}")
print(f"字典的类型是{type(dict2)}")
tup1 = (1, 2, 3,)
dict3 = {}
dict3.fromkeys(tup1, 10)
print(f"使用元组创建字段并提供默认值结果是：{dict3}")
print(f"获取Name对应的值{dict2.get('Name')}")
print(f"判断Age键是不是在字典里{'Age' in dict2}")
print(f"返回字典中的键值对视图{dict2.items()}")
print(f"返回字典中的键视图{dict2.keys()}")
print(f"返回字段中的值视图{dict2.values()}")
dict2.setdefault("Rui")
print(f"甚至字典中的键值对，如果键不存在则直接添加，值为默认值，比如设置一个不存在的Rui键之后{dict2}")
dict2.update({"Ye":1, "Su":2})
print(f"添加其他字段的键值对之后：{dict2}")
dict2.pop("Class")
print(f"删除字段中的键为class的键值对之后：{dict2}")
print(f"什么叫随机返回并删除最后一个键值对？：{dict2.popitem()}")
print(f"删除并返回之后的字典是{dict2}")
