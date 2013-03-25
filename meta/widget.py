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
		try:
			attr = self.__dict__[name]
			return inspect.ismethod(attr)
		except:
			return False
