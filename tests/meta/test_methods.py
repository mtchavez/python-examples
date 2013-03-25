from tests import *
from meta import Widget


class TestMethods(unittest.TestCase):

	def setup_method(self, method):
		self.widget = Widget()

	def test_adding_instance_method(self):
		with self.assertRaises(AttributeError):
			self.widget.new_method()

		self.widget.add_implode()
		assert self.widget.implode() == 'set to implode!'


	def test_adding_class_method(self):
		with self.assertRaises(AttributeError):
			Widget().spin()

		Widget().add_spin()
		assert Widget().spin() == 'class is spinning!'
