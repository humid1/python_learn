

def measure():
    """返回当前温度"""
    print("开始测量...")
    temp = 39
    print("结束测量...")
    return temp

print(measure())

# 返回元组类型数据
def measure2():
    """返回当前温度"""
    print("开始测量...")
    temp2 = 39
    wetness = 10
    print("结束测量...")
    # 如果一个函数返回的是元组，括号可以省略
    return (temp2, wetness)

result = measure2()
print(result[0])
print(result[1])

# 如果函数返回类型是元组，可以使用多个变量接收函数返回的结果
gl_temp, gl_wetness = measure2()
print(gl_temp)
print(gl_wetness)


