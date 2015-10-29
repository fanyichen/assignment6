# This file containts all the functions for managing intervals

from interval import *
class MergeIntervalError(Exception):
	'''user-defined exception when merging is not possible'''
	def __str__(self):
		return "Merging is not possible"


def mergeIntervals(input1, input2):
	'''mergeIntervals is used to merge joint intervals'''
	int1 = interval(input1)
	int2 = interval(input2)
	merge_int = ""
	result = [int1, int2]
	result.sort(key =lambda x:x.lower, reverse = False)

	int1_set = set(int1.list)
	if len(int1_set.intersection(int2.list)) > 0 or int1.upper + 1 == int2.lower:
		if int1.lower < int2.lower : 
			merge_int += int1.string[0 : int1.comma_index]
		elif int2.lower < int1.lower : 
			merge_int += int2.string[0 : int2.comma_index]
		elif int1.lower == int2.lower :
			if int1.string[0] == int2.string[0]:
				merge_int += int1.string[0 : int1.comma_index]
			elif int1.string[0] != int2.string[0]:
				if int1.left < int2.left:
					merge_int += int1.string[0 : int1.comma_index]
				elif int1.left > int2.left:
					merge_int += int1.string[0 : int2.comma_index]
		if int1.upper > int2.upper:
			merge_int += int1.string[int1.comma_index : ]
		elif int2.upper > int1.upper:
			merge_int += int2.string[int2.comma_index : ]
		elif int1.upper == int2.upper or int1.upper + 1 == int2.upper:
			if int1.string[-1] == int2.string[-1]:
				merge_int += int1.string[int1.comma_index : ]
			elif int1.string[-1] != int2.string[-1]:
				if int1.right > int2.right:
					merge_int += int1.string[int1.comma_index:]
				elif int1.right < int2.right:
					merge_int += int2.string[int2.comma_index:]
		return merge_int
	else:
 		raise MergeIntervalError


def mergeOverlapping(intervals):
	''' mergeOverlapping is used to merge overlapping intervals in a list'''
	ints = [interval(element) for element in intervals if element]
	ints.sort(key = lambda x:x.lower, reverse = False)
	sets = [set(element.list) for element in ints if element]
	results = [element.string for element in ints if element]
	i = 0
	while i < len(sets):
		j = i+1
		while j < len(sets):
			if len(sets[i].intersection(sets[j])) > 0 or (ints[i].upper + 1 == ints[j].lower):
				sets[i] = sets[i].union(sets[j])
				results[i] = mergeIntervals(ints[i].string,ints[j].string)
				sets.pop(j)
				ints.pop(j)
				results.pop(j)
				ints = [interval(element) for element in results if element]
			else: j += 1                       
		i += 1
	return results

def insert(intervals, newint):
	''' insert is to intert a new interval to a list of nonoverlapping intervals and merge if possible'''
	intervals.append(newint)
	merge_lst = mergeOverlapping(intervals)
	ints = [interval(element) for element in merge_lst if element]
	results = [element.string for element in ints if element]
	return results
