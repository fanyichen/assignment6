# Define the call interval() and function mergeIntervals(int1, int2), mergeOverlapping(intervals), insert(intervals, newint)
class interval():
    def __init__(self, input_interval):
        self.input_interval = str(input_interval)
        if self.input_interval[0] == "(":
            self.lower = int(self.input_interval.strip("()[]").split(",")[0]) + 1
            self.lower_bound = "("
        else:
            self.lower = int(self.input_interval.strip("()[]").split(",")[0])
            self.lower_bound = "["
        if self.input_interval[-1] == ")":
            self.upper = int(self.input_interval.strip("()[]").split(",")[1]) - 1
            self.upper_bound = ")"
        else:
            self.upper = int(self.input_interval.strip("()[]").split(",")[1])
            self.upper_bound = "]"
        if self.lower > self.upper:
            raise ValueError("Invalid interval")

    def __repr__(self):
        if self.lower_bound == "(":
            self.lower_result = self.lower - 1
        else:
            self.lower_result = self.lower
        if self.upper_bound == ")":
            self.upper_result = self.upper + 1
        else:
            self.upper_result = self.upper
        # combine the result of lower and upper
        result = self.lower_bound + str(self.lower_result) + "," + str(self.upper_result) + self.upper_bound
        return result

def mergeIntervals(int1, int2):
    # takes two intervals and merge them if they overlap or are adjacent, raises exception otherwise 
    if (int1.upper < int2.lower -1 ) or (int1.lower > int2.upper + 1):
        print "The intervals cannot be merged."
    else:
        if int1.lower > int2.lower:
            lower = int2.lower
            lower_bound = int2.lower_bound
        else:
            lower = int1.lower
            lower_bound = int1.lower_bound
        if int1.upper < int2.upper:
            upper = int2.upper
            upper_bound = int2.upper_bound
        else:
            upper = int1.upper
            upper_bound = int1.upper_bound
    # if the bound is exclusive, adjust the value of lower and upper of the interval        
        if lower_bound == "(":
            lower_result = lower - 1
        else:
            lower_result = lower
        if upper_bound == ")":
            upper_result = upper + 1
        else:
            upper_result = upper
        # combine the result of lower and upper
        result = interval(lower_bound + str(lower_result) + "," + str(upper_result) + upper_bound)
        return result

def mergeOverlapping(intervals):
    # takes a list of intervals and merges all overlapping intervals by sorting them first and merging two intervals in turns.
    intervals_sorted = sorted(intervals, key = lambda x:interval(x).lower)
    temp_list = []
    try:
        temp_list = [intervals_sorted[0]]
    except NameError:
        print "Invalid intervals"
    length = len(intervals_sorted)
    for i in range(length - 1):
        # two intervals are not adjacent
        if int(temp_list[-1].upper) + 1 < int(intervals_sorted[i+1].lower):
            temp_list.append(intervals_sorted[i+1])
        else:
            merged_interval = mergeIntervals(temp_list[-1], intervals_sorted[i+1])
            temp_list[-1] = merged_interval
    return temp_list

def insert(intervals, newint):
    # append the new single interval to the list of intervals and then merges all overlapping intervals
    intervals.append(newint)
    result = mergeOverlapping(intervals)
    return result