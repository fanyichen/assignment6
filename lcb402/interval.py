import numpy
import re 
 
class interval(object):
        # represents the range of intergers between a lower and upper bound
        # either of the bounds can be "inclusive" or "exclusive"
        # can be begative or positive
        # both inclusive : lower <= upper
        # inclusive and exclusive : lower < upper
        # both exclusive: lower < upper-1

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

		if self.lower_bound_meta == "in":
			self.interval_min = self.lower_bound
		else:
			self.interval_min = self.lower_bound + 1
		if self.upper_bound_meta == "in":
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
	overlap_test = numpy.unique(numpy.diff(temp_merged_interval))
	print temp_marged_interval
	print overlap_test
	try:
		print overlap_test.all()== 1
	except:
		raise ValueError('Intervals do not overlap') 
		
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
int1 = '[1,6)'
int2 = '[6,18]'
print mergeIntervals(int1,int2)


def mergeOverlapping(intervals):
	intervals_split = intervals.split(",")
	interval_list = []
	for inter in range(0, len(intervals_split)-1,2):
		temp_interval = intervals_split[inter] + "," + intervals_split[inter+1]
		interval_list = interval_list + [str(temp_interval)]
	
	i = 0 
	while i < len(interval_list)-2:
		for j in range(i+1,(len(interval_list)-1)):
			print interval_list[i]
			print interval_list[j] 
			try:
				merged_interval = mergeIntervals(interval_list[i],interval_list[j])
				print merged_interval
				temp_interval_list = interval_list[i+2:]
				interval_list= [merged_interval] + temp_interval_list
				i = i
			except: 
				i = i+1
				False

	print interval_list


intervals= '[1,5],[2,6),(8,10],[8,18]'
mergeOverlapping(intervals)

	def insert(intervals, newint):
		interval_list = intervals.split(", ")
		interval_list = interval_list.append(newint):
		for x in range (0, len(interval_list)-2):
                        mergeIntervals(interval_list[x],interval_list[x+1])
                        x = x+1

our_list = input('List of intervals?')

mergeOverlapping(our_list)

for i in (0, 100):
        int_prompt = input('Interval?')
        if int_prompt == 'quit' or 'Quit' or 'QUIT' or 'q':
                break
        else:
                try:
                        our_list = insert(our_list, int_promt)
                        print our_list
                except:
                        print "Interval entered wrong format"
