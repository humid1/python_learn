class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("1.类初始化！")


    def __del__(self):
        print("类创建的对象被销毁！")

    def __str__(self):
        return  "我是小猫：%s" % self.name   

tom = Cat("Tom")
print(tom)