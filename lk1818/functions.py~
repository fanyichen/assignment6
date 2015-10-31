import operator
from interval_class import interval

# Question 2
# Define a function mergeIntervals(int1, int2) that takes two intervals. 
# If the intervals overlap or are adjacent, returns a merged interval. 

def mergeIntervals(int1, int2):

   # Determines the lower bound and lower parameter of the merged interval, assuming overlapping does exist.
   if int1.lowerParameter > int2.lowerParameter:
      merged_lowerParameter = int1.lowerParameter
      merged_leftBound = int1.leftBound
   elif int1.lowerParameter < int2.lowerParameter:
      merged_lowerParameter = int2.lowerParameter
      merged_leftBound = int2.leftBound
   else:
      if int1.isLeftIncl == int2.isLeftIncl:
	 merged_lowerParameter = int1.lowerParameter
	 merged_leftBound = int1.leftBound
      else:
         merged_lowerParameter = int1.lowerParameter
         merged_leftBound = '('


    # Determines the upper bound and upper parameter of the merged interval, assuming overlapping does exist.
   if int1.upperParameter < int2.upperParameter:
      merged_upperParameter = int1.upperParameter
      merged_rightBound = int1.rightBound
   elif int1.upperParameter > int2.upperParameter:
      merged_upperParameter = int2.upperParameter
      merged_rightBound = int2.rightBound
   else:
      if int1.isRightIncl == int2.isRightIncl:
	 merged_upperParameter = int1.upperParameter
	 merged_rightBound = int1.rightBound
      else:
         merged_upperParameter = int1.upperParameter
         merged_leftBound = ')'


   # If the intervals cannot be merged, an exception should be thrown.
   if merged_lowerParameter > merged_upperParameter:
      raise ValueError('There is no overlapping between these two intervals.')
   elif (merged_lowerParameter == merged_upperParameter) & ((not(merged_leftBound == '[')) | (not(merged_rightBound == ']'))):
      raise ValueError('There is no overlapping between these two intervals.')
   elif (merged_lowerParameter == merged_upperParameter - 1) & ((merged_leftBound == '(') & (merged_rightBound == ')')):
      raise ValueError('There is no overlapping between these two intervals.')

   else: 
      merged_string = merged_leftBound + str(merged_lowerParameter) + "," + str(merged_upperParameter) + merged_rightBound
      merged_interval = interval(merged_string)

   return merged_interval


 

# Question 3
# Define the function mergeOverlapping(intervals) that takes a list of intervals and merges all overlapping intervals.
def mergeOverlapping(intervals):
   isOverlapping = True
   while isOverlapping == True:
      isOverlapping = False
      intervals = sorted(intervals, key = operator.attrgetter('lowerParameter'))
      if len(intervals) == 1:
         break
      for i in range(0, len(intervals) - 1, 1):
         for j in range(i + 1, len(intervals), 1):
            try:
               mergeIntervals(intervals[i], intervals[j])
            except: 
               continue
            else: 
               isOverlapping = True
               int_new = mergeIntervals(intervals[i], intervals[j])
               intervals.append(int_new)
               intervals.remove(intervals[j])
               intervals.remove(intervals[i])
            
               
   return intervals


# Question 4
# Define a function insert(intervals, newint) that takes two arguments: a list of non-overlapping intervals; and a single interval.
# The function should insert newint into intervals, merging the result if necessary. 
# The resulting list should also be sorted according to their lower bounds.
def insert(intervals, newint):
   intervals.append(newint)
   intervals = mergeOverlapping(intervals)
   return intervals
