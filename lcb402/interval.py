class interval:
        # represents the range of intergers between a lower and upper bound
        # either of the bounds can be "inclusive" or "exclusive"
        # can be begative or positive
        # both inclusive : lower <= upper
        # inclusive and exclusive : lower < upper
        # both exclusive: lower < upper-1

        def __init__(self,interval):
		interval = self.interval_string
		if self.interval_string[0] == "(":
			self.lower_bound_meta = "ex"
		elif self.interval_string[0] == "[":
			self.lower_bound_meta = "in"
		else:
			print "Interval not formatted correctly (1)"
		if self.interval_string[-1] == ")":
			self.upper_bound_meta = "ex"
		elif self.interval_string[-1] == "]":
			self.upper_bound_meta == "in"
		else: 
			print "Interval not formatted correctly (2)"

		self.interval_numbs = [int(i) for i in self.interval_string_.split() if i.isdigit()]
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

		if self.inteval_max > self.interval_min:
			print "Cool interval"
		else:
			print "Interval not formatted correctly (4)"

	def mergeIntervals(int1,int2):
		int1.range = range(int1.interval_min, int1.interval_max+1)
		int2.range = range(int2.interval_min, int2_interval_max+1)
		temp_merge_interval = int1.range.append(int2.range)
		temp_merge_interval = sort(numpy.unique(temp_merge_interval))
		if unique(numpy.diff(merge_interval)) == 1:
			return temp_merge_interval
		else: 
			print "Intervals could not be merged"
		
		if int1.lower_bound < int2.lower_bound:
			merge_lower_bound = int1.lower_bound
			merge_lower_bound_meta = int1.lower_bound_meta
		else:
			merge_lower_bound = int2.lower_bound 
			merge_lower_bound_meta = int2.lwoer_bound_meta
		
		if int1.upper_bound > int2.upper_bound:
			merge_upper_bound = int1.upper_bound
			merge_upper_bound_meta = int1.upper_bound_meta
		else:
			merge_upper_bound = int2.upper_bound
			merge_upper_bound_meta = int2.upper_bound_meta

		merge_interval = merge_lower_bound_meta + str(merge_lower_bound) + "," + str(merge_upper_bound) + merge_upper_bound_beta
		return merge_interval

	def mergeOverlapping(intervals):
		interval_list = intervals.split(", ")
		for x in range (0, len(interval_list)-2):
			mergeIntervals(interval_list[x],interval_list[x+1])
			x = x+1

	def insert(intervals, newint):
		interval_list = intervals.split(", ")
		interval_list = interval_list.append(newint):
		for x in range (0, len(interval_list)-2):
                        mergeIntervals(interval_list[x],interval_list[x+1])
                        x = x+1




			

