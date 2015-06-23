from base.BaseProtocol import BaseProtocol
from base.BaseFactory import BaseFactory
from base.OnlineClient import OnlineClient
from base.FactoryContainer import FactoryContainer
from flask import Flask, render_template
from twisted.internet import reactor
from txsockjs.factory import SockJSResource


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'

from flask.ext.twisted import Twisted

twisted = Twisted(app)

onlineClient = OnlineClient()


@app.route("/")
def hello():
    print '\n\n\n\n\n\n'
    print onlineClient.getClients()
    print '\n\n\n\n\n\n'
    return render_template('/client.html')


container = FactoryContainer().setOnlineClient(onlineClient)
container.buildFactory(EchoFactory, 'echo', Echo)


def main():
    twisted.add_resource("echo", SockJSResource(container.getFactory('echo')))
    reactor.listenTCP(8001, container.getFactory('echo'))

    app.run()  # this only runs if the module was *not* imported


if __name__ == '__main__':
    main()
