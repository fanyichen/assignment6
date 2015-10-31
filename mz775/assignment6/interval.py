



class interval(object):
    '''
    Object in this class has 6 attributes, as indicated below
    '''
    left = ''           #left bound of the input
    right = ''          #right bound of the input
    lower_input = 0     #smaller number in the input interval
    upper_input = 0     #bigger number in the input interval
    lower_real = 0      #smallest number in this interval 
    upper_real = 0      #biggest number in this interval

    
    def __init__(self, input_interval):                 #here I define each attributes
      
        self.left = input_interval[0]
        self.right = input_interval[-1]
        self.lower_input = int(input_interval[1:-1].split(',')[0])
        self.upper_input = int(input_interval[1:-1].split(',')[1])
        
              
        if self.left == '(' and self.right == ')':
            self.lower_real = self.lower_input +1
            self.upper_real = self.upper_input -1
            
        if self.left == '[' and self.right == ']':
            self.lower_real = self.lower_input
            self.upper_real = self.upper_input
        
        if self.left == '(' and self.right == ']':
            self.lower_real = self.lower_input +1
            self.upper_real = self.upper_input
            
        if self.left == '[' and self.right == ')':
            self.lower_real = self.lower_input
            self.upper_real = self.upper_input -1
        
        if self.validation() == False:
            raise validationError
    
    def __repr__(self):
        return self.left+str(self.lower_input)+','+str(self.upper_input)+self.right
    
    def validation(self):
        '''
        check if input is in the correct format
        '''
        
        if self.left == '[' or self.left == '(':
            if self.right == ']' or self.right == ')':
                return True
            else:
                return False
        else:
            return False  
    
        if self.left == '[':
            if self.right == ']':
                if self.lower_input <= self.upper_input:
                    return True
                else: 
                    return False
            else: #right = )
                if self.lower_input < self.upper_input:
                    return True
                else: 
                    return False
        else:
            if self.right == ']':
                if self.lower_input < self.upper_input:
                    return True
                else: 
                    return False
            else: 
                if self.lower_input < self.upper_input-1:
                    return True
                else:
                    return False

class validationError(Exception):pass

        
    

                        
            
        
            
        
    
     
