class Interval(object):
    
    """
    Interval object that represents the range of integers between a lower bound and an upper bound.
    Either of the bounds of an interval can be inclusive or exclusive and can be positive or negative.
    The bounds must always meet the requirement that lower <= upper if both bounds are inclusive,
    lower < upper if one bound is exclusive and one inclusive, or lower < upper-1 if both are exclusive.
    """
    start = property(fget=lambda self: self._start, doc="The interval's start")
    end = property(fget=lambda self: self._end, doc="The interval's end")
    leftIncl = property(fget=lambda self: self._leftIncl, doc="If interval is left inclusive")
    rightIncl = property(fget=lambda self: self._rightIncl, doc="if interval is right inclusive")
    
    
    
    def __init__(self, stringForm, start = None, end = None, rightIncl = None):
        self.numberBounds = [None, None]
        if(rightIncl == None):
            "First validify string and parse pieces"
            intervalPieces = self.verifyParseString(stringForm)
        else:
            leftIncl = stringForm
            intervalPieces = [start,end,leftIncl,rightIncl]
        "Assign properties"
        self._start = intervalPieces[0]
        self._end = intervalPieces[1]
        self._leftIncl = intervalPieces[2]
        self._rightIncl = intervalPieces[3]
        if(not self._start == None):
            if(self._leftIncl):
                self.numberBounds[0] = self._start
            else:
                self.numberBounds[0] = self._start + 1
                
            if(self._rightIncl):
                self.numberBounds[1] = self._end
            else:
                self.numberBounds[1] = self._end - 1
        
    def __str__(self):
        "Print out the interval as it's put in"
        startChar = endChar = None
        if self.leftIncl:
            startChar = "["
        else:
            startChar = "("
            
        if self.rightIncl:
            endChar = "]"
        else:
            endChar = ")"
            
        return format('%s%d,%d%s' % (startChar, self.start, self.end, endChar))
    
    def __cmp__(self, other):
        "To determine which interval is more positive/negative"
        if None == other:
            return 1
        start_cmp = cmp(self.numberBounds[0], other.numberBounds[0])
        if 0 != start_cmp:
            return start_cmp
        else:
            return cmp(self.numberBounds[1], other.numberBounds[1])
        
    def verifyParseString(self, stringForm):
        """ Verify string follows {[/(}{int}{,}{int}{)/]} formatting
            Then parse into an array of 
            @return: [start(int),end(int),leftInclusive(boolean),rightInclusive(boolean)]
            or [None,None,None,None] if there's an error
        """
        errorReturn = [None,None,None,None]
        leftInclusive = rightInclusive = start = end = None
        firstChar = stringForm[:1]
        lastChar = stringForm[-1:]
        
        integersWithin = stringForm[1:-1].split(",")
        
        if(firstChar == "("):
            leftInclusive = False
        elif(firstChar == "["):
            leftInclusive = True
        else:
            print(format('Not correct char at beginning of interval : (%s)' % (firstChar)))
            return errorReturn
            
        if(lastChar == ")"):
            rightInclusive = False
        elif(lastChar == "]"):
            rightInclusive = True
        else:
            print(format('Not correct char at end of interval : (%s)' % (lastChar)))
            return errorReturn
            
        if(len(integersWithin) == 2):
            try:
                start = int(integersWithin[0])
                end = int(integersWithin[1])
            except ValueError:
                print(format('Interval ends aren\'t both integers: (%s) , (%s)' % (integersWithin[0],integersWithin[1])))
                return errorReturn
        else:
            print('More than one comma in interval')
            return errorReturn
        
        "Parsed correctly, now check bounds of interval"
        if not self.checkBounds(start,end,leftInclusive,rightInclusive):
            print("Invalid interval")
            "print(format('Based on the bound properties (%s) and (%s) are not proper bounds' % (start, end)))"
            return errorReturn
            
        return [start,end,leftInclusive,rightInclusive]
    
    def checkBounds(self,start,end,leftIncl,rightIncl):
        "Check the bounds of an interval to make sure it's valid"
        "@return Boolean"
        if(leftIncl and rightIncl):
            if(end < start):
                return False
        elif(leftIncl or rightIncl):
            if(end <= start):
                return False
        else:
            if(end <= start +1):
                return False
        return True
    
def mergeInterval(int1, int2):
    "Merges intervals into one"
    start = end = leftIncl = rightIncl = 0
    numberBounds = [None,None]
    if(int1 > int2):
        "Make sure int1 is the lower interval"
        int1, int2 = int2, int1
    if(checkIntervalOverlap(int1,int2)):
        numberBounds[0] = int1.numberBounds[0]
        if(int1.numberBounds[0] == int2.numberBounds[0]):
            if(not(int1.leftIncl or int2.leftIncl)):
                leftIncl=False
                start = int1.numberBounds[0] - 1
            else:
                leftIncl=True
                start = int1.numberBounds[0]
        else:
            leftIncl = int1.leftIncl
            start = int1.start
        
        if(int1.numberBounds[1] == int2.numberBounds[1]):
            if(not(int1.rightIncl or int2.rightIncl)):
                rightIncl=False
                numberBounds[1] = int1.numberBounds[1]
                end = int1.numberBounds[1] + 1
            else:
                rightIncl=True
                numberBounds[1] = int1.numberBounds[1]
                end = int1.numberBounds[1]
        elif(int1.numberBounds[1] > int2.numberBounds[1]):
            numberBounds[1] = int1.numberBounds[1]
            end = int1.end
            rightIncl = int1.rightIncl
        else:
            numberBounds[1] = int2.numberBounds[1]
            end = int2.end
            rightIncl = int2.rightIncl
    else:
        raise ValueError
    
    return Interval(leftIncl, start, end, rightIncl)
    

def mergeOverlapping(intervals):
    """Given a list of intervals merge all overlapping intervals
        @return: List of sorted, merged intervals"""
    overlapsDetected = True;
    while overlapsDetected:
        overlapsDetected = False
        for i in range(0,len(intervals)-1,1):
            if(i < len(intervals) - 1):
                if(checkIntervalOverlap(intervals[i],intervals[i+1])):
                    intervals.insert(i, mergeInterval(intervals[i],intervals[i+1]))
                    intervals.remove(intervals[i+1])
                    intervals.remove(intervals[i+1])
                    overlapsDetected = True
    return intervals

def checkIntervalOverlap(int1, int2):
    "checks if the intervals overlap"
    if(int1 > int2):
        "Make sure int1 is the lower interval"
        int1, int2 = int2, int1
    if(int1.numberBounds[1] >= int2.numberBounds[0]-1):
        return True
    else:
        return False
                
    
def insert(intervalList,newInterval):
    """Insert a newInterval into a supplied intervalList
        @return: intervalList with new interval inserted"""
    inserted = False
    intListLength = len(intervalList)
    if intListLength == 0:
        intervalList.insert(0, newInterval)
        inserted = True
    else:
        for i in range(0,intListLength,1):
            if intervalList[i] < newInterval:
                continue
            else:
                intervalList.insert(i, newInterval)
                inserted = True
                break
        if not inserted:
            intervalList.insert(intListLength, newInterval)
    return intervalList

def printIntervalList(intervalList):
    """Print out interval list"""
    printT =""
    for intv in intervalList:
        printT = printT + str(intv)
        if(not intervalList[len(intervalList)-1] == intv):
            printT = printT + ', '
    print(printT)
    
intervalList = []          
            
if __name__ == '__main__':
    
    intervalInput = raw_input('List of Intervals?')
    intervalInput.replace(" ", "")
    intervalSplits = intervalInput.split(",")
    for i in range(0,len(intervalSplits),2):
        intervalString = intervalSplits[i] + ',' + intervalSplits[i+1]
        parsedInterval = Interval(intervalString)
        if(not parsedInterval.start == None):
            intervalList = insert(intervalList,parsedInterval)
    intervalList = mergeOverlapping(intervalList)
    printIntervalList(intervalList)

    userInput = ''
    while True:
        userInput = raw_input('Interval?')
        userInput.replace(" ", "")
        if(userInput == 'quit'):
            break
        parsedInterval = Interval(userInput)
        if(not parsedInterval.start == None):
            intervalList = insert(intervalList,parsedInterval)
        intervalList = mergeOverlapping(intervalList)
        printIntervalList(intervalList)
        