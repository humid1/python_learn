age = int(input("请输入年龄："))
if age >= 18:
    print("您的是成年人！")
else:
    print("抱歉！您是未成年人")

num1 = 99
# and 表示两个条件都要成立
if num1 >= 0 and num1 <= 100:
    print("数据范围在 0 ~ 100 之间")
else:
    print("*" * 10)

# or 表示两个条件只要成立一个即可
if num1 > 100 or num1 < 0:
    print("数据范围在 0 ~ 100 之间")
else:
    print("*" * 10)

# not 表示取反
if not (num1 > 100 and num1 < 0):
    print("数据范围在 0 ~ 100 之间")
else:
    print("*" * 10)

# 条件可以写成这种形式
if 0 <= num1 <= 100:
    print("数据范围在 0 ~ 100 之间")
elif num1 > 100:
    print("2" * 10)
else:
    print("*" * 10)

# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整数型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 20

print("*" * 5, " if案例 ", "*" * 5)
# 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket:
    print("有车票，可以开始安检...")

    # 安检时，需要检查刀的长度，判断是否超过 20 厘米
    # 如果超过 20 厘米，提示刀的长度，不允许上车
    if knife_length >= 20:
        print("不允许携带 %d 厘米长的刀上车" % knife_length)
    # 如果不超过 20 厘米，安检通过
    else:
        print("安检通过，祝您旅途愉快……")

# 如果没有车票，不允许进门
else:
    print("大哥，您要先买票啊")
