# 添加元素
thisset = set((1,2,3,4))
thisset.add(5)
print(thisset)

# 移除元素
thisset.remove(4)
print(thisset)
# thisset.remove(999)
# print('不存在就会发生错误！')

print("元素个数：",len(thisset))

# 清空集合
thisset.clear()
print(thisset)