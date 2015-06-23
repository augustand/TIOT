# encoding=utf-8
import binascii
import json
from twisted.internet.protocol import Protocol
from common.CommonProtocol import CommonProtocol
class RfidListenerProtocol(CommonProtocol):
    def __init__(self):
        CommonProtocol.__init__(self)
