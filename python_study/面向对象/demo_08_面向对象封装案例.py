class Person:
    """人类"""
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "我叫：%s 体重：%.2f kg" % (self.name, self.weight)

    def run(self):
        print("==== 开始跑步 ====")
        self.weight -= 0.5
        print("结束跑步, 体重减少 0.5kg")

    def eat(self):
        print("==== 开始吃东西 ====")
        self.weight += 1
        print("吃东西，体重增加：1kg")

xm = Person("小明", 60)
xm.eat()
xm.run()
print(xm)

xm2 = Person("小美", 45)
xm2.eat()
xm2.run()
print(xm2)