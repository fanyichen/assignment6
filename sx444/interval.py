import re
import operator


class interval(object):
# define a class named interval that represents the range of integers between a lower bound and upper bound.
    def __init__(self,interval_string):   # this is a constructor that takes a string representation of the interval.
        self.interval_string = interval_string
        numbers = re.findall(r'[-]{0,1}[0-9]+', interval_string) 
        self.lower = int(numbers[0])		
        self.upper = int(numbers[1])
        bounds = re.findall(r'[\(\[\]\)]',interval_string)
        self.lower_bound = bounds[0]
        self.upper_bound = bounds[1]
        if self.lower_bound == '[' and self.upper_bound == ']':
        	if self.lower > self.upper:
        		raise ValueError("Invalid interval")
        if self.lower_bound == '(' and self.upper_bound == ')':
        	if self.lower >= self.upper - 1:
        		raise ValueError("Invalid interval")
        if self.lower_bound == '[' and self.upper_bound == ')':
        	if self.lower >= self.upper:
        		raise ValueError("Invalid interval")
        if self.lower_bound == '(' and self.upper_bound == ']':
        	if self.lower >= self.upper:
        		raise ValueError("Invalid interval")        

    def __repr__(self):    # identify the print format
        return self.lower_bound  + str(self.lower) + ',' + str(self.upper) + self.upper_bound


def mergeIntervals(int1, int2):
# define a function that takes two intervals and merge if necessary.
	if int1.lower > int2.lower:
		change = int2
		int2 = int1
		int1 = change
	if int1.upper_bound == ']':
		if int1.upper >= int2.lower:
			# need merging here
			merged_interval = int1
			merged_interval.lower = int1.lower
			if int1.lower == int2.lower:
				if int1.lower_bound == '(' and int2.lower_bound == '(':
				   merged_interval.lower_bound = '('
				else:
				   merged_interval.lower_bound = '['
			else:
				merged_interval.lower_bound = int1.lower_bound
			if int1.upper < int2.upper:
			   merged_interval.upper = int2.upper
			   merged_interval.upper_bound = int2.upper_bound
			if int1.upper == int2.upper:
			   merged_interval.upper = int1.upper	
			   merged_interval.upper_bound = ']'
			if int1.upper > int2.upper:
			   merged_interval.upper = int1.upper
			   merged_interval.upper_bound = int1.upper_bound
		return merged_interval
	if int1.upper_bound == ')':
		if (int1.upper > int2.lower) or (int1.upper == int2.lower and int2.lower_bound == '['):
			 #need merging here
		   merged_interval = int1
		   merged_interval.lower = int1.lower
		   if int1.lower == int2.lower:
			  if int1.lower_bound == '(' and int2.lower_bound == '(':
				 merged_interval.lower_bound = '('
			  else:
				 merged_interval.lower_bound = '['
		   else:
				 merged_interval.lower_bound = int1.lower_bound
		   if int1.upper < int2.upper:
			  merged_interval.upper = int2.upper
			  merged_interval.upper_bound = int2.upper_bound
		   if int1.upper == int2.upper:
			  merged_interval.upper = int1.upper
			  if int2.upper_bound == ']':
				 merged_interval.upper_bound = ']'
			  else:
			     merged_interval.upper_bound = ')'
		   if int1.upper > int2.upper:
			  merged_interval.upper = int1.upper
			  merged_interval.upper_bound = int1.upper_bound
		
		return merged_interval
		
def mergeOverlapping(intervals):
# define a function to take a list of intervals and merge all the overlapping intervals.
    overlap = True
    while overlap == True:
        overlap = None
        intervals.sort(key=operator.attrgetter('lower'))
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                try:
                    mergeIntervals(intervals[i], intervals[j])
                except:
                    continue
                else:
                    overlap = True
                    new_int = mergeIntervals(intervals[i],intervals[j])
                    intervals.remove(intervals[i])
                    intervals.remove(intervals[j-1])
                    intervals.append(new_int)
    return intervals	
		
    
def insert(intervals, newint):
# define a function to insert a new interval to a list of intervals.
    intervals.append(newint)
    return mergeOverlapping(intervals)
