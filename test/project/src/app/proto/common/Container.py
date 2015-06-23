# encoding=utf-8
from Controller import Controller


class Container(object):

    def __init__(self):
        self.servers = {}
        self.conn = Controller()  # 添加的所有的设备共享同这个控制器，这样就让所有的设备之间通信有了可能

    def buildFactory(self, FactoryName, name, protocol):
        # init Protocol's Factory & build factory obj
        self.servers[name] = FactoryName(name, protocol)
        # add Controller obj to factory obj
        self.servers[name].controller = self.conn
