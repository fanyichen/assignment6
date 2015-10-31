'''
Created on Oct 27, 2015

@author: Urjit Patel - up276
'''
#import sys
import re
import sys
from Interval import Interval
   
def main_function():
    try:    
        str1=raw_input("please enter a list of intervals : ")
        list_pattern = '([\(|\[]-?\d+,-?\d+[\)|\]])'  
        list_intervals=re.findall(list_pattern,str1)
        i=0
        list_of_objects=[]
        #print list_intervals
        for ival in list_intervals:
                    
                    interval1=Interval(ival)
                    list_of_objects.append(interval1)
                       
        New_ival=raw_input("Interval ? : ")
        while(New_ival != 'quit'):
            interval1=Interval(New_ival)
            list_of_objects.append(interval1)
            list_of_objects.sort(key=lambda x: x.RealLowerBound)
            list_of_objects=Interval.mergeOverlapping(list_of_objects)
            #print "list elements after overlapping"
            for i in range(len(list_of_objects)):
                print list_of_objects[i].interval_string,
            #list_of_objects=Interval.insert(list_of_objects,interval1)
            print
            New_ival=raw_input("Interval ? : ")    
        
        print "Successfully terminated the program...Good Bye...!!!"
        sys.exit()
    except:
        print"error in main function...Plz run the program again and enter valid inputs" 

if __name__ == "__main__":
    main_function()
#except:
#    print"error in main function...Plz run the program again and enter valid inputs"    
# To return a new list, use the sorted() built-in function...
#newlist = sorted(ut, key=lambda x: x.count, reverse=True)
    
#print list_of_objects

#print "Converted list is :", ival.list1
#ival.mergeintervals([1,5],[3,7])

        #e = sys.exc_info()[0]
        #write_to_page( "<p>Error: %s</p>" % e )
#       loop()
#   except EOFError:
#       pass
