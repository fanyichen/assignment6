'''
Definition of the class - interval
'''
import re
import custom_exceptions as cexcep

class interval:
	'''Represents a range of integers between a lower bound and an upper bound'''

	def __init__(self, interval_as_string):		# Constructor
		if (are_bound_types_valid(interval_as_string)):
			self.__lower_bound_type = interval_as_string[0]
			self.__upper_bound_type = interval_as_string[-1]

			__lower_bound_value, __upper_bound_value = valid_bounds(interval_as_string, self.__lower_bound_type, self.__upper_bound_type)
			if (__lower_bound_value != None):
				self.__lower_bound_value, self.__upper_bound_value = __lower_bound_value, __upper_bound_value 
			else:
				raise cexcep.InvalidBoundsException("Invalid interval bounds")
		else:
			raise cexcep.InvalidBoundTypeException("Invalid interval bound types")

	def get_lower_bound_value(self):		# Returns the lower bound value
		return self.__lower_bound_value

	def get_upper_bound_value(self):		# Returns the upper bound value
		return self.__upper_bound_value

	def get_lower_bound_type(self):			# Returns the lower bound type
		return self.__lower_bound_type

	def get_upper_bound_type(self):			# Returns the upper bound type
		return self.__upper_bound_type

	def __repr__(self):
		return self.__lower_bound_type + "" + str(self.__lower_bound_value) + ", " + str(self.__upper_bound_value) + self.__upper_bound_type


def are_bound_types_valid(interval_as_string):
	''' To validate the parenthesis'''

	__valid_lower_bound_type = ['(', '[']
	__valid_upper_bound_type = [')', ']']

	lower_bound_type = interval_as_string.strip()[0]
	upper_bound_type = interval_as_string.strip()[-1]

	if (lower_bound_type in __valid_lower_bound_type) and (upper_bound_type in __valid_upper_bound_type):
		return 1
	return 0


def valid_bounds(interval_as_string, __lower_bound_type, __upper_bound_type):
	'''Returns the numbers if they are valid else returns None'''

	bound_values = [int(bound) for bound in re.findall("[-+]?\d+", interval_as_string)]
	temp_bound_values = bound_values[:]
	if (__lower_bound_type == '('):
		temp_bound_values[0] += 1
	if (__upper_bound_type == ')'):
		temp_bound_values[1] -= 1 

	if temp_bound_values[0] <= temp_bound_values[1]:
		return bound_values[0], bound_values[1]
	else:
		return None, None


'''
if __name__ == '__main__':
	interval_obj1 = interval("(2, 5)")
	print "Passed 1: ", interval_obj1
	interval_obj2 = interval("(3, 4(")
	print "Passed 2"
	interval_obj3 = interval("[1, 8)")
	print "Passed 3"
	interval_obj4 = interval("]3, 6]")
	print "Passed 4: ", interval_obj4
	interval_obj5 = interval("[6, 1)")

'''