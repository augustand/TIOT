from twisted.internet.serialport import SerialPort
from txsockjs import factory

# setting
from config import config
from common.util import toFactory, toProtocol
# run in under twisted through wsgi
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from twisted.web.resource import Resource
# twisted required end

from common.ChildrenFirstResource import ChildrenFirstResource
from common.CommonContainer import CommonContainer

#resource = WSGIResource(reactor, reactor.getThreadPool())
#root = ChildrenFirstResource(resource)
root = Resource()

container = CommonContainer()
for dev in config.get('devConfig'):
    devName = dev.get('name')
    container.buildFactory(devName | toFactory, devName, devName | toProtocol)
    root.putChild(devName, factory.SockJSResource(container.factoryContainer[devName]))

site = Site(root)
reactor.listenTCP(config.get('webConfig').get('port'), site)
for dev in config.get('devConfig'):
    devName = dev.get('name')
    reactor.listenTCP(dev.get('port'), container.factoryContainer[devName])

import platform
for dev in config.get('serialConfig'):
    devName = dev.get('name')
    devProtocol = devName | toProtocol

    sysstr = platform.system()
    SerialPort(devProtocol(container.factoryContainer[devName + 'Listener']), dev.get('serialName').get(sysstr), reactor, baudrate=dev.get('baudrate'))
print 'reactor is running '
reactor.run()

# SerialPort(RFIDProtocol(container.servers['rfid_listener']),'COM11',reactor, baudrate=38400)#'/dev/ttyUSB0'
# reactor.listenTCP(9001, container.factoryContainer['xbee'])
# reactor.listenTCP(4001, container.factoryContainer['light'])
# reactor.listenTCP(9999, container.factoryContainer['rfid_listener'])
# reactor.listenTCP(8002, CommandRxFactory())
# SerialPort(USBClient(), '/dev/ttyUSB0', reactor, baudrate=38400)
# reactor.run()


# resource = resource.Resource()
# resource.putChild("kbee", SockJSResource(container.servers['kbee']))
# site = server.Site(resource)
#

# reactor.listenTCP(9000, container.servers['xbee'])
# reactor.listenTCP(9002, site)
#
# reactor.run()



# container.buildFactory(XBeeFactory, 'xbee', XBeeProtocol)
# root.putChild("xbee", factory.SockJSResource(container.factoryContainer['xbee']))
#
# container.buildFactory(LightFactory, 'light', LightProtocol)
# root.putChild("light", factory.SockJSResource(container.factoryContainer['light']))
#
#
# container.buildFactory(CommandFactory, 'rfid_listener', CommandProtocol)
# root.putChild("rfid_listener", factory.SockJSResource(
# container.factoryContainer['rfid_listener']))

# from factory.LightFactory import LightFactory
#
# from xbee.XBeeFactory import XBeeFactory
from app.proto.factory.RFIDFactory import RFIDFactory
# from factory.CommandFactory import CommandFactory
#
# from protocol.LightProtocol import LightProtocol
# from xbee.XBeeProtocol import XBeeProtocol
# from protocol.RFIDProtocol import RFIDProtocol
# from protocol.CommandProtocol import CommandProtocol
