import re


class Interval:
	'''
valid input: an integer interval in standard interval form.  Can have open or closed parenthesis-() or [].  Left bound must be smaller than right bound.  A comma must seperate the left and right numbers. Those numbers must be integers.
If any of these criteria are not met a invalid interval error is thrown
	'''
	def isValidInput(self, testString):
		pattern = '^(\(|\[)(-?\d+),(-?\d+)(\)|\])$'
		match=re.search(pattern,testString)
		if match!=None:
			return True
		else:
			return False

	
	def findBounds(self, testString):
		'''
		sets isInclusive variables
		'''
		self.is_left_inclusive= testString[0]=="["
		self.is_right_inclusive =testString[-1]=="]"
		bounds= testString.split(",")
		self.leftBound = int(bounds[0][1:] )
		self.rightBound = int( bounds[1][:-1] )

	def testLeftRightBounds(self,intervalRepresentation):
		'''
		tests if left bound < right bound and sets true lower and upper bounds
		'''
		if self.realLeftBound > self.realRightBound :
			return False
		else :
			return True
		

	def setRealBounds(self):

		if not self.is_left_inclusive:
			self.realLeftBound=self.leftBound +1
		else :
			self.realLeftBound=self.leftBound
		if not self.is_right_inclusive:
			self.realRightBound=self.rightBound -1
		else :
			self.realRightBound=self.rightBound

	def __init__(self, inputRepresentation):
		
		self.stringRep=""
		self.is_valid_representation= False
		self.is_left_inclusive=True
		self.is_right_inclusive=True
		self.leftBound=None
		self.rightBound=None
		self.realLeftBound=None
		self.realRightBound=None

		self.stringRep=inputRepresentation
		self.rangeRepresentation=[]
		
		if self.isValidInput(inputRepresentation):
			self.findBounds(inputRepresentation)
			self.setRealBounds()
			self.testLeftRightBounds(inputRepresentation)
		else :
			raise Exception("Invalid Interval")
		if not self.testLeftRightBounds(inputRepresentation):
			raise Exception("Left bound must be smaller than right bound")
		
		
		

	def __repr__(self):
		return self.stringRep

