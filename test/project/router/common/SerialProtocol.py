#encoding=utf-8
from twisted.internet import reactor
from twisted.internet.protocol import Protocol

class SerialProtocol(Protocol):

    def __init__(self, factory):
        self.factory = factory
        self.devName = "device##" + self.logPrefix()

    def connectionMade(self):
        self.factory.numProtocols += 1
        print "此设备" + self.devName + "连接成功"
        print '当前客户端的连接数量是:' + str(self.factory.numProtocols)
        self.factory.commonController.addClient(self.devName, self.transport)
        return

    def connectionFailed(self):
        print "Connection Failed:", self.logPrefix()
        reactor.stop()

    def connectionLost(self, reason):
        print "此设备" + self.devName + "连接失败"
        print '连接失败的原因是: '
        print reason
        self.factory.numProtocols -= 1
        print '当前的连接数量是:' + str(self.factory.numProtocols)
        self.factory.commonController.delClient(self.devName)
        return
