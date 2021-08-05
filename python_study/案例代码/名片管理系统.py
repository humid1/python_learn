# 名片列表
dict_list = []

while True:
    # TODO(qjp) 显示系统菜单
    action = input("请选择操作功能:")
    print("您选择的操作是：%s" % action)
    if action in ["1", "2", "3"]:
        pass
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误，请重新输入！")


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
    # 提示用户输入信息
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入QQ:")
    email = input("请输入邮箱:")
    
    card_dict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }
    dict_list.


def show_all():
    """显示全部"""



def search_card():
    """搜索名片"""

