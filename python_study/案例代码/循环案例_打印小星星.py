print("-" * 8, "第1种", "-" * 8)
row = 1
while row <= 5:
    print("*" * row)
    row += 1

print("-" * 8, "第2种", "-" * 8)
row = 1
result = ""
while row <= 5:
    result += "*"
    print(result)
    row += 1

print("-" * 8, "第3种", "-" * 8)
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end = "")
        col += 1
    row += 1    
    print()