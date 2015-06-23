# encoding=utf-8
# from twisted.internet.protocol import Factory
from common.BaseFactory import BaseFactory
class RfidListenerFactory(BaseFactory):
    def __init__(self, quote=None, protocol=None):
        BaseFactory.__init__(self, quote, protocol)

