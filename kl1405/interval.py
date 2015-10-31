
# coding: utf-8

# In[ ]:

class interval(object):
    """A class for generating interval"""
    def __init__(self, string):
        self.string = string
    # Get the bound
        self.bound()
        # Check if valid or not
        self.Check()

    def bound(self):
        # Split the string into two parts.
        Bound = self.string.split(',')

        # Get the lowerbound for inclusive or exclusive
        if Bound[0][0] == '(':
            self.lowerbound = int(Bound[0][1:]) + 1
        elif Bound[0][0] == '[':
            self.lowerbound = int(Bound[0][1:])
        else:
            self.lowerbound = False

        # Get the upperbound for inclusive or exclusive
        if Bound[-1][-1] == ')':
            self.upperbound = int(Bound[1][:-1]) - 1
        elif Bound[-1][-1] == ']':
            self.upperbound = int(Bound[1][:-1])
        else:
            self.upperbound = False

        # Check if this is a valid interval
        if self.lowerbound > self.upperbound:
            self.check = False
        else:
            if self.lowerbound and self.upperbound:
                self.check = True

    # Print the validation result 
    def Check(self):
        if self.lowerbound and self.upperbound and self.check:
            self.check = True
        else:
            self.check = False


