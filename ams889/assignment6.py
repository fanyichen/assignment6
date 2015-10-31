'''
Created on Oct 21, 2015

@author: AMS889
'''
import re
import sys
from IntervalClass import *
from functions import *

if __name__ == '__main__':
    intervalInputList=[]
    intervalInput = raw_input('List of Intervals? ')
    intervalInputNoQuote=intervalInput.replace(" ", "")
    intervalsSplit = intervalInput.split(",")
    for ints in range(0, len(intervalsSplit),2):
        try:
            intervali=interval(intervalsSplit[ints] + "," + intervalsSplit[ints+1])
            intervalInputList.append(intervali)
        except:
            raise ValueError("Invalid Interval List")
    mergedIntervalList = mergeOverlapping(intervalInputList)
    print mergedIntervalList
    while True:
        newIntervalInput = raw_input('Interval?')
        if newIntervalInput.lower() =="quit":
            break
        newIntervalInputNoQuote=newIntervalInput.replace(" ", "")
        try:
            intervaln=interval(newIntervalInputNoQuote)
            mergedIntervalListNew=insert(mergedIntervalList, intervaln)
            print mergedIntervalListNew
        except:
            print("Invalid Interval")
