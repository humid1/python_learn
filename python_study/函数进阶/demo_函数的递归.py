def sum_numbers(num):
    
    print(num)
    # 递归的出口很重要，否则会出现死循环
    if num == 0:
        return
    
    sum_numbers(num - 1)

sum_numbers(3)