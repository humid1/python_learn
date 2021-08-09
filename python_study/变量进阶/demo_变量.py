# id() 查看内存地址

a = 1
print(id(a))
print(id(1))

a = 2

print(id(a))


# ====== 引用 ======
def test(num):

    print(id(num))
    result = "hello"
    print("%s 的内存地址是：%s" % (result, id(result)))
    return result

i = 10

# 内存地址本质就是一串数字
print("i 变量保存数据内存的地址是：%s" % id(a))

# 调用 test 函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
test(a)

print(id(test(a))) # 和方法内部的地址一样

# ====== 可变数据（dict / list）内存地址变化 =======
demo_list = [1, 2, 3]

print("定义列表的内存地址 %d" % id(demo_list))

demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10

print("修改数据后的内存地址 %d" % id(demo_list))

demo_dict = {"name": "小米"}

print("定义字典的内存地址 %d" % id(demo_dict))

demo_dict['age'] = 18
demo_dict.pop("name")
demo_dict['name'] = "小王"

print("修改后的字典内存地址 %d" % id(demo_dict))

# ======== hash ========
print(hash(1))
print(hash("hello"))
print(hash("hello"))
print(hash((1,2)))