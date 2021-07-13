print("hello,world")

# 变量赋值
counter = 100 # 赋值整型变量
miles = 100.00 # 浮点型
name = "John" # 字符型

print(counter)
print(miles)
print(name)

a = 21
b = 10
c = 0

print("a + b =", (a + b))
print("a - b =", (a - b))

print("-" * 100)

# 比较运算符
if (a == b) :
    print("a 等于 b")
else :
    print("a 不等于 b")

# 位运算符
c = a & b
print("a & b", c)

c = a | b
print("a | b", c)

c = a << 2
print("a << 2", c)

# 逻辑运算符
a = 10
b = 20

if (a and b):
    print("a 和 b 的变量都为 true")
else :
    print("a 和 b 有一个或以上不为true")    

if (a or b) :
    print("变量 a 和 b 都为 true，或其中一个变量为 true")
else :
    print("变量 a 和 b 都为 false")

a = 0
if (a and b) :
    print("a 和 b 的变量都为 true")
else :
    print("a 和 b 有一个或以上不为true")

if (a or b) :
    print("变量 a 和 b 都为 true，或其中一个变量为 true")
else :
    print("变量 a 和 b 都为 false")

if not (a and b) :
    print ("变量 a 和 b 都为 false，或其中一个变量为 false")
else :
    print ("变量 a 和 b 都为 true") 

# 成员运算符
a = 10
b = 20
list = [10,20,30,40]

if (a in list) :
    print("变量 a 包含在给定的 list 集合中")
else :
    print("变量 a 包含在给定的 list 集合中")

# 身份运算符
a = 20
b = 20
if (a is b) :
    print("a 和 b 有相同的标识")
else :
    print("a 和 b 没有相同的标识")

if (id(a) == id(b)) :
    print("a 和 b 有相同的标识")
else :
    print("a 和 b 没有相同的标识")

a = 10
if (a is b) :
    print("a 和 b 有相同的标识")
else :
    print("a 和 b 没有相同的标识")

if (id(a) == id(b)) :
    print("a 和 b 有相同的标识")
else :
    print("a 和 b 没有相同的标识")

# 随机数函数
import random
print(random.choice(range(10)))
print(random.random())    

# 三角函数
import math
x = math.cos(90)
print(x)

# 字符串
str = "hello world!"
print("str[1:4]=", str[1:4])
print("str[1]=", str[1])
print("str[:]=", str[:])
print ("已更新字符串 : ", str[:6] + 'Runoob!')

# 转义字符
print("Hello \t World!")
print("\n")
print("\"")

# 条件控制
age = int(input("请输入年龄:"))
if (age < 0) :
    print("呵呵呵呵呵！")
elif (age == 1) : 
    print("厉害了！！")
elif (age == 2) :
    print("hehhehe") 
else :
    print("ok了")

input("点击 enter 键退出") 
