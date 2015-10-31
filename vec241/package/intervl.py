# -*- coding: utf-8 -*-
'''
This modules defines the class interval and various operations possibles on intervals
'''

class interval(object):
    '''
    Represents the range of integers between a lower bound and an upper bound. 
    Either of the bounds of an interval can be “inclusive” or “exclusive” and 
    can be positive or negative. The bounds must always meet the requirement 
    that lower <= upper if both bounds are inclusive, lower < upper if one bound 
    is exclusive and one inclusive, or lower < upper-1  if both are exclusive
    ''' 

    def __init__(self, input_interval):
        '''
        Constructor of the interval. 
        '''
                
        import re
        import types
        
        interval_format = "^[\[\(]([0-9]+),([0-9]+)[\]\)]$" 
        self.input_interval = input_interval
        
        #Makes sure the interval is valid
        try:
            assert type(self.input_interval) is types.StringType   
            if re.match(interval_format, self.input_interval) is None:
                raise ValueError("invalid input interval")
        except AssertionError:
            print("interval under string format expected. Please use '' or \"\" to define your interval")
        except ValueError:
            print("invalid input interval. The interval should be under the format: '[integer,integer]', '(integer,integer)', ...")
       
        else:    
            self.lower_bound = int(re.search(interval_format, self.input_interval).group(1))
            self.upper_bound = int(re.search(interval_format, self.input_interval).group(2))
            self.lower_delimitor = input_interval[0] # [ or (
            self.upper_delimitor = input_interval[-1] # ] or )
            
            if self.lower_delimitor == "[" and self.upper_delimitor == "]":
                try:
                    assert self.lower_bound <= self.upper_bound
                    self.lower_int = self.lower_bound
                    self.upper_int = self.upper_bound
                except AssertionError:
                    print("The lower bound has to be inferior or equal to the upper bound")
            elif self.lower_delimitor == "(" and self.upper_delimitor == ")":
                try:
                    assert self.lower_bound < self.upper_bound - 1
                    self.lower_int = self.lower_bound + 1
                    self.upper_int = self.upper_bound - 1
                except AssertionError:
                    print("The lower bound has to be strictly inferior to the upper bound - 1")
            elif self.lower_delimitor == "(" and self.upper_delimitor == "]":
                try:
                    assert self.lower_bound < self.upper_bound 
                    self.lower_int = self.lower_bound + 1
                    self.upper_int = self.upper_bound
                except AssertionError:
                    print("The lower bound has to be strictly inferior to the upper bound")
            else:
                try:
                    assert self.lower_bound < self.upper_bound 
                    self.lower_int = self.lower_bound
                    self.upper_int = self.upper_bound - 1
                except AssertionError:
                    print("The upper bound has to be strictly inferior to the upper bound")        

         
    def __repr__(self):
        '''
        Gives the information on the interval (type value) when the object is called 
        ''' 
        
        return "{}{},{}{}".format(self.lower_delimitor, self.lower_bound, self.upper_bound, self.upper_delimitor)
 
       
    def __str__(self):
        '''
        Displays the interval when the object is printed
        ''' 
        
        return "{}{},{}{}".format(self.lower_delimitor, self.lower_bound, self.upper_bound, self.upper_delimitor)


def overlapping(int1, int2):
    '''
    Says if intervals int1 and int2 are overlapping or adjacents
    '''
    if ( (int2.lower_int <= int1.upper_int + 1 and int2.upper_int >= int1.lower_int) or (int1.lower_int <= int2.upper_int + 1 and int1.upper_int >= int2.lower_int) ):
        return True
    else:
        return False
    

def mergeIntervals(int1, int2):
    '''
    Returns a merged interval if the intervals overlap or are adjacent.
    '''
    
    try:
        #verifies if interval overlap or are adjacent
        if overlapping(int1, int2) == False:
            raise ValueError("intervals don't overlapp or are not adjacent and though cannot be merged")
    except ValueError:
        print("intervals don't overlapp or are not adjacent and though cannot be merged")
    else:
        max_int = max(int1.upper_int, int2.upper_int)
        min_int = min(int1.lower_int, int2.lower_int)            
        merged_interval = "[" + str(min_int) + "," + str(max_int) + "]"
        return interval(merged_interval)  

    
def mergeOverlapping(intervals):
    '''
    Merges overlapping or adjacent intervals for a given list of intervals 
    '''

    intervals = sorted(intervals, key=lambda interval: interval.lower_int)
    merged_intervals = [] #list of the merged intervals we are going to return
    
    #merges the overlapping/adjacent intervals
    while len(intervals) > 1: 
        merged_interval = intervals[0]
        merged_intervals_index = [0]
        
        for i in range(1, len(intervals)):
            if overlapping(merged_interval, intervals[i]):
                merged_interval = mergeIntervals(merged_interval, intervals[i])
                merged_intervals_index.append(i)
        
        merged_intervals.append(merged_interval)
        merged_intervals_index.sort(reverse=True)
        for k in merged_intervals_index:
            del intervals[k]             

    if len(intervals) == 1: #in case last interval could not be merged
        merged_intervals.append(intervals[0])
        
    return merged_intervals


def insert(intervals, newint):
    '''
    Inserts interval newint into list of intervals, merging the result if necessary.
    Intervals should be a list of non overlapping/adjacent intervals.
    '''
    try:
        merged_interval = intervals[0]
        for i in range(1, len(intervals)):
            if overlapping(merged_interval, intervals[i]):
                raise ValueError("The list of intervals provided contains overlapping interval")
    except ValueError:
        print "The list of intervals provided contains overlapping interval. Please provide a list of non overlapping intervals"   
    else:
        intervals.append(newint)
        intervals = sorted(intervals, key=lambda interval: interval.lower_int)
        intervals = mergeOverlapping(intervals)
        return intervals      
        