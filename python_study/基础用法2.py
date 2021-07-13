# 在python中 * 运算符可用于字符串，计算结果就是字符串重复指定次数的结果
print('7' * 10)

# 算术运算符优先级
print(8 ** 2)
print(8 - 8 + 2)

price = 7.5
weight = 7

money = price * weight

print(money)

# 查询数据类型
print(type(2 ** 64))

# 不同类型之间的变量计算
str1 = 5
str2 = True
str3 = 9.5
print(str1 + str2) # 输出 6  
print(str1 + str3) # 输出 14.5

# 字符串变量之间的使用
first_name = "三"
last_name = "张"
print(last_name + first_name)
print(last_name * 10)

# input 函数实现键盘输入
# password = input("请输入密码：")
# print(password)

# 类型转换函数
a = int("111")
b = float("1111")
print(type(b))

# 关键字
import keyword
print(keyword.kwlist)
