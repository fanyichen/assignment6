'''
Created on Oct 29, 2015

@author: ds-ga-1007
'''
def mergeOverlapping(intervals):
    intervals=sorted(intervals)
    for i in range(0,len(intervals)-1):
        mergeIntervals(intervals[i],intervals[i+1])