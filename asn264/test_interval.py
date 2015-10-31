from unittest import TestCase
from interval import *

int1 = interval("[4,9)")
int2 = interval("  [ 4 , 9  )  ")

#Ensure the interval object properly recognizes the correct bracket/parentheses and lower and upper bounds in standard format
class GoodIntervalTest(TestCase):
	def test_lower_inclusive(self):
		self.assertTrue(int1.lower_inc)
	def test_upper_inclusive(self):
		self.assertFalse(int1.upper_inc)
	def test_lower_bound(self):
		self.assertEqual(int1.lower, 4)
	def test_upper_bound(self):
		self.assertEqual(int1.upper, 9)


#Ensure the interval object properly recognizes the correct bracket/parentheses and lower and upper bounds when there are extra spaces
class GoodIntervalExtraSpacesTest(TestCase):
	def test_extra_spaces_lower_inclusive(self):
		self.assertTrue(int2.lower_inc)
	def test_extra_spaces_upper_inclusive(self):
		self.assertFalse(int2.upper_inc)
	def test_extra_spaces_lower_bound(self):
		self.assertEqual(int2.lower, 4)
	def test_extra_spaces_upper_bound(self):
		self.assertEqual(int2.upper, 9)


#Ensure that the interval class does not create illegal empty intervals for intervals of type [x,y], (x,y), and mixed brackets
class BadIntervalTest(TestCase):
	def test_both_exclusive(self):
		self.assertRaises(InvalidIntervalError, interval, "[4,2]")
	def test_both_inclusive(self):
		self.assertRaises(InvalidIntervalError, interval, "(2,2)")
	def test_mixed_exclusive_inclusive(self):
		self.assertRaises(InvalidIntervalError, interval, "[3,3)")


class BadFormatTest(TestCase):
	#Complain for extra brackets and parentheses
	def test_bad_format_extra_endpoints(self):
		self.assertRaises(InvalidIntervalError, interval, "[[2,4)")
	#Complain for not enough brackets and parentheses
	def test_bad_format_no_endpoints(self):
		self.assertRaises(InvalidIntervalError, interval, "3,4")
	#Complain for extra commas
	def test_bad_format_extra_commas(self):
		self.assertRaises(InvalidIntervalError, interval, "[4,,10]")
	#Complain for no commas
	def test_bad_format_no_commas(self):
		self.assertRaises(InvalidIntervalError, interval, "[4 10]")
	#Complain for non-integers values
	def test_bad_format_nonintegers(self):
		self.assertRaises(InvalidIntervalError, interval, "[5, twelve]")















