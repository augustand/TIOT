#encoding=utf-8
from twisted.web.resource import Resource

#该类为了实现让串口转化为网口,简单来说就是能够让从设备发送过来的数据能够让浏览器前端接收到
class ChildrenFirstResource(Resource):
    """
    A resource that delegates to statically registered children before
    giving up and delegating to a given leaf resource.
    """
    def __init__(self, leaf):
        Resource.__init__(self)
        self.leaf = leaf

    def getChild(self, child, request):
        """
        Reconstructs the request's postpath and prepath as if this
        resource wasn't there, then delegates to the leaf.
        This gets called when ``getChildWithDefault`` failed, i.e. we're
        handing it over to the leaf.

        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        root = ChildrenFirstResource(resource)
        root.putChild("xbee", factory.SockJSResource(container.servers['xbee']))

        """
        request.postpath.insert(0, request.prepath.pop())
        return self.leaf


    def render(self, request):
        """
        Delegates the requests to the leaf.
        """
        return self.leaf.render(request)
