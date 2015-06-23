# encoding=utf-8
'''
#1.定义了7E开头的大网关数据包
##################################
#包含:
#包头        header  8bit
#包长度      len    16bit
#传输方向    dir     8bit
#节点ID      nodeID  64bit
#功能号      funcID  16bit
#数据块数组  datas    64bit *N
    #类型    type     16bit
    #单位    unit     16bit
    #浮点值  floatValue 32bit
#校验部分    crc     8bit 
#########################################################
#2.使用 OptionalGreedyRange可以使解包程序可以处理多个粘包
#########################################################
#3.leftovers存储不完整的包前部片段,frame里面的是完整的包信息和leftovers
#4凡是以小段存储的地方都转换为  Array(4, UbInt8("nodeID",1))的格式，为了以后方便转化
###########################################################################################
'''

from construct import Struct, OptionalGreedyRange, String
from construct import UBInt8, UBInt16
from construct.macros import Array


xbeeFrame = Struct("frame",
                   OptionalGreedyRange(
                       Struct("packets",
                              UBInt8("header"),
                              UBInt16("len"),
                              UBInt8("dir"),
                               Array(8, UBInt8("nodeid")),
                              UBInt16("funcid"),
                              Array(lambda ctx: (ctx.len - 1 - 8 - 2) / 8,
                                    Struct("datas", Array(2, UBInt8("type")), Array(2, UBInt8("unit")),
                                           Array(4, UBInt8("floatValue")), )),
                              UBInt8("crc"),
                       ), ),
                   OptionalGreedyRange(
                       UBInt8("leftovers"),
                   ),
)

# 7E 001B 20 1B00600302110003 5001 0100 0100 6666A641 0200 0200 1F851742 44