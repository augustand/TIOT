from twisted.internet.serialport import SerialPort
from txsockjs import factory

from app.proto.common.ChildrenFirstResource import ChildrenFirstResource
from app.proto.common.Container import Container
from app.proto.factory.LightFactory import LightFactory

from app.proto.factory.XBeeFactory import XBeeFactory
# from app.proto.factory.RFIDFactory import RFIDFactory
from app.proto.factory.CommandFactory import CommandFactory
from app.proto.protocol.LightProtocol import LightProtocol

from app.proto.protocol.XBeeProtocol import XBeeProtocol
from app.proto.protocol.RFIDProtocol import RFIDProtocol
from app.proto.protocol.CommandProtocol import CommandProtocol

from app import app

# run in under twisted through wsgi
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
# twisted required end

container = Container()
resource = WSGIResource(reactor, reactor.getThreadPool(), app)
root = ChildrenFirstResource(resource)


container.buildFactory(XBeeFactory, 'xbee', XBeeProtocol)
root.putChild("xbee", factory.SockJSResource(container.servers['xbee']))

container.buildFactory(LightFactory, 'light', LightProtocol)
root.putChild("light", factory.SockJSResource(container.servers['light']))


container.buildFactory(CommandFactory, 'rfid_listener', CommandProtocol)
root.putChild("rfid_listener", factory.SockJSResource(
    container.servers['rfid_listener']))

site = Site(root)

reactor.listenTCP(5000, site)

reactor.listenTCP(9001, container.servers['xbee'])
reactor.listenTCP(4001, container.servers['light'])
reactor.listenTCP(9999, container.servers['rfid_listener'])
SerialPort(RFIDProtocol(container.servers[
           'rfid_listener']), '/dev/ttyUSB0', reactor, baudrate=38400)  # '/dev/ttyUSB0'

# SerialPort(RFIDProtocol(container.servers['rfid_listener']),'COM11',reactor,
# baudrate=38400)#'/dev/ttyUSB0'
print 'reactor is running '
reactor.run()

# reactor.listenTCP(8002, CommandRxFactory())
# SerialPort(USBClient(), '/dev/ttyUSB0', reactor, baudrate=38400)
# reactor.run()


# resource = resource.Resource()
# resource.putChild("kbee", SockJSResource(container.servers['kbee']))
# site = server.Site(resource)
#

# reactor.listenTCP(9000, container.servers['xbee'])
# reactor.listenTCP(9002, site)
# reactor.run()
