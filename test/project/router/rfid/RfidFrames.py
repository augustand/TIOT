# encoding=utf-8
'''
#2015-1-28  created by wangke


###########################################################################################
'''
from construct import Struct, OptionalGreedyRange, Embed, Enum, Switch
from construct import UBInt8, UBInt16, UBInt32, UBInt64, Byte
from construct.macros import Array

# 接收数据的数据格式定义
rfidFrame = Struct("frame",
                   OptionalGreedyRange(
                       Struct("packets",
                              UBInt16("header"),
                              Enum(Byte("flagID"),
                                   F1=0xF1,
                                   F2=0xF2,
                                   F3=0xF3,
                                   F4=0xF4,
                              ),
                              Switch("datas", lambda ctx: ctx.flagID, {
                                  "F1": Struct("sub", UBInt8("readerID"), UBInt8("len"), UBInt8("status"),
                                               Array(lambda ctx: (ctx.len - 2 - 1 - 1 - 1 - 1 - 2) / 6,
                                                     Struct('blocks', UBInt8('elec'), UBInt16('cardID'),
                                                            UBInt8('triggerID'),
                                                            UBInt16('relativeTime')))),
                                  "F2": Struct("sub", UBInt8("len"), UBInt8("readerID")),
                                  "F3": Struct("sub", UBInt8("len"), UBInt8("readerID"), UBInt8("result")),
                                  "F4": Struct("sub", UBInt8("len"), UBInt8("rssl")),
                              }
                              ),
                              UBInt16("crc"),
                       )
                   ),
                   OptionalGreedyRange(
                       UBInt8("leftovers"),
                   ),
)

# "F1": Struct("sub", UBInt8("readerID"), UBInt8("plen"), UBInt8("status"),
# Array(lambda ctx: (ctx.plen - 2 - 1 - 1 - 1 - 1 - 2) / 6,
# Array(6, UBInt8('block'))), ),

# "F1" : Struct("sub",UBInt8("readerID"),UBInt8("plen"),UBInt8("status"),Array(lambda ctx: (ctx.plen-2-1-1-1-1-2),UBInt8("block")),),
