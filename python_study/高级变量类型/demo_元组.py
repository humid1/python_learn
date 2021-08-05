# 元组定义完，元素不能修改
info_tuple = ("zhangshan", 180, 70.5)

# 查询类型
print(type(info_tuple))

# 取值
print(info_tuple[0])
print(info_tuple[1])

# 定义空元组
empty_tuple = ()
print(type(empty_tuple))

# 定义只包含一个元素的元组
single_tuple = (1)
print(type(single_tuple)) # int 类型

single_tuple2 = (1, )
print(type(single_tuple2))

# 取出索引值
print(info_tuple.index("zhangshan"))

# 统计计数
print("zhangshan 出现了 %s 次" % info_tuple.count("zhangshan"))
print("元组包含 %s 个元素" % len(info_tuple))

# 元组遍历
for info in info_tuple:
    # 使用格式串字符串拼接，这个变量不方便。因为元组中通常保存的数据类型是不同的
    print(info)

# 格式化字符串使用元组
print("名字: %s ,身高：%d cm, 体重：%.2f kg" % info_tuple)

info_str = "名字: %s ,身高：%d cm, 体重：%.2f kg" % info_tuple

print(info_str)

# 元组和列表的转换
num_list = [1, 2, 4, 6]
print(type(num_list))

# 列表转元组
num_tuple = tuple(num_list)
print(type(num_tuple))

# 元组转列表
num_list2 = list(num_tuple)
print(type(num_list2))


