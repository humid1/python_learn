gl_num_list = [1, 4, 2]

# 默认是升序排序
gl_num_list.sort()
print(gl_num_list)

# 降序排序
gl_num_list.sort(reverse = True)
print(gl_num_list)


def print_info(name, gender=True, title=""):
    """判断性别
    
    :param name: 姓名
    :param gender: True 男 False 女
    :param title: 职位
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s" % (name, title, gender_text))


print_info("小明")
print_info("小美", False)    
print_info("小鸣", False, "班长")