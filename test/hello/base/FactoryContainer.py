# encoding=utf-8
from base.OnlineClient import OnlineClient


class FactoryContainer(object):
	def __init__(self):
		self.container = {}
		self.client = OnlineClient()

	def setOnlineClient(self,onlineClient):
		self.client = onlineClient  # 让所有的工厂都来共享这个在线客户端列表，那么就能够让所有的客户端通信了
		return self

	def buildFactory(self,Factory,name,Protocol):
		# 初始化协议工厂
		self.container[name] = Factory(name,Protocol)
		# 向工厂中添加在线客户端对象
		self.container[name].onlineClient = self.client
		return self

	def getFactory(self,name):
		if name in self.container:
			return self.container.get(name)

		print name,'不存在'
		return None

	def getContainer(self):
		return self.container
