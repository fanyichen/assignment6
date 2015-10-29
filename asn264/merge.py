from interval import *

#This error is generally raised when non-adjacent or non-overlapping intervals are passed to mergeIntervals
class invalidMergeError(Exception):
	def __str__(self):
		return "Disjoint intervals cannot be merged."

'''The following  functions are done *to* members of the interval class rather than *by* members of interval class - so they are not member functions of the interval class'''
	
#Determine whether int1 and int2 are disjoint intervals - that is, share no elements
def check_disjoint(int1, int2):
	#Given [a,b] and [c,d] in that order on the number line, if b < c: disjoint
	#Given [c,d] and [a,b] in that order on the number line, if d < a: disjoint
	if int1.get_max() < int2.get_min() or int2.get_max() < int1.get_min():
		return True
	else:
		return False


#Determine whether int1 and int2 are adjacent intervals. Ex: [2,3] and [4,5] are adjacent. [2,3] and [3,5] are not.
def check_adjacent(int1, int2):
	#Given [a,b] and [c,d] in that order on the number line, if b+1 = c: adjacent
	#Given [c,d] and [a,b] in that order on the number line, if d+1 = a: adjacent	
	if int1.get_max()+1 == int2.get_min() or int2.get_max()+1 == int1.get_min():
		return True
	else:
		return False

    
#Determine whether int1 and int2 are overlapping intervals - that is, share at least one element. [2,3] and [3,5] are overlapping.
def check_overlap(int1, int2):
    #Given [a,b] and [c,d] in that order on the number line, if a <= c and b >= c: overlapping
    #Given [c,d] and [a,b] in that order on the number line, if c <= a and d >= a: overlapping
    if (int1.get_min() <= int2.get_min() and int1.get_max() >= int2.get_min()) or (int2.get_min() <= int1.get_min() and int2.get_max() >= int1.get_min()):
        return True
    else:
        return False

#Check whether there are adjacent intervals in the list intervals
def is_adjacent(intervals):
    for i in range(0, len(intervals)):
        for j in range(i+1, len(intervals)):
            if check_adjacent(intervals[i],intervals[j]):
                return True
    return False


#Check whether there are overlapping intervals in the list intervals 
def is_overlapping(intervals):
    for i in range(0, len(intervals)):
        for j in range(i+1, len(intervals)):
            if check_overlap(intervals[i],intervals[j]):
                return True
    return False
            

#Returns a merged interval from the input intervals, if possible
def mergeIntervals(int1, int2):	
	#Only disjoint, non-adjacent intervals cannot be merged
	if (check_disjoint(int1,int2) and check_adjacent(int1,int2)) or not check_disjoint(int1,int2):
		return interval("[" + str(min(int1.get_min(), int2.get_min())) + "," + str( max(int1.get_max(), int2.get_max())) + "]")
	else:
	        raise invalidMergeError	


#Implements bubble sort algorithm on interval objects
def sort_intervals(intervals):
	for i in range(0,len(intervals)):
		for j in range(0,len(intervals)-1-i):
			if intervals[j].get_min() > intervals[j+1].get_min():
				intervals[j], intervals[j+1] = intervals[j+1], intervals[j]
	return intervals
                
#Take a list of intervals and merge all overlapping or adjacent intervals
def mergeOverlapping(intervals):

	#While there is at least one set of intervals that has an overlap or are adjacent
	while is_overlapping(intervals) or is_adjacent(intervals):

		#Sort the intervals in increasing order
		sort_intervals(intervals)
       
		merged = []
		merged_index = []	

		#For the first possible interval pair, conduct a merge if there is an overlap or adjacency and save the new interval in merged
		for i in range(0,len(intervals)): 
			for j in range (i+1, len(intervals)):
				if check_overlap(intervals[i],intervals[j]) or check_adjacent(intervals[i],intervals[j]):				
					merged.append(mergeIntervals(intervals[i], intervals[j]))
					merged_index.append(i)
					merged_index.append(j)
					break

		#If an interval was not involved in a merge, append it to merged
		for i in range(0,len(intervals)):
			if i not in merged_index:
				merged.append(intervals[i])
	
		#In case intervals requires more than one round of merges, reset the value of intervals to merged
		intervals = merged

	return sort_intervals(intervals)
        
        
#Insert newint into intervals (a list of non-overlapping and non-adjacent intervals) and merge the result if necessary 
def insert(intervals, newint):
	#check that intervals is a non-overlapping and non-adjacent list of intervals
	if not is_overlapping(intervals) and not is_adjacent(intervals):
		#append newint to the list
		intervals.append(newint)
		#merge all overlapping and adjacent intervals
		intervals = mergeOverlapping(intervals)
	return intervals
