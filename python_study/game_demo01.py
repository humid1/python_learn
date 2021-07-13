# 猜数字游戏
import random
number = int(random.choice(range(10)))
guess = -1
print("=========本次需要猜的数字是：", number, "==================")
while number != guess:
    guess = int (input("请输入你要猜的数字："))

    if number == guess :
        print("恭喜你猜对了!")
    elif number < guess :
        print("数字猜大了...")
    elif number > guess :
        print("数字猜小了...")

num = int(input("输入一个数字: "))
if (num%2 == 0) :
    if (num%3 == 0) :
        print ("你输入的数字可以整除 2 和 3")
    else :
        print ("你输入的数字可以整除 2，但不能整除 3")
else :
    if (num%3 == 0) :
        print ("你输入的数字可以整除 3，但不能整除 2")
    else :
        print  ("你输入的数字不能整除 2 和 3")
