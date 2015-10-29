class interval(object):
    
    # construct an interval object 
    def __init__(self, input_interval):
        self.input_interval = str(input_interval)
        
        self.comma = self.input_interval.find(",")
        
        if self.input_interval[0] == "[":
            self.lower = int(self.input_interval[1: self.comma])
        elif self.input_interval[0] == "(":
            self.lower = int(self.input_interval[1: self.comma]) + 1
            
        if self.input_interval[-1] == "]":
            self.upper = int(self.input_interval[self.comma + 1: -1])
        elif self.input_interval[-1] == ")":
            self.upper = int(self.input_interval[self.comma + 1: -1]) - 1
            
        if self.lower > self.upper:
            raise ValueError("Invalid interval, try again")
        
        self.interval_range = range(self.lower, self.upper + 1)
    
    # print interval
    def __repr__(self):
        output_string = self.input_interval
        return output_string

# merges two intervals if they are overlap or adjacent
def mergeIntervals(interval1, interval2):
    
    interval1_set = set(interval1.interval_range)
    interval2_set = set(interval2.interval_range)
    
    if len(list(set(interval1_set) & set(interval2_set))) > 0:
        if interval1.upper >= interval2.lower and interval1.upper <= interval2.upper:
            if interval1.lower <= interval2.lower:
                string_ = interval(interval1.input_interval[0] + str(int(interval1.input_interval[1: interval1.comma])) + "," +str(int(interval2.input_interval[interval2.comma + 1: -1])) + interval2.input_interval[-1])
            elif interval1.lower > interval2.lower:
                string_ = interval(interval2.input_interval[0] + str(int(interval2.input_interval[1: interval1.comma])) + "," +str(int(interval2.input_interval[interval2.comma + 1: -1])) + interval2.input_interval[-1])
        
        elif interval2.upper >= interval1.lower and interval2.upper <= interval1.upper:
            if interval2.lower <= interval1.lower:
                string_ = interval(interval2.input_interval[0] + str(int(interval2.input_interval[1: interval2.comma])) + "," +str(int(interval1.input_interval[interval1.comma + 1: -1])) + interval1.input_interval[-1])
            elif interval2.lower > interval1.lower:
                string_ = interval(interval1.input_interval[0] + str(int(interval1.input_interval[1: interval1.comma])) + "," +str(int(interval1.input_interval[interval1.comma + 1: -1])) + interval1.input_interval[-1])
        return string_ 
                
    elif len(list(set(interval1_set) & set(interval2_set))) == 0 and int(interval1.input_interval[interval1.comma + 1: -1]) == int(interval2.input_interval[1: interval2.comma]):
        if interval1.upper + 1 == interval2.lower:
            string_ = interval(interval1.input_interval[0] + str(int(interval1.input_interval[1: interval1.comma])) + "," +str(int(interval2.input_interval[interval2.comma + 1: -1])) + interval2.input_interval[-1])
            return string_
        else:
            print "Value Error"
    
    elif len(list(set(interval1_set) & set(interval2_set))) == 0 and int(interval2.input_interval[interval1.comma + 1: -1]) == int(interval1.input_interval[1: interval2.comma]):
        if interval2.upper == interval1.lower -1:
            string_ = interval(interval2.input_interval[0] + str(int(interval2.input_interval[1: interval2.comma])) + "," +str(int(interval1.input_interval[interval1.comma + 1: -1])) + interval1.input_interval[-1])
            return string_
        else:
            print "Value Error"
    elif len(list(set(interval1_set) & set(interval2_set))) == 0:
        if interval1.upper + 1 == interval2.lower:
            string_ = interval(interval1.input_interval[0] + str(int(interval1.input_interval[1: interval1.comma])) + "," +str(int(interval2.input_interval[interval2.comma + 1: -1])) + interval2.input_interval[-1])
            return string_
        elif interval2.upper == interval1.lower -1:
            string_ = interval(interval2.input_interval[0] + str(int(interval2.input_interval[1: interval2.comma])) + "," +str(int(interval1.input_interval[interval1.comma + 1: -1])) + interval1.input_interval[-1])
            return string_
        else:
            print "Value Error"
            
# takes a list of intervals and merges all overlapping intervals
def mergeOverlapping(intervals):
    
    sorted_intervals = sorted(intervals, key = lambda element:interval(element).lower)
    length = len(sorted_intervals)
    interval_list = []
    interval_list.append(sorted_intervals[0])
    for i in range(length-1):
        if interval_list[-1].upper < sorted_intervals[i+1].lower -1:
            interval_list.append(sorted_intervals[i+1])
        else:
            merged_interval = mergeIntervals(interval_list[-1],sorted_intervals[i+1])
            interval_list[-1] = merged_interval
    
    return interval_list

# insert a new interval to the interval list and then do the merge functions
def insert(intervals, newint):
    intervals.append(newint)
    new_intervals = mergeOverlapping(intervals)
    return new_intervals
