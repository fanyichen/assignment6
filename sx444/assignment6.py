from interval import *
import re
import operator


""" this is to execute the merge. It firstly would ask the user to inout a list of intervals 
and check if the input is valid; then ask the user to input a new interval and check also. It 
would merge the list and the interval if necessary. It would keep asking the user to input a
new interval until the user types 'quit'. """	
def mainMerge():
    while True:
        list_of_intervals = raw_input("List of intervals? ")
        if list_of_intervals == 'quit':
            return
        separated_list = re.findall(r'[[(].*?[\])]',list_of_intervals)
        if len(separated_list) == 0:
            print "Please input a list of intervals"
            continue
        if len(separated_list) == 1:
            print "Please at least input two intervals"
            continue
        intervals = []
       

        for input_interval in separated_list:
            try:
                intervals.append(interval(input_interval))
            except:
                print "Invalid input"
                break
            else:
                intervals.append(interval(input_interval))
        break
        intervals = mergeOverlapping(intervals)

    
    while True:
        input_interval = raw_input("Interval? ")
        if input_interval == 'quit':
            return
        else:
            new_interval = re.findall(r'[[(].*?[\])]', input_interval)
            try:
                new_interval = interval(new_interval[0])
            except:
                print "Invalid interval"
                continue
            else:
                intervals = insert(intervals, new_interval)
                print intervals

if __name__ == "__main__":
# identify this as the main program.
    mainMerge()
