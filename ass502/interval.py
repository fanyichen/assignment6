"""contains the interval class, which represents an interval of the form [a,b) where a and b are integers, the bounds are either open (,) or closed [,], and an interval contains at least one integer"""

class interval:

	def __init__(self, interval):
		"""instantiates an interval object"""
		interval=interval.replace(" ","") #remove whitespace
		if self.checkInputFormat(interval):
			if self.checkIntervalRange(interval):
				#split up the input into the four components of two bounds and two endpoints
				#assign each attribute its corresponding value

				#boolean that represents whether the lower bound is inclusive or not
				self.lowerInclusive=self.isInclusive(interval[0])
				#boolean that represents whether the upper bound is inclusive or not
				self.upperInclusive=self.isInclusive(interval[len(interval)-1])
				#integer that represents the lower endpoint of the interval
				self.lowerInteger=int(interval[1:self.getCommaIndex(interval)])
				#integer that represents the upper endpoint of the interval
				self.upperInteger=int(interval[self.getCommaIndex(interval)+1:len(interval)-1])
			else:
				raise IntervalException()
		else:
			raise ValueError
	
	def __repr__(self):
		"""creates printable representation of an interval object"""
		
		#get chars corresponding to bounds being inclusive/exclusive
		if self.lowerInclusive:
			lowerBound='['
		else:
			lowerBound='('
		if self.upperInclusive:
			upperBound=']'
		else:
			upperBound=')'
			
		#return string representation of the interval
		return lowerBound+str(self.lowerInteger)+","+str(self.upperInteger)+upperBound

	def __eq__(self, other): 
		"""defines equality between instances of interval objects"""
        	return self.__dict__ == other.__dict__
		
	def checkInputFormat(self,interval):
		"""verifies that the string representation of an interval is properly formatted, with opening and closing brackets, a single comma separating the two endpoints, and integers as endpoints"""
	
		#if there is no comma in the input interval, or if it is the last char in the string we know the input is invalid
		if self.getCommaIndex(interval)==len(interval)-1:
			return False
		#split the input into the two boundary and two integer components and check that each part is valid, if so the input has a valid format
		else:
			return self.checkLowerBound(interval[0]) & self.checkInteger(interval[1:self.getCommaIndex(interval)]) & self.checkInteger(interval[self.getCommaIndex(interval)+1:len(interval)-1]) & self.checkUpperBound(interval[len(interval)-1])
				
		
	def checkLowerBound(self,bound):
	    if bound=='(' or bound=='[':
		    return True
	    else:
	        return False

	def checkUpperBound(self,bound):
		if bound==')' or bound==']':
			return True
		else:
			return False
			
	def checkInteger(self,string):
		"""checks if a string is a string representation of an integer"""
		
		try:
			int(string)
			return True
		except ValueError:
			return False

	def getCommaIndex(self,interval):
		"""returns the index of a comma in a string representation of an interval"""
	
		for c in range(0,len(interval)):
			if interval[c]==',':
				break
		return c
		
	def isInclusive(self,bound):
		if bound=='[' or bound==']':
			return True
		elif bound=='(' or bound==')':
			return False
			
	def checkIntervalRange(self,interval):
		"""checks that a properly formatted interval has at least one integer in its range"""
	
		#calculate minimum difference needed between the interval endpoints
		difference = 0
		
		#open bracket means we need an incremental difference of 1, closed means 0
		difference += (1-int(self.isInclusive(interval[0])))
		difference += (1-int(self.isInclusive(interval[len(interval)-1])))
		
		lowerInteger=int(interval[1:self.getCommaIndex(interval)])
		upperInteger=int(interval[self.getCommaIndex(interval)+1:len(interval)-1])
		
		if upperInteger-difference>=lowerInteger:
			return True
		else:
			return False
			
class IntervalException(Exception):
	"""exception for when an interval does not contain any integers"""
	def __str__(self):
		return 'There are no integers contained in the interval'
