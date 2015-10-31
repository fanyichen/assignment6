from unittest import TestCase
from interval import *
from merge import *
from interact import *

class ParseForIntervalsTest(TestCase):
	#Test whether the function successfully parses a correctly formatted input string
	def test_successful_string_parse(self):
		self.assertEqual(parse_for_intervals("[1,3],[2,10],[25,30)"), [interval("[1,3]"), interval("[2,10]"), interval("[25,30)")])
	
