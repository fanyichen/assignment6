import sys
from interval import *

class MergeError(Exception): pass


def mergeInterval(int1, int2):
    '''Merge two intervals if they are overlapping or adjacent. '''
    if int1.actual_left <= int2.actual_left:
        if int2.actual_right <= int1.actual_right:
            merged_interval = int1
        elif int2.actual_left <= int1.actual_right + 1:  
            merged_interval = interval(int1.left_bound + str(int1.left) + ',' + str(int2.right) + int2.right_bound)
        else:
            raise MergeError #raise error if two interval cannot be meged
    else:
        if int1.actual_right <= int2.actual_right:
            merged_interval = int2
        elif int1.actual_left <= int2.actual_right +1:
            merged_interval = interval(int2.left_bound + str(int2.left) + ',' + str(int1.right) + int1.right_bound)
        else:
            raise MergeError#raise error if two interval cannot be meged
    return merged_interval


def mergeOverlapping(intervals):
    '''Merge all overlapping and adjacent intervals from a list of intervals '''
    #sort intervals by its lower bound
    intervals.sort(key = lambda interval: interval.actual_left)
    #create a new list of intervals and initial with the first element in the given interval
    merged_intervals = intervals[0:1]   
    
    #walk through each interval i in the list and merge with intervals in merged_interval list
    for i in intervals[1:]:
        remove_indices = [] 
        for n, j in enumerate(merged_intervals):
            try: 
                merged_interval = mergeInterval(i,j)
                i = merged_interval  
                remove_indices.append(n)
            except MergeError:
                continue    
        merged_intervals.append(i)
        for index in remove_indices:
            merged_intervals.pop(index) 
    
    merged_intervals.sort(key = lambda interval: interval.actual_left)
    
    return merged_intervals


def insert(intervals, newint):
    '''insert a new interval to a interval list and merge it with the intervals in the list'''
    index = -1
    remove_indices = []
    for n, i in enumerate(intervals):
        try:
            newint = mergeInterval(i, newint)
            if index == -1:
                index = n
            else:
                remove_indices.append(n)
        except MergeError:
            continue    
    intervals[index] = newint
    for n in remove_indices:
        intervals.pop(n)
        
    return intervals


def print_interval_list(intervals):
    '''Print the list of intervals to console'''
    for i in intervals:
        if intervals.index(i) != 0:
            print ',',
        i.print_int()
    print
    
    
def read_intervals(user_input):
    '''Validate the format of user input and return a list of interval objects if the input is valid 
    otherwise raise an exception'''
    intervals = []
    temp = ''
    valid_input = '0123456789-,'
    for char in user_input:
        if char in '[(':
            temp = char    
        elif char in valid_input:
            temp = temp + char
        elif char in '])':
            temp = temp + char
            try:
                temp_int = interval(temp)
                intervals.append(temp_int)
            except ValidationError:
                intervals = []
                break
            temp = ''
    return intervals
    
    
def read_interval(user_input):
    '''Validate the format of user input and return a interval object if the input is valid 
    otherwise raise an exception'''
    temp = ''
    valid_input = '0123456789-,'
    temp_int = None
    for char in user_input:
        if char in '[(':
            temp = char    
        elif char in valid_input:
            temp = temp + char
        elif char in '])':
            temp = temp + char
            try:
                temp_int = interval(temp)
            except ValidationError:
                continue
            break
                #raise ValidationError
    if temp_int == None:
        raise ValidationError
    else:
        return temp_int
    
def main():
    intervals = []
    while intervals == []:
        #Ask user for a list of intervals 
        user_input = raw_input("List of intervals?")  
        if user_input == 'quit':
            sys.exit()      
        else:
            intervals = read_intervals(user_input)
            if intervals == []:
                print "Invalid intervals"
            
    #Merge overlaping intervals in the list  
    intervals = mergeOverlapping(intervals)
    
    #ask user for additional intervals and insert into the interval list till 'quit' entered    
    user_input = raw_input("Interval?")
    while user_input != 'quit':
        try:
            newint = read_interval(user_input)
            insert(intervals, newint)
            print_interval_list(intervals)
        except ValidationError:
            print "Invalid interval"
        user_input = raw_input("Interval?")
    sys.exit()
        

if __name__ == "__main__":
    main()


