people_dict = {"name": "小明"}

# ==== 取值 ====
print(people_dict["name"])

# ==== 增加、修改 ====
people_dict["age"] = 20  # 增加
people_dict["height"] = 172.5
people_dict["age"] = 21  # key存在，就修改

# ==== 删除 ====
people_dict.pop("name") # 清空 key 为 name 的键值对；若key值不存在就会报错

print(people_dict)
   
# ==== 统计键值对数量 ====
print(len(people_dict))

# ==== 合并字典 ====
temp_dict = {"sex": True, "age": 25}
people_dict.update(temp_dict)  # 如果合并的字典包含已经存在的键值对，会覆盖原有的键值对

# 循环遍历字典
for k in people_dict:
    print("%s : %s" % (k, people_dict[k]))

# ==== 清空字典 ====
people_dict.clear() 

print(people_dict)

# 字典列表集
card_list = [
    {"name": "用户1", "phone": "123456"},
    {"name": "用户2", "phone": "123456"}
]

for card_info in card_list:
    print(card_info)