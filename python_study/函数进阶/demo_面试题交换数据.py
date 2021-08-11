# 交换两个数据的值
a = 10
b = 30

print("交换前：a = %d, b = %d" % (a, b))


def exchange1(p1, p2):
    """不产生其他变量"""
    p1 = p1 + p2
    p2 = p1 - p2
    p1 = p1 - p2
    print("交换后：a = %d, b = %d" % (p1, p2))


def exchange2(p1, p2):
    """使用其他变量"""
    p3 = p1
    p1 = p2
    p2 = p3
    print("交换后：a = %d, b = %d" % (p1, p2))
    

def exchange3(p1, p2):
    """使用python元组交换"""
    p1, p2 = p2, p1
    print("交换后：a = %d, b = %d" % (p1, p2))

exchange1(a, b)
exchange2(a, b)
exchange3(a, b)

