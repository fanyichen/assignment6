import intervalevaluation
import sys
import re
from intervalevaluation import Interval, insert

# This try/except design I discussed with Sida because I was struggling with how to start the program. I tride mimicking what was in Adventure and failed.

if __name__ == '__main__':
    try:
        while True:
            userinput = raw_input('List of intervals? ')
            userWantsToQuit = re.match("quit", userinput)
            if userWantsToQuit != None:
                sys.exit()
            try:
                splitinput = userinput.split(', ')
                acceptableIntervals = [Interval(i) for i in splitinput]
                break
            except Exception as e: raise

        while True:
            userinput = raw_input('Intervals? ')
            userWantsToQuit = re.match("quit", userinput)
            if userWantsToQuit != None:
                sys.exit()
            try:
                newInterval = Interval(userinput) #validate using constructor of Interval class that it is a valid interval.
            except ValueError:
                print "Invalid Interval"
            else:
                finalAcceptableIntervals = insert(acceptableIntervals, newInterval)
                printableListOfIntervalsAsStrings = [str(i) for i in finalAcceptableIntervals]
                print ', '.join(printableListOfIntervalsAsStrings)
    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"
