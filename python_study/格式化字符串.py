# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
a = 'd1232,13123'
print(str(a))
print(repr(a))

#  repr() 函数可以转义字符串中的特殊字符
b = 'fsdafdsf\n'
print(b)
print(repr(b))

print("========= 输出一个平方表和立方表 =============")
# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
# 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
for i in range(1, 11) :
    print(repr(i).rjust(2), repr(i * i).rjust(3), end=" ")
    print(repr(i * i * i).rjust(4))

for x in range(1, 11) :
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print("============ zfill(), 它会在数字的左边填充 0 =============")
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print("============ str.format() 的基本使用 ==============")
print("参数1：{} 参数2：{}".format("str1", "str2"))
print("{0} , {1}".format("java", "python"))
print("{1} , {0}".format("java", "python"))
print("{name}, {age}".format(name = "jack", age = 21))
import math
print("常量 π 的近似值：{}".format(math.pi))
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print("常量 π 的近似值：{!r}".format(math.pi))
print("常量 π 的近似值(保留3位)：{0:.3f}".format(math.pi))

table = {"arr1": 1, "arr2": 2}
for name, val in table.items() :
    print("{0:10} ==> {1:10d}".format(name, val))

print("arr1: {0[arr1]:d}; arr2: {0[arr2]:d}".format(table))
print("arr1: {arr1:d}; arr2: {arr2:d}".format(**table))

# 旧式字符串格式化
print('常量 π 的近似值是: %5.3f' % math.pi)







