# DS-GA 1007 HW6
# Author: Sida Ye

import unittest

""" Create an interval class. """

class interval(object):
    def __init__(self, string):
        self.string = string                                # record input string
        self.front = string[0]                              # record the front parenthesis or brackets of interval
        self.back = string[-1]                              # record the back parenthesis or brackets of interval
        self.clean_str = self.string.strip("([])")          # get rid of "()[]"
        self.split_str = self.clean_str.split(",")          # split string by comma
        if len(self.split_str) != 2:                        # check whether the input interval has three elements.
            raise ValueError('Invalid Intervals.')          # For example, [1,2,3]
        try:
            int(self.split_str[0])                          # convert lower bound from string to int
            int(self.split_str[1])                          # convert upper bound from string to int
        except:
            raise ValueError('Invalid Intervals.')
        self.lower = int(self.clean_str.split(",")[0])
        self.upper = int(self.clean_str.split(",")[1])
        # use modified lower and upper in order to record interval in a consistant way
        # for example, record (2,4] as [3,4]
        self.mod_lower = self.lower 
        self.mod_upper = self.upper
        if self.front == '(':
            self.mod_lower += 1
        if self.back == ')':
            self.mod_upper -= 1
        if self.mod_lower > self.mod_upper:
            raise ValueError('Invalid Intervals! Incorrect: Lower and upper bound')
    def __repr__(self):
        return self.front + str(self.lower) + ',' + str(self.upper) + self.back



def canMerge(int1, int2):

    """ A helper function to return whether two intervals can merge. """

    if (int1.mod_upper < int2.mod_lower - 1) or (int2.mod_upper < int1.mod_lower - 1):
        return False
    return True


def mergeIntervals(int1, int2):

    """ mergeIntervals(int1, int2) takes two intervals as arguments. 
    If the two intervals overlap or are adjacent, it returns a merged interval,
    which is the union of these two intervals. """


    if canMerge(int1, int2) == False:
         raise ValueError('Disjoint intervals!') # raise exception if two intervals are disjoint.
    if int1.mod_lower <= int2.mod_lower and int1.lower <= int2.lower:   # pick lower bound. For example, '(2' and '[3'
        merged_lower = int1.lower
        merged_front = int1.front
    else:
        merged_lower = int2.lower
        merged_front = int2.front
    if int1.mod_upper >= int2.mod_upper and int1.upper >= int2.upper:
        merged_upper = int1.upper
        merged_back = int1.back
    else:
        merged_upper = int2.upper
        merged_back = int2.back
    result = merged_front + str(merged_lower) + ',' + str(merged_upper) + merged_back
    return interval(result)



def mergeOverlapping(intervals):
    """ mergeOverlapping takes a list of intervals.
    And merge all overlapping intervals. """
    intervals.sort(key = lambda x:x.lower)                             # sort intervals by their lower bounds
    if len(intervals) == 0 or len(intervals) == 1:                     # base case for recursion
        return intervals
    if canMerge(intervals[0], intervals[1]):
        front_result = mergeIntervals(intervals[0], intervals[1])
        intervals = intervals[2:]
        intervals.insert(0, front_result)
        return mergeOverlapping(intervals)
    else:
        return intervals[:1] + mergeOverlapping(intervals[1:])


def insert(intervals, newint):
    """insert function takes two arguments: a list of non-overlapping intervals,
    and a single interval. The function should insert an interval into lists of intervals. """
    intervals.append(newint)
    return mergeOverlapping(intervals)

if __name__ == '__main__':
    unittest.main()
    


