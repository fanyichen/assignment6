import numpy
import re 
 
class interval(object):
        # represents the range of intergers between a lower and upper bound

        def __init__(self,interval_string):
		self.interval_string = interval_string
		if self.interval_string[0] == "(":
			self.lower_bound_meta = "("
		elif self.interval_string[0] == "[":
			self.lower_bound_meta = "["
		else:
			print "Interval not formatted correctly (1)"
		if self.interval_string[-1] == ")":
			self.upper_bound_meta = ")"
		elif self.interval_string[-1] == "]":
			self.upper_bound_meta = "]"
		else: 
			print "Interval not formatted correctly (2)"

		self.interval_numbs = map(int, re.findall('\d+', self.interval_string))
		if len(self.interval_numbs) != 2:
			print "Interval not formatted correctly (3)"

		self.lower_bound = self.interval_numbs[0]
		self.upper_bound = self.interval_numbs[1]

		if self.lower_bound_meta == "[":
			self.interval_min = self.lower_bound
		else:
			self.interval_min = self.lower_bound + 1
		if self.upper_bound_meta == "]":
			self.interval_max = self.upper_bound
		else: 
			self.interval_max = self.upper_bound - 1


		try:
			self.interval_max > self.interval_min
		except:
			False

		self.standardized_interval = range(self.interval_min,self.interval_max+1)
		
def mergeIntervals(int1,int2):
	int1 = interval(int1)
	int2 = interval(int2)
	temp_merged_interval = sorted(numpy.unique(int1.standardized_interval + int2.standardized_interval))
	overlap_test = sum(numpy.unique(numpy.diff(temp_merged_interval)))
	if overlap_test == 1 : 
		
		if int1.lower_bound < int2.lower_bound:
			merge_lower_bound = int1.lower_bound
			merge_lower_bound_meta = int1.lower_bound_meta
		else:
			merge_lower_bound = int2.lower_bound 
			merge_lower_bound_meta = int2.lower_bound_meta
	
		if int1.upper_bound > int2.upper_bound:
			merge_upper_bound = int1.upper_bound
			merge_upper_bound_meta = int1.upper_bound_meta
		else:
			merge_upper_bound = int2.upper_bound
			merge_upper_bound_meta = int2.upper_bound_meta
	
		merge_interval = merge_lower_bound_meta + str(merge_lower_bound) + "," + str(merge_upper_bound) + merge_upper_bound_meta
		return merge_interval
	else:
		raise ValueError('Intervals do not overlap')

def mergeOverlapping(intervals):
	intervals_split = intervals.split(",")
	interval_list = []
	for inter in range(0, len(intervals_split)-1,2):
		temp_interval = intervals_split[inter] + "," + intervals_split[inter+1]
		interval_list = interval_list + [str(temp_interval)]

	new_interval_list = []
	should_restart = True
	while should_restart:
		for i in range(0,len(interval_list)):
			for j in range(i+1,len(interval_list)): 
				should_restart = False
				try:	
					merged_interval = mergeIntervals(interval_list[i],interval_list[j])
					temp_interval_list = interval_list
					first = interval_list[i]
					second = interval_list[j]
					temp_interval_list.remove(first)
					temp_interval_list.remove(second)
					for m in range(0,len(temp_interval_list)):
						new_interval_list.append(temp_interval_list[m])
					new_interval_list.append(merged_interval)
					interval_list = new_interval_list
					new_interval_list = []
					if len(interval_list) > 1:
						should_restart = True
						break
					else:
						continue
				except: 
					continue
	print interval_list
	return interval_list

def insert(intervals, newint):
	intervals = intervals + ',' + newint
	return mergeOverlapping(intervals)

our_list = input('List of intervals? ')
mergeOverlapping(our_list)
quit = False
q = False
for i in (0, 100):
        int_prompt = input('Interval? ')
        if int_prompt == False:
                break
        else:
		try:
			print ('our list 1') + str( our_list)
                	our_list = str(insert(our_list, int_prompt))
			print ('our_list 2') +str(our_list)
		except:
                        print "Error: Interval entered wrong format?"
