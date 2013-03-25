import inspect

class ExtendedObject(object):

	def has_method(self, name):
		attrs = self.__dict__
		return inspect.ismethod(attrs.get(name, None))

	def responds_to(self, name):
		attrs = set( dir(self) )
		return name in attrs
