import sys

class interval(object): 
    intRappresentation=""
    rightInclusive=False
    leftInclusive=False
    lowerBound=0
    upperBound=0
    numbers=[]
    
    def __init__(self,intRappresentation):
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
            raise Exception('Not Valid interval!\n The first number of the interval should be the lowest one')  
        self.lowerBound=int(self.numbers[0])
        self.upperBound=int(self.numbers[1])       

    # The two interval can overlap in 4 different ways:
    # The first interval starts before the second one
    # The second interval starts after the second one
    # The first interval contains the second one
    # The first interval is contained by the second one   
    def mergeIntervals(self, int1,int2):
        leftBracket=""
        rightBracket=""
        intervalList1 = self.fromIntervalToList(int1)
        intervalList2 = self.fromIntervalToList(int2)
        mergedInterval=""
        if not (len(set(intervalList1).intersection(intervalList2))!= 0 or intervalList1[-1]==intervalList2[0]-1 or intervalList1[0]==intervalList2[-1]-1):
            raise Exception('Intervals not mergeable!')         
        if float(intervalList1[-1])>=float(intervalList2[0]-1) and  float(intervalList2[-1])>= float(intervalList1[-1]-1) and float(intervalList1[0])<float(intervalList2[0]):
            leftBracket="[" if int1.leftInclusive else "("
            rightBracket="]" if int2.rightInclusive else ")"
            mergedInterval=leftBracket+str(int1.lowerBound)+","+str(int2.upperBound)+rightBracket
        elif float(intervalList2[-1])>=float(intervalList1[0]) and  float(intervalList1[-1])>= float(intervalList2[-1]) and float(intervalList2[0])<float(intervalList1[0]):
            leftBracket="[" if int2.leftInclusive else "("
            rightBracket="]" if int1.rightInclusive else ")"
            mergedInterval=leftBracket+str(int2.lowerBound)+","+str(int1.upperBound)+rightBracket 
        elif float(intervalList1[0])<=float(intervalList2[0]) and  float(intervalList1[-1])>=float(intervalList2[-1]):
            leftBracket="[" if int1.leftInclusive else "("
            rightBracket="]" if int1.rightInclusive else ")"
            mergedInterval=leftBracket+str(int1.lowerBound)+","+str(int1.upperBound)+rightBracket
        elif float(intervalList2[0])<=float(intervalList1[0]) and  float(intervalList2[-1])>=float(intervalList1[-1]):
            leftBracket="[" if int2.leftInclusive else "("
            rightBracket="]" if int2.rightInclusive else ")"
            mergedInterval=leftBracket+str(int2.lowerBound)+","+str(int2.upperBound)+rightBracket
        return mergedInterval    

    # The list of intervals is checked taking two intervals at the time and trying to merging them. 
    # If the merge is successful the two intervals are replaced by the merged interval. 
    # Otherwise they are simply copied in the newIntervalList.
    def mergeOverlapping(self,intervals):
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
        boundsInt=intervalToParse.intRappresentation.replace(')','').replace('(','').replace(']','').replace('[','').split(",")
        if not intervalToParse.leftInclusive:
            boundsInt[0]=int(float(boundsInt[0]))+1
        if intervalToParse.rightInclusive:
            boundsInt[1]=int(float(boundsInt[1]))+1  
        #print boundsInt   
        return list( range(int(float(boundsInt[0])),int(float(boundsInt[1])))) 

    def insert(self,intervals, newint):
        intervalsString=""
        for i in range(len(intervals)):
            intervalsString=intervalsString+intervals[i].intRappresentation+"," 
        intervalsString=intervalsString+newint  
        intervalsParsed=parseInput(intervalsString)  
        newListIntervals=self.mergeOverlapping(intervalsParsed)
        return newListIntervals

    def __cmp__(self, other):
        if hasattr(other, 'lowerBound'):
            return self.lowerBound.__cmp__(other.lowerBound)
   
def parseInput(inputIntervals):
    validatedIntervals=[]
    intervals=inputIntervals.replace('),', ')*').replace('],',']*').split('*')
    if inputIntervals.strip('0123456789(,)[]- ') or inputIntervals=="":
        print "wrong format for interval string"
        print "The input string should be like this:\n [-10,-7], (-4,1], [3,6), (8,12), [15,23]"
        sys.exit()
    else:
        for intervalInList in intervals:
            intervalInstance = interval(intervalInList.strip())
            validatedIntervals.append(intervalInstance)   
    return validatedIntervals   
 
def start():
    intervals=[]
    try:        
        while len(intervals)==0:
            inputIntervals = raw_input("List of intervals?")   
            if (inputIntervals == "quit"):
                print "quitting"
                sys.exit()
            intervals=parseInput(inputIntervals) 
            if len(intervals)!=0:
                newIntervalList = intervals[0].mergeOverlapping(intervals)
                userViewString=""
                for i in range(len(newIntervalList)):
                    userViewString+=newIntervalList[i].intRappresentation+","
                print userViewString[:-1]
            
        while True: 
            newint = raw_input("Interval?") 
            if (inputIntervals == "quit"):
                print "quitting"
                sys.exit()                 
            newIntervals=intervals[0].insert(newIntervalList, newint)
            
            newIntervalList=newIntervals
            
            userViewStringSecond=""
            for i in range(len(newIntervals)):
                userViewStringSecond += newIntervals[i].intRappresentation+","    
            print userViewStringSecond[:-1]    
    except Exception, e: 
        print "exception: ", e 

if __name__ == '__main__':
    start()
    
    