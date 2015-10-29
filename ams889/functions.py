'''
Created on Oct 28, 2015

@author: ams889
'''
import re
import sys
from IntervalClass import *

def test_number(num):
    try: #Returns true if tested value is a number, used in interval input validation
        float(num)
        return True
    except:
        return False

def mergeIntervals(int1, int2):
    #Merges two intervals if they overlap or are adjacent
    sortedInt = sorted([int1, int2], key=lambda x:x.lower)
    if sortedInt[1].lower <= sortedInt[0].upper+1: 
        return interval("[" + str(sortedInt[0].lower)+", "+str(sortedInt[1].upper) + "]")
    else: raise ValueError("Intervals must be adjacent or overlapping to be merged")


def mergeOverlapping(intervals):
    #Merges overlapping or adjacent intervals input in a list
    sortedInt = sorted(intervals, key=lambda x:x.lower)
    intervalList=[sortedInt[0]]  #begins list with first interval to compare with next intervals
    for intx in range(1, len(sortedInt)):
        if sortedInt[intx].lower <= intervalList[-1].upper+1: 
            intervalList[-1].upper = max(intervalList[-1].upper, sortedInt[intx].upper)
        else:
            intervalList.append(sortedInt[intx])
    return intervalList
                
def insert(intervals, newint):
    #Takes a list of non-overlapping intervals and inserts a single interval into the list, merging if necessary
    intervals.append(newint)
    return mergeOverlapping(intervals)