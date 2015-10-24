'''
Created on Oct 24, 2015

@author: ds-ga-1007
'''

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
        self.bounds
        self.inclusive


    def _parse_interval(self, interval_string):
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

		>>> _parse_interval("(0,1)")
		(0, 1, False, False)

		>>> _parse_interval("[0,1]")
		(0, 1, True, True)

		>>> _parse_interval("[-1, 3)")
		(-1, 3, True, False)

		>>> _parse_interval("[-1, 3.5)")
		Raises exception: needs to be an integer
		(-1, 3.5, True, False)

		>>> _parse_interval("[0 13]")
		Raises exception: no comma

		>>> _parse_interval("{12, 15}")
		Raises exception: braces instead of valid delimiters

		>>> _parse_interval("12, 15")
		Raises exception, no delimiters

		Note, as shown in following test, that this method does not validate
		the actual interval (i.e. checking that lower bound is below upper
		bound); that is done in _validate_interval.
		>>> _parse_interval("(300, -300]")
		(300, -300, False, True)


		"""
