"""Class that creates an interval of integers. Takes a string representation of an interval of integers and ensures that the string conforms to the following interval requirements: 
(1) contains inclusive brackets [] and/or exclusive brackets, 
(2) contains a delimiter that separates the lower bound integer from the upper bound integer, 
(3) contains a lower bound integer and an upper bound integer, and 
(4) the lower bound integer is smaller than or equal to the upper bound integer."""

from errorHandling import InvalidIntervalError

class Interval:
	# Set the delimiter here. The delimiter separates the lower bound integer from the upper bound integer.
	validDelimiter = ","	

	# Values of the Interval object
	lowerBracketIsExclusive = True	# True when lower bracket is "(" and False when lower bracket is "["	
	upperBracketIsExclusive = True	# True when upper bracket is ")" and False when lower bracket is "]"	
	delimiter = None	
	lowerBound = None
	upperBound = None
	
	def __init__(self, interval):
		self.interval = interval
		
		# If the interval is empty, an error is raised.
		if len(interval) == 0: raise InvalidIntervalError('Empty String \n')
		
		# Checks bracket validity. If valid, the bracket value is updated. If invalid, an error is raised.
		if self.__hasValidBrackets(interval):
			self.__updateExclusivityOfBrackets(interval)			
		else:
			raise InvalidIntervalError('Brackets are INVALID \n')
		
		# Checks delimiter validity. If valid, the delimiter value is updated. If invalid, an error is raised.
		if self.__hasDelimiter(interval):
			self.delimiter = self.validDelimiter
		else:
			raise InvalidIntervalError('Delimiter is missing or INVALID. \n')

		# Checks the validity of the integer bounds. If valid, the upperBound and lowerBound values are updated. 
		# If invalid, an error is raised.
		if self.__hasValidBounds(interval[1:-1]):
			self.lowerBound = int(interval[1:-1].split(self.validDelimiter, 1)[0])
			self.upperBound = int(interval[1:-1].split(self.validDelimiter, 1)[1])
		else:
			raise InvalidIntervalError('Integer or integer relationship is INVALID \n')

	# Prints a valid Interval object.
	def printInterval(self):
		s = ""
		if self.lowerBracketIsExclusive:
			s += "("
		else:
			s += "["
		
		s += "%s,%s" %(self.lowerBound, self.upperBound)

		if self.upperBracketIsExclusive:
			s += ")"
		else:
			s += "]"

		print s,

	# Helper functions to check bracket validity.	
	def __hasValidBrackets(self, interval):
		return self.__lowerBracketIsValid(interval[0]) and self.__upperBracketIsValid(interval[-1])

	def __lowerBracketIsValid(self, lowerBracket):
		return (lowerBracket == "[" or lowerBracket == "(")

	def __upperBracketIsValid(self, upperBracket):
		return (upperBracket == "]" or upperBracket == ")")	

	
	# Helper function to update the bracket constructor. This function is only called if brackets are valid.
	def __updateExclusivityOfBrackets(self, interval):
		if interval[0] == "[":
			self.lowerBracketIsExclusive = False
		if interval[-1] == "]":
			self.upperBracketIsExclusive = False

	# Helper function to check delimiter validity.
	def __hasDelimiter(self, interval):
		for n in interval:
			if n == self.validDelimiter:
				return True
		return False
	
	# Helper functions to check the validity of integer bounds. 
	def __hasValidBounds(self, interval):
		lowerBound = interval.split(self.validDelimiter, 1)[0]
		upperBound = interval.split(self.validDelimiter, 1)[1]
		
		# Integer bounds are valid if both upper bound and lower bound are integers 
		# and the lower bound is less than or equal to the upper bound.
		return self.__isValidInteger(lowerBound) and self.__isValidInteger(upperBound) and self.__hasProperUpperLowerBoundRelationship(lowerBound, upperBound)

	# Helper function to check whether a bound is a valid integer.
	# Adapted from Triptych on Stack Overflow (http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except)
	def __isValidInteger(self, bound):
		try:
			int(bound)
			return True
		except ValueError:
			return False

	# Helper function to check whether the lower bound is less than or equal to the upper bound.
	def __hasProperUpperLowerBoundRelationship(self, lowerBound, upperBound):
		if self.lowerBracketIsExclusive:
			lowerBound = int(int(lowerBound) + 1)
		if self.upperBracketIsExclusive:
			upperBound = int(int(upperBound) - 1)
		return int(lowerBound) <= int(upperBound)

# Credit to Adrian Mak on approaches to creating the class and error handling.
