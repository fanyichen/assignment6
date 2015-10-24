'''
Created on Oct 24, 2015

@author: ds-ga-1007
'''
import re

class IntervalParseException(Exception):
    pass

class InvalidIntervalException(Exception):
    pass

def parse_interval(interval_string):
    """Method to parse a interval string.

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


class bound(object):
    def __init__(self, value, is_inclusive):
        self.value = value
        self.is_inclusive = is_inclusive

class lowerBound(bound):
    pass

class upperBound(bound):
    pass

class interval(object):
    '''
    classdocs
    '''


    def __init__(self, interval_string):
        '''
        Constructor
        '''
        (self.lower_bound, self.upper_bound,
            self.lower_is_inclusive, self.upper_is_inclusive) = parse_interval(interval_string)
        self.validate_interval()

    def __str__(self):
        return "%s%d, %d%s" % (
            "[" if self.lower_is_inclusive else "(",
            self.lower_bound,
            self.upper_bound,
            "]" if self.upper_is_inclusive else ")"
        )

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
