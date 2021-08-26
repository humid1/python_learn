class Gun:
    """枪类"""

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullect_count = 0

    def add_bullect(self, count):
        """添加子弹"""

        self.bullect_count += count

    def shoot(self):
        if self.bullect_count <= 0:
            print("子弹数量不足，请及时补充！")
            return
        
        self.bullect_count -= 1

        print("%s 发射子弹 [剩余 %d] ..." % (self.model, self.bullect_count))


class Soldier:
    """士兵类"""
    def __init__(self, name):
         # 姓名
        self.name = name
         # 枪，士兵初始没有枪 None 关键字表示什么都没有
        self.gun = None

    def fire(self): 
        # if self.gun == None:
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)

            return    
        
        print("冲冲冲... [%s]" % self.name)

        self.gun.add_bullect(100)

        self.gun.shoot()

# 创建枪对象
ak47 = Gun("AK47")
# ak47.add_bullect(100)
# ak47.shoot()

# 创建人类
people = Soldier("士兵")
people.gun = ak47

people.fire()