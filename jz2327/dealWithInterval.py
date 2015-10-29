import interval
from interval import interval
import userExceptions
from userExceptions import merge_bad

def mergeIntervals(interval_1, interval_2):
'''merge two intervals by using interval class to understand the real interval and judge whether two can merge'''
	interval_1 = interval(interval_1)
	interval_2 = interval(interval_2)
	interval_1.realInterval()
	interval_2.realInterval()

	if interval_1.realLowerBound > interval_2.realUpperBound+1 or interval_1.realUpperBound+1 < interval_2.realLowerBound:               # the intervals not overlap on adjacent would raise an error
		raise merge_bad()
	else:
		if int(interval_1.lowerBound) <= int(interval_2.lowerBound):
			return '%s%s,%s%s' % (interval_1.leftBound,int(interval_1.lowerBound), int(interval_2.upperBound), interval_2.rightBound)
		else:
			return '%s%s,%s%s' % (interval_2.leftBound,int(interval_2.lowerBound), int(interval_1.upperBound), interval_1.rightBound)

def sortIntervals(intervalList):
'''sort the list of intervals to be an ascending order by comparing the real lower bound of the intervals'''
	
	realIntervalList = []
	for interval in range(len(intervalList)):
		singleInterval = interval(intervalList[interval])
		singleInterval.realInterval()
		realIntervalList.append(singleInterval)

	# each loop would return an interval with a minimum real lower bound and add it to the intervalListSorted list.
	intervalLength = len(intervalList)
	intervalListSorted = []
	while intervalLength > 0:                                                     #there are n = intervalLength intervals so sort n times.
		minimumLower = float("inf")
		listLength = 0
		listNumber = 0
		for i in range(0,len(realIntervalList)):                                  #each loop to find a minimum.
			if minimumLower > realIntervalList[i].realLowerBound:
				minimumLower = realIntervalList[i].realLowerBound
				listNumber = i
				listLength = len(realIntervalList[i].realIntervalInput)
			elif minimumLower == realIntervalList[i].realLowerBound:
				if len(realIntervalList[i].realIntervalInput) > listLength:
					listNumber = i
					listLength = len(realIntervalList[i].realIntervalInput)
		intervalListSorted.append(intervalList[listNumber])                       #add the interval to the new list
		del intervalList[listNumber]
		del realIntervalList[listNumber]
		intervalLength = intervalLength - 1

	return intervalListSorted

def mergeOverLapping(intervalList):
'''merge a list of intervals by 
	1 sort the interval list by using sortIntervals()
	2 merge interval pairs by using mergeIntervals()'''

	intervalListSorted = sortIntervals(intervalList)
	intervalPositon = len(intervalListSorted) - 1

	# comparing the sorted list of intervals from end to start. each time take two intervals to merge or determine they cannot merge.
	while intervalPositon > 0:
		try:
			newInterval = mergeIntervals(intervalListSorted[intervalPositon-1],intervalListSorted[intervalPositon])
			del intervalListSorted[intervalPositon]
			del intervalListSorted[intervalPositon-1]
			intervalListSorted.append(newInterval)
			intervalListSorted = sortIntervals(intervalListSorted)
			intervalPositon = intervalPositon - 1
		except merge_bad:
			intervalPositon = intervalPositon - 1 

	return sortIntervals(intervalListSorted)

def insert(intervalsInserted, newint):
'''insert a interval to a interval list and do the merge function by using mergeOverLapping()'''

	intervalsInserted.append(newint)                                     #insert the new interval to the list form a new list
	newIntervalList = mergeOverLapping(intervalsInserted)                #do mergeOverLapping() in the new list
	return newIntervalList
