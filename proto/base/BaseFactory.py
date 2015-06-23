# encoding=utf-8
# 该类定义所有用到与工厂类相关的公共工厂类

# encoding=utf-8
from twisted.internet.protocol import Factory


class BaseFactory(Factory):
	def __init__(self,idName=None,protocol=None):
		self.idName = idName or 'idName'  # idName是一个标记
		self.clientNum = 0  # 在线客户端数量
		self.protocol = protocol  # 将协议传递给工厂
		self.onlineClient = None  # 工厂要拥有一个共同的在线客户端列表
		print self.idName + ' service listener is started!'
