'''
Created on Oct 29, 2015

@author: up276
'''
import re

class Interval:
        
    merge_flag=False  #variable to check whether merge happened for set of intervals or not
    def __init__(self, interval_str):
        
        #print "str = ",self.str1

        try:
            self.interval_string = interval_str  
            self.validate_string_and_compute_bounds(self.interval_string)
        except:
            print "error in entered string"


    def validate_string_and_compute_bounds(self,interval_str):
        """
        This function receives the intervals and set the real lower and upper bound
        """
        try:
            interval_string= interval_str
            pattern = '(\(|\[)(-?\d+),(-?\d+)(\)|\])'
            ival_format = False
            m=re.search(pattern,interval_string)
            
            if(m!=None):
                    
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
                
                
                if ((self.LowerBoundInclusive == True and self.UpperBoundInclusive == True) 
                    and (self.LowerBound<=self.UpperBound)):
                    ival_format = True
                    self.RealLowerBound = self.LowerBound
                    self.RealUpperBound = self.UpperBound
                   
                if ((self.LowerBoundInclusive == True and self.UpperBoundInclusive == False)
                      and self.LowerBound<self.UpperBound):
                    ival_format = True
                    self.RealLowerBound = self.LowerBound
                    self.RealUpperBound = self.UpperBound-1
                    
                if (((self.LowerBoundInclusive == False and self.UpperBoundInclusive == True)) 
                      and self.LowerBound<self.UpperBound):
                    ival_format = True
                    self.RealLowerBound = self.LowerBound+1
                    self.RealUpperBound = self.UpperBound
                    
                if (((self.LowerBoundInclusive == False) and (self.UpperBoundInclusive == False)) and (self.LowerBound<
    ((self.UpperBound)-1))):
                    ival_format = True
                    self.RealLowerBound = self.LowerBound+1
                    self.RealUpperBound = self.UpperBound-1
        
                
            else:
                print("Bad Format")     
            
        
        except:
            print "error in Validating string"   
    
    @staticmethod
    def mergeIntervals(interval1, interval2):
        """
        This function receives the set of two intervals and perform the merge if possible
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
            else:
                raise
        except:
       
            return "bad intervals"
            
    @staticmethod
    def mergeOverlapping(intervals):
        """
        This function receives the whole set of intervals and perform the merge by calling mergeInterval 
        function for set of two intervals
        """
        try:
            merging_window_index=0
            for i in range(len(intervals)-1):
                #print i,"th element",intervals[i].str1
                merged_interval=Interval.mergeIntervals(intervals[merging_window_index],intervals[merging_window_index+1])            
                #print Interval.merge_flag
                #print"in4"
                if Interval.merge_flag:
                    intervals.pop(merging_window_index)
                    intervals.pop(merging_window_index)
                    intervals.append(merged_interval)
                else:
                    merging_window_index=merging_window_index+1
                intervals.sort(key=lambda x: x.RealLowerBound)
    
            return intervals
        except:
            print "error in overlapping intervals"      
    
    #@staticmethod
    #def insert(intervals,new_interval):
    #    """
    #    This function receives the whole set of intervals & new interval then 
    #    append it in the interval list
    #    """
    #    try:
    #        intervals.append(new_interval)
    #        intervals.sort(key=lambda x: x.RealLowerBound)
    #        intervals=Interval.mergeOverlapping(new_interval)
    #        #print "list elements after overlapping"
    #        for i in range(len(intervals)):
    #            print intervals[i].str1,
    #        return intervals
