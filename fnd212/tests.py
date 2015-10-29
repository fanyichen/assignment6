from unittest import TestCase
from intervals import *
from assignment6 import add_input

class IntervalsTest(TestCase):


    def setUp(self):
        self.invalid_syntax = ['asdf','[]','[a,b]',10]
        self.invalid_intervals = ['[1,-10]','(1,1)']
        self.valid_intervals = ['[1,1]','(1,5)','[100,200]','(-10,0)','(-1,1)']
        self.reduced_valid_intervals = [intervalInt('[-9,4]'),intervalInt('[100,200]')]

    def test_syntax(self):
    	for interval_instance in self.invalid_syntax:
    		with self.assertRaises(MalformedInterval):
    			intervalInt(interval_instance)

    def test_intervals(self):
    	for interval_instance in self.invalid_intervals:
    		with self.assertRaises(InvalidInterval):
    			intervalInt(interval_instance)

    	# Check that valid intervals do not raises exceptions:
    	for interval_instance in self.valid_intervals:
    		intervalInt(interval_instance)

    def test_walk(self):
    	interval_list = []
    	
    	for interval_instance in self.invalid_syntax:
    		with self.assertRaises(MalformedInterval):
    			interval_list = add_input(interval_list,interval_instance)

    	for interval_instance in self.invalid_intervals:
    		with self.assertRaises(InvalidInterval):
    			interval_list = add_input(interval_list,interval_instance)

    	for interval_instance in self.valid_intervals:
    		interval_list = add_input(interval_list, interval_instance)
    	print interval_list
    	self.assertEqual(interval_list,self.reduced_valid_intervals)
    	