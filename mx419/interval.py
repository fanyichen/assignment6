"""this module define the class interval and three functions to realize the merge operation"""
'''Author: Muhe Xie  ID:mx419'''

import re
from user_defined_exceptions import *

'''This class represent a single interval like (3,6]'''
class interval(object):
    #take a string as input
    def __init__(self,interval_string): #constructor takes a string like '[1,4]' as input
        self.interval_str = interval_string
        lowertmp, uppertmp = re.findall(r'[-]{0,1}[0-9]+', interval_string)  #use regular expression to extract the bound
        self.lower = int(lowertmp)			#lower bound, if the interval is '(4,7)', the lower bound is 4
        self.true_lower = self.lower        #true lower bound, if the interval is '(4,7)', the true lower bound should be 5 after check
        self.upper = int(uppertmp)			#upper bound, if the interval is '(4,7)', the upper bound is 7
        self.true_upper = self.upper     	#true upper bound, if the interval is '(4,7)', the true upper bound should be 6 after check
        self.lower_bound_type, self.upper_bound_type = re.findall(r'[\(\[\]\)]',interval_string) #use regular expression to extract the bound type
        if self.lower_bound_type == '(':
            self.true_lower = self.lower +1
        if self.upper_bound_type == ')':
            self.true_upper = self.upper -1
        if self.true_upper < self.true_lower:
            raise Bound_Error
    def __repr__(self):                  	#print format
        return self.lower_bound_type  + str(self.lower) + ',' + str(self.upper) + self.upper_bound_type




'''This function take two intervals as parameter, return the merged interval if they overlap, other wise raise Exception'''
def mergeIntervals(int1, int2):
    if int1.true_lower > int2.true_lower: 	#swap the order if int1's real lower bound is bigger 
        inttmp = int1
        int1 = int2 
        int2 = inttmp
    if int1.true_upper < int2.true_lower-1: # not overlap
        raise Not_Overlap_Error
    elif int1.true_upper  == int2.true_lower-1:
        int1.upper = int2.upper
        int1.true_upper = int2.true_upper
        int1.upper_bound_type = int2.upper_bound_type
        return int1
    elif  int1.true_upper <= int2.true_upper:
        int1.upper = int2.upper
        int1.true_upper = int2.true_upper
        int1.upper_bound_type = int2.upper_bound_type
        return int1
    else:
        return int1
    
'''This function take a list of intervals as parameter, return the interval list after merging the overlap intervals  '''
def mergeOverlapping(intervals):
    sorted_intervals_tmp = sorted(intervals,key= lambda x:x.true_lower) #a temporary variable to store the sorted list
    new_intervals_list = [] # an empty list to put in the intervals after merge
    for i in range(len(sorted_intervals_tmp)):
        if len(new_intervals_list) == 0:
            new_intervals_list.append(sorted_intervals_tmp[i]) #insert the first interval to the empty list
        else:
            try:
                merged_result_of_two_intervals = mergeIntervals(new_intervals_list[-1],sorted_intervals_tmp[i]) #merge intervals
                new_intervals_list.pop()
                new_intervals_list.append(merged_result_of_two_intervals)
            except Not_Overlap_Error: #if not merge, just insert the new interval
                new_intervals_list.append(sorted_intervals_tmp[i])
                
    return new_intervals_list

'''This function take a list of intervals and a new single interval as parameters, return the interval list after inserting and merging the overlap intervals  '''
def insert(intervals, newint):
    intervals.append(newint)
    return mergeOverlapping(intervals)
    
    


   