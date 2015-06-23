# encoding=utf-8
import binascii
import json
from twisted.internet.protocol import Protocol
from common.CommonProtocol import CommonProtocol
from common.util import hexStr_to_hex
from light import LightFrames


class LightProtocol(CommonProtocol):
    def __init__(self):
       CommonProtocol.__init__(self)
    def dataReceived(self, data):
        devs = self.factory.commonController.onlineDevs

        if data in LightFrames.order.keys():
            for dev in devs:
                if dev == self.devName:
                    print "设备" + dev + "正在把数据:"

            data_hex = LightFrames.order.get(data)
            print data_hex
            data_hex = data_hex | hexStr_to_hex

            for dev in devs:
                if dev.split("##")[-1] == self.logPrefix():
                    devs[dev].write(data_hex)
                    print "传递给:" + dev
        else:
            print self.devName+"发送的指令码"+data+"不正确!"
        return
