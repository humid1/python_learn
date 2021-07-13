# 比较两个数大小
# 使用 def 定义函数方法
def max(a, b) :
    if (a > b) :
        return a
    elif (a < b) :
        return b
    else :
        return '相等'
a = 1
b = 2
print(max(a, b))        

# 定义函数
def printme (str) :
    print(str)
    return

# 调用函数
printme("调用函数！！！")

# 默认参数
def printinfo(str, str2 = 1) :
    print(str, ',', str2)
    # print(str2)
    return

printinfo(11)
printinfo(22, 33)

# 可写函数说明
def printinfo2( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo2 函数
printinfo2( 70, 60, 50 )
printinfo2( 70 )

def printinfo3( arg1, **vartuple ) :
    print (arg1, "", vartuple)

printinfo3(1, a = 3, b = 4)