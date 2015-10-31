import sys
from Functions import *

IntervalInput = []

while True:
    if not IntervalInput:
        IntervalList = raw_input("List of Intervals?")
        if IntervalList == "quit":
            sys.exit()
        IntervalSplit = IntervalList.split(",")
        try:
            for x in IntervalSplit:
                temp_interval = interval(x)
                IntervalInput.append(temp_interval)
        except:
            raise ValueError("Invalid list of intervals")

        IntervalInput = mergeOverlapping(IntervalInput)

while True:
    InsertInterval = raw_input("Intervals")
    if InsertInterval == "quit":
        sys.exit()
    try:
        NewInterval = interval(InsertInterval)
    except:
        raise ValueError("Invalid interval")

    IntervalInput = insert(IntervalInput, NewInterval)

    print(IntervalInput)



