import re
import operator

class Interval(object):  
             
    
    def __init__(self, string_interval):
        #initialize attributes
        self.string_rep = string_interval
        self.lower_bound = 0
        self.upper_bound = 0
        self.lower_bound_inclusive = False
        self.upper_bound_inclusive = False
    
        pattern = '(\(|\[)(-?\d+),(-?\d+)(\)|\])'    
        match = re.search(pattern, string_interval)
        #search string input for interval
        if not match:
            raise ValueError 
            print 'Please enter valid interval.'
        if match:
            self.lower_bound = int(match.group(2))
            self.upper_bound = int(match.group(3))
            self.lower_bound_inclusive = (match.group(1) == '[')
            self.upper_bound_inclusive = (match.group(4) == ']')
            
        #test to see if interval is valid interval      
        if self.lower_bound_inclusive == self.upper_bound_inclusive:
            if self.lower_bound_inclusive == True:
                if not self.lower_bound <= self.upper_bound:
                    print 'Please enter a valid interval'   
                    raise ValueError
            else:
                if not self.lower_bound < (self.upper_bound - 1):
                    print 'Please enter a valid interval'
                    raise ValueError                
                                    
        if self.lower_bound_inclusive != self.upper_bound_inclusive:
            if not self.lower_bound < self.upper_bound:
                print 'Please enter a valid interval' 
                raise ValueError
                
        #set the real upper and lower bounds        
        if self.lower_bound_inclusive == False:
            self.real_lower_bound = self.lower_bound + 1
        if self.upper_bound_inclusive == False:
            self.real_upper_bound = self.upper_bound - 1 
        if self.lower_bound_inclusive == True:
            self.real_lower_bound = self.lower_bound
        if self.upper_bound_inclusive == True:    
            self.real_upper_bound = self.upper_bound           
                           
    def __rep__(self):
        return self.string_rep


def mergeIntervals(int1, int2):
    '''function to merge two overlapping or adjacent intervals. 
    If intervals are disjoint, function will raise ValueError'''
    
    if int1.lower_bound > int2.lower_bound:
        s = int2
        int2 = int1
        int1 = s         
    
    Real_upper_bound = max(int1.real_upper_bound, int2.real_upper_bound)
    Real_lower_bound = min(int1.real_lower_bound, int2.real_lower_bound)
        
    if int1.real_upper_bound >= int2.real_lower_bound - 2:
        merged_interval = "[" + str(Real_lower_bound) + "," + str(Real_upper_bound) + "]" 
        return Interval(merged_interval)  
    else:
        raise ValueError
 
        
  
def mergeOverlapping(intervals):
    '''mergeOverlapping function takes a list of intervals 
    and merges intervals that are overlapping or adjacent. Returns
    new merged list'''
    
    intervals.sort(key = lambda x: x.lower_bound)
    overlaps = True
    while overlaps:
        overlaps = False
        for i in range(0,len(intervals)-1):
            if(i < len(intervals) - 1):
                try:
                    mergeIntervals(intervals[i], intervals[i+1])
                except:
                    continue
                else:
                    intervals.insert(i, mergeIntervals(intervals[i],intervals[i+1]))
                    intervals.remove(intervals[i+1])
                    intervals.remove(intervals[i+1])
                    overlaps = True
    return intervals



def insert(intervals, new_int):
    '''insert function takes a list of intervals and a separate interval as arguments, 
    and returns a list of all arguments, merging if necessary'''
    
    intervals.append(new_int)
    mergeOverlapping(intervals)
    intervals.sort(key = lambda x: x.lower_bound)
    return intervals
