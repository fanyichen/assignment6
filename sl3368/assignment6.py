import sys
from interval import *

# used to run the program 
def main():
    interval_list = []
    try:
        while True:
            if len(interval_list) == 0:
                interval_input_1 = raw_input("List of intervals?")
                if interval_input_1 == "quit":
                    return
                try:
                    interval_input_1 = interval_input_1.replace(' ', '')
                    comma_split = interval_input_1.split(",")
                    for i in range(0, len(comma_split), 2):
                        interval_i = interval(comma_split[i] + "," + comma_split[i+1])
                        interval_list.append(interval_i)
                except ValueError:
                    print "Invalid interval"
            
                interval_list = mergeOverlapping(interval_list)
        
            else:
                interval_input_1 = raw_input("Interval?")
                if interval_input_1 == "quit":
                    return
                try:
                    new_interval = interval(interval_input_1)
                    interval_list = insert(interval_list, new_interval)
                    print interval_list
                except ValueError:
                    print "Invalid interval"
                
            
    except KeyboardInterrupt:
        print "Keyboard Interrupted"
        
    except EOFError:
        print "EOFError"
        
if __name__ == "__main__":
    main()
    