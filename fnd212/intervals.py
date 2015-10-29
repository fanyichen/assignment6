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
	'''Generic interval class, support for integer intervals as well as float intervals'''

	valid_lower_bounds = '[('
	valid_upper_bounds = '])'
	inclusive_bounds = '[]'
	exclusive_bounds = '()'

	def __init__(self,str_representation):
		
		if not isinstance(str_representation,str):
			raise MalformedInterval
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
	''' Special sub-class of interval composed of integers '''
	# Implementation decision: Always prefer closed intervals over open intervals when possible. 
	# Since the class is defined for ranges of integers, the intervals (2,5) and [3,4] are equivalent.
	# Whenever the class has to decide between using (2,5) and [3,4], will always choose [3,4]. 
	def __init__(self,str_representation):
		#Use the init from the parent class but changing the values to int instead of float.
		interval.__init__(self,str_representation)
		self.lower_limit = int(self.lower_limit)
		self.upper_limit = int(self.upper_limit)


	def max_element(self):
		'''Return the maximum element of the interval (only defined for integer intervals)'''
		if self.upper_bound == ')':
			return self.upper_limit - 1
		else:
			return self.upper_limit
	def min_element(self):
		'''Return the minimum element of the interval (only defined for integer intervals)'''
		if self.lower_bound == '(':
			return self.lower_limit + 1
		else: 
			return self.lower_limit


	def __eq__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')
		#Two intervals are considered to be equal if their max and min elements are the same. 
		return self.max_element() == other.max_element() and self.min_element() == other.min_element()

	def __ne__(self,other):
		if not isinstance(other,intervalInt):
			raise TypeError('Comparison must be done against an instance of intervalInt class')

		return not self.__eq__(other)
	
	#Interval comparission was defined based on the comparission between the minimum
	#elements of each interval. 
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
		'''Determine whether the interval is contained into other_interval.
		If the argument is not an intervalInt instance, a TypeError exception is raised'''
		if not isinstance(other_interval,intervalInt):
			raise TypeError('Argument must be instance of intervalInt class')
		
		return self.min_element() >= other_interval.min_element() and self.max_element() <= other_interval.max_element()

	def overlaps_with(self, interval_to_compare_with):
		'''Determine if the interval overlaps with the passed interval. 
		If the argument is not an intervalInt instance, a TypeError exception is raised'''
		if not isinstance(interval_to_compare_with,intervalInt):
			raise TypeError('Argument must be instance of intervalInt class')

		return intervalInt('[{},{}]'.format(self.min_element(),self.min_element())).isin(interval_to_compare_with) \
			or intervalInt('[{},{}]'.format(self.max_element(),self.max_element())).isin(interval_to_compare_with)



def mergeIntIntervals(int1,int2):
	''' If the integer intervals overlap or are adjacent, returns a merged interval. 
	If the intervals cannot be merged, a ValueError exception is raised. 
	If the arguments are not intervalInt instances, a TypeError exception is raised'''

	if not isinstance(int1,intervalInt) or not isinstance(int2,intervalInt):
		raise TypeError('Both arguments must be instances of intervalInt class')

	if not int1.overlaps_with(int2) and int1.max_element() != (int2.min_element()-1) \
		and int2.max_element() != (int1.min_element()-1):
		raise ValueError('Intervals are neither overlapping nor adjacent, therefore they cannot be merged')

	#Returns a new interval with min_element as the minimum element between the two arguments, 
	#and max_element as the maximum element between the two arguments. 
	return intervalInt('[{},{}]'.format( min(int1.min_element(),int2.min_element()), \
					max(int1.max_element(),int2.max_element())))

def mergeIntOverlapping(intervals):
	''' Takes as input a list of intervals and merges all overlapping intervals.'''
	if not isinstance(intervals,list): 
		raise TypeError('intervals argument must be a list of intervalInts')
	for interval_instance in intervals:
		if not isinstance(interval_instance,intervalInt): 
			raise TypeError('All values in the list must be instances of intervalInt class')
	
	intervals_tmp = sorted(intervals)	#work with intervals_tmp instead of intervals
										#to avoid modifying the original list.
	merged = [intervals_tmp[0]]

	for interval_instance in intervals_tmp: 
		#Try to merge, if not possible, append to the merged list. 
		try:
			merged[-1]=mergeIntIntervals(merged[-1],interval_instance)
		except ValueError:
			merged.append(interval_instance)
	return merged

def insert(intervals,newint):
	if not isinstance(intervals,list): 
		raise TypeError('intervals argument must be a list')
	if not isinstance(newint,intervalInt):
		raise TypeError('newint argument must be an instance of itervalInt')

	intervals_tmp = intervals 	#work with intervals_tmp instead of intervals
								#to avoid modifying the original list.
	intervals_tmp.append(newint)
	
	return mergeIntOverlapping(intervals_tmp)
	

