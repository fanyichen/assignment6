'''
Created on Oct 29, 2015

@author: jj1745
'''
import sys
import intervals
from intervals import interval
from methods import *

#def print_intervals(intervals):
#    '''print the list'''
#    out = ''
#    for i in intervals:
#        if intervals.index(i) != 0:
#            out = out + ', ' + i.input
            

if __name__ == '__main__':
    
    
    lists = []
    try:
        while True:
            inputs = raw_input('List of Intervals?')
            if inputs == 'quit':
                sys.exit()
            try:
                temp = inputs.split(', ')
                lists = [interval(i) for i in temp]
                print len(lists)
                break
            except ValueError:
                print temp
                print "Invalid intervals: Please make sure you use comma and one whitespace between intervals"
            
        while True:
            inputs = raw_input('Intervals?')
            if inputs == 'quit':
                sys.exit()
            try:
                # print input
                newint = interval(inputs)
            except ValueError:
                print "Invalid Interval: make sure your input is a proper interval"
            else:
                output = insert(lists, newint)
                print len(output)
                strings = [i.input for i in output]
                print ', '.join(strings)                  
            
    except MergeError:
        print "There is merge error"
