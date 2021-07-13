# 把一个元素添加到列表的结尾
a = [1, 2, 3]
a.append(4)
print(a)

# 添加指定列表的所有元素来扩充列表
b = [9]
b.extend(a)
print(b)

# 在指定位置插入一个元素
b.insert(1, 0)
print(b)

# 删除列表中值为 x 的第一个元素, 如果没有这样的元素，就会返回一个错误。
b.remove(9)
print(b)

# 从列表的指定位置移除元素，并将其返回。
print(b.pop(4))
print(b)

# 返回列表中第一个值为 x 的元素的索引
print(b.index(3))

# 返回 x 在列表中出现的次数。
print(b.count(2))

b.insert(2, 10)
print(b)

# 对列表中的元素进行排序。
b.sort()
print(b)

# 倒排列表中的元素。
b.reverse()
print(b)

# 返回列表的浅复制，等于a[:]。
a = b.copy()
print("a =", a)

# 移除列表中的所有项，等于del a[:]。
b.clear()
print(b)
