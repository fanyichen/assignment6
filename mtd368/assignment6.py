import interval
import sys
import re
from interval import Interval, insert

# This try/except design I discussed with Sida because I was struggling with how to start the program. I tride mimicking what was in Adventure and failed.

try:
    while True:
        userinput = raw_input('List of intervals? ')
        userWantsToQuit = re.match("quit", userinput)
        if userWantsToQuit != None:
            sys.exit()
        try:
            splitinput = userinput.split(', ')
            acceptableInterval = [Interval(i) for i in splitinput]
            break
        except Exception as e: raise

    while True:
        userinput = raw_input('Intervals? ')
        userWantsToQuit = re.match("quit", userinput)
        if userWantsToQuit != None:
            sys.exit()
        try:
            newInterval = Interval(userinput)
        except Exception as e: raise
        else:
            acceptableInterval = insert(acceptableInterval, newInterval)
            printableListOfIntervalsAsStrings = [str(i) for i in acceptableInterval]
            print ', '.join(printableListOfIntervalsAsStrings)

except KeyboardInterrupt, ValueError:
    print "\n Interrupted!"
except EOFError:
    print "\n Interrupted!"