# 定义支持多值参数的函数
def demo(num, *args, **kwargs):
    
    print(num)  # 1
    print(args) # (2, 3, 4, 5)
    print(kwargs) # {'name': '小明', 'age': 11, 'gender': True}

demo(1, 2, 3, 4, 5, name="小明", age=11, gender=True)


# 计算任意多个值的和
def sum_numbers(*args):
    
    num = 0
    for n in args:
        num += n
    
    return num

print(sum_numbers(1, 2, 3, 4, 5))