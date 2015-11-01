'''
Created on Oct 29, 2015

@author: up276
'''
import re

#class to hadle the Exceptions
class Interval_Exception(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Interval:
        
    merge_flag=False  #variable to check whether merge happened for set of intervals or not
    def __init__(self, interval_str):
        
            self.interval_string = interval_str  
            self.validate_string_and_compute_bounds(self.interval_string)

    def validate_string_and_compute_bounds(self,interval_str):
        """
        This function receives the intervals and compute the real lower and upper bound
        """
        interval_string= interval_str
        pattern = '(\(|\[)(-?\d+),(-?\d+)(\)|\])'    #pattern to check whether received inteval format is correct or not
        m=re.search(pattern,interval_string)         #compares the user input with the pattern and sets group values
        
        #if received input's format is incorrect then value of 'm' will be NULL
        #so in that case it will directly go into else part, otherwise it will check for values and bounds
        if(m!=None):
            try:    
                self.LowerBound = m.group(2)
                self.UpperBound = m.group(3)
                self.LowerBound = int(self.LowerBound)
                self.UpperBound = int(self.UpperBound)
                if (m.group(1)=='['):
                    self.LowerBoundInclusive = True
                    
                if (m.group(1)=='('):
                    self.LowerBoundInclusive = False
                   
                if (m.group(4)==']'):
                    self.UpperBoundInclusive = True
                   
                if (m.group(4)==')'):
                    self.UpperBoundInclusive = False
      
                if ((self.LowerBoundInclusive == True and self.UpperBoundInclusive == True)):
             
                    self.RealLowerBound = self.LowerBound
                    self.RealUpperBound = self.UpperBound
                  
                   
                if ((self.LowerBoundInclusive == True and self.UpperBoundInclusive == False)):
                   
                    self.RealLowerBound = self.LowerBound
                    self.RealUpperBound = self.UpperBound-1
                    
                    
                if (((self.LowerBoundInclusive == False and self.UpperBoundInclusive == True))):
                   
                    self.RealLowerBound = self.LowerBound+1
                    self.RealUpperBound = self.UpperBound
                  
                    
                if (((self.LowerBoundInclusive == False) and (self.UpperBoundInclusive == False))):
                 
                    self.RealLowerBound = self.LowerBound+1
                    self.RealUpperBound = self.UpperBound-1
             
                
                if (self.RealLowerBound>self.RealUpperBound):            
                    raise Interval_Exception("Invalid interval")
                
            except:     
                raise Interval_Exception("Invalid interval")
            
        else:
            raise Interval_Exception("Invalid interval")
            
 
    @staticmethod
    def mergeIntervals(interval1, interval2):
        """
        This function receives the set of two intervals and perform the merge if possible
        It is being called from mergeOverlapping function and returns merged interval 
        """
        try:
            Interval.merge_flag=False
            if (interval1.RealUpperBound >= (interval2.RealLowerBound-1)):
                
                if (interval1.RealLowerBound<=interval2.RealLowerBound):
                    new_lower_bound = interval1.LowerBound
                  
                    if interval1.LowerBoundInclusive:
                        new_lower_bound_character = '['
                    else:
                        new_lower_bound_character = '('
                else:
                    
                    new_lower_bound = interval2.LowerBound
                    if interval2.LowerBoundInclusive:
                        new_lower_bound_character = '['
                    else:
                        new_lower_bound_character = '('
    
                if (interval1.RealUpperBound>=interval2.RealUpperBound):
                    new_upper_bound = interval1.UpperBound
                    if interval1.UpperBoundInclusive:
                        new_upper_bound_character = ']'
                    else:
                        new_upper_bound_character = ')'
                else:
                    new_upper_bound = interval2.UpperBound
                    
                    if interval2.UpperBoundInclusive:
                        new_upper_bound_character = ']'
                    else:
                        new_upper_bound_character = ')'
    
    
                Interval.merge_flag=True
                NewInterval = Interval("{0}{1},{2}{3}".format(new_lower_bound_character,new_lower_bound,new_upper_bound,new_upper_bound_character))
                return NewInterval
   
        except:    
            raise Interval_Exception("Error in merging two intervals")
            
    @staticmethod
    def mergeOverlapping(intervals):
        """
        This function receives the whole set of intervals and perform the merge by calling mergeInterval 
        function for set of two intervals.This is being called from Insert function and returns the new list 
        after merging all possible intervals
        """
        try:
            merging_window_index=0        #Local variable which holds the list index for merging the set of intervals one by one
            for i in range(len(intervals)-1):

                merged_interval=Interval.mergeIntervals(intervals[merging_window_index],intervals[merging_window_index+1])            
                
                #if Merging occurs for the set of intervals then below code will relace old intervals with the new one in the list
                if Interval.merge_flag:
                    intervals.pop(merging_window_index)
                    intervals.pop(merging_window_index)
                    intervals.append(merged_interval)
                else:
                    merging_window_index=merging_window_index+1
                intervals.sort(key=lambda x: x.RealLowerBound)
    
            return intervals
        except:
            raise Interval_Exception("Error in merging Overlapping intervals")      
    
    @staticmethod
    def insert(intervals,new_interval):
        """
        This function receives the whole set of intervals & new interval then 
        append it in the interval list. This is being called from main_function and returns new list after 
        appending new interval and checking for possible merge
        """
        try:
            intervals.append(new_interval)
            intervals.sort(key=lambda x: x.RealLowerBound)
            return Interval.mergeOverlapping(intervals)
        except:
            raise Interval_Exception("error in inserting interval")
