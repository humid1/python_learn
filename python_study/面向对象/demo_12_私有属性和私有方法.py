class Women:
    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 18

    def __secret(self):
        """私有方法"""
        print("%s 的年龄是：%d" % (self.name, self.__age))


xh = Women("小红")
# 无法访问私有方法和属性
# xh.__secret()     
# print(xh.__age)   

# 处理方式：在 名称 前面加上 _类名 => _类名__名称
print(xh._Women__age)
xh._Women__secret()