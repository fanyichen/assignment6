import interval
import sys
from interval import mergeIntervals, mergeOverlapping, insert, canMerge, interval

try:


    while True:
        x = raw_input('List of intervals? ')
        if x == 'quit':
            sys.exit()
        try:
            temp = x.split(', ')
            result = [interval(i) for i in temp]
            break
        except ValueError:
            print "Invalid Intervals.Expected input format: [1,2], [3,4]"

    while True:
        y = raw_input('Intervals? ')
        if y == 'quit':
            sys.exit()
        try:
            newint = interval(y)
        except ValueError:
            print "Invalid Interval. Incorrect: Lower and upper bounds"
        else:
            result = insert(result, newint)
            str_result = [str(i) for i in result]
            print ', '.join(str_result)

except KeyboardInterrupt, EOFError, ValueError:
    print "\n Interrupted!"
