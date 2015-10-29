'''Contains functions to operate on interval objects'''

import interval as inter
import custom_exceptions as cexcep

def returnInIncreasingOrder(int1, int2):
	'''Returns the intervals in the increasing order according to lower bound values'''

	if int1.get_lower_bound_type == '(':
		int1_lower_bound_value = int1.get_lower_bound_value() + 1
	else:
		int1_lower_bound_value = int1.get_lower_bound_value()

	if int2.get_lower_bound_type == '(':
		int2_lower_bound_value = int2.get_lower_bound_value() + 1
	else:
		int2_lower_bound_value = int2.get_lower_bound_value()

	# Check which interval has the least lower bound and return the appropriate order
	if int1_lower_bound_value > int2_lower_bound_value:
		return int2, int1 
	return int1, int2

def mergeIntervals(old_int1, old_int2):
	'''Merging overlapping and adjacent intervals'''
	# Assumption : int1 has the least lower bound. 
	# If not, the intervals are swapped to make so

	int1, int2 = returnInIncreasingOrder(old_int1, old_int2) 

	if int1.get_upper_bound_type() == ')':
		int1_upper_bound_value = int1.get_upper_bound_value() - 1
	else:
		int1_upper_bound_value = int1.get_upper_bound_value()
	
	if int2.get_lower_bound_type() == '(':
		int2_lower_bound_value = int2.get_lower_bound_value() + 1
	else:
		int2_lower_bound_value = int2.get_lower_bound_value()


	if (int1_upper_bound_value - int2_lower_bound_value) >= -1:		# Either adjacent or overlapping
		new_lower_bound = int1.get_lower_bound_type()  	# Dealing with open and closed intervals - lower bound
		if (int1.get_lower_bound_type() == '(' and int2.get_lower_bound_type() == '[') or (int2.get_lower_bound_type() == '(' and int1.get_lower_bound_type() == '['):
			if int1.get_lower_bound_value() == int2.get_lower_bound_value():
				new_lower_bound = '['

		new_upper_bound = int2.get_upper_bound_type()	# Dealing with open and closed intervals - upper bound
		if (int1.get_lower_bound_type() == ')' and int2.get_lower_bound_type() == ']') or (int2.get_lower_bound_type() == ')' and int1.get_lower_bound_type() == ']'):
			if int1.get_upper_bound_value() == int2.get_upper_bound_value():
				new_upper_bound = ']'

		# Knitting the final output interval object
		new_upper_bound_value = max(int2.get_upper_bound_value(), int1.get_upper_bound_value())
		new_interval = new_lower_bound + str(int1.get_lower_bound_value()) + ", " + str(new_upper_bound_value) + new_upper_bound
		new_interval_object = inter.interval(new_interval)
		return new_interval_object
	else:
		raise cexcep.IntervalRangeException("The intervals cannot be merged")

def get_lower_bound_interval(intervals):
	'''Returns the interval with the least lower bound in the list of intervals'''

	lower_bounds_list = []
	for interval in intervals:
		lower_bounds_list.append(interval.get_lower_bound_value())
	lowest_value_index = 0
	for lower_bound_index in range(1, len(lower_bounds_list)):
		if lower_bounds_list[lower_bound_index] <= lower_bounds_list[lowest_value_index]:
			lowest_value_index = lower_bound_index
	return intervals[lowest_value_index]


def sort_intervals(intervals):
	'''To sort the intervals according to the lower bound'''

	sorted_list_of_intervals = []
	for index in range(len(intervals) - 1):
		least_lower_bound_interval = get_lower_bound_interval(intervals)
		sorted_list_of_intervals.append(least_lower_bound_interval)
		intervals.remove(least_lower_bound_interval)
	sorted_list_of_intervals.append(intervals[0])
	return sorted_list_of_intervals

def mergeOverlapping(intervals):
	'''Merging overlapping intervals'''

	sorted_list_of_intervals = sort_intervals(intervals)
	merged_intervals = []
	merged_intervals.append(sorted_list_of_intervals[0])
	sorted_list_of_intervals.remove(sorted_list_of_intervals[0])
	for inter in sorted_list_of_intervals:
		try:
			stack_top = merged_intervals.pop()
			temp_merged = mergeIntervals(stack_top, inter)
			merged_intervals.append(temp_merged)
		except cexcep.IntervalRangeException:
			merged_intervals.append(stack_top)
			merged_intervals.append(inter)
		else:
			continue
	return [x for x in merged_intervals]


def insert(intervals, newint):
	'''Inserting a new interval to a list of intervals'''

	intervals.append(newint)
	new_intervals = mergeOverlapping(intervals)
	return [x for x in new_intervals]
