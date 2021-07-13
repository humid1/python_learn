# while True :
#     try : 
#         x = int (input("请输入一个数字："))
#         print("输入的数字是:", x)
#         break
#     except ValueError :
#         print("输入的不是数字，请重新输入！")
        

import sys

try :
    f = open("tmp/foo.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err :
    print("OS error: {0}".format(err))
except ValueError :
    print("Could not convert data to an integer")
except :
    print("Unexpected error", sys.exit()[0])
    raise

# try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
# try 语句中判断文件是否可以打开，如果打开文件时正常的没有发生异常则执行 else 部分的语句
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# try-finally 语句
# try-finally 语句无论是否发生异常都将执行最后的代码。
def runoob() :
    print("test")


try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

# 抛出异常
# x = 10
# if x > 5:
#     raise Exception("x 不能小于 5，x 的值为 {}".format(x))

# try :
#     raise NameError("HiThree")
# except NameError:
#     print("an exception flew by !")
#     raise

# 自定义处理异常
class MyError(Exception) :
    def __init__ (self, value) :
        self.value = value
    def __str__ (self) :
        return repr(self.value)

try : 
    raise MyError(2 * 2)
except MyError as e :
    print("my exception occurred, value:", e.value)

print("=====================================")

import sys

try : 
    f = open('tmp/foo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as error : 
    print ("OS error: {0}".format(err))
except ValueError :
    print("could not convent data to an integer")
except :
    print("Unexpected error:", sys.exc_info()[0])
    raise 

print("=====================================")

def divide(x, y) :
    try : 
        result = x / y
    except ZeroDivisionError :
        print("division by zero")
    except :
        print("result is ", result)
    finally :
        print("executing finally clause")

divide(2, 1)      
divide(2, 0)          