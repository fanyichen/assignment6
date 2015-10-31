# Use class interval() and the built functions to reads a list of intervals from the user, and creates a list containing these intervals
# Then read a interval from the user, and insert it into the list of intervals
import sys
from intervals import *

def main():
    intervals_list = []
    while True:
        try:
            # if there is no valid list of intervals recorded, let the use input the initial list of intervals
            if len(intervals_list) == 0:
                initial_input = raw_input("List of intervals?")
                # quit the program if the input is "quit"
                if initial_input == "quit":
                    break
                try:
                    processed_input = initial_input.replace(' ', '').split(",")
                    for i in range(0, len(processed_input), 2):
                        interval_i = interval(processed_input[i] + "," + processed_input[i+1])
                        intervals_list.append(interval_i)
                except ValueError:
                    print "Invalid interval"
            
                intervals_list = mergeOverlapping(intervals_list)
            # if there is a valid list of intervals recorded, let the use input the interval to be inserted
            else:
                initial_input = raw_input("Interval?")
                if initial_input == "quit":
                    break
                try:
                    new_interval = interval(initial_input)
                    intervals_list = insert(intervals_list, new_interval)
                    # print the list of intervals one by one
                    print ', '.join(str(x) for x in intervals_list)
                except ValueError:
                    print "Invalid interval"

        # raise exception if the user input nothing        
        except IndexError:
            print "Do not input nothing, input quit to exit"
        # raise exception if the user press ctrl+c  
        except KeyboardInterrupt:
            print "\r"
            print "Input quit to exit"
        # raise exception if the user press ctrl+d
        except EOFError:
            print "\r"
            print "Input quit to exit"
        
if __name__ == "__main__":
    main()