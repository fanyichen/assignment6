'''
Created on Oct 28, 2015

@author: ams889
'''
import re
import sys
from functions import *

class interval(object):
    #Represents the range of integers between a lower bound and an upper bound
    def __init__(self, inputString):
        newString = inputString.replace(" ", "")
        if newString[0]=="[" and newString[-1]=="]":
            self.rangeType="InclusiveAll"
        elif newString[0]=="[" and newString[-1]==")":
            self.rangeType="InclusiveLower"
        elif newString[0]=="(" and newString[-1]=="]":
            self.rangeType="InclusiveUpper"
        elif newString[0]=="(" and newString[-1]==")":
            self.rangeType="ExclusiveAll"
        else: 
            raise TypeError("Intervals can only be specified using parentheses or brackets '()[]'")

        if test_number(newString.rpartition(",")[0][1:]) == False :
            raise ValueError("Interval must contain two numbers in numeric form, e.g. 2, 3, etc.")
        if test_number(newString.rpartition(",")[2][:-1]) == False:
            raise ValueError("Interval must contain two numbers in numeric form, e.g. 2, 3, etc.")

        
        self.lower = int(newString.rpartition(",")[0][1:])
        self.upper = int(newString.rpartition(",")[2][:-1])
        
        if self.rangeType=="InclusiveAll":
            if self.lower > self.upper:
                raise ValueError("Lower bound must be less than or equal to upper bound")
        elif self.rangeType=="InclusiveLower":
            self.upper=self.upper-1
            if self.lower >= self.upper+1:
                raise ValueError("Lower bound must be less than upper bound")
        elif self.rangeType=="InclusiveUpper":
            self.lower=self.lower+1
            if self.lower-1 >= self.upper:
                raise ValueError("Lower bound must be less than upper bound")
        elif self.rangeType=="ExclusiveAll":
            self.lower=self.lower+1
            self.upper=self.upper-1
            if self.lower-1 >= self.upper:
                raise ValueError("Lower bound must be less than upper bound minus 1")
        
    def __repr__(self):
        if self.rangeType=="InclusiveAll":
            return("[" + str(self.lower) + "," + str(self.upper) + "]")
        elif self.rangeType=="InclusiveLower":
            return("[" + str(self.lower) + "," + str(self.upper+1) + ")")
        elif self.rangeType=="InclusiveUpper":
            return("(" + str(self.lower-1) + "," + str(self.upper) + "]")          
        elif self.rangeType=="ExclusiveAll":
            return("(" + str(self.lower-1) + "," + str(self.upper+1) + ")")
