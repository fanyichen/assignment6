import re

# I initially tried to create a system to handle the entire list of initially input intevals, but then after discussing the problems I faced with this design with Sida, I opted to break the string down after doing some initial validation of the input and handle the interval evaluation and merging based on his general design pattern approach.
# tried to make the naming of variables more clear.

class Interval(object):
	def __init__ (self, userinput):
		self.userinput = userinput
		self.validinput = re.match(r'[\200-\377]|[\100-\132]|[\134]|[\136-\137]|[\140-\176]|[\072-\077]|[\055-\057]|[\052-\053]|[\052-\053]|[\041-\047]|\0|\v|\f|\a|\n|\r|\t|\s',self.userinput) #robust regex expression to make sure the User Input is really clean.
		if self.validinput != None or not(self.userinput): # also accounting for the user just hitting return here.
			raise ValueError('Invalid Intervals. found a character that does not belong')
		self.openbrace = userinput[0] 
		self.closingbrace = userinput[-1]
		self.removebraces = self.userinput.strip("[]()")
		self.getintervalvalues = self.removebraces.split(",")
		try:
			self.integers = [int(i) for i in self.getintervalvalues]
		except:
			raise ValueError('Invalid Intervals. probably not integer ')
		if len(self.integers) != 2:
			raise ValueError('Invalid Intervals. to few or too many integers')
		self.lowerOriginal = self.integers[0]
		self.upperOriginal = self.integers[1]
		self.lowerCheckedAndAdjusted = self.integers[0]
		self.upperCheckedAndAdjusted = self.integers[1]
		if self.openbrace == '(':
			self.lowerCheckedAndAdjusted += 1
		if self.closingbrace == ')':
			self.upperCheckedAndAdjusted -= 1
		if self.lowerCheckedAndAdjusted >= self.upperCheckedAndAdjusted:
			raise ValueError('Invalid Intervals. integers are too close')
	def __repr__(self):
		return self.openbrace + str(self.lowerOriginal) + ',' + str(self.upperOriginal) + self.closingbrace
	
def mergeIntervals(int1, int2):

    """ This is a function that takes two intervals as arguments.
    Checks whether they overlap and merges them if they do. """

    if intervalsCanMerge(int1, int2) == False:
        raise ValueError('Disjoint intervals!')
    if int1.lowerCheckedAndAdjusted <= int2.lowerCheckedAndAdjusted and int1.lowerOriginal <= int2.upperOriginal: 
        merged_lower = int1.lowerOriginal
        merged_front = int1.openbrace
    else:
        merged_lower = int2.lowerOriginal
        merged_front = int2.openbrace
    if int1.upperCheckedAndAdjusted >= int2.upperCheckedAndAdjusted and int1.lowerOriginal >= int2.upperOriginal:
        merged_upper = int1.upperOriginal
        merged_back = int1.closingbrace
    else:
        merged_upper = int2.upperOriginal
        merged_back = int2.closingbrace
    result = merged_front + str(merged_lower) + ',' + str(merged_upper) + merged_back
    return Interval(result)

def mergeOverlapping(intervals):
    
    """ This is a function that takes a list of lists. The lists are intervals.
    It sorts the intervals and then determines whether it can merge them together using
    intervalsCanMerge function and then merges them using the mergeIntervals function."""
    
    intervals.sort(key = lambda x:x.lowerOriginal)
    if len(intervals) == 0 or len(intervals) == 1:  									#checks to make sure there isn't a single interval remaining.
        return intervals
    if intervalsCanMerge(intervals[0], intervals[1]): 									#determines whether the two intervals currenlty selected can be merged.
        firstMergedIntervalsAsceding = mergeIntervals(intervals[0], intervals[1]) 		#merges the first two intervals in the list.
        intervals = intervals[2:] 														#sets the interval variable to all of the intervals above the first two because it is assumed they have been merged.
        intervals.insert(0, firstMergedIntervalsAsceding)								#inserts the newly created interval into the existing list in the 0 position so it checked against the next
        return mergeOverlapping(intervals) 
    else:
        return intervals[:1] + mergeOverlapping(intervals[1:]) 							#merging the interval list just checked back to the result of the mergeOverlapping function after running the function on the remaing elements in the list.

def insert(intervals, newInterval):
    
    """insert function takes two arguments: a list of non-overlapping intervals,
    and a single interval. The function should insert an interval into lists of intervals. """
    
    intervals.append(newInterval)
    return mergeOverlapping(intervals)

def intervalsCanMerge(int1, int2):

	"""intervalsCanMerge takes two intervals as arguments and
	 checks whether two intervals can be merged"""

	if (int1.upperCheckedAndAdjusted < int2.lowerCheckedAndAdjusted - 1) or (int2.upperCheckedAndAdjusted < int1.lowerCheckedAndAdjusted - 1):
		return False
	return True
