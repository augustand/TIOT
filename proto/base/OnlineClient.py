# -*- coding: utf-8 -*-

# 客户端在线模块，用来保存客户端在线的状态


class OnlineClient(object):
	def __init__(self):
		self.__clients = {}  # 在线客户端

	# 传入一个字典类型的配置文件
	def setConfig(self,config_dict):
		self.config = config_dict
		return self

	def getClient(self,name):
		if name in self.__clients:
			return self.__clients.get(name)
		print name,"不存在"
		return None

	def addClient(self,name,protocol):
		self.__clients[name] = protocol
		print "现在的在线客户端为:"
		print self.__clients
		return self

	def delClient(self,name):
		if name in self.__clients:
			del self.__clients[name]
		else:
			print name,"不存在"
		print "现在的在线客户端为:"
		print self.__clients
		return self

	def getClients(self):
		return self.__clients
