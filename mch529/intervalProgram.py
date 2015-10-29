from assignment6 import Interval
import re
import sys



def isMergable(interval1,interval2):
	'''
	input: two intervals , as objects not strings
	helper function for mergeIntervals and mergeOverlapping,
	returns boolean
	'''
	realmin= min(interval1.realLeftBound, interval2.realLeftBound)
	realmax= max(interval1.realRightBound, interval2.realRightBound)
	int2Length= interval2.realRightBound - interval2.realLeftBound + 1
	int1Length= interval1.realRightBound - interval1.realLeftBound + 1
	
#the length of the merged interval must be smaller or equal to the sum of the length of the two intervals
	if realmax-realmin + 1 > int2Length +int1Length:
		return False
	else:
		return True
	

def mergeIntervals(int1,int2):
	'''
	Takes two intervals objects and returns a merged interval object.  Throws an error if they do not intersect or are adjacent
	'''
	
	if  int1.realLeftBound > int2.realLeftBound: 
		#swap if lower bound is in int1 is bigger than lower bound in int2
		dummy=int2
		int2=int1
		int1=dummy
		
	try:
		realmin= min(int1.realLeftBound, int2.realLeftBound)
		realmax= max(int1.realRightBound, int2.realRightBound)
		mergedInterval = "["+ str(realmin) + "," + str(realmax) +"]"
		if isMergable(int1,int2):
			return Interval(mergedInterval)
		else:	
			raise
	except:

		ValueError('Cannot merge intervals')
	
		

def mergeOverlapping(intervals):
	''' 
	merges a set of intervals objects
	returns a list of interval objects
	'''

	finalList=[]
	intervals.sort(key=lambda x: x.realLeftBound)
	while len(intervals)>1:  #greater than 1 so there is always atleast two elements to pop out
		
		if isMergable(intervals[0],intervals[1]):

			merged_intervals = mergeIntervals(intervals[0],intervals[1])
			intervals.pop(0)
			intervals.pop(0)
			intervals.insert(0,merged_intervals)  #replace first two with merged version
		else:
			finalList.append(intervals.pop(0))

	finalList.append(intervals.pop(0))  # pop out last element in list
	return finalList

def insert(intervals, int1):
	'''
	input: a list of intervals and an interval
	returns: merged interval
	'''
	intervals.append(int1)

	return mergeOverlapping(intervals)

intervalList = []

while len(intervalList)==0:
	try:

		intervals = raw_input("Please enter a list of Intervals:  ")
		if intervals=="quit":
			break
		
		dummy = re.compile('([\[(].*?,.*?[\])])')
		testList = dummy.findall(intervals)	

		for inter in testList:   # change text to class for elements in our list
			intervalList.append(Interval(inter))
		if len(intervalList)==0:
			print("Invalid list of intervals. Try again. ")
		

	except Exception as msg:
		print msg
		intervalList = []  #try again
	

while True: 
	newInterval= raw_input("another interval? ")
	if newInterval== ("quit" or "Quit"):
		break
	try:
		intervalList = insert(intervalList , Interval(newInterval) )
		print intervalList
	except Exception as msg:
		print msg

	
