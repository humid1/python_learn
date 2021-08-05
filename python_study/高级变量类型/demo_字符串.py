str1 = "hello word"
str2 = "我是xxxx\"lala\""

print(str1[4])

# 遍历字符串长度
for char in str2:
    print(char, end = " ")

print()
# 统计字符串长度
print("%s" % len(str1))

# 统计一个小字符出现的次数
print(str1.count("o"))

# 查找一小个字符串第一次出现的索引位置，注意：不存在的值执行会报错
print(str1.index("l"))


# ==== 字符串的判断方法 ====
str3 = "    \t\r\n"

# 判断是否是空白字符
print(str3.isspace())

# 判断是否只包含数字
num_str = "1"
print(num_str.isdecimal()) # 如果 string 只包含数字则返回 True，全角数字 (常用)
print(num_str.isnumeric()) # 如果 string 只包含数字则返回 True，全角数字、⑴、\u00b2 
print(num_str.isdigit())   # 如果 string 只包含数字则返回 True，全角数字，汉字数字

# ==== 字符串替换和查找 ====
hello_str = "hello world"

print("字符串是否以 hell 开头: %s" % hello_str.startswith("hell"))

print("字符串是否以 ld 结尾: %s" % hello_str.endswith("ld"))

# index方法，如果字符串不存在就报错。find方法，如果字符串不存在 就返回 -1
print("查找指定字符串索引位置：%s" % hello_str.find("llo"))

# 替换字符串 (注意：不会修改原有字符串内容)
print(hello_str.replace("world", "python"))
print(hello_str)

# ==== 文本对齐, 去除空白字符 ====
poem = ["\t登鹳雀楼",
        "王之涣",
        "白日依山尽\r\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    # print("|%s|" % poem_str.center(10, "　"))
    # print("|%s|" % poem_str.ljust(10, "　"))
    # strip 去除空白字符，rjust 向右对齐
    print("|%s|" % poem_str.strip().rjust(10, "　"))


# ==== 字符串拆分和拼接 =====
poem_str = "\t登鹳雀楼\t 王之涣\t 白日依山尽\r\n\t 黄河入海流\t 欲穷千里目\t 更上一层楼"

# 拆分字符串 (不传参使用任何空白字符进行拆分)
poem_list = poem_str.split()
print(poem_list)

# 合并字符串
result = " ".join(poem_list)
print(result)

