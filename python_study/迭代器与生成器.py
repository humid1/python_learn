import sys # 引入 sys 模块

# 迭代器
list = [1,2,3,4,5]
it = iter(list)
# print(next(it))
# print(next(it))

for a in it :
    print(a, end=" ")

print()

# 创建一个迭代器
class MyNumbers :
    def __iter__ (slef) :
        slef.a = 1
        return slef
    def __next__ (slef) :
        x = slef.a
        slef.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# 创建一个迭代器2
class MyNumber2 :
    def __iter__(self) :
        self.a = 1
        return self
    def __next__(self) :
        if self.a <= 20 :
            x = self.a
            self.a += 1
            return x
        else :
            raise StopIteration      

myclass2 = MyNumber2()
myiter2 = iter(myclass2)

for x in myiter2 :
    print("自定义迭代器的值：", x)   


# 生成器
def fibona(n) :
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n) :
            return
        yield a
        a, b = b, a + b
        counter += 1 
f = fibona(10) # f 是一个迭代器，由生成器返回生成         

while True:
    try :
        print(next(f), end = " ")
    except StopIteration:
        break
        
# 使用 next
# list2 = [1,2,3]
# it2 = iter(list2)

# while True:
#     try:
#         print(next(it2))
#     except StopIteration:
#         sys.exit()        