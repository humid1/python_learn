class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        self.name = new_name

    def eat(self):
        print("%s 喜欢吃！！！" % self.name)

tom = Cat("Tom")
tom.eat()

lazy_cat = Cat("Ele")
lazy_cat.eat()