import types
import lib

class Widget(lib.ExtendedObject):

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
