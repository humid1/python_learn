name_list = ["zhangshan", "lishi", "wangwu"]

# ==== 取值和取索引值 ====
print(name_list[0])  # 以0开始，不能超出列表范围，否则报错！ list index out of range
# 取出索引
print(name_list.index("zhangshan"))  # 若列表不包含这个值会报错！'zhanghang' is not in list

# ===== 修改 =====
name_list[0] = "张三"
# name_list[3] = "wuli" # 会报程序索引超出指定范围：IndexError: list assignment index out of range

# =====增加 =====
name_list.append("王二") # 在列表末尾追加
name_list.append([1, 2, 3]) # 将这个列表当成一个元素追加
print(name_list)

name_list.insert(3, "cs") # 在指定索引后追加

temp_list = [1, 2, 3, 4]
name_list.extend(temp_list)  # 把其他的列表，追加到这个列表的末尾

# ===== 删除 =====
name_list.remove("王二")  # remove 删除指定元素，（只删除第一次出现的，元素不存在就会报错）
name_list.pop()     # pop 无参数默认会把列表 最后一个元素 移除
name_list.pop(0)    # 把 指定索引 的元素删除
name_list.clear()   # 清空列表所有数据

print(name_list)

# ===== del 删除变量 =====
name_list2 = ["张三", "李四", "王五"]
# del 关键字本质上是用来将一个变量从内存中删除的
del name_list2[2]
print(name_list2)

# ==== len 统计列表长度， count 元素出现的次数 ====
print("列表包含 %s 个元素" % len(name_list2))
print("李四出现 %s 次" % name_list2.count("李四"))

# ==== sort、reserve 列表排序、反转 =====
name_list3 = ["a", "b", "d", "c", "f"]
num_list = [1, 3, 5, 9, 7]

# 升序
# name_list3.sort()
# num_list.sort()

# 降序
# name_list3.sort(reverse=True)
# num_list.sort(reverse=True)

# 反转
name_list3.reverse()
num_list.reverse()

print(name_list3)
print(num_list)