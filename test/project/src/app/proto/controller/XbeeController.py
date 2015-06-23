#encoding=utf-8
import binascii
from app.proto.common.hachi.core import XBee
from app.proto.frames.xbeeFrames import xbee_frame

#########################################################
#1.Xbee.feed程序将自动各处转义前的数据包
############################################################################
#2.程序可以处理网络导致的拆分包问题，
########################################
#问题：不会处理粘包的问题,粘包时会取得最后一个包，
#级别：acceptable

from app.proto.common.data_parse import *
class XBeeController():

    def __init__(self, escaped=True):
        # self.xbee=XBee()
        pass
    def parse_pkgs(self,bytestream):
        '''
        未处理leftovers数据 todo
        '''
        container = xbee_frame.parse(bytestream)
        return container.packets, container.leftovers

        # Container({'type': [9, 0], 'value': [0, 0, 128, 63], 'unit': [18, 0]})

    def dev_id(self,dec_list):  # 小段存储的设备id号转化为正常的id号,输入为十进制列表

       # print dec_list.__class__.__name__
       if dec_list.__class__.__name__ == "ListContainer" :
            dec_list.reverse()
            strhex = ""
            for x in dec_list:
                # print x
                str_hex = dec_to_hex(str(x))
                if len(str_hex) == 1:
                    strhex += '0' + str_hex
                else:
                    strhex += str_hex
                    # print str_hex
       else:
            str_hex = dec_to_hex(dec_list)
            # print str_hex
            str_hex = [str_hex[i:i + 2] for i in range(0, len(str_hex), 2)]
            # print str_hex
            str_hex.reverse()
            # print str_hex
            strhex = "".join(str_hex)
            # print str_hex
       return strhex



    def getPackets(self, str_hex):
       '''
       解析包,得到整个包的数据
       :param str_hex:
       :return:
       '''
       frame = bytearray.fromhex(str_hex)
       # print frame
       # self.xbee.feed(frame)
       # print self.xbee
       pkgs,leftovers=self.parse_pkgs(frame)
       # print self.xbee.buffer
       # print pkgs
       self.pkgs = pkgs
       return self

    def get_import_data(self):
        div_name = []
        # print self.pkgs
        nodeid = self.dev_id(self.pkgs[0].nodeid)
        # print nodeid
        data_p = {}
        data_p["nodeid"] = nodeid
        for x in self.pkgs[0].block:

            ddd = self.dev_id(x.type)
            mmm = self.dev_id(x.value)
            if ddd == '0001':
                data_p["tmp"] = self.get_float(mmm)
            if ddd == '0002':
                data_p["hum"] = self.get_float(mmm)
            if ddd == '0009':
                data_p["hot"] = self.get_float(mmm)
		print data_p["nodeid"]
                print "vbghvghvggggggggggggggggggggggggggggggg\n\n\n\n\n\n\n"

            if ddd == '000e':
                data_p["smog"] = self.get_float(mmm)
                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"



            #tp代表温度,hd代表湿度
        div_name.append(data_p)
            # print div_name
        return div_name

    def parse_data(self,cnt):  # 解析数据,比如温度,湿度等等
        # print str_hex
        # str_hex = dec_to_hex(str_hex)
        # print str_hex
        # str_hex = str_hex[::-1]
        # print len(str_hex)
        # print str_hex+"0"
        # if len(cnt.type) < 4:
        #     str_hex =  + '0' * (16 - len(str_hex))
        # # print str_hex
        # str_hex = [str_hex[i + 1] + str_hex[i] for i in range(0, len(str_hex) - 1, 2)]
        # # print str_hex
        # str_hex1 = str_hex[6:8] + str_hex[4:6] + str_hex[:4]
        # # print str_hex1
        # str_hex1 = "".join(str_hex1)
        # # print str_hex1

        return

    # print parse_data("72058695267558977")

    def get_float(self,str_hex):
        return hex_to_float(str_hex)

if __name__ == '__main__':
    c=XBeeController()
    print c.getPackets("7E001B201B006003021100035001010001006666A641020002001F85174244").get_import_data()
    frame = bytearray.fromhex("7E001B201B006003021100035001010001006666A641020002001F85174244")
    print c.parse_pkgs(frame)
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

