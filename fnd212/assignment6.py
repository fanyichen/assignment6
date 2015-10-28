class InvalidInterval(Exception):
	def __str__(self):
		return '''Invalid Interval: 
				The bounds must always meet the requirement
				that lower <= upper if both bounds are inclusive,
				lower < upper if one bound is exclusive and one inclusive,
				or lower < upper-1 if both are exclusive. '''
class MalformedInterval(Exception):
	def __str__(self):
		return '''Interval argument should be a string
				of the form '[a,b]', '(a,b]', '[a,b)' or '(a,b)'
				where a and be must be integer or float numbers '''



class interval(object):

	valid_lower_bounds = '[('
	valid_upper_bounds = '])'
	inclusive_bounds = '[]'
	exclusive_bounds = '()'

	def __init__(self,str_representation):
		
		if len(str_representation) < 5:
			raise MalformedInterval
		elif str_representation[0] not in self.valid_lower_bounds or str_representation[-1] not in self.valid_upper_bounds:
			raise MalformedInterval
		elif ',' not in str_representation:
			raise MalformedInterval

		self.lower_bound = str_representation[0]
		self.upper_bound = str_representation[-1]
		str_representation = str_representation[1:-1]

		try:
			self.lower_limit,self.upper_limit = str_representation.rsplit(',')
			self.lower_limit = float(self.lower_limit)
			self.upper_limit = float(self.upper_limit)
		except:
			raise MalformedInterval

		if self.lower_bound in self.inclusive_bounds and self.upper_bound in self.inclusive_bounds:
			if not self.upper_limit >= self.lower_limit:
				raise InvalidInterval
		elif self.lower_bound in self.exclusive_bounds and self.upper_bound in self.exclusive_bounds:
			if not self.lower_limit < (self.upper_limit -1):
				raise InvalidInterval
		else:
			if not self.lower_limit < self.upper_limit:
				raise InvalidInterval

	def __repr__(self):
			return 'Interval{}{},{}{}'.format(self.lower_bound,self.lower_limit,self.upper_limit,self.upper_bound)	


class intervalInt(interval):
	''' Special class of interval composed of integers '''
	# Implementation decision: Always prefer closed intervals over open intervals when possible. 
	# Since the class is defined for ranges of integers, the intervals (2,5) and [3,4] are equivalent.
	# Whenever the class has to decide between using (2,5) and [3,4], always choose [3,4]. 

	def max_element(self):
		if self.upper_bound == ')':
			return self.upper_limit - 1
		else:
			return self.upper_limit
	def min_element(self):
		if self.lower_bound == '(':
			return self.lower_limit + 1
		else: 
			return self.lower_limit

	def __eq__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')

		return self.max_element() == other.max_element() and self.min_element() == other.min_element()

	def __ne__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')

		return not self.__eq__(other)

	def __lt__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')
		
		return self.min_element() < other.min_element()

	def __gt__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')
		return self.min_element() > other.min_element()
	def __le__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')
		return self.min_element() <= other.min_element()
	def __ge__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')
		return self.min_element() >= other.min_element()


	def isin(self, other_interval):
		if not isinstance(other_interval,intervalInt):
			raise TypeError('Argument must be instance of intervalInt class')
		
		return self.min_element() >= other_interval.min_element() and self.max_element() <= other_interval.max_element()

	
	def overlaps_with(self, interval_to_compare_with):
		if not isinstance(interval_to_compare_with,intervalInt):
			raise TypeError('Argument must be instance of intervalInt class')

		return intervalInt('[{},{}]'.format(self.min_element(),self.min_element())).isin(interval_to_compare_with) \
			or intervalInt('[{},{}]'.format(self.max_element(),self.max_element())).isin(interval_to_compare_with)



def mergeIntIntervals(int1,int2):
	if not isinstance(int1,intervalInt) or not isinstance(int2,intervalInt):
		raise TypeError('Both arguments must be instances of intervalInt class')

	if not int1.overlaps_with(int2) or int1.max_element() == (int2.min_element()-1) \
		or int2.max_element() == (int1.min_element()-1):
		raise ValueError('Intervals are neither overlapping nor adjacent, therefore they cannot be merged')


	merged_lower_limit = min(int1.min_element,int2.min_element)
	merged_lower_bound = 1
	return intervalInt('[{},{}]'.format( min(int1.min_element(),int2.min_element()), \
					max(int1.max_element(),int2.max_element())))

def mergeIntOverlapping(intervals):
	for interval_instance in intervals:
		if not isinstance(interval_instance,intervalInt) 
			raise TypeError('All values in the list must be instances of intervalInt class')
	merged = []
	if len(intervals) == 2:
		try:
			merged = mergeIntIntervals(intervals[0],intervals[1])
		except ValueError:
			merged = intervals
		finally:
			return merged
	else:
		merged = mergeIntOverlapping(intervals[:-1])
		

	



	merged_intervals = intervals
	while 1:



