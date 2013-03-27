from tests import *
from threads import naming_threads
import sys
import StringIO

class TestNamingThreads(unittest.TestCase):

  	def test_default_naming(self):
  		old_stdout = sys.stdout
  		capturer = StringIO.StringIO()
  		sys.stdout = capturer
  		naming_threads.naming()
  		sys.stdout = old_stdout
  		output = capturer.getvalue()
  		self.assertRegexpMatches(output, r'Thread-1')

	def test_adding_name(self):
		old_stdout = sys.stdout
  		capturer = StringIO.StringIO()
  		sys.stdout = capturer
  		naming_threads.naming('RAWR')
  		sys.stdout = old_stdout
  		output = capturer.getvalue()
  		self.assertRegexpMatches(output, r'RAWR')
