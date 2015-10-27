'''
Created on Oct 21, 2015

@author: ds-ga-1007
'''
from interval_class import interval
import operator
import re

def mergeIntervals(int1, int2):
    ''' mergeIntervals(int1, int2) takes two interval objects
    as arguments. If the two interval objects are adjacent or
    overlapping, it merges them and returns a single, merged
    interval object that containst the union of the two input
    integer intervals.'''
    if (len(set(int1.integers) & set(int2.integers)) > 0):
        if  int1.lower_limit < int2.lower_limit:
           merged_interval = int1.lower_bound + str(int1.lower_limit) + ','
        elif int2.lower_limit < int1.lower_limit:
            merged_interval = int2.lower_bound + str(int2.lower_limit) + ','
        elif int1.lower_limit == int2.lower_limit:
            if (int1.lower_bound == '(' and int2.lower_bound == '('):
                merged_interval = '(' + str(int2.lower_limit) + ','
            else: 
                merged_interval = '[' + str(int2.lower_limit) + ','
                
        if  int1.upper_limit < int2.upper_limit:
            merged_interval = merged_interval + str(int2.upper_limit) + int2.upper_bound
        elif int2.upper_limit < int1.upper_limit:
            merged_interval = merged_interval + str(int1.upper_limit) + int1.upper_bound
        elif int1.upper_limit == int2.upper_limit:
            if (int1.upper_bound == ')' and int2.upper_bound == ')'):
                merged_interval = merged_interval + str(int2.upper_limit) + ')'
            else: 
                merged_interval = merged_interval + str(int2.upper_limit) + ']'

    elif ((int1.lower_bound == '[' or int2.upper_bound == ']') and\
             (int1.lower_limit == int2.upper_limit)):
        merged_interval = int2.lower_bound + str(int2.lower_limit) + ',' + str(int1.upper_limit) + int1.upper_bound
    
    elif ((int1.upper_bound == ']' or int2.lower_bound == '[') and\
             (int1.upper_limit == int2.lower_limit)):
        merged_interval = int1.lower_bound + str(int1.lower_limit) + ',' + str(int2.upper_limit) + int2.upper_bound

    elif ((int1.lower_bound == '[' and int2.upper_bound == ']') and\
             (int1.lower_limit - 1 == int2.upper_limit)):
        merged_interval = int2.lower_bound + str(int2.lower_limit) + ',' + str(int1.upper_limit) + int1.upper_bound

    elif ((int1.upper_bound == ']' and int2.lower_bound == '[') and\
             (int1.upper_limit + 1 == int2.lower_limit)):
        merged_interval = int1.lower_bound + str(int1.lower_limit) + ',' + str(int2.upper_limit) + int2.upper_bound
        
    else:
        raise ValueError('The two input intervals do not overlap')
    
    return interval(merged_interval)

def mergeOverlapping(intervals):
    ''' mergeOverlapping(intervals) takes a list of interval objects
    as an argument. It then completes all possible merges on
    intervals contained within this list, and returns a new list
    of disjoint (defined in this context as non-overlapping and
    non-adjacent) intervals.'''
    overlap = 'found'
    while overlap == 'found':
        overlap = None
        intervals = sorted(intervals, key=operator.attrgetter('lower_limit'))
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                try:
                    mergeIntervals(intervals[i], intervals[j])
                except:
                    continue
                else:
                    overlap = 'found'
                    new_int = mergeIntervals(intervals[i],intervals[j])
                    intervals.remove(intervals[i])
                    intervals.remove(intervals[j-1])
                    intervals.append(new_int)
    return intervals

def insert(intervals, newint):
    '''insert(intervals, newint) inserts the new interval 'newint' into
    the list of intervals 'intervals'. Then it completes all possible
    merges before returning a of disjoint (defined in this context as
    non-overlapping and non-adjacent) intervals..'''
    intervals.append(newint)
    return mergeOverlapping(intervals)

def user_input_function():
    '''user_input_function() takes no arguments. Instead, it gets a
    keyboard input list of intervals from the caller. Then, it repeatedly
    gets a new interval from the caller and inserts this new interval
    into the list, finally printing the merged list to the screen. It
    quits upon keyboard input 'quit'.'''
    need_input = True
    while need_input:
        list_of_intervals = raw_input("List of intervals? ")
        if list_of_intervals == 'quit':
            return
        split_list = re.findall(r'[[(].*?[\])]',list_of_intervals)
        if len(split_list) == 0:
            print "No intervals in input list- try again"
            continue
        intervals = []
        need_input = False
        for input_interval in split_list:
            try:
                intervals.append(interval(input_interval))
            except:
                print "Invalid interval in list- try again"
                need_input = True
                break
            else:
                intervals.append(interval(input_interval))
        intervals = mergeOverlapping(intervals)
    
    while True:
        new_interval = raw_input("Interval? ")
        if new_interval == 'quit':
            return
        else:
            processed_interval = re.findall(r'[[(].*?[\])]',new_interval)
            try:
                processed_interval = interval(processed_interval[0])
            except:
                print "Invalid interval"
                continue
            else:
                intervals = insert(intervals, processed_interval)
                print intervals

user_input_function()