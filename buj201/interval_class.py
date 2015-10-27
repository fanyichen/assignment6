import re
import operator

class interval(object):
    def __init__(self, name):
        self.name = str(name)
        no_bounds = re.findall(r'[[(].*?[\])]',self.name)[0][1:-1]
        lower_upper_values = re.split(r'[\s]?,[\s]?', no_bounds)
        if len(lower_upper_values) != 2:
            raise ValueError("An input interval should specify two integer\
             values separated by a comma- a lower and an upper bound.")
        try:
            self.lower_limit = int(lower_upper_values[0])
            self.upper_limit = int(lower_upper_values[1])
        except ValueError:
            print "An input interval should specify two integer\
            values separated by a comma- a lower and an upper bound."
        if self.lower_limit > self.upper_limit:
            raise ValueError("The lower bound must be lower than the upper bound")
        self.validate_input_name(name)
        self.list_interval_integers()
    
    def __repr__(self):
        return self.name 

    def parse_bounds_from_input_string(self):
        self.lower_bound = re.search(r'[[(]', self.name).group()
        self.upper_bound = re.search(r'[)\]]', self.name).group()
    
    def construct_input_validation_test_paramaters(self):
        bounds = self.parse_bounds_from_input_string()
        if self.lower_bound == '[' and self.upper_bound == ']':
            test_operator = operator.le
            constant = 0
        elif self.lower_bound == '[' and self.upper_bound == ')':
            test_operator = operator.lt
            constant = 0
        elif self.lower_bound == '(' and self.upper_bound == ']':
            test_operator = operator.lt
            constant = 0
        elif self.lower_bound == '(' and self.upper_bound == ')':
            test_operator = operator.lt
            constant = 0
        else:
            raise ValueError("The input interval must be a character\
            string, with the first character being '[' (closed bound) or '('\
            (open bound) and the last character being ']' (closed bound) or ')'\
            (open bound).")
        return test_operator, constant
    
    def lower_and_upper_are_valid(self):
        test_operator, constant = self.construct_input_validation_test_paramaters()
        if not test_operator(self.lower_limit, self.upper_limit - constant):
            raise ValueError("The input interval does not contain any integers")
        return True
    
    def validate_input_name(self,n):
        if self.lower_and_upper_are_valid():
            self.name = str(n)
    
    def list_interval_integers(self):
        if self.lower_bound == '[':
            minimum_int = self.lower_limit
        elif self.lower_bound == '(':
            minimum_int = self.lower_limit + 1
        if self.upper_bound == ']':
            maximum_int = self.upper_limit
        elif self.upper_bound == ')':
            maximum_int = self.upper_limit-1
        self.integers = range(minimum_int, maximum_int+1)
        if len(self.integers)==0:
            raise ValueError('The input interval does not contain any integers')
        
interval('   [   1  ,   9)')
