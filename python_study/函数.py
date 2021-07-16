
def find_abs():
    """返回数字的绝对值"""
    print(abs(-1000))


def create_dict():
    """创建字典"""
    print(dict())
    print(dict(a='a', b='b', c='c'))
    print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
    print(dict([('one', 1), ('two', 2)]))


def find_help():
    """查看帮助信息"""
    print(help("sys"))

# 调用函数
# find_abs()
# create_dict()
# find_help()


def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


say_hello()


def sum(num1, num2):
    """计算两个数的和"""
    result = num1 + num2
    print("{} + {} = {}".format(num1, num2, result))


sum(1, 2)


def sum2(num1, num2):
    """计算两个数的和,有返回值"""
    result = num1 + num2
    return result

result = sum2(1, 3)

print(result)