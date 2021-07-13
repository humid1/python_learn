# 测试自动发送QQ消息

import win32gui
import win32api
import win32con
import win32clipboard as w
import time

#发送的消息
msg = "测试一下2"
# 将测试消息复制到剪切板中
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
w.CloseClipboard()

# 窗口名字
name = "hdfx_聊天"
# 获取窗口句柄
handle = win32gui.FindWindow(None, name)
print(handle)

# 窗体前端显示
win32gui.ShowWindow(handle, 1)
#填充消息
win32gui.SendMessage(handle, 770, 0, 0)
#回车发送消息
win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
