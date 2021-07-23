def print_line(char, count):
    """打印一行分隔符"""
    print(char * count)


def print_lines():
    """打印多行分隔符"""
    row = 0
    while row < 5:
        print_line('&', 50)
        row += 1
    

# print_lines()        