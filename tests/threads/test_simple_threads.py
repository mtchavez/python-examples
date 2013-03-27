from tests import *
import sys
import StringIO

class TestSimpleThreads(unittest.TestCase):

	def test_simple(self):
		from threads import simple_threads
		old_stdout = sys.stdout
		capturer = StringIO.StringIO()
		sys.stdout = capturer
		simple_threads.simple()
		sys.stdout = old_stdout
		output = capturer.getvalue()
		for i in range(0,2):
			self.assertRegexpMatches(output, r'Thread %s' % i)
