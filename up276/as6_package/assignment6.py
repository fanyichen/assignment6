'''
Created on Oct 27, 2015

@author: Urjit Patel - up276
'''

import re

from Interval import Interval,Interval_Exception
   
def main_function():
    '''
    Body of main_function from where all necessary execution of the program starts.
    Flow of the Program is as below,
    main_function() <-> insert(list,new_interval)<->mergeOverlapping(list)<->merge_interval(interval1,interval2)
    '''
    try:
        quit_flag= False    #to check whether user wants to quit the game or not
        print "INSTRUCTIONS  ::"
        print "------------------------------------------------------------------------------------------"
        print "Welcome to Merging the intervals Program. Please note that for the first User input, "
        print "user can enter as many intervals as he wants. Program will only consider valid intervals "
        print "from the list. After that user can enter only single interval each time."
        print "Error will be show for all wrong cases. Enter 'Quit' / 'quit' to exit"    
        print "------------------------------------------------------------------------------------------"
        Initial_Interval=raw_input("please enter a list of intervals : ")
        Initial_Interval = Initial_Interval.strip().replace(' ', '')    #removes all white spaces from user input
        
        if Initial_Interval in ('quit','Quit','QUIT'):
            quit_flag=True
            #print "Successfully terminated the program...Good Bye...!!!"
            #sys.exit()
        else:
            try:
                list_pattern = '([\(|\[]-?\d+,-?\d+[\)|\]])'               #pattern to find all valid intervals in user input
                list_intervals=re.findall(list_pattern,Initial_Interval)   #finds all valid interval in initial string       
                list_of_objects=[]                                         #list containing all valid interval objects
                #for loop to check all valid intervals and print them
                for ival in list_intervals:
                            try:
                                interval=Interval(ival)                    # Instance creation of Interval class
                                print ival,
                                list_of_objects.append(interval)
                            except Interval_Exception as exception:
                                print exception,                 
                print
            except:    
                raise Interval_Exception("Invalid interval")    
        if quit_flag:
            print "You successfully exited from the program ! See you soon again !"    
        #to keep asking for new interval untill user quits   
        while not quit_flag:
            Input=raw_input("Interval ? : ")
            Input = Input.strip().replace(' ', '')
            if Input in ('quit','Quit','QUIT'):
                quit_flag=True
            else:
                try:
                    interval=Interval(Input)
                    list_of_objects=Interval.insert(list_of_objects,interval)
                    
                    i=0
                    for i in range(len(list_of_objects)):
                        print list_of_objects[i].interval_string,
                    #list_of_objects=Interval.insert(list_of_objects,interval1)
                    print
                
           
                except Interval_Exception as exception:
                        print exception   
            
            if quit_flag:
                print "You successfully exited from the program ! See you soon again !"  
        
    except Interval_Exception as exception:
        print "Interval Error:", exception 

if __name__ == "__main__":
    main_function()  #call to main_function()
"""

Sample Output :-

INSTRUCTIONS  ::
------------------------------------------------------------------------------------------
Welcome to Merging the intervals Program. Please note that for the first User input, 
user can enter as many intervals as he wants. Program will only consider valid intervals 
from the list. After that user can enter only single interval each time.
Error will be show for all wrong cases. Enter 'Quit' / 'quit' to exit
------------------------------------------------------------------------------------------
please enter a list of intervals : [2,6](9,14](23,29]
[2,6] (9,14] (23,29]
Interval ? : (-1,5]
(-1,6] (9,14] (23,29]
Interval ? : (9,12)
(-1,6] (9,14] (23,29]
Interval ? : wefer
'Invalid interval'
Interval ? : (6,2)
'Invalid interval'
Interval ? : [3,9]
(-1,14] (23,29]
Interval ? : (24,31)
(-1,14] (23,31)
Interval ? : quit
You successfully exited from the program ! See you soon again !
"""