import sys
from interval import interval
from merge import *


#The first prompt to the user
def start():
    try:
        return raw_input("List of intervals?")
    #Account for ctrl+c, ctrl+d, etc.
    except (KeyboardInterrupt,EOFError):
        sys.exit()
        
#Every subsequent prompt to the user
def prompt():
    try:
        return raw_input("Interval?")
    #Account for ctrl_c, ctrl_d, etc.
    except (KeyboardInterrupt, EOFError):
        sys.exit()
        
#Reads raw input from the user as a string and determines whether to quit the program. Otherwise, parse for intervals
def parse_input(str):
    if str.lower() == "quit":
            #quit the program
        sys.exit()
    else:
        return parse_for_intervals(str)

#Reads raw input from the user as a string and returns a list of valid intervals, if provided
def parse_for_intervals(str):

    #record all the intervals parsed from input
    ints = []
    
    #parse as long as the string is non-empty
    while len(str) > 0:

        #look for a right parentheses
        right_enc = len(str)+1
        try:
            right_enc = str.index(")")
        except ValueError:
            pass

        #look for a right bracket - if it is before the right parentheses, save it as right_enc
        try: 
            right_bracket = str.index("]")
            if right_bracket < right_enc:
                right_enc = right_bracket
        except ValueError:
            pass

        #if neither a right parentheses nor a right bracket were found, this will throw an index error
        try:
            dummy = str[right_enc]
        except IndexError:
            print "Invalid interval"
            ints = ints[-1:0]
            break
        
        if right_enc != len(str)+1:
            #Try to create an interval from this substring
            try:
                newInt = interval(str[0:right_enc+1])
                #Delete the part of the substring that was passed to the interval init function
                str = str[right_enc+1:].strip()
                #If the string is not empty, there should be a comma at the front - delete it
                if len(str) > 0:
                    try:
                        comma_index = str.index(",")
                        str = str[comma_index+1:]
                        #If there is no comma, throw an error
                    except ValueError:
                        print "Invalid interval"
                        ints = ints[-1:0]
                        break
                    #Append the int to the list, if it was successfully created
                ints.append(newInt)
                #Handle this error if the intervals were not properly formatted
            except InvalidIntervalError:
                print "Invalid interval"
                ints = ints[-1:0]
                break
    return ints

#Asks the user for for a list of intervals and parses the input
def get_list():
    insist = True
    while insist:
        usr_ints = parse_input(start())
        #Demand more than one interval 
        if len(usr_ints) > 0:
            insist = False
    return usr_ints

#Asks the user for individual intervals and parses the input
def add_to_list():
    insist = True
    while insist:
        new_int = parse_input(prompt())
        #Demand exactly one interval
        if len(new_int) == 1:
            insist = False
        elif len(new_int) > 1:
            print "Enter only one interval at a time"
    return new_int

