# 命名空间
# var1全局变量
var1 = 5
def some_func() :
    # var2 局部变量
    var2 = 6
    def some_inner_func() :
        # var3 是内嵌局部变量
        var3 = 7


# 作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

# 这是一个全局变量
total = 0
# 函数
def sum(arg1, arg2) :
    # 返回2个参数的和
    total = arg1 + arg2 # total在这是局部变量
    print("函数内是局部变量：", total)
    return total

# 调用sum函数
sum(1, 3)
print("函数外的全局变量：", total)

print("======================================")
# global 和 nonlocal关键字
num = 1
def fun1 () :
    # 需要使用 global关键字
    global num
    print(num)
    num = 123
    print(num)

fun1()
print(num)

print("======================================")
# 嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer() :
    num = 10
    def inner() :
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()        