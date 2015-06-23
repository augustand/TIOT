# encoding=utf-8
import binascii
from common.util import crc_xmodel, hexStr_to_decList,hexStr_to_hex
from RfidController import RfidController
from common.SerialProtocol import SerialProtocol
import functools
from twisted.internet import reactor


class RfidProtocol(SerialProtocol):
    def __init__(self, factory):
        SerialProtocol.__init__(self, factory)
        self.all_data = ""  #用来拼接接阅读器发送过来的的不完整的数据,因为阅读器发送过来的数据是不完整的
        self.controller = RfidController()
	

    # 定时器
    def ping(self,timeout):
        # do something
        frame = "FF FF F1 06 07 F0"
        #frame = RfidFrames.order.get('1')
        self.transport.write(frame | hexStr_to_hex)
        cb = functools.partial(self.ping, timeout=timeout)
        reactor.callLater(timeout, cb)

    def connectionMade(self):
        SerialProtocol.connectionMade(self)
        self.ping(timeout=1)
        return

    def dataReceived(self, data):

        self.all_data += binascii.b2a_hex(data)

        #bytestream = self.all_data | hexStr_to_hex  #"FF FF F1 07 0E 01 00 13 8E 88 00 04 00 47 "
        pkgs, leftovers = self.controller.parsePkgs(self.all_data)  #FF FF F1 06 07 F0

        if len(self.all_data) > 4:
            if self.all_data[0:4] != "ffff":
                self.all_data = "ffff" + self.all_data.split("ffff")[-1]

        if len(pkgs) != 0 and len(leftovers) == 0:
            if self.all_data | hexStr_to_decList | crc_xmodel != 0:
                self.all_data = ''
                return

            important_data = self.controller.data_p(pkgs)
            #print important_data
            if len(important_data) == 1:
                print "数据为空"
            else:
		devs = self.factory.commonController.onlineDevs
                for dev in devs:
                    if dev == self.devName:
                        print "设备" + dev + "正在把数据:"

                print important_data
                for dev in devs:
                    if dev.split("##")[-1] == self.logPrefix():
                        devs[dev].write(important_data)
                        print "传递给" + dev

            self.all_data = ""
        return

