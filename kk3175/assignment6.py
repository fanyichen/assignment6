"""Main program that prompts a user for integer intervals and creates a list containing merges of the intervals."""

from interval import Interval
from errorHandling import InvalidIntervalError
from errorHandling import MergeError
import re, sys

# Merges two intervals if they overlap. If the two intervals do not overlap, an exception is thrown. 
def mergeIntervals(int1, int2):	
	# Convert int1 to the format of (a,b) and int2 to the format of (c,d). 
	# Convert the interval's bracket and integer relationship to "(" and ")" to represent exclusivity.
	a = int1.lowerBound
	b = int1.upperBound
	c = int2.lowerBound
	d = int2.upperBound
	if(not int1.lowerBracketIsExclusive):
		a -= 1
	if(not int1.upperBracketIsExclusive):
		b += 1
	if(not int2.lowerBracketIsExclusive):
		c -= 1
	if(not int2.upperBracketIsExclusive):
		d += 1
	
	# If a > c, swap int1 and int2.
	if a > c:
		e = a
		f = b
		a = c
		b = d
		c = e
		d = f

	# If the intervals do not overlap, an exception is raised.	
	if b <= c:
		raise MergeError('Cannot merge intervals; the intervals do not overlap.\n')
	# Otherwise, the intervals overlap and are merged.	
	elif b > d:
		s = "(%s,%s)" %(a,b)		
		return Interval(s)
	else:
		s = "(%s,%s)" %(a,d)		
		return Interval(s)

# Helper function to sort a list of Intervals in order of increasing lower bound values.
def intervalComparison(int1, int2):
	# Convert int1 to the format of (a,b) and int2 to the format of (c,d). 
	# Convert the interval's bracket and integer relationship to "(" and ")" to represent exclusivity.
	a = int1.lowerBound
	b = int1.upperBound
	c = int2.lowerBound
	d = int2.upperBound
	if(not int1.lowerBracketIsExclusive):
		a -= 1
	if(not int1.upperBracketIsExclusive):
		b += 1
	if(not int2.lowerBracketIsExclusive):
		c -= 1
	if(not int2.upperBracketIsExclusive):
		d += 1

	# Returns for the comparison function.
	if a < c: return -1
	elif a == c:
		if b < d: return -1
		elif b == d: return 0
		else: return 1	# else b > d 
	else: return 1		# else a > c

# Takes a list of Intervals and merges all overlapping intervals.
def mergeOverlapping(intervals):
	# Sort intervals	
	intervals.sort(intervalComparison)
	
	# Merge overlapping intervals
	i = 0
	j = 1
	while j < len(intervals):
		try:
			mergedInterval = mergeIntervals(intervals[i], intervals[j])
			intervals[i] = mergedInterval
			del intervals[j]
		except MergeError:
			i += 1
			j += 1

# Takes a list of non overlapping intervals and a single interval and merges the result if appropriate.
def insert(intervals, newint):
	intervals.append(newint)
	mergeOverlapping(intervals)


# Main	
print("This program merges your list of integer intervals.")
print("Use a comma to separate the lower bound integer in your interval from the upper bound integer.")

# Contains the final list of intervals.
intervalList = []

while not intervalList:
	try:
		# Prompts the user for a list of intervals.
		userList = raw_input("List of intervals? ")
	
		# Separates each interval into a list of strings.
		p = re.compile('[\[(].*?,.*?[\])]')
		intermediateList = p.findall(userList)	
		
		# Creates a list of intervals where each interval is of class Interval.	
		for i in intermediateList:
			intervalList.append(Interval(i))
		if not intervalList:
			print("Invalid list of intervals. Try again.")

	except InvalidIntervalError as e:
		print("Invalid list of intervals. Try again.")
		# Resets the final list of intervals to empty.
		intervalList = []

	except MergeError as e:
		print 'A MergeError occurred: ', e.value

# Prompts the user to enter additional intervals to be merged with their list of intervals.
print("You may now enter additional integer intervals one at a time.")
print("Type \"quit\" to exit.")

while True:
	try:
		additionalInterval = raw_input("Interval? ")
		if additionalInterval == "quit":
			break

		insert(intervalList, Interval(additionalInterval))

		# Displays the merged intervals.
		j = 0		
		for i in intervalList:
			i.printInterval()
			if j < (len(intervalList) - 1):		
				sys.stdout.write(', ')
			j += 1
		print "\n",
		
	except InvalidIntervalError:
		print 'Invalid interval'
