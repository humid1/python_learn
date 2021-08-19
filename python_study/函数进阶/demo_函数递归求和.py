def sum_numbers(num):
    # 1.出口
    if num == 1:
        return 1
    # 2. 数字的累加 num
    temp = sum_numbers(num - 1)
    return num + temp

print(sum_numbers(100))