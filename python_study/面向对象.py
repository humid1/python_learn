class MyClass :
    """一个简单的类实例"""
    i = 12345
    def f (self) :
        return 'hello world'

# 实例化类
x = MyClass()

print(x.i)
print(x.f())

class MyClass2 : 
    # 定义构造方法
    def __init__ (self, realpart, imagpart) :
        self.r = realpart
        self.i = imagpart

x = MyClass2(3, 3.9)

print(x.r, "====>", x.i)


class Test :
    def test (self) :
        print(self)
        print(self.__class__)

t = Test() 
t.test()

print("================================")

class People :
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性在类外部无法直接进行访问
    _height = 0
    # 定义构造方法
    def __init__(self, n, a, h) :
        self.name = n
        self.age = a
        self._height = h
    def speak(self) :
        print("%s 说: 我 %d 岁了.我有 %s cm" %(self.name, self.age, self._height))    

p = People('小明', 12, 120)
p.speak()
