from dealinterval import *
import sys

def main():
    interval_list = []#creat an empty interval list for further step
    try:

        while True:
        
            if len(interval_list) == 0:

                initial_list_input = raw_input('List of intervals?')  
        
                if initial_list_input == 'quit':
                    sys.exit()

                interval_string = initial_list_input.replace(' ','')
                input_split = interval_string.split(',')
                for i in range(0, len(input_split), 2):

                    try:
                        intnew = dealinterval(input_split[i] + ',' + input_split[i+1])
                        interval_list.append(intnew)

                    except ValueError:
                        print "Invalid input"
                    except IndexError:
                        print "Invalid input2"
                
            else:
                interval_input = raw_input('Intervals?')
                if interval_input == 'quit':
                    sys.exit()
                try:
                    new_int = dealinterval(interval_input)
                except ValueError:
                    print "Invalid interval"
                else:
                    final_list = insert(interval_list, new_int)  # merge the input interval with the permanent list
                    print final_list  # print out the final list
    except KeyboardInterrupt:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"