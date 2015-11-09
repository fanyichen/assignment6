from unittest import TestCase
from interval import *
import unittest


class Test_Inertval_Module(TestCase): # test the functions in interval.py
    def setUp(self):
        pass
   
    def test_mergeIntervals(self): # test the function of mergeIntervals.
        intervals = []
        intervals.append(interval('(0,5)'))
        intervals.append(interval('[4,9)'))
        merged_intervals = mergeIntervals(intervals[0], intervals[1])
        self.assertEqual('(0,9)', str(merged_intervals.__repr__()))
               
    def test_mergeOverlapping(self): # test the function of mergeOverlapping
        intervals = []
        intervals.append(interval('(2,5)'))
        intervals.append(interval('[4,10)'))
        intervals.append(interval('(-10,0]'))
        self.assertEqual('[(-10,0], (2,10)]', str(mergeOverlapping(intervals)))

    def test_insert(self): # test the function of insert
        interval_list = []
        interval_list.append(interval('(2,5)'))
        interval_list.append(interval('[4,10)'))
        interval_list.append(interval('(-10,0]'))
        new_interval = interval('[-20,-14)')
        self.assertEqual('[[-20,-14), (-10,0], (2,10)]', str(insert(interval_list,new_interval)))

if __name__ == '__main__':
    unittest.main()