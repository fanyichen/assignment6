'''
Created on Oct 24, 2015

@author: ds-ga-1007
'''
import re

# Define some custom exceptions
class IntervalParseException(Exception):
    '''Exception to be raised when an interval string cannot be parsed.'''
    pass

class InvalidIntervalException(Exception):
    '''Exception to be raised when an interval is invalid.'''
    pass

class IntervalMergeException(Exception):
    '''Exception to be raised when problem merging intervals'''
    pass




def parse_interval(interval_string):
    """Function to parse an interval string.

    The string should contain two integers, separated by a comma.
    The first number is the lower bound, the second number the
    upper bound. The two integers should be enclosed in an opening
    and closing character, with each being either a bracket--"["/"]"--
    or a parenthesis--"("/")"; brackets indicate that the bound is
    inclusive (i.e. that the bound is included in the interval), while
    parentheses indicate that the bound is exclusive.

    If the interval string cannot be parsed, the method raises an
    IntervalParseException.

    >>> parse_interval("(0,1)")
    (False, 0, 1, False)

    >>> parse_interval("[0,1]")
    (True, 0, 1, True)

    >>> parse_interval("[-1, 3)")
    (True, -1, 3, False)

    >>> parse_interval("[-1, 3.5)")
    Traceback (most recent call last):
        ...
    IntervalParseException: Could not parse interval. Must be 2 integers, separated by comma, enclosed in some combination of parenthses/brackets.


    >>> parse_interval("[0 13]")
    Traceback (most recent call last):
        ...
    IntervalParseException: Could not parse interval. Must be 2 integers, separated by comma, enclosed in some combination of parenthses/brackets.

    >>> parse_interval("{12, 15}")
    Traceback (most recent call last):
        ...
    IntervalParseException: Could not parse interval. Must be 2 integers, separated by comma, enclosed in some combination of parenthses/brackets.

    >>> parse_interval("12, 15")
    Traceback (most recent call last):
        ...
    IntervalParseException: Could not parse interval. Must be 2 integers, separated by comma, enclosed in some combination of parenthses/brackets.

    Note, as shown in following test, that this method does not validate
    the actual interval.

    >>> parse_interval("(300, -300]")
    (False, 300, -300, True)
    """
    parse_regex = re.compile(r'^\s*([[(])\s*([-+]?\d+)\s*,\s*([-+]?\d+)\s*([])])\s*$')
    m = parse_regex.match(interval_string)
    if m:
        lower_inclusive = m.group(1)=="["
        lower_bound = int(m.group(2))
        upper_bound = int(m.group(3))
        upper_inclusive = m.group(4)=="]"
        return (lower_inclusive, lower_bound, upper_bound, upper_inclusive)

    else:
        raise IntervalParseException("Could not parse interval. Must be 2 integers, separated by comma, enclosed in some combination of parenthses/brackets.")



def interval_to_string(interval_tuple):
    '''Function to convert an interval tuple to a string'''
    return "%s%d, %d%s" % (
        "[" if interval_tuple[0] else "(",
        interval_tuple[1],
        interval_tuple[2],
        "]" if interval_tuple[3] else ")"
    )


class interval(object):
    '''
    This interval class is used to represent a range of integers. Each interval
    has a lower and upper bound, and each bound is either inclusive (i.e. closed)
    or exclusive (open). If both bounds are inclusive, lower bound must be <=
    upper bound. If one bound is inclusive and one is exclusive, lower bound
    must be < upper bound. If both bounds are exclusive, lower bound must be
    < upper bound - 1.
    '''


    def __init__(self, interval_string):
        '''
        Constructor. Parse the interval string into upper and lower bounds,
        and create booleans for whether each is inclusive or not. Then,
        ensure those parameters describe a valid interval.
        '''
        (self.lower_is_inclusive, self.lower_bound,
            self.upper_bound, self.upper_is_inclusive) = parse_interval(interval_string)
        self.validate_interval()

    def __str__(self):
        '''String representation of intervals should use bracket/paren notation'''
        return interval_to_string((self.lower_is_inclusive,
                                    self.lower_bound,
                                    self.upper_bound,
                                    self.upper_is_inclusive))

    def __eq__(self, other):
        '''Test if one interval is equal to another; true if both are same class
        and both have same string representation.'''
        if isinstance(other, self.__class__):
            return self.__str__() == other.__str__()
        else:
            return False

    def __ne__(self, other):
        '''Intervals are not equal to each other if __eq__() returns False'''
        return self.__eq__(other) == False


    def validate_interval(self):
        '''Tests whether the parsed interval is valid.
        If not, raises an InvalidIntervalException.'''
        if self.lower_bound < self.upper_bound - 1:
            # Valid regardless of whether bounds are inclusive
            return
        elif self.lower_bound < self.upper_bound:
            # Only valid if at least one bound is inclusive
            if self.lower_is_inclusive or self.upper_is_inclusive:
                return
            else:
                raise InvalidIntervalException("Invalid interval. Lower bound must be < upper bound - 1 for open intervals")
        elif self.lower_bound == self.upper_bound:
            if self.lower_is_inclusive and self.upper_is_inclusive:
                return
            else:
                raise InvalidIntervalException("Invalid interval. Lower and upper bounds can only be equal for closed intervals")
        else:
            raise InvalidIntervalException("Invalid interval. Lower bound cannot be greater than upper bound")

    def contains(self, number):
        '''Returns True if number is contained in interval, False otherwise'''
        # First test if number is an integer
        if int(number) != number:
            raise ValueError("Intervals can only contain integer values")

        return number >= self.min_integer() and number <= self.max_integer()

    def max_integer(self):
        '''Returns the maximum integer contained in interval'''
        return self.upper_bound if self.upper_is_inclusive else self.upper_bound - 1

    def min_integer(self):
        '''Returns the minimum integer contained in interval'''
        return self.lower_bound if self.lower_is_inclusive else self.lower_bound + 1




def mergeIntervals(int1, int2):
    '''Function to merge two intervals. If they overlap or are adjacent, then
    return the merged interval. If they cannot be merged, throw an
    IntervalMergeException.'''

    # Test each interval to see if it contains the minimum integer in the other
    # If it does, that means we want its lower bound/inclusiveness to be the
    # lower bound for the merged interval, unless the other interval has
    # a lower but open bound - i.e. we want (2, 5) and [3, 4]. to merge to
    # (2, 5), even though both intervals have the same numbers.
    # Then we do the same for the upper
    lower_bound = None
    lower_is_inclusive = None
    upper_bound = None
    upper_is_inclusive = None

    if int1.contains(int2.min_integer()) or int1.contains(int2.min_integer() - 1) or \
        int2.contains(int1.min_integer()) or int2.contains(int1.min_integer() - 1):
        # Intervals are overlapping or adjacent. Now we need to figure out which
        # interval's lower bound to use. First try to get the lowest lower bound
        # (i.e. want (0, 5) over [1, 5)). If they're equal, pick whichever has
        # the lowest minimum integer (i.e. want [1, 5] over (1, 5])
        if int1.lower_bound < int2.lower_bound or int1.min_integer() < int2.min_integer():
            lower_bound, lower_is_inclusive = int1.lower_bound, int1.lower_is_inclusive
        else:
            lower_bound, lower_is_inclusive = int2.lower_bound, int2.lower_is_inclusive
        #
        # elif int2.lower_bound > int1.lower_bound or int2.min_integer() < int1.min_integer():
        #     lower_bound, lower_is_inclusive = int2.lower_bound, int2.lower_is_inclusive
        # else:
        #     # Both lower bounds are the same, so just pick the second one
        #
        # elif int1.min_integer() < int2.min_integer():
        #     # Both lower bounds are equal, but int1 is inclusive and the other is not
        #     lower_bound, lower_is_inclusive = int1.lower_bound, int1.lower_is_inclusive
        # else:
        #     lower_bound, lower_is_inclusive = int2.lower_bound, int2.lower_is_inclusive


    if int1.contains(int2.max_integer()) or int1.contains(int2.max_integer() + 1) or \
        int2.contains(int1.max_integer()) or int2.contains(int1.max_integer() + 1):
        if int1.upper_bound > int2.upper_bound or int1.max_integer() > int2.max_integer():
            upper_bound, upper_is_inclusive = int1.upper_bound, int1.upper_is_inclusive
        else:
            upper_bound, upper_is_inclusive = int2.upper_bound, int2.upper_is_inclusive

    #     elif int2.upper_bound > int1.upper_bound:
    #         upper_bound, upper_is_inclusive = int2.upper_bound, int2.upper_is_inclusive
    #     elif int1.max_integer() > int2.max_integer:
    #         upper_bound, upper_is_inclusive = int1.upper_bound, int1.upper_is_inclusive
    # elif int2.contains(int1.max_integer()) or int2.contains(int1.max_integer() + 1):
    #
    #         upper_bound, upper_is_inclusive = int2.upper_bound, int2.upper_is_inclusive
    #     else:
    #         upper_bound, upper_is_inclusive = int1.upper_bound, int1.upper_is_inclusive

    # First, get minimum/maximum values in each interval
    if lower_bound is None or upper_bound is None or \
        lower_is_inclusive is None or upper_is_inclusive is None:
        raise IntervalMergeException("Cannot merge intervals %s and %s; they are neither overlapping nor adjacent." % (int1, int2))

    return interval(interval_to_string((
            lower_is_inclusive,
            lower_bound,
            upper_bound,
            upper_is_inclusive
        )))



def mergeOverlapping(intervals):
    '''Merge all overlapping intervals in the list intervals.'''
    # If not at least 2 intervals, just return the input
    if len(intervals) <= 1:
        return intervals
    #
    # merged = None
    # try:
    #     merged = mergeIntervals(intervals[0], intervals[1])
    # except IntervalMergeException:
    #     pass
    # else:
    #     intervals = intervals[2:].append(merged)

    result = []
    for i, int1 in enumerate(intervals):
        for j, int2 in enumerate(intervals):
            merged = None
            try:
                merged = mergeIntervals(int1, int2)
            except IntervalMergeException:
                print "NO MERGE:", int1, int2, merged
            else:
                print int1, int2, "=>", merged
                result.append(merged)
    print "Results:", [str(i) for i in result]
    return intervals
