class Cat:
    """这是一个猫类"""
    def eat(self, name):
        print(name + ", 在吃饭！")

cat = Cat()
cat.eat("小猫")

# 可以使用 .属性名，利用赋值语句就可以
cat.name = "dddd"

print(cat.__dict__)

# ===============================
class Cat2:
    """这是一个猫类"""
    def eat(self):
        print("%s 爱吃鱼" % self.name)

tom = Cat2()
tom.name = "Tim"
tom.eat()