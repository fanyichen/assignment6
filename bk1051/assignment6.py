from interval import *
import sys
'''
5.	Write a program using this class and these functions that prompts the user
for a list of intervals, reads a string from the user, and creates a list
containing these intervals. Once this string has been read, the program should
continue prompting for intervals from the user, insert the interval into the
list, and display the list at the end of each operation. The program should
be careful to correctly validate the input from the user. The following shows
 an example of the program being run.

List of intervals? [-10,-7], (-4,1], [3,6), (8,12), [15,23]
Interval? [4,8]
[-10,7], (-4,1], [3,12), [15,23]
Interval? [24,24]
[-10,7], (-4,1], [3,12), [15,24]
Interval? [4,-1]
Invalid interval
Interval? [12,13)
[-10,7], (-4,1], [3,13), [15,24]
Interval? (3,4)
Invalid interval
Interval? (2,12)
[-10,7], (-4,1], [3,13), [15,24]
Interval? (-7,-2]
[-10,1], [3,13), [15,24]
Interval? foo
Invalid interval
Interval? [-2,5]
[-10,13), [15,24]
Interval? quit
'''

QUIT = "quit"

def ask_for_interval_list():
    return raw_input("List of intervals? ")

def ask_for_interval():
    return raw_input("Interval? ")

def parse_interval_input(input_string):
    '''Parse user input for interval prompt.
    Will exit program if user inputs the value of the QUIT variable.'''
    if input_string.lower().find(QUIT) >= 0:
        sys.exit()
    else:
        return interval(input_string)

def interval_list_to_string(intervals):
    return intervals_to_strings(intervals).join(", ")

def parse_interval_list_input(input_string):
    '''Parse a list of intervals'''
    pass

def run():
    intervals_string = ask_for_interval_list()
    intervals = parse_interval_list_input(intervals_string)
    while (True):
        try:
            input_string = ask_for_interval()
            newint = parse_interval_input(input_string)
            intervals = insert(intervals, newint)
            print interval_list_to_string(intervals)

        except IntervalParseException:
            print "Invalid interval"

        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print "\nGoodbye!"
