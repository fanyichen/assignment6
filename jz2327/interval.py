import numpy as np
import string
import userExceptions
from userExceptions import interval_bad_leftbound, interval_bad_rightbound, interval_bad_invalidbound, interval_bad_zero, interval_bad_nocomma

class interval():
"""create a class to understand the real interval and print the right format"""

	def __init__(self,intervalInput):

		self.intervalInput = intervalInput
		self.realIntervalInput = []

		#check the leftside of interval is correct
		self.leftBound = intervalInput[0]
		if self.leftBound != '[' and self.leftBound != '(': 
			raise interval_bad_leftbound()

		#check the rightside of interval is correct
		self.rightBound = intervalInput[-1]
		if self.rightBound != ']' and self.rightBound != ')':
			raise interval_bad_rightbound()

		#check the interval contains a comma
		self.commaPosition = intervalInput.find(',')		
		if self.commaPosition == -1:
			raise interval_bad_nocomma()

		self.lowerBound = (intervalInput[1 : intervalInput.find(',')])
		self.upperBound = (intervalInput[intervalInput.find(',')+1 : -1])
		self.reallowerBound = 0
		self.realUpperBound = 0
		
		#check the lower and upper bound is valid integer
		try:
			int(self.lowerBound)
			int(self.upperBound) 
		except:
			raise interval_bad_invalidbound()

		#check the length of interval > 0 
		if (self.realLower()) > (self.realUpper()):
			raise interval_bad_zero()

	def realLower(self):
	'''get the real lower bound of the interval'''
		if self.leftBound == '[':
			self.realLowerBound = int(self.lowerBound)
			return self.realLowerBound
		elif self.leftBound == '(':
			self.realLowerBound = int(self.lowerBound) + 1
			return self.realLowerBound

	def realUpper(self):
		'''get the real upper bound of the interval'''
		if self.rightBound == ']':
			self.realUpperBound = int(self.upperBound) 
			return self.realUpperBound
		elif self.rightBound == ')':
			self.realUpperBound = int(self.upperBound) -1
			return self.realUpperBound

	def realInterval(self):
		'''get the real interval'''
		self.realIntervalInput = np.arange(self.realLower(), self.realUpper()+1)
		return self.realIntervalInput

	def __repr__(self):
		'''print the right format for the interval'''
		return '%s%d,%d%s' % (self.leftBound, int(self.lowerBound), int(self.upperBound), self.rightBound)

