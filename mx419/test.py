"""this module contains unittest for the functions in the program"""
'''Author: Muhe Xie  ID:mx419'''

from unittest import TestCase
from interval import *
import unittest

#test the class and functions in the module interval.py
class Test_Inertval_Module(TestCase):

    def setUp(self):
        pass

    #test whether the class interval check the bound correctly
    def test_interval_bound_check(self):
        with self.assertRaises(Bound_Error):
            interval('[5, -4]')
        with self.assertRaises(Bound_Error):
            interval('(7, 8)')
        with self.assertRaises(Bound_Error):
            interval('(5, 6)')
 
    #   test whether the class read the interval correctly
    def test_interval_initialize(self):
        string1 = "( 6, 8 ]"
        string2 = '[9,11 ) '
        interval1 = interval(string1)
        interval2 = interval(string2)

        self.assertEqual(6,interval1.lower)
        self.assertEqual(8,interval1.upper)
        self.assertEqual('(',interval1.lower_bound_type)
        self.assertEqual(']',interval1.upper_bound_type)
        self.assertEqual('(6,8]',str(interval1.__repr__()))

        self.assertEqual(9,interval2.lower)
        self.assertEqual(11,interval2.upper)
        self.assertEqual('[',interval2.lower_bound_type)
        self.assertEqual(')',interval2.upper_bound_type)
        self.assertEqual('[9,11)',str(interval2.__repr__()))

    #   test whether the function merge two intervals correctly     
    def test_merge_intervals(self):
        interval_list = []
        interval_list.append(interval('(3,5)'))
        interval_list.append(interval('[5,9)'))
        interval_list.append(interval('(3,9)'))
        interval_list.append(interval('[4,10)'))
        interval_list.append(interval('(3,5)'))
        interval_list.append(interval('(5,9)'))

        merged_intervals1 = mergeIntervals(interval_list[0], interval_list[1])
        merged_intervals2 = mergeIntervals(interval_list[2], interval_list[3])
        

        self.assertEqual('(3,9)', str(merged_intervals1.__repr__()))
        self.assertEqual('(3,10)',str(merged_intervals2.__repr__()))
        with self.assertRaises(Not_Overlap_Error):
            merged_intervals3 = mergeIntervals(interval_list[4], interval_list[5])
            
        
    def test_mergeOverlapping(self):
        interval_list = []
        interval_list.append(interval('(3,5)'))
        interval_list.append(interval('[5,8)'))
        interval_list.append(interval('(-1,0]'))
        interval_list.append(interval('[4,12)'))
        interval_list.append(interval('(7,9)'))
        self.assertEqual('[(-1,0], (3,12)]',str(mergeOverlapping(interval_list)))
    


    def test_insert(self):
        interval_list = []
        interval_list.append(interval('(3,5)'))
        interval_list.append(interval('[5,8)'))
        interval_list.append(interval('(-1,0]'))
        interval_list.append(interval('[4,12)'))
        interval_list.append(interval('(7,9)'))
        newint = interval('[12,13)')
        self.assertEqual('[(-1,0], (3,13)]',str(insert(interval_list,newint)))


if __name__ == '__main__':
    unittest.main()