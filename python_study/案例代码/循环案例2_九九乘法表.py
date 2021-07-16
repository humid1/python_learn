def multiple_tabel():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %2d" % (col, row, row * col), end = "  ")
            col += 1
        print()
        row += 1

# multiple_tabel()