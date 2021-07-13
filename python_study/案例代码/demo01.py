# 案例  
# price_str = input("请输入苹果的价格：")
# weight_str = input("请输入苹果的总量：")
# weight = float(weight_str)
# price = float(price_str)
# print(weight * price)

# 以上方式定义了多个变量 (改进方法), 
#   1.节约空间，只需要为一个变量分配空间
#   2.起名字方便，不需要为中间变量起名
price = float(input("请输入苹果的价格："))
weight = float(input("请输入苹果的总量："))
# 格式化输出
print("苹果单价 %.02f 元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (price, weight, weight * price))