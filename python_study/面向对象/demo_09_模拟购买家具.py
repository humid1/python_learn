class HouseItem:
    """房子家具类"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "【%s】占地面积是：%.2f 平方米" % (self.name, self.area)


class House:
    """房子类"""

    def __init__(self, name, area):
        # 房屋类型
        self.hosue_type = name
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def __str__(self):
        return ("************ \n 户型：【%s】 \n 面积：%.2f 【剩余 %.2f】 \n 添加的家具有 %s \n************"
                % (self.hosue_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        """添加家具"""

        # 1. 判断家具面积
        if item.area > self.free_area:
            print("%s 的面积太大，无法添加！" % item.name)
            return

        # 2. 计算剩余面积
        self.free_area -= item.area

        # 3. 添加家具
        self.item_list.append(item.name)
        print("要添加 %s" % item)


# 1.创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_house = House("三房两厅", 80)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)
