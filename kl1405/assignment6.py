import sys
from interval import interval
def mergeIntervals(int1,int2):
	# If int1 and int2 are valid, merge if it meets conditions.
	if int1.upperbound + 1 >= int2.lowerbound  and int2.upperbound + 1 >= int1.lowerbound:
		if int1.lowerbound < int2.lowerbound:
			#the first part of mergestr will be the first part of int1
			mergestr = int1.string.split(',')[0] 
		else:
			#the first part of mergestr will be the first part of int2
			mergestr = int2.string.split(',')[0]
		mergestr += ',' #include a ','

        
		if int1.upperbound > int2.upperbound:
			#the second part of mergestr will be the second part of int1
			mergestr += int1.string.split(',')[1]
		else:
			#the second part of mergestr will be the second part of int2
			mergestr += int2.string.split(',')[1]
			#return the merged interval mergestr
		return interval(mergestr)
	else:
		return False

def mergeOverlapping(intervals):
	#merge overlapping intervals
	for i in xrange(len(intervals) - 1):
		for j in xrange(i + 1,len(intervals)):
			if mergeIntervals(intervals[i],intervals[j]):
				intervals[j] = mergeIntervals(intervals[i],intervals[j])
				intervals.remove(intervals[i])
				#return a list of interval
				return mergeOverlapping(intervals)
				#sort the output interval
	return sorted(intervals, key = lambda x:x.lowerbound)

def insert(intervals, newint):
	intervals.append(newint)
	return mergeOverlapping(intervals)

# the main function
def main():
	while True:
		try:
			#ask for an interval list
			Input = raw_input('List of intervals? ')
			if Input == 'quit':
				raise KeyError
			Intervals = map(interval, Input.split(', '))
			break
			#if invalid input
		except NameError:
			print 'Invalid intervals'
		except KeyError:
			return 0
	
#ask for another interval and insert to the previous interval list
	Inputtext = raw_input('Interval? ')
	while Inputtext != 'quit':
		try:
			Interval = interval(Inputtext)
			Intervals = insert(Intervals, Interval)
			for i in Intervals[:-1]:
				print '%s, ' % i.string,
			print Intervals[-1].string
			Inputtext = raw_input('Interval? ')
		except NameError:
			print 'Invalid interval'
			Inputtext = raw_input('Interval? ')
	return 0

main()