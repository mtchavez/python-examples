from tests import *
import types


class TestMethods(unittest.TestCase):

	def test_adding_instance_method(self):
		widget = Widget()
		with self.assertRaises(AttributeError):
			widget.new_method()

		def implode(self):
			return 'set to implode!'
		widget.implode = types.MethodType(implode, widget)

		assert widget.implode() == 'set to implode!'
