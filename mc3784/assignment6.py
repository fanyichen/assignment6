from  assignment6 import NotValidBoundError
from  assignment6 import interval

def parseInput(inputIntervals):
    """
    This function take the input inserted by the user and return a list of intervals
    """
    validatedIntervals=[]
    intervals=inputIntervals.replace('),', ')*').replace('],',']*').split('*')
    if inputIntervals.strip('0123456789(,)[]- ') or inputIntervals=="":
        print "wrong format for interval string"
        print "The input string should be like this:\n [-10,-7], (-4,1], [3,6), (8,12), [15,23]"
        sys.exit()
    else:
        for intervalInList in intervals:
            try:
                intervalInstance = interval(intervalInList.strip())
            except NotValidBoundError, e: 
                sys.quit()
            validatedIntervals.append(intervalInstance)   
    return validatedIntervals   

def start():
    intervals=[]
    try:        
        while len(intervals)==0:
            intervals = raw_input("List of intervals?")   
            if (intervals == "quit"):
                print "quitting"
                sys.exit()
            intervals=parseInput(intervals) 
            if len(intervals)!=0:
                newIntervalList = intervals[0].mergeOverlapping(intervals)
                userViewString=""
                for i in range(len(newIntervalList)):
                    userViewString+=newIntervalList[i].intRappresentation+","
                print userViewString[:-1]
            
        while True: 
            newint = raw_input("Interval?") 
            if (newint == "quit"):
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
    
    