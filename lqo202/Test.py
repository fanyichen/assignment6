__author__ = 'lqo202'

import unittest as unittest
from unittest import TestCase
from assignment6 import loop
from Interval import interval

class AssignmentGeneralTest(TestCase):
    def testloop_possibleanswers(self):
        loop()

        #Listing for test
        listpositiveanswer = ['[2,3],[4,5]']
        listloopanswer = ['b','a']

        #Testing the lists
        for answer in listpositiveanswer:
            loop.yesnocallback=self.assertTrue
            raw_input([answer])

        for answer in listloopanswer:
            loop.yesnocallback=self.assertIsNotNone
            raw_input([answer])

if __name__ == '__main__':
    unittest.main()

