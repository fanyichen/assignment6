'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
class Interval:
    def __init__(self,interval):
        try:
            self.name=interval
            delimiter=','
            self.LeftBound=int(interval.split(delimiter)[0][1])
            self.RightBound=int(interval.split(delimiter)[1][0])
            self.LeftOperator=interval.split(delimiter)[0][0]
            self.RightOperator=interval.split(delimiter)[1][1]
            self.LeftIsInclu=bool(self.LeftOperator=='[')
            self.RightIsInclu=bool(self.RightOperator==']')
        except ValueError:
            print('Please input an legal string interval')
            
        # keep statues of the interval, whether the interval is legitimate
        # lower < upper-1 if both bounds are exclusive
        # lower < upper if one bound is exclusive and the other is inclusive
        self.isBothExclu=bool((not self.LeftIsInclu) & (not self.RightIsInclu))
        self.isBothInclu=bool(self.LeftIsInclu & self.RightIsInclu)
        self.isOneExOneIn=bool((not self.isBothExclu)&(not self.isBothInclu))
        
        if self.isBothExclu:
            self.isLegit=bool(self.LeftBound <= self.RightBound-1)
        elif self.isBothInclu:
            self.isLegit=bool(self.LeftBound < self.RightBound)
        else:
            self.isLegit=bool(self.LeftBound < self.RightBound)
            
        if (not self.isLegit):
            print('The interval is not legitimate')
            
    def __repr__(self):
        return '"%s" represents the numbers %d through %d' % (self.name, self.LeftBound, self.RightBound)

# test code
if __name__=='__main__':    
    a=Interval('[3,4]') 
    print a       
