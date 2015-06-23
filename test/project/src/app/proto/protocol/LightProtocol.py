# encoding=utf-8
import binascii
import json
from twisted.internet.protocol import Protocol

class LightProtocol(Protocol):
    def __init__(self):
        self.ip = ''
        self.port = ''

    def connectionMade(self):
        # import socket
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

        # print 'recv data from ip:' + self.ip + ' port:' + self.port + ' data:' + "\n" + data
        kdiv = self.factory.controller.online_session

        # data = str(data)
        data_hex = ''
	data_hex1 = ''
        if data == '1':
            data_hex = ' 7e 00 16 10 00 00 7d 33 a2 00 40 71 54 0a ff fe 00 00 01 00 00 01 00 00 00 00 2c'
            data_hex = str(bytearray.fromhex(data_hex))#无

	    data_hex1 = '7e 00 16 10 00 00 7d 33 a2 00 40 71 53 bc ff fe 00 00 01 00 00 01 00 00 00 00 7b'
	    data_hex1 = str(bytearray.fromhex(data_hex1))#风扇

            print data_hex
        elif data == '2':
            data_hex = ' 7e 00 16 10 00 00 7d 33 a2 00 40 71 54 0a ff fe 00 00 01 00 00 02 00 00 00 00 2b'
            data_hex = str(bytearray.fromhex(data_hex))#灯
            print data_hex


	    data_hex1 = '7e 00 16 10 00 00 7d 33 a2 00 40 71 53 bc ff fe 00 00 01 00 00 02 00 00 00 00 7a'
	    data_hex1 = str(bytearray.fromhex(data_hex1))#灯

        elif data == '3':
            data_hex = ' 7e 00 16 10 00 00 7d 33 a2 00 40 71 54 0a ff fe 00 00 01 00 00 03 00 00 00 00 2a'
            data_hex = str(bytearray.fromhex(data_hex))
            print data_hex



	    data_hex1 = '7e 00 16 10 00 00 7d 33 a2 00 40 71 53 bc ff fe 00 00 01 00 00 03 00 00 00 00 79'
	    data_hex1 = str(bytearray.fromhex(data_hex1))

        elif data == '0':
            data_hex = ' 7e 00 16 10 00 00 7d 33 a2 00 40 71 54 0a ff fe 00 00 01 00 00 00 00 00 00 00 2d'
            data_hex = str(bytearray.fromhex(data_hex))
            print data_hex

	    data_hex1 = '7e 00 16 10 00 00 7d 33 a2 00 40 71 53 bc ff fe 00 00 01 00 00 00 00 00 00 00 7c'
	    data_hex1 = str(bytearray.fromhex(data_hex1))

      
        for div in kdiv:
            if div == self.divName:
                print "设备" + div + "正在把数据-->"
        for div in kdiv:
            # print div.split("##")[-1]," ",self.__class__.__name__
            if div.split("##")[-1] == self.__class__.__name__:
                kdiv[div].write(data_hex)
		kdiv[div].write(data_hex1)
                print div
                print "传递给:" + div
        print "\n"
        return
