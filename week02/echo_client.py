# 客户端创建步骤：
# 创建一个socket
# 连接服务器 指定 服务器地址和端口号 (地址, 端口号) 注意是元组哦
# 开始收发数据 loop

import socket

client_sock = socket.socket()
client_sock.connect(('127.0.0.1', 8000))
# 发送个连接信息
client_sock.send('from 127.0.0.1'.encode('utf-8'))
while 1:
    print(client_sock.recv(1024).decode('utf-8'))
    # 有关输入的
    aa = input("echo >>:")
    if aa == 'exit':
        break
    while not aa:
        aa = input("echo >>:")
     # 重点就是上下两句
    client_sock.send(aa.encode('utf-8'))
client_sock.close()