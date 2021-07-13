# 访问字典里的值
dict = {'name': 'my', 'likes': 'java', 'url': 'www.test.com'}
print(dict['name'])
print(dict['likes'])
# print(dict['not']) # 如果字典没有数据就会报错

# 修改字典
dict = {'name': 'bob', 'age': 7, 'class': 'first'}
dict['age'] = 8
dict['school'] = 'beijin university'
print(dict['school'])

# 字典内置函数&方法
print(str(dict))
print(type(dict))

# 删除字典里的元素
del dict['name']  # 删除键 ‘name’
print(dict)
dict.clear() # 清空字典表
print(dict)
del dict     # 删除字典
print('result:',dict['school'])