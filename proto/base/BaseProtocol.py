# encoding=utf-8
from twisted.internet.protocol import Protocol

# 公共协议实现了其子协议大部分的工作,让那些子协议不需要花费他爱多的工作在这方面


class BaseProtocol(Protocol):
	def __init__(self):
		self.name = ''

	def onConnection(self):
		pass

	def connectionMade(self):
		import socket
		self.transport.socket._sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		# 在客户端连接上那一瞬间就会触发服务器,然后服务器开始循环发送数据

		self.name = str(self.transport.client[0]) + ":" + str(self.transport.client[1]) + "##" + self.logPrefix()
		print self.name

		self.factory.onlineClient.addClient(self.name,self)
		self.factory.clientNum += 1
		print '当前客户端数量为:',self.factory.clientNum
		self.onConnection()

		return

	def onDisConnection(self):
		pass

	def connectionLost(self,reason):
		print "客户端" + self.name + "连接中断"
		print '原因是: '
		print reason

		self.factory.onlineClient.delClient(self.name)
		self.factory.clientNum -= 1
		print '当前客户端的连接数量是:',self.factory.clientNum
		self.onDisConnection()

		return
