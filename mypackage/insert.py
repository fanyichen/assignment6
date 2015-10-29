'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
def insert(intervals,newint):
    intervals.append(newint)
    mergedintervals=mergeOverlapping(intervals)
    return mergedintervals