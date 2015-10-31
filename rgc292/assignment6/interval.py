'''
Created on Oct 22, 2015

@author: Rafael Garcia (rgc292)
'''
import re as re
import sys
import readline

class Interval(object):
    '''
    This class represents the range of integers between a 
    lower bound and an upper bound guaranteeing its formatted requirements. 
    This class is public for anyone's needs 
    '''
    #Variables grouping intervals 
    input_interval = list()
    all_included = list()
    left_included = list()
    right_included = list()
    all_excluded = list()
    
    #Variables for determining the bounds for intervals
    all_included_bound = list()
    left_included_bound = list()
    right_included_bound = list()
    all_excluded_bound = list()
    
    #Variable that contain the interval ready for task manipulation
    all_intervals_bounds = list()
    
    
    def __init__(self, intervals):
        '''
        Constructor
        '''
        self.interval = intervals
         
         
    #Validate input        
    def check_input_format(self,intervals): 
        self.interval = intervals
        global input_interval
        flag = 1
        try:   
            self.formatted = re.search("(\[[0-9],[0-9]\])|(\[[0-9],[0-9]\))|(\([0-9],[0-9]\])|(\([0-9],[0-9]\))", self.interval)
            self.formatted.group()
            self.input_interval = re.findall("(\[[0-9],[0-9]\])|(\[[0-9],[0-9]\))|(\([0-9],[0-9]\])|(\([0-9],[0-9]\))", self.interval)     
        except EOFError:
            flag = 0
            pass    
        except KeyboardInterrupt:
            flag = 0
            pass
        except IOError:
            flag = 0
            print "Invalid input!"
        except AttributeError:
            flag = 0
            print "Invalid input!"       
        return flag  
       
       
    #Separate input among features such as included or excluded   
    def separate_by_group(self, input_intervals):
        global all_included
        global left_included
        global right_included
        global all_excluded
        self.interval_list = input_intervals 
        
        #Variable for iteration
        x = -1
        y = -1
        
        while x <= len(self.interval_list):
            x += 1
            
            try:   
                self.all_included.append(self.interval_list[x][0])
                self.left_included.append(self.interval_list[x][1])
                self.right_included.append(self.interval_list[x][2])
                self.all_excluded.append(self.interval_list[x][3])
            except IndexError:
                pass    
        
        
    #Filter intervals only 
    def remove_empty_element(self, interval):
        self.list = interval
        self.value = ''
        try:
            for element in self.list:
                self.list.remove(self.value)
            
            for element in self.list:
                self.list.remove(self.value)          
        except ValueError:
            pass
        return self.list 
    
    
    #Set the bounds per group       
    def get_bounds_allincluded(self, interval):
        self.short_list = interval
        self.lower_bound = ""
        self.upper_bound = "" 
        global all_included_bound  
        
        for element in self.short_list:
            try:
                self.lower_bound = element
                self.left = self.lower_bound.split(",")
                self.lower_bound = self.left[0]
                self.left = self.lower_bound.split("[")
                self.lower_bound = self.left[1]
                self.lower_bound = int(self.lower_bound)
                
                self.upper_bound = element
                self.right = self.upper_bound.split(",")
                self.upper_bound = self.right[1]
                self.right = self.upper_bound.split("]")
                self.upper_bound = self.right[0]
                self.upper_bound = int(self.upper_bound)
                
                self.all_included_bound.append([self.lower_bound,self.upper_bound])  
            except (ValueError, IndexError):
                pass
        
                     
    def get_bounds_leftincluded(self, interval):
        self.short_list = interval
        self.lower_bound = ""
        self.upper_bound = "" 
        global left_included_bound    
        
        for element in self.short_list:
            try:
                self.lower_bound = element
                self.left = self.lower_bound.split(",")
                self.lower_bound = self.left[0]
                self.left = self.lower_bound.split("[")
                self.lower_bound = self.left[1]
                self.lower_bound = int(self.lower_bound)
            
                self.upper_bound = element
                self.right = self.upper_bound.split(",")
                self.upper_bound = self.right[1]
                self.right = self.upper_bound.split(")")
                self.upper_bound = self.right[0]
                self.upper_bound = int(self.upper_bound)
                self.upper_bound = self.upper_bound - 1
            
                self.left_included_bound.append([self.lower_bound,self.upper_bound])
            except (ValueError, IndexError):
                pass
        
        
    def get_bounds_rightincluded(self, interval):
        self.short_list = interval
        self.lower_bound = ""
        self.upper_bound = "" 
        global right_included_bound    
        
        for element in self.short_list:
            try:
                self.lower_bound = element
                self.left = self.lower_bound.split(",")
                self.lower_bound = self.left[0]
                self.left = self.lower_bound.split("(")
                self.lower_bound = self.left[1]
                self.lower_bound = int(self.lower_bound)
                self.lower_bound = self.lower_bound - 1
            
                self.upper_bound = element
                self.right = self.upper_bound.split(",")
                self.upper_bound = self.right[1]
                self.right = self.upper_bound.split("]")
                self.upper_bound = self.right[0]
                self.upper_bound = int(self.upper_bound)
                self.upper_bound = self.upper_bound
            
                self.right_included_bound.append([self.lower_bound,self.upper_bound]) 
            except (ValueError, IndexError):
                pass
      
            
    def get_bounds_allexcluded(self, interval):
        self.short_list = interval
        self.lower_bound = ""
        self.upper_bound = "" 
        global all_excluded_bound    
        
        for element in self.short_list:
            try:
                self.lower_bound = element
                self.left = self.lower_bound.split(",")
                self.lower_bound = self.left[0]
                self.left = self.lower_bound.split("(")
                self.lower_bound = self.left[1]
                self.lower_bound = int(self.lower_bound)
                self.lower_bound = self.lower_bound - 1
            
                self.upper_bound = element
                self.right = self.upper_bound.split(",")
                self.upper_bound = self.right[1]
                self.right = self.upper_bound.split(")")
                self.upper_bound = self.right[0]
                self.upper_bound = int(self.upper_bound)
                self.upper_bound = self.upper_bound - 1

                self.all_excluded_bound.append([self.lower_bound,self.upper_bound])            
            except (ValueError, IndexError):
                pass
      
            
    #Join each group of intervals in a final one    
    def join_intervals(self, all_included, left_included, right_included, all_excluded ):     
        self.all_in = all_included
        self.left = left_included
        self.right = right_included
        self.all_ex = all_excluded
        global all_intervals_bounds
        
        self.all_intervals_bounds.extend(self.all_in)
        self.all_intervals_bounds.extend(self.left)
        self.all_intervals_bounds.extend(self.right)
        self.all_intervals_bounds.extend(self.all_ex)
      
        
    #Validate requirement between lower and upper bound     
    def validate_lower_upper(self, interval):
        self.range = interval
        self.array = []
        try:
            for element in self.range:
                self.array = element[0]
                if self.array[0] > self.array[1]:
                    print "Invalid input!"
                else:
                    pass
        except TypeError:
            pass                             
      
      
    #Reset variables for new routine  
    def clear_list(self):
        global all_intervals_bounds
        global input_interval
        global all_included
        global left_included
        global right_included
        global all_excluded
        global all_included_bound
        global left_included_bound
        global right_included_bound
        global all_excluded_bound
        
        del self.all_intervals_bounds[:] 
        del self.input_interval[:]
        del self.all_included[:]
        del self.left_included[:]
        del self.right_included[:]
        del self.all_excluded[:]
        del self.all_included_bound[:]
        del self.left_included_bound[:]
        del self.right_included_bound[:]
        del self.all_excluded_bound[:]        
        
        
        
        
    
                               
                  
                         
            
           
            
        
                
             
        
        
        
    
            
            
            
            
            
            
            
            
            
            
        