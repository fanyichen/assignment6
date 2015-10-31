'''
Created on Oct 23, 2015

@author: jj1745
'''

class interval(object):
    '''
    the class that represents the range of intergers between a lower bound and an upper bound
    '''

    def __init__(self, input_string):
        '''
        Constructor
        '''
        self.input = input_string
        self.lower_bound = input_string[0]
        self.upper_bound = input_string[-1]
        
        if self.checkFormat() == False:
            raise ValueError('The upper or lower bound is not valid')
        
        self.input_list = self.input.split(',')
        
        if len(self.input_list) != 2:
            raise ValueError('Your input does not have the right number of input values')
        
        self.input_value = self.getValue()
        
               
        if self.checkInterval() == False:
            raise ValueError('Your input is not a proper interval')
        
        self.starting_value = self.getStartingValue()
        self.ending_value = self.getEndingValue()
        
                
    
    def checkFormat(self):
        '''
        Checks if the first char and the char are valid inputs for a string.
        '''
        if self.lower_bound == '(' or '[':
            if self.upper_bound == ')' or ']':
                return True
        else:
            return False    
        
    def getValue(self):
        '''
        Converts input value into a list of two numbers
        '''
        n = len(self.input)
        stripped_string = self.input[1:n-1]
        values = stripped_string.split(',')
        lower = values[0]
        upper = values[1]
        if self.getInts(lower) and self.getInts(upper):
            lower = int(values[0])
            upper = int(values[1])
            return [lower,upper]
        else:
            raise ValueError('Your input is not a number')
        
    
    def getInts(self,s):
        '''
        a helper function that make sure we get integers from the input
        '''
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    def checkInterval(self):
        '''
        Check if the input is a valid interval. Deal with inclusive/exclusive issues
        '''
        values = self.input_value
        lower = values[0]
        upper = values[1]
        if values[0] > values[1]:
            return False
        if self.lower_bound == '(' and self.upper_bound == ']':
            if lower < upper:
                return True
            else:
                return False
        elif self.lower_bound == '[' and self.upper_bound == ')':
            if lower < upper:
                return True
            else:
                return False
        elif self.lower_bound == '(' and self.upper_bound == ')':
            if lower < upper - 1:
                return True
            else:
                return False
        else:
            return True
        
    
    def getStartingValue(self):
        '''
        get the actual starting value of the interval
        '''
        values = self.input_value
        if self.lower_bound == '(':
            return values[0] + 1
        else:
            return values[0]
        
    def getEndingValue(self):
        '''
        get the actual starting value of the interval
        '''
        values = self.input_value
        if self.upper_bound == ')':
            return values[1] - 1
        else:
            return values[1]
        
         
            
            
             
            