from tests import *
from meta import Widget


class TestMethods(unittest.TestCase):

	def test_adding_instance_method(self):
		widget = Widget()
		with self.assertRaises(AttributeError):
			widget.new_method()

		widget.add_implode()
		assert widget.implode() == 'set to implode!'
