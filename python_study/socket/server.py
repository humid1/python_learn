# 服务端
import socket, sys

# 创建 socket 对象
serversocket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名称
host = socket.gethostname()

port = 8888

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

# 建立客户端连接
while True :
    clientsocket, addr = serversocket.accept()
    print("连接地址: %s" % str(addr))
    msg = "欢迎访问 socket 服务" + "\r\n"
    clientsocket.send(msg.encode("utf-8"))
    clientsocket.close()