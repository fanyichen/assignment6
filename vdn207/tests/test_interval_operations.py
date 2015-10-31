'''Unit tests for functions working with intervals'''

from unittest import TestCase
import interval as inter 
from interval_operations import mergeIntervals, mergeOverlapping, insert
import custom_exceptions as cexcep

class IntervalOperationTests(TestCase):
	'''Defines the tests for different functions'''

	def setUp(self):
		self.int1 = inter.interval("[-10,-7]")
		self.int2 = inter.interval("(-4,1]")
		self.int3 = inter.interval("[3,13)")
		self.int4 = inter.interval("[15,24]")
		self.int5 = inter.interval("(-7,-2]")

	def test_correctness_of_mergeIntervals(self):
		merged_interval = mergeIntervals(self.int1, self.int5)
		self.assertIsNotNone(merged_interval)

	def test_exception_when_intervals_cannot_be_merged(self):
		self.assertRaises(cexcep.IntervalRangeException, mergeIntervals, self.int2, self.int3)

	def test_mergeOverlapping(self):
		list_of_intervals = mergeOverlapping([self.int1, self.int2, self.int3, self.int4, self.int5])
		self.assertEqual(len(list_of_intervals), 3)

	def test_insert(self):
		list_of_intervals = insert([self.int1, self.int2, self.int3, self.int4], self.int5)
		self.assertEqual(len(list_of_intervals), 3)