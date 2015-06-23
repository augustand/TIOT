# coding=utf-8
'''
#2015-1-28  created by wangke


###########################################################################################
'''
from construct import Struct, OptionalGreedyRange, Embed, Enum, Switch
from construct import UBInt8, UBInt16, UBInt32, UBInt64, Byte
from construct.macros import Array


rfid_frame = Struct("parser",
                    OptionalGreedyRange(
                        Struct("packets",
                               UBInt16("header"),
                               Enum(Byte("cmdcode"),
                                    F1=0xF1,
                                    F2=0xF2,
                                    F3=0xF3,
                                    F4=0xF4,
                               ),
                               Switch("data", lambda ctx: ctx.cmdcode,
                                      {


                                          "F1": Struct("sub", UBInt8("readerID"), UBInt8("plen"), UBInt8("status"),
                                                       Array(lambda ctx: (ctx.plen - 2 - 1 - 1 - 1 - 1 - 2) / 6,
                                                             Struct('block', Array(3, UBInt8('CardID')),
                                                                    UBInt8('triggerID'),
                                                                    Array(2, UBInt8('relativeTime'))))),

                                          # "F1": Struct("sub", UBInt8("readerID"), UBInt8("plen"), UBInt8("status"),
                                          #              Array(lambda ctx: (ctx.plen - 2 - 1 - 1 - 1 - 1 - 2) / 6,
                                          #                    Array(6, UBInt8('block'))), ),

                                          # "F1" : Struct("sub",UBInt8("readerID"),UBInt8("plen"),UBInt8("status"),Array(lambda ctx: (ctx.plen-2-1-1-1-1-2),UBInt8("block")),),
                                          "F2": Struct("sub", ),
                                          #"F3" : UBInt32("spam"),
                                          #"F4" : UBInt32("spam"),
                                      }
                               ),
                               UBInt16("crc"),
                        )
                    ),
                    OptionalGreedyRange(
                        UBInt8("leftovers"),
                    ),
)


