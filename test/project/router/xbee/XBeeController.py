# encoding=utf-8
import binascii

from XBeeFrames import xbeeFrame
from common.util import hex_to_float, parsePkgs, littleEndian, hexStr_to_hex
#########################################################
#1.Xbee.feed程序将自动各处转义前的数据包
############################################################################
#2.程序可以处理网络导致的拆分包问题，
########################################
#问题：不会处理粘包的问题,粘包时会取得最后一个包，
#级别：acceptable

class XBeeController():
    def parseData(self, data):
        pkgs = xbeeFrame | parsePkgs(data | hexStr_to_hex)
        # print pkgs[0][0]
        return self.getImportData(pkgs[0][0])

    def getImportData(self, pkgs):
        devName = []

        nodeid = pkgs.nodeid | littleEndian
        # print nodeid
        data_p = {}
        data_p["nodeid"] = nodeid
        for x in pkgs.datas:

            #tmp代表温度,hum代表湿度
            type = x.type | littleEndian
            floarValue = self.get_float(x.floatValue | littleEndian)
            if type == '0001':
                data_p["tmp"] = floarValue
            if type == '0002':
                data_p["hum"] = floarValue

        devName.append(data_p)
        # print dev_name
        return devName

    def get_float(self, str_hex):
        return str_hex | hex_to_float


if __name__ == '__main__':
    c = XBeeController()
    print c.parseData("7E001B201B006003021100035001010001006666A641020002001F85174244")
    # frame = bytearray.fromhex("7E001B201B006003021100035001010001006666A641020002001F85174244")
    # print c.parse_pkgs(frame)
    # print c.dev_id(c.parse_pkgs(frame)[0][0].nodeid)
    # for x in c.parse_pkgs(frame)[0][0].block[0].type:
    #     print x
    # print c.dev_id(c.parse_pkgs(frame)[0][0].block[0].type)


    #7E 00 1B 20 1B 00 60 03 02 11 00 03 50 01 01 00 01 00 66 66 A6 41 02 00 02 00 1F 85 17 42 44#7E001B201B006003021100035001010001006666A641020002001F85174244
    # frame_buff=c.getPackets(frame)
    # print frame_buff
    # print hex(frame_buff[0].dir)
    # print hex(frame_buff[0].nodeid)
    # print hex(frame_buff[0].funcid)
    #print hex(frame_buff[0].type)
    #print hex(frame_buff[0].unit)
    #print hex(frame_buff[0].value)
    # print hex(frame_buff[0].sum)
    #
    # print frame_buff[0].data[0]

