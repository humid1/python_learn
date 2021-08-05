num_str = "0123456789"

# 截取从 2 ~ 5 位置 的字符串
print(num_str[2:6])

# 截取从 2 ~ 末尾 的字符串
print(num_str[2:])

# 截取从 开始 ~ 5 位置 的字符串
print(num_str[:6])

# 截取完整的字符串
print(num_str[:])

# 从开始位置，每隔一个字符截取字符串
print(num_str[::2])

# 从索引 1 开始，每隔一个取一个
print(num_str[1::2])

# 截取从 2 ~ 末尾 - 1 的字符串
print(num_str[2:-1])

# 截取字符串末尾两个字符
print(num_str[-2:])

# 字符串的逆序（面试题）
print(num_str[::-1])