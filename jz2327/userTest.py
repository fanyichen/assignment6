import dealWithInterval
import unittest
from unittest import TestCase
from interval import interval
from userExceptions import interval_bad_leftbound, interval_bad_rightbound, interval_bad_invalidbound, interval_bad_zero, interval_bad_nocomma, merge_bad

class assignment6_test(TestCase):

	#test when interval is valid
	def test_class_interval_isvalid(self):
		self.assertTrue(interval('[5,10]'), '[5,10]')

	#test when interval's left bound is not valid
	def test_class_interval_leftbound_isinvalid(self):
		self.assertRaises(interval_bad_leftbound, lambda: interval('$5,10]'))

	#test when interval's right bound is not valid
	def test_class_interval_rightbound_isinvalid(self):
		self.assertRaises(interval_bad_rightbound, lambda: interval('(5,10t'))

	#test when interval's comma is missing
	def test_class_interval_no_comma(self):
		self.assertRaises(interval_bad_nocomma, lambda: interval('[5@10]'))

	#test when interval's lower/upper bound is not valid
	def test_class_interval_bound_isinvalid(self):
		self.assertRaises(interval_bad_invalidbound, lambda: interval('[lower,10]'))

	#test when interval's length is zero
	def test_class_interval_iszero(self):
		self.assertRaises(interval_bad_zero, lambda: interval('[10,5]'))

	#test two overlapping intervals merge successfully
	def test_mergeIntervals_merge_success_overlap(self):
		self.assertTrue(dealWithInterval.mergeIntervals('(3,8]','[5,11)'), '(3,11)')

	#test two adjacent intervals merge successfully
	def test_mergeIntervals_merge_success_adjacent(self):
		self.assertTrue(dealWithInterval.mergeIntervals('(3,6]','[7,11)'), '(3,11)')

	#test two non-overlapping or non-adjacent intervals merge failed
	def test_mergeIntervals_merge_fail(self):
		self.assertRaises(merge_bad, lambda: dealWithInterval.mergeIntervals('(3,5]','[8,11)'))

	#test a list of intervals can get intervals merged as designed
	def test_mergeOverLapping_success(self):
		self.assertTrue(dealWithInterval.mergeOverLapping(['(8,12)', '[15,23]', '[3,6)', '[-10,-7]', '(-4,1]']),['[-10,-7]', '(-4,1]', '[3,12)', '[15,24]'])

	#test a new interval can be merged or joined in the list of other intervals
	def test_insert_success(self):
		self.assertTrue(dealWithInterval.insert(['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]'],'[4,8]'),['[-10,-7]', '(-4,1]', '[3,12)', '[15,23]'])


if __name__ == '__main__':
	unittest.main()