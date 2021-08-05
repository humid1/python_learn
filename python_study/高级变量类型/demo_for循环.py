for num in [1, 2, 3]:
    print(num)
    if num == 1:
        break
else:
    # 使用了break，else内的代码不会执行
    print("执行？")

print("循环结束！")    


students = [
    {"name": "阿兰"},
    {"name": "阿紫"}
]
# 搜索指定姓名
find_name = "小明"
for student in students:
    print(student)
    if find_name == student["name"]:
        print("找到了 %s" % find_name)
        break
else:
    print("抱歉没有找到！%s" % find_name)

print("循环结束！")        