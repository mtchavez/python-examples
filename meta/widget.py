import types


class Widget(object):
	"""Test class to use"""
	def __init__(self):
		super(Widget, self).__init__()

	def add_implode(self):
		def implode(self):
			return 'set to implode!'
		self.implode = types.MethodType(implode, self)

	@classmethod
	def add_spin(cls):
		def spin(cls):
			return 'class is spinning!'
		cls.spin = spin
