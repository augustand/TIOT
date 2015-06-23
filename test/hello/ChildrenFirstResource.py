from twisted.web import wsgi, resource
class ChildrenFirstResource(resource.Resource):
    """
    A resource that delegates to statically registered children before
    giving up and delegating to a given leaf resource.
    """
    def __init__(self, leaf):
        resource.Resource.__init__(self)
        self.leaf = leaf


    def getChild(self, child, request):
        """
        Reconstructs the request's postpath and prepath as if this
        resource wasn't there, then delegates to the leaf.
        This gets called when ``getChildWithDefault`` failed, i.e. we're
        handing it over to the leaf.
        """
        request.postpath.insert(0, request.prepath.pop())
        return self.leaf


    def render(self, request):
        """
        Delegates the requests to the leaf.
        """
        return self.leaf.render(request)
