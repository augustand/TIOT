# encoding=utf-8
import functools
from twisted.internet import reactor
from common import util
from common.SuperConfig import SuperConfig
from common.util import hexStr_to_hex
from rfid import RfidFrames
from rfid.RfidFrames import rfidFrame


class RfidController:

    
    def data_p(self, pkgs):
        important_data = ""
        for pkg in pkgs[0].datas.blocks:

            cardID = str(pkg.cardID)
            if pkg.elec == 1:
                print cardID+ "电量异常"

            triggerID = str(pkg.triggerID)
            if triggerID != 0:
                important_data += cardID + ":" + triggerID + ","

        return important_data[0:-1]+"\n"

    # 解包函数,得到处理后的数据包和未处理的数据
    def parsePkgs(self, data):
        return rfidFrame | util.parsePkgs(data  | hexStr_to_hex)

    def getParseData(self, order):
        if order in self.cfg.items():
            return self.cfg.get(order) | hexStr_to_hex
        else:
            print "指令不存在"
            return 0

    def write(self, dev, data):
        data = eval(data)
        for x in data:
            if not x.get('devname'):
                if len(x.get('cname')) == 0:
                    pass
                else:
                    pass
            else:
                if len(x.get('cname')) == 0:
                    pass
                else:
                    pass
            pass
            pass
        pass

    # 打包函数
    def make_packet(packet, *args, **kwargs):
        print


if __name__ == '__main__':
    rfid = RfidController()
    # frame = bytearray.fromhex("FF FF F1 07 0E 01 00 13 8E 88 00 04 00 47")
    # print "FFFFF1070E0100138E0000F21D65" | util.hexStr_to_hex
    print rfid.parsePkgs("FFFFF1070E0100138E0000F21D65" | util.hexStr_to_hex)[0]
    # print rfid.cfg.get('readID')
    # frame = bytearray.fromhex("ff ff f1 07 44 0a 80 13 8e 00003f80139400003f 00138d00003f 00138f00003f00139a00003f00139c00003f00138a00003d00138c00003d00139900003d00139b0000066e32")
    # FF FF F1 07 26 05 00 13 9A 00 00 1D 80 13 8E 00 00 1D 00 13 8C 00 00 1D 00 13 8D 00 00 15 80 13 94 00 00 13 77 F9
    # pkgs,leftovers = rfid.parsePkgs(frame)
    # print pkgs
    #
    # data = ""
    # for pkg in pkgs[0].data.block:
    # for cardID in pkg.CardID:
    # data += dec_to_hex(cardID)
    #     print hex_to_dec(data)
    #     print dec_to_hex(pkg.triggerID) == ""
    #     data = ""

    # print pkgs
    # print pkgs[0].data.block[0].CardID
    # print pkgs[0].data.block[0].triggerID
    # print pkgs[0].data.block[1].CardID
    # print len(leftovers)

    # data = ""
    # for ii in pkgs[0].data.block[0].CardID:
    #     data += dec_to_hex(ii)

    # print data

    # sent_getReaderID = None
    # sent_scanReader = None
    # sent_getDoorForbValue = None
    # sent_setDoorForbValue = None
    #
    # 设置得到阅读器id的指令
    # def set_getReaderID(self,getReaderID_str_hex):
    #     self.sent_getReaderID = getReaderID_str_hex
    #     return self
    #
    # get_readerID
    # 得到阅读器id:get_readerID(receive_ReaderID)
    # def get_readerID(receive_ReaderID):
    #     return receive_ReaderID[8:10]
    #
    # 设置扫描电子标签的指令
    # def set_scanReader(self,scanReader_str_hex):
    #     self.sent_scanReader = scanReader_str_hex
    #     return self
    #
    # 设置得到门禁值的指令
    # def set_getDoorForbValue(self,getDoorForbValue_str_hex):
    #     self.sent_getDoorForbValue = getDoorForbValue_str_hex
    #     return self
    #
    # 设置设置门禁值的指令
    # def set_setDoorForbValue(self,setDoorForbValue_str_hex):
    #     self.sent_setDoorForbValue = setDoorForbValue_str_hex
    #     return self
    #
    # get_reader_status
    # 得到阅读器的状态
    # def get_reader_status(receive_scanReaderValue):
    #     return receive_scanReaderValue[10:12]
    #
    # get_three_values
    # 解析扫描阅读器后得到的，电子标签，低频触发器，卡片的相对时间
    # 返回的格式为[[str1,str2,str3]，[]，[]，[]]，其中str1是电子标签的ID，str2是低频触发器ID，str3是相对时间
    # def get_three_values(
    # receive_scanReaderValue):  # FF FF F1 07 0E 01            00 13 8E     00      00 F2           1D 65
    #     scan_values = receive_scanReaderValue[12:-4]
    #     values_list = []
    #     for x in range(0, len(scan_values), 12):
    #         values_list.append(scan_values[0 + x:12 + x])
    #         print values_list[x]
    #         return [[hex_to_dec(y[0:6]), hex_to_dec(y[6:8]), hex_to_dec(y[8:12])] for y in values_list]
    #
    # print get_three_values("FFFFF1070E0100138E0000F21D65")
    #
    # 得到门限值
    # def get_DoorForbValue(receive_DoorForbValue):
    #     return receive_DoorForbValue[8:10]
    #
    # set_DoorForbValue
    # def set_DoorForbValue(str_intDoorForbValue):
    #     return "FFFFF306" + str_intDoorForbValue + "校验结果"
    #
    # parse_setDoorForbResult
    # 解析设置门限的返回结果信息，如果结果得到的是AA,那么就是设置成功，如果是55，那么就是设置失败
    # def parse_setDoorForbResult(receive_setDoorForbResult):
    #     return receive_setDoorForbResult[8:10]
    #
    # get_instruct_code
    # 得到指令码：get_instruct_code("FFFFF205F7")
    # def get_instruct_code(str_instruct):
    #     return str_instruct[4:6]
    #
    # get_instruct_length
    # 得到指令长度:get_instruct_length("FFFFF205F7")
    # def get_instruct_length(str_instruct):
    # if (0 == cmp(str_instruct, receive_scanReaderValue)):
    # return str_instruct[8:10]
    # return str_instruct[6:8]
