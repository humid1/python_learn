# 客户端

# 导入 socket、sys 模块
import socket
import sys

# 获取本地主机名称
host = socket.gethostname()

port = 8888

if __name__ == '__main__':
    while True:
        str_msg = input("请输入要发送信息(输入 exit 退出循环)：")
        if "exit" == str_msg :
            break   
        elif str_msg != "":
            bytes_msg = bytes(str_msg, encoding = "gbk")
            # 创建 socket 对象
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 连接服务，指定主机和端口
            client.connect((host,port))
            # 发送数据
            client.send(bytes_msg)
            print(str(client.recv(8192),encoding="utf-8"))
            client.close()
        
