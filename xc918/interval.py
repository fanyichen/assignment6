#Auther: Xing Cui
#NetID: xc918
#Reference: github, Google.
#Date: Oct.28 2015


#Three exceptions. 
class ValidationError(Exception): 
    pass
class ValueError(Exception): 
    def __str__(self):
        return 'Invalid values\n'
class mergeError(Exception):
    def __str__(self):
        return 'The intervals do not overlap\n'

class interval(object):
    """This class is used to merge intervals together if they are overlapping"""

    def __init__(self, inputIntervalString):
        
        self.inputIntervalString = inputIntervalString      #initial inputs are strings
        newIntervalString = inputIntervalString.split(',')  #split each string by comma
        self.lowerbound = int(newIntervalString[0][1:])     #get lowerbound by the number at left of comma
        self.upperbound = int(newIntervalString[1][:-1])    #get upperbound by the number at right of comma
        
        #get true bound value for the interval. such as (1,5) actually means [2,4]
        if self.inputIntervalString[0] == "(":
            if self.inputIntervalString[-1] == ")":
                self.intervalType = "Open"
                self.lowerbound = self.lowerbound + 1
                self.upperbound = self.upperbound - 1           
            elif self.inputIntervalString[-1] == "]":
                self.intervalType = "RightOpen"
                self.lowerbound = self.lowerbound + 1
                self.upperbound = self.upperbound
        elif self.inputIntervalString[0] == "[":
            if self.inputIntervalString[-1] == ")":
                self.intervalType = "LeftOpen"
                self.lowerbound = self.lowerbound
                self.upperbound = self.upperbound - 1
            elif self.inputIntervalString[-1] == "]":
                self.intervalType = "Close"
                self.lowerbound = self.lowerbound
                self.upperbound = self.upperbound       
        else:
            raise ValidationError("Invalid input. Example: [1,2],(1,3),(2,5],[3,4].")

            
        #validating interval is correct or not. [10,3] is not validated. 
        if self.lowerbound <= self.upperbound:
            valid_range = range(self.lowerbound, self.upperbound)
            self.valid_range = valid_range
        else:
            raise ValidationError("Invalid input. Example: [1,2],(1,3),(2,5],[3,4].")


    def __repr__(self):
        #giving format for four types of intervals
        if self.intervalType == "Open":
            return("(" + str(self.lowerbound-1) + "," + str(self.upperbound+1) + ")")
        elif self.intervalType == "RightOpen":
            return("(" + str(self.lowerbound-1) + "," + str(self.upperbound) + "]") 
        elif self.intervalType == "LeftOpen":
            return("[" + str(self.lowerbound) + "," + str(self.upperbound+1) + ")")
        elif self.intervalType == "Close":
            return("[" + str(self.lowerbound) + "," + str(self.upperbound) + "]")
         
        
        




def mergeInterval(int1, int2):
    #this function is merging two intervals into one if they have the same ranges that overlap.

    #merge two intervals by looking at their different overlapping range.
    if int1.upperbound + 1 >= int2.lowerbound and int2.upperbound + 1 >= int1.lowerbound:
        if int1.lowerbound < int2.lowerbound:
            lowerbound = int1.inputIntervalString.split(',')[0]
        else:
            lowerbound = int2.inputIntervalString.split(',')[0]
        if int2.upperbound > int1.upperbound:
            upperbound = int2.inputIntervalString.split(',')[1]
        else:
            upperbound = int1.inputIntervalString.split(',')[1]
    else:
        raise mergeError
    merge_interval = interval(lowerbound+','+upperbound)    #get the lowerbound from smaller side and its "(" or "[", vice versa.
    return merge_interval


def mergeOverlapping(intervals):
    
    #merge all intervals have overlapping part from a interval list.
    if len(intervals) == 1:
        return intervals
    for i in range(len(intervals)-1):   #if there are n intervals in the list, this is for the n-1 intervals.
        for j in range(i+1, len(intervals)):#this is for the previous n-1 intervals to compare and merge with the one right after it on the left.
            try:
                
                if intervals[i].inputIntervalString == intervals[j].inputIntervalString: #if two same ones, drop one and keep one.
                    intervals[j] = merged_result
                    intervals.remove(intervals[i])
                    return mergeOverlapping(intervals)
                merged_result = mergeInterval(intervals[i], intervals[j])#any two are different, merge two into one
                intervals[j] = merged_result                             #keep the merged one
                intervals.remove(intervals[i])                           #remove the one that has been merged in.
                return mergeOverlapping(intervals)
            
            except mergeError:
                continue
    intervals = sorted(intervals,key=lambda interval: interval.lowerbound)#sorting the list makes it look good.
    return intervals

def insert(intervals, newint):
    intervals.append(newint)#add the new input interval into the list.

    return mergeOverlapping(intervals)#merge the new interval into the merged ones if it is applicable.








    
    
    
    
    
    
    

    
    
    
    
    

