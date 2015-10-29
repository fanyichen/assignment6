from unittest import TestCase
from interval import *
from merge import *

class MergeIntervalTest(TestCase):
	#Check no unnecessary merges
	def test_no_merge(self):
		self.assertRaises(invalidMergeError,mergeIntervals, interval("[1,2]"),interval("[4,5]"))
	#Merge adjacent intervals
	def test_adjacent_merge(self):
		self.assertEqual(mergeIntervals(interval("[1,3]"),interval("[4,6]")), interval("[1,6]"))
	#Merge overlapping intervals
	def test_overlapping_merge_needed(self):
		self.assertEqual(mergeIntervals(interval("[1,5]"), interval("[3,6]")), interval("[1,6]"))

class MergeOverlappingTest(TestCase):
	#When no merges are needed
	def test_merge_no_intervals(self):
		self.assertEqual(mergeOverlapping([interval("[1,2]"), interval("[4,6]"), interval("[8,12]")]), [interval("[1,2]"), interval("[4,6]"), interval("[8,12]")])
	#When adjacent intervals need to be merged
	def test_merge_adjacent_intervals(self):
		self.assertEqual(mergeOverlapping([interval("[1,3]"), interval("[4,6]"), interval("[7,9]")]), [interval("[1,9]")])
	#When overlapping intervals need to be merged
	def test_merge_overlapping_intervals(self):
		self.assertEqual(mergeOverlapping([interval("[1,3]"), interval("[2,5]"), interval("[4,7]")]), [interval("[1,7]")])
	#When there are overlapping and adjacent intervals
	def test_merge_adjacent_and_overlapping(self):
		self.assertEqual(mergeOverlapping([interval("[1,3]"), interval("[2,5]"), interval("[6,7]")]), [interval("[1,7]")])
	#When there are multiple duplicate intervals
	def test_merge_duplicates(self):
		self.assertEqual(mergeOverlapping([interval("[1,3]"), interval("[1,3]"), interval("[1,3]")]), [interval("[1,3]")])

