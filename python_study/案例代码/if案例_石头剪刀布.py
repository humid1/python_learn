# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
import random

# 需定义到调用方法前，不然报错 NameError: name 'pname' is not defined
def pname(count):
    if count == 1:
        return "剪刀"
    elif count == 2:
        return "石头"
    else:
        return "布"


while True:
    try:
        player = int(input("请出拳 石头（1）剪刀（2）布（3）："))
        if player != 1 or player != 2 or player != 3:
            print("请输入指定的数字！")
            continue
        # 电脑 随机 出拳
        computer = random.randint(1, 3)  # 生成的随机数n: 1 <= n <= 3
        # 比较胜负
        print("您出拳：{} vs 电脑出拳：{}".format(pname(player), pname(computer)))
        if ((player == 1 and computer == 2)
                or (player == 2 and computer == 3)
                or (player == 3 and computer == 1)):
            print("恭喜你，你赢了！")
        elif player == computer:
            print("你们出的的一样的，平局！")
        else:
            print("电脑战胜了你，再接再厉~~~")
    except ValueError as error:
        print("请输入指定的数字！", error)
