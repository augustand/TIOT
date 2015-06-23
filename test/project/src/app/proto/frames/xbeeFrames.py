#encoding=utf-8
'''
#2014-12-19  created by wangke
##################################
#1.定义了7E开头的大网关数据包
##################################
#包含:
#包头        header  8bit
#包长度      plen    16bit
#传输方向    dir     8bit
#节点ID      nodeid  64bit
#功能号      funcid  16bit
#数据块数组  data    64bit *N
#校验部分    crc     8bit 
#########################################################
#2.使用 OptionalGreedyRange可以使解包程序可以处理多个粘包
#########################################################
#3.leftovers存储不完整的包前部片段

###########################################################################################
'''

from construct import Struct,OptionalGreedyRange,Embed
from construct import UBInt8,UBInt16,UBInt32,UBInt64
from construct.macros import  Array


xbee_frame = Struct("parser",
            OptionalGreedyRange(
                Struct("packets",
                  UBInt8("header"),
                  UBInt16("plen"),
                  UBInt8("dir"),
                  UBInt64("nodeid"),
                  UBInt16("funcid"),
                  #Array(lambda ctx: (ctx.plen-1-8-2)/8,Embed(block)),
#                  Array(lambda ctx: (ctx.plen-1-8-2)/8,UBInt64("data")),
                  Array(lambda ctx: (ctx.plen-1-8-2)/8,Struct("block",Array(2,UBInt8("type")),Array(2,UBInt8("unit")),Array(4,UBInt8("value")),)),
#Array(3, UBInt8('CardID'))
                  UBInt8("sum"),
                  ),),
            OptionalGreedyRange(
                  UBInt8("leftovers"),
            ),
        )
