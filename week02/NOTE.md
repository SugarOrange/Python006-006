### 学习笔记

###### 1、了解 OSI 参考模型

###### 		1.1了解 OSI 参考模型

​			著名的OSI协议参考模型,它是基于国际标准化组织ISO的建议发展起来的,从上到下共分为 7 层:应用层、表示层、会话层、传输层、网络层、数据链路层及物理层。这个 7 层的协议模型虽然规定得非常细致和完善,但在实际中却得不到广泛的应用,其重要的原因之一就在于它过于复杂。但它仍是此后很多协议模型的基础,这种分层架构的思想在很多领域都得到了广泛的应用。与此相区别的TCP/IP协议模型从一开始就遵循简单明确的设计思路,它将TCP/IP的 7层协议模型简化为 4 层,从而更有利于实现和使用。TCP/IP的协议参考模型和OSI协议参考模型的对应关系如下图所示。

![image-20201231161756147](C:\Users\cailei\AppData\Roaming\Typora\typora-user-images\image-20201231161756147.png)



###### 		1.2了解 TCP/IP 协议簇

​				由于OSI模型和协议比较复杂，所以并没有得到广泛的应用。而TCP/IP(transfer control protocol/internet protocol,传输控制协议/网际协议)模型因其开放性和易用性在实践中得到了广泛的应用，TCP/IP协议栈也成为互联网的主流协议。

TCP/IP模型是一系列网络协议的总称，这些协议的目的，就是使计算机之间可以进行信息交换。所谓”协议”可以理解成机器之间交谈的语言，每一种协议都有自己的目的。TCP/IP模型一共包括几百种协议，对互联网上交换信息的各个方面都做了规定。

这些协议可以大致分成四个层次，分别为连接层(Link Layer)、网络层(Internet Layer)、传输层(Transport Layer)、应用层(Application Layer)，上一层的协议都以下一层的协议为基础，数据传输的的过程如下图所示：



协议栈向下传递数据，并添加报头和报尾的过程称为`封装`，数据被封装并通过网络传输后，接收设备将删除添加的信息，并根据报头中的信息决定如何将数据沿协议栈上传给合适的应用程序，这个过程称为`解封装`。不同设备的对等层之间依靠封装和解封装来实现相互间的通信。

 

整个的因特网就是一个单一的、抽象的网络。IP地址就是给因特网上的每一个主机（或路由器）的每一个接口分配一个在全世界范围内唯一的32位的标识符。

###### 		1.3了解 Socket 的工作原理

   Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。

​    前人已经给我们做了好多的事了，网络间的通信也就简单了许多，但毕竟还是有挺多工作要做的。以前听到Socket编程，觉得它是比较高深的编程知识，但是只要弄清Socket编程的工作原理，神秘的面纱也就揭开了。
​    一个生活中的场景。你要打电话给一个朋友，先拨号，朋友听到电话铃声后提起电话，这时你和你的朋友就建立起了连接，就可以讲话了。等交流结束，挂断电话结束此次交谈。

![image-20201231162259258](C:\Users\cailei\AppData\Roaming\Typora\typora-user-images\image-20201231162259258.png)

###### 		1.4掌握基于 TCP 的 Socket 编程

​		\# TCP通信设计

\# 服务器端

```
# coding=utf-8
from socket import *
# 服务器端
# 创建服务器端套接字对象
serverSocket = socket(AF_INET,SOCK_STREAM)
# 绑定端口
serverSocket.bind(("", 5050))
# 监听
serverSocket.listen()
# 等待客户端的连接
clientSocket, clientInfo = serverSocket.accept()
# 多次通信
while True:
    # 接收客户端的消息
    receiveData = clientSocket.recv(1024)
    print("客户端说：{}".format(receiveData.decode("utf-8")))
    # 发送消息
    message = input(">>:")
    clientSocket.send(message.encode("utf-8"))
# 客户端
# coding=utf-8
from socket import *
# 客户端
# 创建客户端套接字对象
clientSocket = socket(AF_INET, SOCK_STREAM)
# 调用connect方法与服务器建立连接
clientSocket.connect(("127.0.0.1", 5050))
# 通信
while True:
    # 客户单发送消息
    message = input(">>:")
    clientSocket.send(message.encode("utf-8"))
    # 客户端接收消息
    receiveData = clientSocket.recv(1024)
    print("服务器端说：", receiveData.decode("utf-8"))
```



#### 2、requests 库与 HTTP 协议

​     熟悉 HTTP 协议

​	使用 requests 库进行 HTTP 请求： 

1. 发送请求 
2.  传递URL参数 
3.  定制请求头 
4. POST请求 
5. 响应状态 
6. cookie 
7.  请求超时处理 
8. 错误和异常处理



#### 3、用 requests 实现爬虫程序 并将数据存储至文件

1. 掌握requests库的
2. 使用 掌握with上下文管理器 
3. 掌握文件操作 
4. 掌握异常的捕获与处理



##### 4、用 requests 实现爬虫程序并将数据存储至文件

1. 用 requests 实现爬虫程序并将数据存储至文件 
2. 掌握 with 上下文管理器和文件路径处理 
3. 掌握异常的捕获与处理



##### 5、了解常用的前端知识

1. 了解常用的前端知识 HTML、
2. CSS 语法和样式控制 
3. 了解 JavaScript 基础 
4. 理解 jQuery 的 AJAX 如何请求后端数据做页面渲染



##### 6、使用 XPath 解析 HTML

1. 深入理解 HTML 
2. 掌握 XPath 的匹配规则



##### 7、使用 XPath 解析 HTML

1. 使用 XPath 解析 HTML 实战 
2. 模拟爬虫实现自动翻页功能 
3. 自顶向下设计：将爬虫代码拆解模拟 Scrapy 框架

#### 总结

1. 掌握 TCP、HTTP 协议 
2. 掌握 Socket 编程 
3. 掌握 requests 实现 HTTP 客户端 
4. 掌握文件操作 
5. 掌握异常处理