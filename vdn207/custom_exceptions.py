'''Few custom exceptions for the program'''

class IntervalRangeException(Exception):	# Exception for invalid range within an interval
	pass

class InvalidBoundsException(Exception):	# Exception for invalid bound values in an interval
	pass

class InvalidBoundTypeException(Exception):	# Exception for invalid bound types in an interval
	pass