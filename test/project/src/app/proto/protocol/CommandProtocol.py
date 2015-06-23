# encoding=utf-8
import binascii
import json
from twisted.internet.protocol import Protocol
from app.proto.protocol.RFIDProtocol import RFIDProtocol
from twisted.internet import reactor
import functools


class CommandProtocol(Protocol):
    def __init__(self):
        self.ip = ''
        self.port = ''

    def connectionMade(self):

        #import socket
        #self.transport.socket._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      #在客户端连接上那一瞬间就会触发服务器,然后服务器开始循环发送数据

        self.ip = str(self.transport.client[0])
        self.port = str(self.transport.client[1])
        self.factory.numProtocols += 1

        print 'conn build From ip:' + self.ip + ' port:' + self.port
        print 'current conn num is ' + str(self.factory.numProtocols) + "\n"

        self.divName = self.ip + ":" + self.port + "##" + self.__class__.__name__
        self.factory.controller.add_client(self.divName, self.transport)

        # import threading
        # timer = threading.Timer(0, self.dataReceived, [""])
        # timer.start()

        return

    def connectionLost(self, reason):
        print 'conn lost reason --> ' + str(reason)
        self.factory.numProtocols -= 1

        print 'conn lost. ip:' + self.ip + ' port:' + self.port
        print 'current conn num is ' + str(self.factory.numProtocols) + "\n"
        self.factory.controller.del_client(self.divName)
        return

    def dataReceived(self, data):
        pass
        # print 'recv data from ip:' + self.ip + ' port:' + self.port + ' data:' + "\n" + binascii.b2a_hex(data)
        # kdiv = self.factory.controller.online_session
        # for div in kdiv:
        #     if div == self.divName:
        #         print "设备" + div + "正在把数据-->"
        # for div in kdiv:
        #     if div.split("##")[-1] == 'RFIDProtocol':
        #         print "FF FF F1 06 07 F0","扫描阅读器命令\n"
        #         frame = bytearray.fromhex("FF FF F1 06 07 F0")
        #         kdiv[div].write(frame)
        #         print "传递给:" + div
        # print "\n"

        #继续数据接受循环事件
        # import threading
        # timer = threading.Timer(0.5, self.dataReceived, [data])
        # timer.start()

        # cb = functools.partial(self.dataReceived, data=data)
        # reactor.callLater(0.5, cb)

        return
