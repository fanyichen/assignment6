import Interval
from Interval import mergeIntervals, mergeOverlapping, insert


def print_intervals(intervalList):
    x = ",".join([i.string_rep for i in intervalList])
    print x
           
               
if __name__ == "__main__":
    interval_list = []
    
    while(len(interval_list)==0):
        input = raw_input('List of Intervals?')
        if input == 'quit':
            break
        input.replace(" ", "")
        input = input.split(",")
    
        try:
            for i in range(0,len(input),2):
                interval = input[i] + ',' + input[i+1]
                try:
                    parsedInterval = Interval.Interval(interval)
                    interval_list = insert(interval_list,parsedInterval)
                except:
                    print "Please enter a valid list of intervals separated by commas." 
                    interval_list = []
        except:
            print "Please enter a valid list of intervals separated by commas." 
            interval_list = []
        
    interval_list = mergeOverlapping(interval_list)
    print_intervals(interval_list)

    userInput = ''
    while True:
        userInput = raw_input('Interval?')
        if(userInput == 'quit'):
            break
        try:
            parsedInterval = Interval.Interval(userInput)
        except:
            print "Please enter a valid interval."
             
        interval_list = insert(interval_list, parsedInterval)
        interval_list = mergeOverlapping(interval_list)
        print_intervals(interval_list)
        