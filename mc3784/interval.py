class NotValidBoundError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class interval(object): 
    """
    The interval class has a constructor that take as argument a string representing an interval (intRappresentation).  
    """
    intRappresentation=""
    rightInclusive=False
    leftInclusive=False
    lowerBound=0
    upperBound=0
    numbers=[]
    
    def __init__(self,intRappresentation):
        """
        Constructor of the class. Check if the interval has valid bound and raise NotValidBoundError if it doesn't. The bounds are to be such that:
        -lower <= upper if both bounds are inclusive
        -lower < upper if one bound is exclusive and one inclusive
        -lower < upper-1  if both are exclusive
        """
        self.setIntRappresentation(intRappresentation)
        goodInterval=False      
        if intRappresentation[-1]=="]":
            self.rightInclusive=True
        elif intRappresentation[-1]==")":    
            self.rightInclusive=False
        else: 
            raise Exception('Error in the interval format ')         
        if intRappresentation[0]=="[":
            self.leftInclusive=True
        elif intRappresentation[0]=="(":    
            self.leftInclusive=False
        else: 
            raise Exception('Error in the interval format ')       
        self.numbers=intRappresentation.replace(')','').replace('(','').replace(']','').replace('[','').split(',')     
        if not (self.rightInclusive and self.leftInclusive) and float(self.numbers[0])<float(self.numbers[1]):
            goodInterval=True
        elif (self.rightInclusive and self.leftInclusive) and float(self.numbers[0])<=float(self.numbers[1]):
            goodInterval=True
        elif float(self.numbers[0])<(float(self.numbers[1])-1):
            goodInterval=True
        else:
            print "wrong interval:",intRappresentation
            errorMessage=self.intRappresentation," is not a valid interval"
            raise NotValidBoundError(errorMessage) 
        self.lowerBound=int(self.numbers[0])
        self.upperBound=int(self.numbers[1])       
 
    def mergeIntervals(self, int1,int2):
        """
        This function take two intrval that could be of any kind (inclusive, exclusive or mixed), and trys to merge them. 
        If there us not an overlap between the two interval the function rise an exception.  
         The two interval can overlap in 4 different ways:
        -The first interval starts before the second one
        -The second interval starts after the second one
        -The first interval contains the second one
        -The first interval is contained by the second one   
        """   
        leftBracket=""
        rightBracket=""
        intervalList1 = self.fromIntervalToList(int1)
        intervalList2 = self.fromIntervalToList(int2)
        mergedInterval=""
        if not (len(set(intervalList1).intersection(intervalList2))!= 0 or intervalList1[-1]==intervalList2[0]-1 
                or intervalList1[0]==intervalList2[-1]-1):
            raise Exception('Intervals not mergeable!')         
        if (float(intervalList1[-1])>=float(intervalList2[0]-1) and  float(intervalList2[-1])>= float(intervalList1[-1]-1) 
            and float(intervalList1[0])<float(intervalList2[0])):
            leftBracket="[" if int1.leftInclusive else "("
            rightBracket="]" if int2.rightInclusive else ")"
            mergedInterval=leftBracket+str(int1.lowerBound)+","+str(int2.upperBound)+rightBracket
        elif (float(intervalList2[-1])>=float(intervalList1[0]) and  float(intervalList1[-1])>= float(intervalList2[-1]) 
              and float(intervalList2[0])<float(intervalList1[0])):
            leftBracket="[" if int2.leftInclusive else "("
            rightBracket="]" if int1.rightInclusive else ")"
            mergedInterval=leftBracket+str(int2.lowerBound)+","+str(int1.upperBound)+rightBracket 
        elif (float(intervalList1[0])<=float(intervalList2[0]) and  float(intervalList1[-1])>=float(intervalList2[-1])):
            leftBracket="[" if int1.leftInclusive else "("
            rightBracket="]" if int1.rightInclusive else ")"
            mergedInterval=leftBracket+str(int1.lowerBound)+","+str(int1.upperBound)+rightBracket
        elif (float(intervalList2[0])<=float(intervalList1[0]) and  float(intervalList2[-1])>=float(intervalList1[-1])):
            leftBracket="[" if int2.leftInclusive else "("
            rightBracket="]" if int2.rightInclusive else ")"
            mergedInterval=leftBracket+str(int2.lowerBound)+","+str(int2.upperBound)+rightBracket
        return mergedInterval    


    def mergeOverlapping(self,intervals):
        """
        In this function the list of intervals is checked taking two intervals at the time and trying to merging them. 
        If the merge is successful the two intervals are replaced by the merged interval. 
        Otherwise they are simply copied in the newIntervalList.
        """
        numberOfIntervals=len(intervals)
        intervals=sorted(intervals)  
        newIntervalList=[]  
        newIntervalIndex=0
        if numberOfIntervals>=2:  
            newIntervalList.append(intervals[0]) 
            for i in range(numberOfIntervals-1):
                try:
                    newInterval= intervals[0].mergeIntervals(intervals[i],intervals[i+1])
                    intervals[i+1]=interval(newInterval)
                    newIntervalList[newIntervalIndex]=interval(newInterval)
                except Exception, e:
                    newIntervalList.append(intervals[i+1])
                    newIntervalIndex=newIntervalIndex+1
        return newIntervalList
    
    def getIntRappresentation(self):
        return self.intRappresentation
    
    def setIntRappresentation(self, intRappresentation):
        self.intRappresentation = intRappresentation

    def fromIntervalToList(self,intervalToParse):
        """
        This function takes an string rapresenting an interval in the form [1,5) and return the corresponding list of number that the interval contains.
        """
        boundsInt=intervalToParse.intRappresentation.replace(')','').replace('(','').replace(']','').replace('[','').split(",")
        if not intervalToParse.leftInclusive:
            boundsInt[0]=int(float(boundsInt[0]))+1
        if intervalToParse.rightInclusive:
            boundsInt[1]=int(float(boundsInt[1]))+1  
        #print boundsInt   
        return list( range(int(float(boundsInt[0])),int(float(boundsInt[1])))) 

    def insert(self,intervals, newint):
        """
        This function takes a list of intervals and a single interval as an argument. And place the interval in the right position. 
        It uses  
        """        
        intervalsString=""
        for i in range(len(intervals)):
            intervalsString=intervalsString+intervals[i].intRappresentation+"," 
        intervalsString=intervalsString+newint  
        intervalsParsed=self.parseStringInterval(intervalsString)  
        newListIntervals=self.mergeOverlapping(intervalsParsed)
        return newListIntervals

    def __cmp__(self, other):
        """
        Function implemented fo sort the interval by their lower bound. 
        """
        if hasattr(other, 'lowerBound'):
            return self.lowerBound.__cmp__(other.lowerBound)
        
    def parseStringInterval(self,intervalsString):
        """
        This function take a string as argument and return a list of intervals.
        """
        validatedIntervals=[]
        intervals=intervalsString.replace('),', ')*').replace('],',']*').split('*')
        for intervalInList in intervals:
            intervalInstance = interval(intervalInList.strip())
            validatedIntervals.append(intervalInstance)   
        return validatedIntervals  