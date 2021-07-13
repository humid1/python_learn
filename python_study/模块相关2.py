import 模块相关
模块相关.print_func("测试，按标准不能使用中文的模块名称")

# import fibo
# fibo.fib(1000)
# print(fibo.fib2(100))

# 按需导入
from fibo import fib, fib2
fib(1000)
print(fib2(100))