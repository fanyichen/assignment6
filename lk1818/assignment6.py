from interval_class import interval
from functions import *
import operator


interval_list = []

while True:
   if len(interval_list) == 0:
      input_string = raw_input('List of Intervals?')
      if input_string == 'quit':
         break
      input_string = input_string.replace(' ', '')
      input_split = input_string.split(',')
      try:
         for i in range(0, len(input_split), 2):
            int_i = interval(input_split[i] + ',' + input_split[i+1])
            interval_list.append(int_i)
      except:
         print('Invalid intervals') 
      interval_list = mergeOverlapping(interval_list)
   


   else:
      input_string = raw_input('Interval?')

      if input_string == 'quit':
         break
      
      input_string = input_string.replace(' ', '')
      
      try:
         int_new = interval(input_string) 
      except:
         print('Invalid intervals')

      interval_list = insert(interval_list, int_new)
      
      print(interval_list)



      
      
      
    
