# encoding=utf-8
# 该类定义所有用到与工厂类相关的公共工厂类

# encoding=utf-8
from twisted.internet.protocol import Factory


class BaseFactory(Factory):
    def __init__(self, idName=None, protocol=None):
        self.idName = idName or 'idName'  #idName是一个标记
        self.numProtocols = 0  #协议设备在线连接数量
        self.protocol = protocol  #将协议传递给工厂
        self.commonController = None  #工厂要拥有一个共同的控制器来维护在线所有协议设备
        print self.idName + ' service listener is started!'
