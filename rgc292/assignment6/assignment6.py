'''
Created on Oct 27, 2015

@author: Rafael Garcia (rgc292)
'''
from interval import Interval as i
from tasks import Task as tk
import readline
import sys


if __name__ == '__main__':
    pass

print "Hi! Let's play with intervals.\n"
print "I can accept intervals with these formats:\n"
print "[1,2] or (2,4) or (-3,6]"
print "A square bracket means the number is included.\n"
print "A parenthesis means the number is not included.\n"
print "Therefore, the previous example means:\n"
print "[1,2] or [1,3] or [-2,6]"
print "First, you are going to be requested to type a list of intervals:\n"
print "Please, type as many as you want separated with commas like this:\n"
print "[1,3],(5,9]"
print "At any time type exit to stop the program.\n"

user_input = ""
intervals = i(user_input)
task = tk()
flag = 0
previous_interval = list()
current_interval = list()
new_interval = list()
counter_a = 1
valid_input = ""

""" The assignment6 file is an executable program for interaction with an user
    interested on playing with intervals"""
    
while True:
    #Check input format
    counter_a += 1
    user_input = raw_input("Type your intervals: ")
    if user_input.lower() == "exit":
        print "Good bye!"
        sys.exit(1)
        
    flag = intervals.check_input_format(user_input)
    #Prepare interval for manipulation if formatted correctly
    if flag == 1:
        
        by_group = intervals.input_interval   
        intervals.separate_by_group(by_group)
        intervals.all_included = intervals.remove_empty_element(intervals.all_included)
        intervals.left_included = intervals.remove_empty_element(intervals.left_included)
        intervals.right_included = intervals.remove_empty_element(intervals.right_included)
        intervals.all_excluded = intervals.remove_empty_element(intervals.all_excluded)
        intervals.get_bounds_allincluded(intervals.all_included)
        intervals.get_bounds_leftincluded(intervals.left_included)
        intervals.get_bounds_rightincluded(intervals.right_included)
        intervals.get_bounds_allexcluded(intervals.all_excluded)
        intervals.join_intervals(intervals.all_included_bound, 
                                 intervals.left_included_bound, 
                                 intervals.right_included_bound, 
                                 intervals.all_excluded_bound)
        intervals.validate_lower_upper(intervals.all_intervals_bounds)
        
        #Counter only for first input list
        if counter_a == 2:
            previous_interval = list(intervals.all_intervals_bounds)
            print previous_interval
            intervals.clear_list()
        else:
            current_interval = list(intervals.all_intervals_bounds)   
            intervals.all_intervals_bounds = list(task.insert(previous_interval, current_interval))
            task.clear_list()
            del previous_interval[:]
            previous_interval = intervals.all_intervals_bounds
            print previous_interval 
    else:
        continue
    


       
        
       
        
        
        
        
        
        
        
        
        
        
    