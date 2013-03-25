from tests import *
from meta import Sprocket
from meta import SprocketMetaclass


class TestMetaclass(unittest.TestCase):

	def test_metaclass_applied(self):
		sprocket = Sprocket()
		assert hasattr(sprocket, 'name') == False
		assert hasattr(sprocket, 'NAME') == True

	def test_using_metaclass(self):
		# Use Metaclass for new class
		class Foo(object):
			__metaclass__ = SprocketMetaclass
			name = 'default'

		foo = Foo()
		assert hasattr(foo, 'name') == False
		assert hasattr(foo, 'NAME') == True
