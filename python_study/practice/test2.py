# 测试自动发送QQ消息

import win32gui
import win32api
import win32con
import win32clipboard as w
import time

def send(name, msg):
    #打开剪贴板
    w.OpenClipboard()
    #清空剪贴板
    w.EmptyClipboard()
    #设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    #获取剪贴板内容
    date = w.GetClipboardData()
    #关闭剪贴板
    w.CloseClipboard()
    #获取qq窗口句柄
    handle = win32gui.FindWindow(None, name)
    if handle == 0:
        print('未找到窗口！')
    #显示窗口
    win32gui.ShowWindow(handle,win32con.SW_SHOW)
    # win32gui.ShowWindow(handle,win32con.SW_SHOWNORMAL)
    #把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(handle, win32con.WM_PASTE, 0, 0)
    #按下后松开回车键，发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(2)#延缓进程

def main():
    name = 'hdfx_聊天' #QQ聊天窗口的名字
    print('开始')
    for i in range(1,2):
    # send(name, '第'+str(i)+'次测试')
        send(name,'测试一下' + str(i))
    print('结束')

main()    