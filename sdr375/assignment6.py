import interval


import re
def main_function():
    ListOfIntervals = list()
    while len(ListOfIntervals)==0:
        try:
            InputIntervals = raw_input("List of intervals?:")
            if InputIntervals == "quit":
                break
            temp = (re.compile('(\(|\[)(-?\d+),(-?\d+)(\)|\])')).findall(InputIntervals)
            InputIntervals = temp
            

            for i in temp:
                ListOfIntervals.append(interval.interval(i))
            if len(ListOfIntervals)==0:
                print("Bad input. Please try again with the proper input format")

        except Exception as ErrorMessage:
            print ErrorMessage

    while True:
        NewInt = raw_input("another interval?")
        if InputIntervals == "quit" or "Quit":
            break
        try:
            ListOfIntervals = interval.interval.insert(ListofIntervals,interval.interval(NewInt))
            print ListOfIntervals
        except Exception and ErrorMessage:
            print ErrorMessage


if __name__ == "__main__":
    main_function()