# encoding=utf-8
# CommonController是为了维护在线列表设备中的各种协议
class CommonController(object):
    def __init__(self):
        self.onlineDevs = {}  #在线设备列表

    #添加客户端
    def addClient(self, devName, transport):
        self.onlineDevs[devName] = transport
        print "您现在的在线设备是:", self.onlineDevs
        print "\n\n"

    #删除客户端
    def delClient(self, devName):
        if devName in self.onlineDevs.keys():
            print "您要删除的设备是:" + devName
            self.onlineDevs.pop(devName)
        else:
            print "您要删除的设备不存在"
        print "您现在的在线设备是:", self.onlineDevs
        print "\n\n"
