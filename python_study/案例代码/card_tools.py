# 名片列表
dict_list = []


def show_menu():
    """"显示菜单"""  
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新建名片"""
    print("-" * 50)
    print("功能：新建名片")
    
    # 1.提示用户输入信息
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入QQ:")
    email = input("请输入邮箱:")
    
    # 2.将用户信息保存到一个字典
    card_dict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }
    
    # 3.将用户字典添加到名片列表中
    dict_list.append(card_dict)
    print(dict_list)

    print("成功添加 %s 的名片" % name)



def show_all():
    """显示全部"""
    print("-" * 50)
    print("功能：新建名片")

    # 判断有无名片记录
    if len(dict_list) == 0:
        print("提示：无任何名片记录！")
        return

    # 打印表头
    for title in ["姓名", "电话", "QQ", "邮箱"]:
        print(title, end="\t\t")

    print()

    print("=" * 50)

    for dict in dict_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (dict["name"], dict["phone"], dict["qq"], dict["email"]))
    else:
        print("-" * 50)

def search_card():
    """搜索名片"""
    name = input("请输入要搜索的姓名：")
    for dict in dict_list:
        if dict["name"] == name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("%s\t\t%s\t\t%s\t\t%s" % (dict["name"], dict["phone"], dict["qq"], dict["email"]))
            print("-" * 50)
            deal_card(dict)
            break
    else:
        print("抱歉，没有找到姓名为: %s" % name)


def deal_card(find_dict):
    """操作搜索到的名片字典
    
    :param find_dict:找到的名片字典
    """
    print(find_dict)

    action_str = input("请选择要执行的操作: [1] 修改 [2] 删除 [0] 返回上一级")
    if action_str == "1":
        update_card(find_dict)
    elif action_str == "2":
        dict_list.remove(find_dict)
        print("删除成功！")
            

def update_card(find_dict):
    """ 更新某个字典名片信息

    :param find_dict:找到的名片字典
    """
    action_str = input("请选择要修改的操作: [1] 姓名 [2] 电话 [3] QQ [4] 邮箱 [0] 返回上一级")
    if action_str == "1":
        find_dict["name"] = input("请输入姓名:")
    elif action_str == "2":
        find_dict["phone"] = input("请输入电话:")
    elif action_str == "3":    
        find_dict["qq"] = input("请输入QQ:")
    elif action_str == "4":
        find_dict["email"] = input("请输入邮箱:")
    print("修改后的名片：%s" % find_dict)