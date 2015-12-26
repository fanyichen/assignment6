from dealinterval import *
import unittest
from unittest import TestCase


class test6(TestCase):
	def test_dealinterval(self):#check if interval read correctly
		self.assertTrue(interval('[5,10]'),'[5,10]')

	def test_mergeInterval(self):#check if intervals merged correctly
		self.assertTrue(dealinterval.mergeInterval('(3,8)','[5,11)'),'(3,11)')

	def test_insert(self):#check whether a new interval can be merged or joined correctly
		self.assertTrue(dealinterval.insert(['[3,6)','(8,12)','[15,23]']),'[3,6)','(8,12)','[15,23]')
if __name__ == '__main__':
	unittest.main()