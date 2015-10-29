
from interval import *
import sys

def no_space(interval_string):
    '''
    use this function to get rid of white space in intervals from users
    '''
    no_space_str = str()
    for element in interval_string:
        if element != ' ':
            no_space_str += element
    return no_space_str


def mergeIntervals(int1,int2):
    '''
    Question 2. This is a function to merge two overlapping intervals, and would throw an value error if two intervals
    do not overlap.
    '''
    int1 = no_space(int1)
    int2 = no_space(int2)
    int1 = interval(int1)
    int2 = interval(int2)

    if int1.upper_real >= int2.lower_real or int1.lower_real >= int2.upper_real:
        # see if there is overlapping
        integers = [int1.lower_input,int1.upper_input,int2.lower_input,int2.upper_input]
        integers.sort()
        #sort 4 integers from user
        merged_lower_integer = str(integers[0])
        merged_upper_integer = str(integers[-1])
        #get the biggest and smallest integers that can be integer bounds for merged interval
        int1_convert_list = [int1.left,str(int1.lower_input),str(int1.upper_input),int1.right]
        int2_convert_list = [int2.left,str(int2.lower_input),str(int2.upper_input),int2.right]
        #use multiple if statement to rearrange integer bounds and interval bounds to get merged interval               
        if merged_lower_integer in int1_convert_list:
            if merged_lower_integer in int2_convert_list:
                if int1_convert_list [0] == int2_convert_list [0]:
                    merged_left = int1_convert_list [0]
                else:
                    merged_left = '['
            else:
                merged_left = int1_convert_list [0]
        else:
            merged_left = int2_convert_list [0]
            
        if merged_upper_integer in int1_convert_list:
            if merged_upper_integer in int2_convert_list:
                if int1_convert_list [-1] == int2_convert_list [-1]:
                    merged_right = int1_convert_list [-1]
                else:
                    merged_right = ']'
            else:
                merged_right = int1_convert_list [-1]
        else:
            merged_right = int2_convert_list [-1]    
        merged_interval_list = [merged_left,merged_lower_integer,',',merged_upper_integer,merged_right]
        merged_interval = ''.join(merged_interval_list)
    else:
        raise ValueError
    return merged_interval



def interval_list(interval_list_input):
    '''
    this is a function that converts a string consisting of multiple intervals such as '(1,3),(2,5),[9,10]' into 
    a string list containing many interval elements, such as ['(1,3)','(2,5)','[9,10]']
    '''
    interval_list_input = no_space(interval_list_input)
    interval_list_split1 = interval_list_input.split('],')
    interval_list=[]
    for element in interval_list_split1:
        if element[-1] != ']' and element[-1] != ')':
            element = element + ']'
        interval_list.append(element)
        
    interval_list_1=[]
    
    for element in interval_list:
        element = element.split('),')
        interval_list_1.append(element)
        interval_list_2=[]
        interval_list_3=[]
    for i in range(0,len(interval_list_1)):
        for j in range(0,len(interval_list_1[i])):
            if interval_list_1[i][j][-1] != ')' and interval_list_1[i][j][-1] != ']':
                interval_list_1[i][j] = interval_list_1[i][j] + ')'
                interval_list_2.append(interval_list_1[i][j])
            else:
                interval_list_3.append(interval_list_1[i][j])
                
    interval_list_final = interval_list_2+interval_list_3
    new = []
    for element in interval_list_final:
        try:
            element=interval(element)
            new.append(element)
        except validationError:
            new=[]
    if len(new) == len(interval_list_final):
        
        return interval_list_final
    else:
        raise validationError



            
def sorting(int1,int2):
    '''
    this is a function that sorts intervals by the smallest number in the interval
    '''
    int1=no_space(int1)
    int2=no_space(int2)
    int1 = interval(int1)
    int2 = interval(int2)
    if int1.lower_real < int2.lower_real:
        return -1
    if int1.lower_real > int2.lower_real:
        return 1
    else:
        return 0 
                   
        

def mergeOverlapping(intervals):
    '''
    Question 3. This is a function that merges a list of intervals.
    '''
    intervals = interval_list(intervals)    #convert the input into a list of many interval strings
    intervals.sort(sorting)                 #sort the intervals by their smallest number 
    intervals_list=[]                       # an empty list used to store merged and unmerged intervals
    for i in range(0,len(intervals)):
        if len(intervals_list) == 0:
            intervals_list.append(intervals[i])
        else:
            try:
                merged = mergeIntervals(intervals_list[-1],intervals[i])
                intervals_list.pop()
                intervals_list.append(merged)
            except ValueError:
                intervals_list.append(intervals[i])    
    return intervals_list



def insert(intervals,newint):
    '''
    Question 4. This is a function that inserts a new interval into a list of intervals and returns merged results
    '''
    intervals = intervals + ','+newint 
    return mergeOverlapping(intervals)
    

def main():
    '''
    Question 5. This function takes input from users and return merged results.
    '''
    user_input = raw_input('List of intervals?')
    while len(user_input) == 0:
        print 'please enter intervals'
        user_input = raw_input('List of intervals?')
    
    if user_input == 'quit':
        sys.exit()
    else: 
        try:
            user_input_convert = interval_list(user_input)
            user_input_valid = user_input
        except validationError:
            raise validationError('there is invalid interval(s) in your list, please re-enter in the correct format')
    
    if len(user_input_convert) > 0:
        user_input_single_interval = raw_input('Interval?')
        while len(user_input_single_interval) == 0:
            print 'please enter interval or quit'
            user_input_single_interval = raw_input('Interval?') 
        while len(user_input_single_interval) != 0:           
            if user_input_single_interval == 'quit':
                sys.exit()
            else:
                user_input_single_interval_check = interval(user_input_single_interval)
                while user_input_single_interval_check.validation() == False:
                    print 'invalid interval'
                    user_input_single_interval = raw_input('Interval?')    
                new_int_list = insert(user_input_valid,user_input_single_interval)
                user_input_valid = user_input_valid+','+user_input_single_interval            
                print new_int_list
                user_input_single_interval = raw_input('Interval?') 



if __name__ == '__main__':
    main()
   
        
        
    
        
        
        
    
        
    
    
          

                
                    
                
                
         
    
    
            
        
    
    
        
        
        
