"""this module define some user-defined exceptions"""
'''Author: Muhe Xie  ID:mx419'''

# user input empty
class Empty_Input_Error(Exception):
	# raised when user input is empty
    def __str__(self):
        return 'The input is empty\n'
         
class Input_Format_Error(Exception):
	# raised when user's input's format is wrong
    def __str__(self):
        return 'The input format is wrong\n'
    
class Test_Error(Exception):
	# for test
    def __str__(self):
        return 'The input format is wrong\n'

class Bound_Error(Exception):
	# raised when the upper bound and the lower bound of the interval do not conform the requirement
    def __str__(self):
        return 'The interval bound is wrong\n'

class Not_Overlap_Error(Exception):
	# raised when the upper bound and the lower bound of the interval do not conform the requirement
    def __str__(self):
        return 'The intervals do not overlap\n'