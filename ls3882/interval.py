
class interval:
    left_bound, right_bound = '', ''
    left, right = 0, 0
    actual_left, actual_right = 0, 0
    
    def __init__(self, user_input):
        
        self.left_bound= user_input[0];
        self.left = int(user_input[1:user_input.index(',')])
        self.right_bound = user_input[-1]
        self.right = int(user_input[user_input.index(',')+1:-1])
        
        if self.left_bound == '(':
            self.actual_left = self.left + 1
        else:
            self.actual_left = self.left
        
        if self.right_bound == ')':
            self.actual_right = self.right - 1
        else:
            self.actual_right = self.right
            
        if self.validate_interval() == False:
            raise ValidationError
            
    def validate_interval(self):
        '''Check if left and right bounds of the interval is valid'''
        if self.left_bound == '[':
            if self.right_bound == ']':
                if self.left <= self.right:
                    return True
                else:
                    return False
            elif self.right_bound == ")":
                if self.left < self.right:
                    return True    
                else:
                    return False
        elif self.left_bound == '(':
            if self.right_bound == ']':
                if self.left-1 < self.right:
                    return True
                else:
                    return False
            elif self.right_bound == ")":
                if self.left < self.right-1:
                    return True  
                else:
                    return False
        else:
            return False
        
    def print_int(self):
        print self.left_bound + str(self.left) + ',' + str(self.right) + self.right_bound,

class ValidationError(Exception): pass
    
        