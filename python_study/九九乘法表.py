
print("=================== 第1种 ===================")
for a in range(1,10) :
    for b in range(1, a + 1):
        print(a * b, "\t", end="")
    print("")

print("=================== 第2种 ===================")
i = 10
while i > 1 :
    i -= 1
    a = 1
    while a < i + 1 :
        print('{0:1d} * {1:1d} = {2:2d}'.format(a, i, a * i), end= '  ')
        a += 1
    print("")

print("=================== 第3种 ===================")    
i = 0
while i < 9 :
    i += 1
    a = 1
    while a < i + 1 :
        print('{0:1d} * {1:1d} = {2:2d}'.format(a, i, a * i), end= '  ')
        a += 1
    print("")

print("=================== 第4种 ====================")  
i = 0
while i < 9 :
    i += 1
    a = 1
    b = 1
    while b < 10 - i :
        print("{0:10}".format(" "), end= "  ")
        b += 1
    while a < i + 1 :
        print('{0:1d} * {1:1d} = {2:2d}'.format((i - a + 1) , i, (i - a + 1) * i), end= '  ')
        a += 1
    print("")

print("===================== 第5种 =====================")  
i = 10
while i > 0 :
    i -= 1
    a = 1
    b = 1
    while b < 10 - i :
        print("{0:10}".format(" "), end= "  ")
        b += 1
    while a < i + 1 :
        print('{0:1d} * {1:1d} = {2:2d}'.format((i - a + 1) , i, (i - a + 1) * i), end= '  ')
        a += 1
    print("")   