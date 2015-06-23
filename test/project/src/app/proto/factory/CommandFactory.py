# encoding=utf-8
from twisted.internet.protocol import Factory


class CommandFactory(Factory):
    protocol = None

    def __init__(self, quote=None, protocol=None):
        self.quote = quote or 'An apple a day keeps the doctor away!'
        self.numProtocols = 0
        self.conn = None
        self.protocol = protocol
        self.controller = None
        print self.quote + ' service listener is started!'

    def get_message(self, name, message):
        print name, message

    def message_sibling(self, message):
        self.root.message_child(self.name, message)
