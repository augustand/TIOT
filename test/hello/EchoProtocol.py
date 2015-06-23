from base.BaseProtocol import BaseProtocol


class EchoProtocol(BaseProtocol):
	def __init__(self):
		BaseProtocol.__init__(self)

		"""This is just about the simplest possible protocol"""


	def dataReceived(self,data):
		"As soon as any data is received, write it back."
		print 'client:',data
		print self.transport.getPeer()
		print self.transport.client

		self.transport.write(data)
