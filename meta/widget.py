import types
import inspect

class Widget(object):

	def __init__(self):
		self.name = 'widget'
		super(Widget, self).__init__()

	@classmethod
	def add_spin(cls):
		def spin(cls):
			return 'class is spinning!'
		cls.spin = spin

	def add_implode(self):
		def implode(self):
			return 'set to implode!'
		self.implode = types.MethodType(implode, self)

	def has_method(self, name):
		attrs = self.__dict__
		return inspect.ismethod(attrs.get(name, None))

	def responds_to(self, name):
		attrs = self.__dict__
		return True if attrs.get(name, None) else False
