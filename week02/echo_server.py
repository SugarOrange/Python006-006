# 服务端创建步骤：
# 创建一个 socket 连接 参数默认不填就是 TCP 连接
# 绑定地址和端口号注意是一个元组(主机名/地址, 端口号)
# 准备监听连接 ，5表示可以接受客户端的连接数量，多余的会阻塞 不过这些多线程才有效
# 接受客户端连接
# 发送和接收数据 (loop: 注意收是成对的 服务端有接收，那么客户端对应的也有发送)

import socket

sock = socket.socket()  # 创建一个socket(family = AF_INET，type = SOCK_STREAM)
sock.bind(('127.0.0.1', 8000))  # 绑定地址端口号
sock.listen(5)  # 准备监听连接
while 1:
    client, addr = sock.accept()  # 阻塞接受客户端连接
    while 1:
        cr = client.recv(1024)  # 接收数据
        print(cr.decode('utf-8'))
        client.send('your addr is {}'.format(addr).encode('utf-8') + cr)  # 发送数据
    client.close()  # 连接关闭