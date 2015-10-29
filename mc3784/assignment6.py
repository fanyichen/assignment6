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
            raise Exception('Not Valid interval!')  
        self.lowerBound=int(self.numbers[0])
        self.upperBound=int(self.numbers[1])       
    
    def mergeIntervals(self, int1,int2):
        leftBracket=""
        rightBracket=""
        intervalList1 = self.fromIntervalToList(int1)
        intervalList2 = self.fromIntervalToList(int2)
        mergedInterval=""
        if not (len(set(intervalList1).intersection(intervalList2))!= 0 or intervalList1[-1]==intervalList2[0]-1 or intervalList1[0]==intervalList2[-1]-1):
            raise Exception('Intervals not mergeble!')    
        #First interval less than second:
        if float(intervalList1[-1])>=float(intervalList2[0]-1) and  float(intervalList2[-1])>= float(intervalList1[-1]-1) and float(intervalList1[0])<float(intervalList2[0]):
            leftBracket="[" if int1.leftInclusive else "("
            rightBracket="]" if int2.rightInclusive else ")"
            mergedInterval=leftBracket+str(int1.lowerBound)+","+str(int2.upperBound)+rightBracket

        if float(intervalList2[-1])>=float(intervalList1[0]) and  float(intervalList1[-1])>= float(intervalList2[-1]) and float(intervalList2[0])<float(intervalList1[0]):
            leftBracket="[" if int2.leftInclusive else "("
            rightBracket="]" if int1.rightInclusive else ")"
            mergedInterval=leftBracket+str(int2.lowerBound)+","+str(int1.upperBound)+rightBracket
 
        if float(intervalList1[0])<=float(intervalList2[0]) and  float(intervalList1[-1])>=float(intervalList2[-1]):
            leftBracket="[" if int1.leftInclusive else "("
            rightBracket="]" if int1.rightInclusive else ")"
            mergedInterval=leftBracket+str(int1.lowerBound)+","+str(int1.upperBound)+rightBracket
            
        if float(intervalList2[0])<=float(intervalList1[0]) and  float(intervalList2[-1])>=float(intervalList1[-1]):
            leftBracket="[" if int2.leftInclusive else "("
            rightBracket="]" if int2.rightInclusive else ")"
            mergedInterval=leftBracket+str(int2.lowerBound)+","+str(int2.upperBound)+rightBracket         
        return mergedInterval    

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

    def getLowerBound(self):
        return self.lowerBound
    
    def insert(self,intervals, newint):
        intervalsString=""
        for i in range(len(intervals)):
            intervalsString=intervalsString+intervals[i].intRappresentation+","
        #print intervalsString    
        intervalsString=intervalsString+newint  
        #print intervalsString
        intervalsParsed=parseInput(intervalsString)  
        #print "intervalsParsed: ",intervalsParsed
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
        #sys.exit()
    else:
        for intervalInList in intervals:
            intervalInstance = interval(intervalInList.strip())
            validatedIntervals.append(intervalInstance)   
    return validatedIntervals   
 
    
"""
def start():
    intervals=[]
    try:     
        inputIntervals = raw_input("List of intervals?")   
        intervals=parseInput(inputIntervals) 
        newIntervalList = intervals[0].mergeOverlapping(intervals)
        print "Intervalli nel nuovo caso:"
        for i in range(len(newIntervalList)):
            print newIntervalList[i].intRappresentation
        
    except Exception, e: # catch *all* exceptions  
        print "exception: ", e 

"""
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
                #userViewString += "," if i<len(newIntervalList) else "," 
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
    except Exception, e: # catch *all* exceptions  
        print "exception: ", e 

            
            


if __name__ == '__main__':
    start()
    
    