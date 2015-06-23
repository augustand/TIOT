# -*- coding: utf-8 -*-

# Flask
from flask import Flask
from base.OnlineClient import OnlineClient
from base.FactoryContainer import FactoryContainer

from EchoFactory import EchoFactory
from EchoProtocol import EchoProtocol
from ChildrenFirstResource import ChildrenFirstResource

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource


from txsockjs.factory import SockJSResource

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'


from flask.ext.twisted import Twisted
twisted = Twisted(app)


# onlineClient = OnlineClient()


@app.route("/")
def hello():
    # print onlineClient.getClients()
    return "Hello Twisted!"

container = FactoryContainer()
container.buildFactory(EchoFactory, 'echo', EchoProtocol)


# resource = WSGIResource(reactor, reactor.getThreadPool(), app)
# root = ChildrenFirstResource(resource)

# root.putChild("echo", SockJSResource(container.getFactory('echo')))
# site = Site(resource)

reactor.listenTCP(8001, container.getFactory('echo'))


# reactor.listenTCP(5000, site)
# reactor.listenTCP(8001, container.getFactory('echo'))

# Main
if __name__ == "__main__":
    reactor.run()
