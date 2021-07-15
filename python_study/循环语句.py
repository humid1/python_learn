"""
while 循环
"""
i = 0
while i < 5:
    print("hello python！")
    i += 1

print("i 的值是：{}".format(i))

print("*" * 30)

j = 0
sum = 0
sum2 = 0
while j <= 100:
    if j % 2 == 0:
        sum += j
    else:
        sum2 += j
    j += 1
print("0 ~ 100 的偶数和是：{}".format(sum))
print("0 ~ 100 的奇数和是：{}".format(sum2))

print("*" * 30)

