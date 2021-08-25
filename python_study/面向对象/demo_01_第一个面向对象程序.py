class Cat:
    """这是一个猫类"""
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")    

# 创建猫类对象
tom = Cat()

tom.eat()
tom.drink()

print("10进制内存地址是：%d" % id(tom))
print("16进制内存地址是：%x" % id(tom))

# 新建一个对象
lazy_cat = Cat()
print("两个对象是否相等：%s" % (tom == lazy_cat))
