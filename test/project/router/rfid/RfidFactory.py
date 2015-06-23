# encoding=utf-8
# from twisted.internet.protocol import Factory
from common.BaseFactory import BaseFactory
class RfidFactory(BaseFactory):
    def __init__(self, idName=None, protocol=None):
        BaseFactory.__init__(self, idName, protocol)