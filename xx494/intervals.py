import re
import operator

class interval:
    def __init__(self,user_input):
        self.input=user_input
        self.lower_value,self.upper_value=self.interval_process()
        self.valid_input,self.lower_bound,self.upper_bound=self.valid_test(self.input)
        self.print_list()
    def interval_process(self):
        values_bound=re.findall(r'[[(].*?[)\]]',self.input)[0][1:-1]
        values=re.split(r'[\s]*,[\s]*',values_bound)
        if len(values) !=2:
            print "interval enter error:more than two arguments"
        lower_value=int(values[0])
        upper_value=int(values[1])
        if lower_value>upper_value:
            print "lower value should be lower or equal than upper value"
            
        return lower_value,upper_value

    def valid_test(self,input):
        lower_bound=re.search(r'[[(]',self.input).group()
        upper_bound=re.search(r'[)\]]',self.input).group()
        if lower_bound == '[' and upper_bound == ']':
            test_operator = operator.le
            constant = 0
        elif lower_bound == '[' and upper_bound == ')':
            test_operator = operator.lt
            constant = 0
        elif lower_bound == '(' and upper_bound == ']':
            test_operator = operator.lt
            constant = 0
        elif lower_bound == '(' and upper_bound == ')':
            test_operator = operator.lt
            constant = 0
        else:
            print "input error"
            
        if test_operator and constant==0:
            return str(input),lower_bound,upper_bound
    def print_list(self):
        if self.lower_bound == '[':
            minimum_int = self.lower_value
        elif self.lower_bound == '(':
            minimum_int = self.lower_value + 1
        if self.upper_bound == ']':
            maximum_int = self.upper_value
        elif self.upper_bound == ')':
            maximum_int = self.upper_value-1
        self.integers = range(minimum_int, maximum_int+1)
        #print self.integers
        if len(self.integers)==0:
            print 'The input interval does not contain any integers'

if __name__=="__main__":
    i=interval('[1,3]')



