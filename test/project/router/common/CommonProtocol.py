# encoding=utf-8
from twisted.internet.protocol import Protocol

# 公共协议实现了其子协议大部分的工作,让那些子协议不需要花费他爱多的工作在这方面


class BaseProtocol(Protocol):

    def __init__(self):
        self.ip = str(self.transport.client[0])
        self.port = str(self.transport.client[1])
        self.devName = self.ip + ":" + self.port + "##" + self.logPrefix()
        self.devID = self.ip + ":" + self.port

    def connectionMade(self):
        # import socket
        # self.transport.socket._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 在客户端连接上那一瞬间就会触发服务器,然后服务器开始循环发送数据

        self.factory.numProtocols += 1
        print "此次客户端" + self.devID + "连接成功"
        print '当前客户端的连接数量是:' + str(self.factory.numProtocols)
        self.factory.commonController.addClient(self.devName, self.transport)
        return

    def connectionLost(self, reason):
        print "此次客户端" + self.devID + "连接失败"
        print '连接失败的原因是: '
        print reason
        self.factory.numProtocols -= 1
        print '当前客户端的连接数量是:' + str(self.factory.numProtocols)
        self.factory.commonController.delClient(self.devName)
        return
