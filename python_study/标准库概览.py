# 操作系统接口
import os
print(os.getcwd()) # 返回当前工作目录信息

# 文件通配符
import glob
print(glob.glob("*.py")) # 输出当前文件下所有的 .py 文件

# 命令行参数
import sys
print(sys.argv) # 输出当前文件所在路径

# 字符串正则匹配
import re
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

# 数学函数
import math
print(math.sin(90))

import random
print(random.random())
firuts = ['apple', 'pear', 'banana']
print(random.choice(firuts))         # 取一个数组内的随机值
print(random.sample(range(100), 10)) # 100以内随机数，取10个
print(random.randrange(10))          # 取1个10以内的数

# 访问 互联网
from urllib.request import urlopen
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)


import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()        

# 日期和时间
from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))