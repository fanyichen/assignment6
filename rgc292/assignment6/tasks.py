'''
Created on Oct 22, 2015

@author: Rafael Garcia (rgc292)
'''
from user_exception import Raised_exception

class Task(object):
    '''
    This class has all functions for executing tasks over intervals and it is
     public for anyone's needs
    '''
    recurssive_break = 0
    new_interval_list = list()
    result_list = list()
    new_interval = list()
    
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
    #Merger intervals        
    def mergeIntervals(self, interval1, interval2):
        self.lower_bound1 = 0
        self.upper_bound1 = 0
        self.joined_interval = list()
        
        if ((interval1[1]) < (interval2[0] -1) or 
            (interval2[1]) < (interval1[0] -1)):
            raise (IOError, Raised_exception)
            return False
        
        else:
            if interval1[0] <= interval2[0]:
                self.lower_bound1 = interval1[0]
            else:
                self.lower_bound1 = interval2[0]
            
            if interval1[1] >= interval2[1]:
                self.upper_bound1 = interval1[0]
            else:
                self.upper_bound1 = interval2[0]
        self.joined_interval.extend([self.lower_bound1,self.upper_bound1])    
        return self.joined_interval
    
    
    #Merger overlapping intervals    
    def mergeOverlapping(self, interval_list):
        global recurssive_break
        global new_interval_list
        self.first_interval = []
        self.second_interval = []
        self.lower_bound2 = 0
        self.upper_bound2 = 0
        self.count_first = -1
        self.count_second = -1
        self.new_interval_list = interval_list
        self.recurssive_break = 0
        
        if (self.recurssive_break < len(self.new_interval_list)):
            
            for item in self.new_interval_list:
                try:
                    self.first_interval[0] = item
                    self.count_first += 1
                    self.recurssive_break += 1
                
                    for item in self.new_interval_list:
                        self.second_interval[0] = item
                        self.count_second += 1
                        self.outcome = self.mergeIntervals(self.first_interval[0], 
                                                       self.second_interval[0])
                        if self.outcome != False: 
                            del self.new_interval_list[self.count_first]
                            del self.new_interval_list[self.count_second]
                            self.new_interval_list.extend(self.outcome)
                        else:
                            pass    
                        self.sorted_list = list()
                        self.fixed_interval = list()
                        
                        for item1 in self.new_interval_list:
                            self.item1 = []
                            self.item1 = item1
                            self.first_interval[0] = item[0]
                            self.sorted_list.extend(self.fixed_interval)
                            
                            for item2 in self.new_interval_list:
                                self.item2 = []
                                self.item2 = item2
                                self.second_interval[0] = item[0]
                                
                                if self.first_interval[0] < self.second_interval[0]:
                                    self.fixed_interval[0] = self.item1
                                else:
                                    self.fixed_interval[0] = self.item2  
                                     
                        self.mergeOverlapping(self.sorted_list)
                except (IndexError, Raised_exception, IOError):
                    pass       
        else:
            self.interval_list = list(self.new_interval_list)       
        return self.new_interval_list  


    #Insert a new interval into a current list of intervals
    def insert(self, new_list, new_interval):
        
        self.new_list = new_list
        self.new_list.extend(new_interval)
        global result_list
        self.result_list.extend(self.mergeOverlapping(self.new_list))
        return self.result_list
    
    
    #Reset variables for new routine
    def clear_list(self):
        global recurssive_break
        global new_interval_list
        global result_list
        global new_interval
        self.recurssive_break = 0
        del self.new_interval_list[:]
        del self.result_list[:]
        del self.new_interval[:]
        
    
            
            
            
            
            
            
            
            
            
            
        