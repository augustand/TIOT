# encoding=utf-8
import binascii

from pipe import Pipe

# 判断列表的值是否和集合的一样
@Pipe
def isList_set(kist):
    if isinstance(kist, list):
        return kist == list(set(kist))
    print "参数:列表"
    return

# print [1,2,3,1] | is_list_set#False
# print [1,2,3] | is_list_set #True
# print "www" | is_list_set


# python模块介绍 - binascii：二进制和ASCII互转以及其他进制转换

# 字符转ascll
# print binascii.b2a_hex('hello')#68656c6c6f
# ascll转字符
# print binascii.a2b_hex(binascii.b2a_hex('hello'))#hello


# 得到十六进制字符串
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
# print base #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


# 将十六进制字符串转化为十六进制比如"FFFFF10607F0"转化为'\xff\xff\xf1\x06\x07\xf0'
@Pipe
def hexStr_to_hex(hexStr):
    try:
        if isinstance(hexStr, list):
            hexStr = "".join(hexStr)

        byteStream = str(bytearray.fromhex(hexStr))
        return byteStream  # "FF FF F1 06 07 F0"
    except Exception, e:
        print "错误原因:"
        print e
        print "参数类型: FF FF F1 06 07 F0,FFFFF10607F0,[FF,FF,F1,06,07,F0]"


# "FFFFF10607F0" | hexStr_to_hex  #'\xff\xff\xf1\x06\x07\xf0'
# ['FF', 'FF', 'F1', '06', '07', 'F0'] | hexStr_to_hex
# {1:'FFFFF1060xxx7F0'} | hexStr_to_hex

@Pipe
def toHex(dec):
    hexStr = hex(dec)[2:]
    if len(hexStr) % 2 ==1:
        hexStr = '0'+hexStr
    return hexStr
# print 1234 | toHex #04d2
# 十进制转化为十六进制,输入格式为:十进制字符串

@Pipe
def dec_to_hexStr(decStr):
    try:
        num = decStr
        if type(num) == type('hello'):
            num = int(num)

        mid = []
        while True:
            num, rem = divmod(num, 16)
            mid.append(base[rem])
            if num == 0: break
        # print mid
        return ''.join([str(x) for x in mid[::-1]])
    except Exception, e:
        print "错误原因:"
        print e
        print "参数格式是: '16705445875445' "


# dh = "16705" | dec_to_hexStr  #4141
# print dh
# print 7525 | dec_to_hexStr


# 十六进制字符串转化为十进制列表
@Pipe
def hexStr_to_decList(hexStr):
    try:
        decList = []
        for i in range(1, len(hexStr), 2):
            decList.append(int(hexStr[i - 1:i + 1], 16))
        # print list
        return decList
    except Exception, e:
        print "错误原因:"
        print e
        print "参数格式: 'FFFFF2070884A1' "


# print 'FFFFF2070884A1' | hexStr_to_decList#[255, 255, 242, 7, 8, 132, 161]


# 十六进制字符串转化为十六进制列表
@Pipe
def hexStr_to_hexList(hexStr):
    try:
        decList = hexStr | hexStr_to_decList
        hexList = [hex(i) for i in decList]
        # print hexList
        return hexList
    except Exception, e:
        print "错误原因:"
        print e
        print "参数格式: 'FFFFF2070884A1' "


# print 'FFFFF2070884A1' | hexStr_to_hexList#['0xff', '0xff', '0xf2', '0x7', '0x8', '0x84', '0xa1']
# print "".join('FFFFF2070884A1' | strHex_to_listhex)#0xff0xff0xf20x70x80x840xa1


# print ischildof([1,2],list)
# print [].__class__.__name__#list
# for i in list.__bases__:
# print i
# if i is list or isinstance(i, list):
#         print "ok"
# ll = list
# print ll is list
# print [] is list
# print isinstance([],list)


@Pipe
def hexList_to_hexStrList(hexList):
    return [binascii.b2a_hex(x) for x in hexList]
# mm = ['\x03','\xf1']
# print mm | hexList_to_hexStrList #['03', 'f1']

@Pipe
def littleEndian(decList):  # 小段存储的设备id号转化为正常的id号,输入为十进制列表

    hexStr = ""
    if type(decList) == type([1, 2]) or decList.__class__.__name__ == "ListContainer":
        hex_strList = decList[::-1]
        for x in hex_strList:
            hexStr += x | toHex
    return hexStr

# print [12,34,1] | littleEndian


#hex_to_dec
# 十六进制 to 十进制:int(str,n=16)
@Pipe
def hexStr_to_dec(hexStr):
    return int(hexStr, 16)

# print "0e" | hexStr_to_dec


# 8位十六进制数转化为浮点数
@Pipe
def hex_to_float(hex_str):
    try:
        if len(hex_str) != 8:
            print "您输入的值不是8位"
            print hex_str
            return None
        else:
            import struct

            return struct.unpack('!f', hex_str.decode('hex'))[0]
    except Exception, e:
        print "错误原因:"
        print e
        print "参数错误"


# 字符串转字节串:
#
# 字符串编码为字节码: '12abc'.encode('ascii') == > b'12abc'
# 数字或字符数组: bytes([1, 2, ord('1'), ord('2')]) == > b'\x01\x0212'
# 16
# 进制字符串: bytes().fromhex('010210') == > b'\x01\x02\x10'
# 16
# 进制字符串: bytes(map(ord, '\x01\x02\x31\x32')) == > b'\x01\x0212'
# 16
# 进制数组: bytes([0x01, 0x02, 0x31, 0x32]) == > b'\x01\x0212'

#去除空格
def del_space(str):
    return str.replace(" ", "")


# print del_space("23 4343 fdfd   vdvd")


#crc16反模式数据校验算法
@Pipe
def crc_xmodel(hex_list):
    crc_value = 0
    polynomial = 0x1021
    for x in hex_list:
        for i in range(0, 8):
            bit = x >> (7 - i) & 1
            c15 = crc_value >> 15 & 1
            crc_value <<= 1
            if c15 ^ bit:
                crc_value ^= polynomial
                # print crc_value
    crc_value &= 0xffff
    return crc_value

    # print [0xFF, 0xFF, 0xF2, 0x07, 0x08, 0x84, 0xA1] | crc_xmodel()#ok
    #print 'FFFFF2070884A1' | hexStr_to_decList | crc_xmodel


    # list = ['10', '20', '30']
    # 将str数组转换为int数组
    # int_list = [int(i) for i in list]
    # 将int数组转换为16进制数组
    # hex_list = [hex(i) for i in int_list]
    #
    # print list
    # print int_list
    # print hex_list



    # 解包函数,得到处理后的数据包和未处理的数据


@Pipe
def parsePkgs(struct, bytestream):
    try:
        container = struct.parse(bytestream)
        return container.packets, container.leftovers
    except Exception, e:
        print "错误原因:"
        print e
        print "输入的参数1不是Struct"
        print "输入的参数2不是字节流"


# 将字符串的第一个字母转化为大写
@Pipe
def firstChar_toUpper(str):
    try:
        if len(str) == 1:
            return str.upper()
        return str[0].upper() + str[1:]
    except Exception, e:
        print '运行错误:'
        print e


# print 'hello' | firstChar_toUpper


# 将字符串转化为工厂类
@Pipe
def toFactory(str):
    try:
        if str.__contains__("Listener"):
            print str
            str = str.replace("Listener","")
        print str
        firstCharUpper = str | firstChar_toUpper

        str = str.lower()
        factoryModule = __import__(str + '.' +firstCharUpper + 'Factory')
        return eval('factoryModule.' + firstCharUpper + 'Factory.' +firstCharUpper + 'Factory')
    except Exception, e:
        print '运行错误:'
        print e

# 将字符串转化为协议类
@Pipe
def toProtocol(str):
    try:
        if str.__contains__("Listener"):
            str = str.replace("Listener", "")

        firstCharUpper = str | firstChar_toUpper
        str = str.lower()
        protocolModule = __import__(str + '.' + firstCharUpper + 'Protocol')
        return eval('protocolModule.' + firstCharUpper + 'Protocol.' + firstCharUpper + 'Protocol')
    except Exception,e:
        print '运行错误:'
        print e

@Pipe
def xor(order):
    try:
        m = 0
        data_list = []
        if type(order) == type([1,2]):
            data_list = order
        else:
            data_list = order.split(" ")

        for x in data_list:
            m ^= int(x,16)
        return m
    except Exception, e:
        print '运行错误:'
        print e
        print "输入格式为字符串'ff ff f1 f5' 或者[11,ff,22,f1,f2]"
