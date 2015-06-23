#encoding=utf-8
import binascii
import functools
import json
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from app.proto.common.data_parse import dec_to_hex, hex_to_dec, CRC_XModem, strHex_toHex
from app.proto.controller.RFIDController import RFIDController

class RFIDProtocol(Protocol):

    def __init__(self, factory):
        self.factory = factory
        self.data_list = ""#用来拼接接阅读器发送过来的的不完整的数据
        self.rfid = RFIDController()
        self.kdiv = self.factory.controller.online_session

    def connectionMade(self):

        #import socket
        #self.transport.socket._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.factory.numProtocols += 1
        print 'current conn num is ' + str(self.factory.numProtocols) + "\n"

        self.divName = repr(self) + "##" + self.__class__.__name__
        self.factory.controller.add_client(self.divName, self.transport)

        # cb = functools.partial(self.dataReceived)
        # reactor.callLater(0.5, cb)
        self.ping(timeout=1)
        return


    def ping(self,timeout):
        # do something
        #frame = bytearray.fromhex("FF FF F1 06 07 F0")
        frame="\xFF\xFF\xF1\x06\x07\xF0"
        self.transport.write(frame)
        cb = functools.partial(self.ping, timeout=timeout)
        reactor.callLater(timeout, cb)

    def connectionFailed(self):
        print "Connection Failed:", self.__class__.__name__
        reactor.stop()

    def connectionLost(self, reason):
        print 'conn lost reason --> ' + str(reason)+"\n"
        self.factory.numProtocols -= 1

        print 'current conn num is ' + str(self.factory.numProtocols) + "\n"
        self.factory.controller.del_client(self.divName)
        return

    def dataReceived(self, data):
        # print binascii.b2a_hex(data)
        # xbeeController = XBeeController()
        # print 'recv data from' + self.divName + "\n" + binascii.b2a_hex(data)
        # print 'recv data from ip:' + self.ip + ' port:' + self.port + ' data:' + "\n" + binascii.b2a_hex(data)

        self.data_list += binascii.b2a_hex(data)
        # print self.data_list+"\n"

        frame = bytearray.fromhex(self.data_list)#"FF FF F1 07 0E 01 00 13 8E 88 00 04 00 47 "
        pkgs,leftovers= self.rfid.parse_pkgs(frame)#FF FF F1 06 07 F0
        # print self.rfid.parse_pkgs(frame)#FF FF F1 06 07 F0

        if len(self.data_list) >4:
            if self.data_list[0:4] != "ffff":
                self.data_list = "ffff"+self.data_list.split("ffff")[-1]

        if len(pkgs) != 0 and len(leftovers) == 0:
            # print self.data_list+"----------"
            # print pkgs

            if CRC_XModem(strHex_toHex(self.data_list)) != 0:
                self.data_list = ''
                return

            important_data = self.data_p(pkgs)
            #print important_data
            for div in self.kdiv:
                if div == self.divName:
                    print "设备" + div + "正在把数据-->"
            for div in self.kdiv:
                if div.split("##")[-1] == 'CommandProtocol':
                    # print self.data_list
                    # data = str(binascii.b2a_hex(data))
                    # data = xbeeFrames.parse_Packets(data)
                    # data = xbeeController.getPackets(
                    # "7E 00 1B 20 1B 00 60 03 02 11 00 03 50 01 01 00 01 00 66 66 A6 41 02 00 02 00 1F 85 17 42 44").get_import_data()
                    # print data
                    # str_data = json.dumps(data)
                    # print str_data
                    # triggerID = pkgs[0].CardID

                    # data = ""#处理卡号和触发器id
                    # important_data = ""
                    # for pkg in pkgs[0].data.block:
                    #     cardID = pkg.CardID
                    #     if cardID[0] != 0:
                    #         print cardID[0]
                    #     data += dec_to_hex(cardID[1])
                    #     data += dec_to_hex(cardID[2])
                    #
                    #
                    #     print hex_to_dec(data)
                        # print dec_to_hex(pkg.triggerID) == ""
                        # triggerID = str(pkg.triggerID)
                        # important_data += hex_to_dec(data)+":"+triggerID+","
                        # data = ""

                    # important_data = important_data[0:-1]+"\n"

                    if len(important_data) == 1:
                        print "数据为空\n"

                    # print type(important_data)
                    # print len(important_data)

                    if len(important_data) != 1:
						print important_data
						self.kdiv[div].write(important_data)
						print "传递给:" + div
                  #  important_data = ""

            else:
					print important_data

            print "\n"
            # print self.data_list
	    important_data = ""
            self.data_list = ""
        return


    def data_p(self,pkgs):

        data = ""  # 处理卡号和触发器id
        important_data = ""
        for pkg in pkgs[0].data.block:
            cardID = pkg.CardID
            if cardID[0] == 1:
                print dec_to_hex(cardID[1])+dec_to_hex(cardID[2]),"电量异常"
            data += dec_to_hex(cardID[1])
            data += dec_to_hex(cardID[2])

            triggerID = pkg.triggerID
            if triggerID != 0:
                important_data += hex_to_dec(data) + ":" + str(triggerID) + ","
            data = ""

        important_data = important_data[0:-1] + "\n"
        return important_data
