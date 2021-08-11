
# ====== 不可变类型 =======
def demo(num, num_list):
    num = 1
    num_list = [4, 5, 6]
    print(num)
    print(num_list)

num = 2
num_list = [1, 2, 3]
demo(num, num_list)
# 查看是否被修改
print(num)
print(num_list)    


# ====== 可变类型参数 ======
def mutable(num_list):

    num_list.extend([1, 2, 3])
    print(num_list)

num_list2 = [6, 7, 8]
mutable(num_list2)
# 内容被修改了
print(num_list2)   