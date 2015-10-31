# test case

import unittest
from unittest import TestCase
import interval
from interval import mergeIntervals
from interval import mergeOverlapping
from interval import insert

"""test funcstion in interval.py"""

class interval_unittest(unittest.TestCase):

    def setUp(self):
        pass

    # merge interval test

    def test_mergeIntervals_1(self):
        a = interval.interval('[1,5]')
        b = interval.interval('[2,7]')
        c = interval.mergeIntervals(a,b)
        self.assertEqual(str(c), '[1,7]')

    def test_mergeIntervals_2(self):
        a = interval.interval('[1,2]')
        b = interval.interval('[3,4]')
        c = interval.mergeIntervals(a,b)
        self.assertEqual(str(c), '[1,4]')

    def test_mergeIntervals_3(self):
        a = interval.interval('[3,12)')
        b = interval.interval('[12,13)')
        c = interval.mergeIntervals(a,b)
        self.assertEqual(str(c), '[3,13)')

    def test_mergeIntervals_4(self):
        a = interval.interval('[1,2)')
        b = interval.interval('(2,4]')
        with self.assertRaises(ValueError) as cm:
            interval.mergeIntervals(a,b)
        the_exception = cm.exception
        self.assertEquals(str(the_exception), 'Disjoint intervals!')

    # mergeOverlapping test

    def test_mergeOverlapping_1(self):
        a = ['[1,2]', '[3,4]', '[5,6]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))
        b = interval.mergeOverlapping(lst)
        self.assertEqual(str(b), '[[1,6]]')

    def test_mergeOverlapping_2(self):
        a = ['[1,2)', '(2,4]', '(4,6]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))
        b = interval.mergeOverlapping(lst)
        self.assertEqual(str(b), '[[1,2), (2,6]]')

    def test_mergeOverlapping_3(self):
        a = ['[1,5)', '(2,4]', '[5,6]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))
        b = interval.mergeOverlapping(lst)
        self.assertEqual(str(b), '[[1,6]]')

    def test_mergeOverlapping_4(self):
        a = ['[1,5)', '(5,7]', '(7,10]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))
        b = interval.mergeOverlapping(lst)
        self.assertEqual(str(b), '[[1,5), (5,10]]')

    # insert test    

    def test_insert_1(self):
        a = ['[1,3]', '[6,9]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))   
        b = interval.interval('[2,5]')
        c = interval.insert(lst, b)
        self.assertEqual(str(c), '[[1,9]]')


    def test_insert_2(self):
        a = ['[1,2]', '(3,5)', '[6,7)', '(8,10]', '[12,16]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))   
        b = interval.interval('[4,9]')
        c = interval.insert(lst, b)
        self.assertEqual(str(c), '[[1,2], (3,10], [12,16]]')

    def test_insert_3(self):
        a = ['[1,3]', '[6,9]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))   
        b = interval.interval('[4,5]')
        c = interval.insert(lst, b)
        self.assertEqual(str(c), '[[1,9]]')

    def test_insert_3(self):
        a = ['[1,3]', '[6,9]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))   
        b = interval.interval('(4,5]')
        c = interval.insert(lst, b)
        self.assertEqual(str(c), '[[1,3], (4,9]]')

    def test_insert_4(self):
        a = ['[1,2)', '(2,9]']
        lst = []
        for item in a:
            lst.append(interval.interval(item))   
        b = interval.interval('(3,10]')
        c = interval.insert(lst, b)
        self.assertEqual(str(c), '[[1,2), (2,10]]')



if __name__ == '__main__':
    unittest.main()
