class interval():

    def __init__(self,interval):
                
        # When the class is printed, intervals are displayed using 
        # square brackets [ ] for inclusive bounds
        # parenthesis ( ) for exclusive bounds. 
        if interval.split(",")[0][0] == "(":
            range_start = (int(interval.split(",")[0][1:])+1)
            start_bound = "("
        elif interval.split(",")[0][0] == "[":
            range_start = int(interval.split(",")[0][1:])
            start_bound = "["
        else:
            raise ValueError("Must start square brackets or parenthesis")
        
        # The bounds must always meet the requirement that
        # lower <= upper if both bounds are inclusive,
        # lower < upper if one bound is exclusive and one inclusive, or 
        # lower < upper if both are exclusive.
        try:
            start = int(interval.split(",")[0][1:])
        except ValueError:
            print ("The start is not a number")
            
        try:
            end = int(interval.split(",")[1][:-1])
        except ValueError:
            print ("The end is not a number")
            
        if start > end:
            raise ValueError("Start is greater than end")
           
        if interval.split(",")[1][-1] == ")":
            range_end = (int(interval.split(",")[1][:-1]))
            end_bound = ")"
        elif interval.split(",")[1][-1] == "]":
            range_end = (int(interval.split(",")[1][:-1])+1)
            end_bound = "]"
        else:
            raise ValueError('Must end square brackets or parenthesis')
        
        
        if interval.split(",")[1][-1] == ")":
            real_end = (int(interval.split(",")[1][:-1])-1)
        elif interval.split(",")[1][-1] == "]":
            real_end = (int(interval.split(",")[1][:-1]))
        
        self.start = start
        self.end = end
        self.real_end = real_end
        self.start_bound = start_bound
        self.end_bound = end_bound
        self.range_start = range_start
        self.range_end = range_end
        
    def num_list(self):
        num_list = list()
        for i in range(self.range_start,self.range_end):
            num_list.append(i)
        return num_list
    
    def start(self):
        return self.range_start
    def end(self):
        return self.range_end
    
    def start_bound(self):
        return self.start_bound
    def end_bound(self):
        return self.end_bound
    
    # The class should have a constructor that takes a string representation of the interval
    # and must ensure that interval in this string conforms to these requirements.
        
    def __repr__(self):
        return (str(self.start_bound)+str(self.start)+","+str(self.end)+str(self.end_bound))   

def mergeIntervals(int1, int2):
    
    if int1.start < int2.start:
        if int1.real_end >= int2.start:
            if int1.real_end <= int2.real_end:
                new_interval_start = int1.start_bound+str(int1.start)
                new_interval_end   = str(int2.end)+int2.end_bound
            else:
                new_interval_start = int1.start_bound+str(int1.start)
                new_interval_end = str(int1.end)+int1.end_bound
        else:
            raise ValueError("no overlap")
            #If the intervals do not overlap, an exception should be thrown.
            
    elif int1.start > int2.start:
        if int2.real_end >= int1.start:
            if int2.real_end <= int1.real_end:
                new_interval_start = int2.start_bound+str(int2.start)
                new_interval_end   = str(int1.end)+int1.end_bound
            else:
                new_interval_start = int2.start_bound+str(int2.start)
                new_interval_end = str(int2.end)+int2.end_bound
        else:
            raise ValueError("no overlap")
            
    else:
        if int1.real_end >= int2.real_end:
            new_interval_start = int1.start_bound+str(int1.start)
            new_interval_end   = str(int1.end)+int1.end_bound
        else:
            new_interval_start = int1.start_bound+str(int1.start)
            new_interval_end   = str(int2.end)+int2.end_bound
    
    new_interval = interval(str(new_interval_start+","+new_interval_end))
    return new_interval

def mergeOverlapping(intervals):
    #Takes a list of intervals and merges all overlapping intervals.
    
    intervals.sort(key=lambda intervals: int(intervals.split(",")[0][1:]))
     
    overlap = True
    while overlap == True:
        overlap = False
        for i in range(len(intervals)):
            for n in range(i+1,len(intervals)):
                try:
                    mergeIntervals(interval(intervals[i]),interval(intervals[n]))
                except:
                    continue
                else:
                    merged = mergeIntervals(interval(intervals[i]),interval(intervals[n]))
                    intervals.append(str(merged))
                    intervals.remove(intervals[i])
                    intervals.remove(intervals[n-1])
                    overlap = True
    return intervals

def insert(intervals, newint):
    # insert newint into intervals, merging the result if necessary.
    intervals.append(newint)
    result = mergeOverlapping(intervals)
    
    return result

