import re
from interval import Interval, IntervalException

try:
    ask_list_flag = True
    continue_flag = True

    #Keeps asking the user a list of Intervals until a valid one is provided
    while ask_list_flag:
        user_intervals_input = raw_input("List of Interval?: ")
        intervals_list_pattern = '([\(|\[]-?\d+,-?\d+[\)|\]])'
        user_intervals_list = re.findall(intervals_list_pattern, user_intervals_input)

        if user_intervals_list:
            ask_list_flag = False
            # Creates the interval instances for all the elements of the input of the user
            interval_objects_list = []
            for u_interval in user_intervals_list:
                new_interval = Interval(u_interval)
                interval_objects_list.append(new_interval)
        else:
            print "Provide list with intervals please"

    #Keeps asking the user for a new interval until the word 'quit' is given.
    while continue_flag:
        user_input = raw_input("Interval?: ")
        if user_input == "quit":
            continue_flag = False
        else:
            try:
                # Validate the users interval input. Strips white spaces.
                user_input = user_input.strip().replace(' ', '')
                # Uses a regular expression to verify the format of the input
                lone_interval_pattern = '([\(|\[]-?\d+,-?\d+[\)|\]])'
                match = re.findall(lone_interval_pattern, user_input)
                # If there is a match continues with the program, if not, an exception is raised.
                if match:
                    user_input = match[0]

                    interval_to_insert = Interval(user_input)
                    interval_objects_list = Interval.insert(interval_objects_list, interval_to_insert)
                    print interval_objects_list
                else:
                    raise IntervalException("User Interval Input with invalid format. Try again")

            except IntervalException as e:
                print e

except IntervalException as e:
    print "Interval Error:", e
except ValueError as e:
    print "Interval Error:", e


"""
interval3 = Interval('[-10,-7]')
interval4 = Interval('(-4,1]')
interval5 = Interval('[3,6)')
interval6 = Interval('(8,12)')
interval7 = Interval('[15,23]')

interval8 = Interval('[4,8]')

test_list = Interval.insert([interval3, interval4, interval5, interval6, interval7], interval8)
print test_list

interval9 = Interval('[24,24]')
test_list = Interval.insert(test_list, interval9)
print test_list

interval10 = Interval('[12,13)')
test_list = Interval.insert(test_list, interval10)
print test_list

interval11 = Interval('(2,12)')
test_list = Interval.insert(test_list, interval11)
print test_list

interval12 = Interval('(-7,-2]')
test_list = Interval.insert(test_list, interval12)
print test_list

interval13 = Interval('[-2,5]')
test_list = Interval.insert(test_list, interval13)
print test_list
"""
