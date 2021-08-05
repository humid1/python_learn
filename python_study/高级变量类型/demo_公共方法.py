str_list = ["a", "d", "c", "b", "g"]

# ======= 内置函数 =======
# 列表长度
print(len(str_list))

# 字符串 比较符合以下规则： "0" < "A" < "a"
print(max(str_list))

print(min(str_list))

# ======= 切片 =======
print(str_list[0:3])

print((0, 1, 2, 3, 4)[0:3])

# 字典类型无法进行切片
# print({0, 1, 2}[0:1])

# ======== 运算符 ========
# + 合并
tuple_new = (1, 2, 3) + (4, 5)
print(tuple_new)

# * 重复
print([1, 2] * 3)
