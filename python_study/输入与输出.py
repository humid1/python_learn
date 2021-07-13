# 读取键盘输入
# str = input('请输入：')
# print('输入的值是：', str)

# 读和写文件
# 第一个参数为要打开的文件名。
# 第二个参数描述文件如何使用的字符。 
#   mode 可以是 
#       'r' 如果文件只读, 
#       'w' 只用于写 (如果存在同名文件则将被删除)
#       'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 
#       'r+' 同时用于读写。 mode 参数是可选的; 
#       'r' 将是默认值。

# 打开一个文件
# f = open('tmp/foo.txt', 'w')
# f.write("Python 是一门非常好的语言。\n yes,it is good!\n")
# num = f.write("Python 是一门非常好的语言。\n yes,it is good!\n")

# print("返回写入的字符数:",num)

# 写入非字符串,需要进行转换
# val = ('java', 'python')
# f.write(str(val))

# 关闭打开的文件
# f.close()

# =================== 读取文件 =========================

# f1 = open('tmp/foo.txt', 'r')
# str = f1.read()
# print(str)

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# str2 = f1.readline()

# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割
# str2 = f1.readlines()
# print(str2)

# 迭代一个文件对象然后读取每行
# for line in f1 :
    # print(line, end = "")


# 关闭打开的文件
# f1.close()

# =================== 读取文件2 =========================

f2 = open('tmp/foo.txt', 'rb+')
num = f2.write(b'sfasfsadfsdfsdfs')

print("字符串长度：", num)

# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾

print(f2.seek(1))
print(f2.seek(2))
print(f2.read(1))
print(f2.seek(-3, 2))   
print(f2.read(1))

# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

import pprint, pickle

data1 = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ('string', u'Unicode string'),
    'c': None
}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()  

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()