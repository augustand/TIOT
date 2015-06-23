from base.BaseFactory import BaseFactory


class EchoFactory(BaseFactory):
	def __init__(self,idName=None,protocol=None):
		BaseFactory.__init__(self,idName=None,protocol=None)
