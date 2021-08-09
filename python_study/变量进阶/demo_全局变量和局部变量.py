# ===== 局部变量的演示 ======

def demo01():
    
    num = 10

    print(num)

    num = 20

    print("修改后 %d" % num)


def demo02():

    num = 100

    print(num)


# demo01()
# demo02()

print("over")

# ===== 全局变量 ======

num2 = 30

def demo03():

    # global 关键字，告诉 Python 解释器 num2 是一个全局变量
    global num2
    # ====== 局部变量不能修改全局变量 ======
    num2 = 40
    print("num2 ===> %s" % num2)

def demo04():

    print("num2 ===> %s" % num2)

demo03()
demo04()

print("over")

