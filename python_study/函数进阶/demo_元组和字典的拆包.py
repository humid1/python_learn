def demo(*args, **kwargs):
    
    print(args)
    print(kwargs)

# 元组/字典变量
gl_nums = (1, 2, 3, 4)
gl_dict = {"name": "小明", "age": 11}

demo(*gl_nums, **gl_dict)