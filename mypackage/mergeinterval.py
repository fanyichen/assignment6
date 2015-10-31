'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
from interval import Interval
def mergeIntervals(int1,int2):
    # determine the lower bound of merge interval
    if int1.LeftBound < int2.LeftBound:
        mergeLeftBound=int2.LeftBound
        mergeLeftOperator=int2.LeftOperator
    elif int1.LeftBound > int2.LeftBound:
        mergeLeftBound=int1.LeftBound
        mergeLeftOperator=int1.LeftOperator
    else:
        mergeLeftBound=int1.LeftBound
        if int1.LeftOperator==int2.LeftOperator:
            mergeLeftOperator=int2.LeftOperator
        else:
            mergeLeftOperator='('
    
    # determine the upper bound of the merge interval        
    if int1.RightBound < int2.RightBound:
        mergeRightBound=int1.RightBound
        mergeRightOperator=int1.RightOperator
    elif int1.RightBound > int2.RightBound:
        mergeRightBound=int2.RightBound
        mergeRightOperator=int2.RightOperator
    else:
        mergeRightBound=int2.RightBound
        if int1.RightOperator==int2.RightOperator:
            mergeRightOperator=int2.RightOperator
        else:
            mergeLeftOperator=')'
    
    if mergeLeftBound > mergeRightBound:
        raise ValueError('There is no overlapping between %s and %s' % (int1,int2))
    else:
        mergeinterval=mergeLeftOperator+str(mergeLeftBound)+','+str(mergeRightBound)+mergeRightOperator
        print mergeinterval
        mergedinterval=Interval(mergeinterval)
        print mergedinterval
        
    return mergedinterval


            
            
            
            
            
            
            
            
            
            
            
            
            