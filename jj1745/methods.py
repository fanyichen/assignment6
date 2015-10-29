'''
Created on Oct 29, 2015

@author: jj1745
'''
import intervals
from intervals import interval

class MergeError(Exception):
    pass

def mergeIntervals(int1, int2):
    '''
    Merge two overlapping intervals. Raise error if they are not adjacent
    '''
    if int1.starting_value <= int2.ending_value:
        if int1.ending_value <= int2.ending_value:
            return int2
        else:
            return interval(int2.lower_bound + str(int2.input_value[0]) + ',' + str(int1.input_value[1]) + int1.upper_bound)
    elif int2.starting_value <= int1.ending_value:
        if int2.ending_value <= int1.ending_value:
            return int1
        else:
            return interval(int1.lower_bound + str(int1.input_value[0]) + ',' + str(int2.input_value[1]) + int2.upper_bound)
    else:
        raise MergeError
        
        
def mergeOverlapping(intervals):
    '''
    Try to merge a list of intervals. If cannot merge, just append it at the end of the output list
    '''
    intervals.sort(key = lambda ints:ints.starting_value)
    if len(intervals) == 0:
        raise MergeError
    elif len(intervals) == 1:
        return intervals[0]
    else:
        merged = [intervals[0], intervals[1]]
        for i in intervals[1:]:
            marked = []
            for ind, j in enumerate(merged):
                try: 
                    i = mergeIntervals(i, j)
                    marked.append(ind)
                except MergeError:
                    pass
            merged.append(i)

        
        return merged
        

def insert(intervals,newint):
    '''
    add a new intervals to the existing list. Merge if possible
    '''
    intervals.append(newint)
    return mergeOverlapping(intervals)
                                        
    
        
        
        
        