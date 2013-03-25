from tests import *
from meta import Sprocket


class TestMetaclass(unittest.TestCase):

	def test_metaclass_used(self):
		sprocket = Sprocket()
		assert hasattr(sprocket, 'name') == False
		assert hasattr(sprocket, 'NAME') == True
