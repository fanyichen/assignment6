#Auther: Xing Cui
#NetID: xc918
#Reference: github, Google.
#Date: Oct.28 2015

import sys
from interval import *



try:
    while True:
        inputIntervalList = []
        inputIntervals = raw_input('Please enter a list of intervals or type "quit" to exit. ')
        if inputIntervals == 'quit':
            print "Thank you for using me. Bye~"
            sys.exit()
        
        
        try:
            #put all input intervals into a list to be merged.
            inputIntervals_split = inputIntervals.split(' ')
            for i in inputIntervals_split:
                int_i = interval(i)
                inputIntervalList.append(int_i)
            inputIntervalList = mergeOverlapping(inputIntervalList)
            break
        except ValidationError:
            print "Invalid input. Example: [1,2],(1,3),(2,5],[3,4]." 
    

    while True:
        #add one more interval to merge.
        singleInterval = raw_input('Add an interval? ')
        if singleInterval == 'quit':
            print "Thank you for using me. Bye~"
            sys.exit()
           
        try:
            newint = interval(singleInterval)
            result = insert(inputIntervalList, newint)
            stringResults = [i.inputIntervalString for i in result]
            print ', '.join(stringResults)
        except ValidationError:
            print "Invalid Interval. Incorrect: Lower and upper bounds"

#if something goes wrong, it makes people oops.            
except ValidationError:
    print "Oops! Wrong"


