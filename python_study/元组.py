# 访问元组
var1 = ('Google', 'java', 'json', 'javascript')

print(var1[1])

# 修改元祖
var2 = (1,2,3)
var3 = (3,5,6)
var4 = var2 + var3
print(var4)

# 元祖运算符
print(len(var4)) # 计算元素个数
print(var4 + (4,6)) # 连接
print(('Hi! ') * 4) # 复制
print(3 in (1,2,3)) # 判断元素是否存在
# 迭代
for i in var4 :
    print(i, " ", end="")
print()

# 元组内置函数
print(max(var4)) # 返回元组中元素最大值
print(min(var4)) # 返回元组中元素最小值
var5 = [1, 2, 3, 4, 5]
print(tuple(var5)) # 将可迭代系列转换为元组


# 删除元祖
del var4
print('删除后的元祖：', var4)