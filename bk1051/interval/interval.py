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
    (0, 1, False, False)

    >>> parse_interval("[0,1]")
    (0, 1, True, True)

    >>> parse_interval("[-1, 3)")
    (-1, 3, True, False)

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
    (300, -300, False, True)
    """
    parse_regex = re.compile(r'^\s*([[(])\s*([-+]?\d+)\s*,\s*([-+]?\d+)\s*([])])\s*$')
    m = parse_regex.match(interval_string)
    if m:
        lower_inclusive = m.group(1)=="["
        lower_bound = int(m.group(2))
        upper_bound = int(m.group(3))
        upper_inclusive = m.group(4)=="]"
        return (lower_bound, upper_bound, lower_inclusive, upper_inclusive)

    else:
        raise IntervalParseException("Could not parse interval. Must be 2 integers, separated by comma, enclosed in some combination of parenthses/brackets.")





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
        (self.lower_bound, self.upper_bound,
            self.lower_is_inclusive, self.upper_is_inclusive) = parse_interval(interval_string)
        self.validate_interval()

    def __str__(self):
        '''String representation of intervals should use bracket/paren notation'''
        return "%s%d, %d%s" % (
            "[" if self.lower_is_inclusive else "(",
            self.lower_bound,
            self.upper_bound,
            "]" if self.upper_is_inclusive else ")"
        )

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

        # Rather than testing if number is in interval, we actually go through
        # each case where number would NOT be in the interval, returning False
        # if any test succeeds. If we get to the end without having returned,
        # it therefore means the number is within the interval (return True)
        if self.lower_is_inclusive and number < self.lower_bound:
            return False
        elif not self.lower_is_inclusive and number <= self.lower_bound:
            return False

        if self.upper_is_inclusive and number > self.upper_bound:
            return False
        elif not self.upper_is_inclusive and number >= self.upper_bound:
            return False

        # number doesn't fail any test, so it must be in the interval
        return True

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
    # First, get minimum/maximum values in each interval
    pass
