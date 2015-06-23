#encoding=utf-8

from .base.BaseFactory import BaseFactory
from .base.BaseProtocol import BaseProtocol
from .base.FactoryContainer import FactoryContainer
from .base.OnlineClient import OnlineClient

# 实例化一个工厂容器，用来构建工厂
factoryContainer=FactoryContainer()

# 实例化一个客户端在线列表
onlineClient=OnlineClient()
