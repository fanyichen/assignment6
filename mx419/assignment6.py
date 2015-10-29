"""this is the main program that interact with users and generates the result """
'''Author: Muhe Xie  ID:mx419'''

from interval import *
from user_defined_exceptions import *
import re



#import re
#import sys
def start_merge():
    Intervals = []  #inlcude all the original intervals 
    #this block will read the input of the interval of the list
    while True:
        Intervals = [] #to make sure that once initialization fails, the original Interval will be cleaned
        print "Please Enter a list of intervals (format like [1,2] ,[3,5] enter \'quit\' to exit):"
        initial_interval_list_string = raw_input()
        if initial_interval_list_string == "quit": #quit the program
            print "Bye bye"
            return
            
        else:
            try:
                if initial_interval_list_string == "": #test empty input 
                    raise Empty_Input_Error
                else:
                	#use regular expression to check the format, a valid format like (3,6],(6,7], [-100,-99)
                    if  not re.match(r"\s*(\(|\[)\s*(-){0,1}[0-9]+\s*,\s*(-){0,1}[0-9]+\s*(\)|\])\s*(,(\s*(\(|\[)\s*(-){0,1}[0-9]+\s*,\s*(-){0,1}[0-9]+\s*(\)|\]))\s*){0,}$", initial_interval_list_string): 
                        raise Input_Format_Error
                        
                    else:
                        #use regular expression to extract the interval string, pattern like '[2,6]'
                        interval_lists = re.findall(r"[\(\[]\s*[-]{0,1}[0-9]+\s*,\s*[-]{0,1}[0-9]+\s*[\]\)]", initial_interval_list_string)
                        for i in range(0,len(interval_lists)):
                            Intervals.append(interval(interval_lists[i]))
                        break 
                            
            except Empty_Input_Error:
                print "The input is empty, please re-enter the intervals"

            except Input_Format_Error:
                print "The input format is wrong, please re-enter the intervals"
                
            except Test_Error:
                print "this is a test error"
                
            except Bound_Error:
                print "The interval bound is wrong,please re-enter the intervals"
    
    
    #this will merge the origin interval list and return a sorted result, the result is stored in this variable
    Merged_Intervals = mergeOverlapping(Intervals)

    #this block will take the input of a single interval and keep printing the result of the intervals after merge
    while True:
        print "Please Enter a interval (format like [1,2] enter \'quit\' to exit):"
        single_new_interval_str = raw_input()
        if single_new_interval_str == "quit":
            print "Bye bye"
            return
        else:
            try:
                if single_new_interval_str == "": #test empty input 
                    raise Empty_Input_Error
                else:
                	#use regular expression to check the format, a valid format like (3,6]
                    if not re.match(r"\s*[\(\[]\s*[-]{0,1}[0-9]+\s*,\s*[-]{0,1}[0-9]+\s*[\]\)]\s*$",single_new_interval_str):
                        raise Input_Format_Error
                    else:
                    	#use regular expression to extract the interval string, pattern like '[2,6]'
                        single_interval_str= re.findall(r"[\(\[]\s*[-]{0,1}[0-9]+\s*,\s*[-]{0,1}[0-9]+\s*[\]\)]", single_new_interval_str)
                        single_interval = interval(single_interval_str[0])
                        Merged_Intervals = insert(Merged_Intervals,single_interval)
                        print Merged_Intervals
                        
                        
            except Empty_Input_Error:
                print "The input is empty,please re-enter the interval"
                
            except Input_Format_Error:
                print "The input format is wrong,please re-enter the interval"       
                
            except Bound_Error:
                print "The interval bound is wrong,please re-enter the intervals"
            
                


if __name__ == "__main__":
    try:
        start_merge()

    except KeyboardInterrupt:
        print "the program has been stopped by KeyboardInterrupt, thanks for trying, Byebye"
    except EOFError:
        print "the program has been stopped by EOFERROR, thanks for trying, Byebye"
