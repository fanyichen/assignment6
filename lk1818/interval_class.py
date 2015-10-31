
# Question 1
class interval(object):

   # The class should have a constructor that takes a string representation of the interval.
   def __init__(self, interval):
      self.name = interval
      # Captures type of bounds - inclusive or exclusive - from the 
      # string that constructor takes in.
      try:
	 self.leftBound = interval.split(',')[0][0]
	 self.rightBound = interval.split(',')[1][-1]
	 self.isLeftIncl = bool(self.leftBound == '[')
	 self.isLeftExcl = bool(self.leftBound == '(')
	 self.isRightIncl = bool(self.rightBound == ']')
	 self.isRightExcl = bool(self.rightBound == ')') 
      except ValueError:
	    print('Please input a string for the interval.')

      # Captures the lower integer of the interval
      if self.isLeftIncl:
         try: 
	    self.lowerParameter = int(interval.split(',')[0][1:])
         except ValueError:
	    print('The lower of the interval should be an integer.')
      elif self.isLeftExcl:
         try:
	    self.lowerParameter = int(interval.split(',')[0][1:])
         except ValueError:
            print('The lower of the interval should be an integer.')
      else: 
         raise ValueError('An interval object should start with either a square bracket or a parenthesis.')


      # Captures the upper integer of the interval
      if self.isRightIncl:
         try: 
	    self.upperParameter = int(interval.split(',')[1][:-1])
         except ValueError:
	    print('The upper of the interval should be an integer.')
      elif self.isRightExcl:
         try:
	    self.upperParameter = int(interval.split(',')[1][:-1])
         except ValueError:
	    print('The upper of the interval should be an integer.')
      else: 
         raise ValueError('An interval object should end with either a square bracket or a parenthesis.')

	
      # These variables keep track of the status of both bounds of an interval	
      self.isBothIncl = bool((self.leftBound == '[') & (self.rightBound == ']'))
      self.isBothExcl = bool((self.leftBound == '(') & (self.rightBound == ')'))
      self.isOneInclOneExcl = bool((not(self.isBothIncl)) & (not(self.isBothExcl)))

      # The bounds must always meet the requirement that lower <= upper if both bounds are inclusive, 
      # lower < upper if one bound is exclusive and one inclusive, or lower < upper-1 if both are exclusive.    
      if self.isBothIncl:
	 self.isBoundsLegit = bool(self.lowerParameter <= self.upperParameter)
      elif self.isBothExcl:
	 self.isBoundsLegit = bool(self.lowerParameter < self.upperParameter - 1)
      else:
	 self.isBoundsLegit = bool(self.lowerParameter < self.upperParameter)
     
      # This error handling ensures that the interval in this string conforms to above requirements.
      if not(self.isBoundsLegit):
	 raise ValueError('This interval is empty.')
	

   # When the class is printed, intervals are displayed using square brackets for inclusive bounds 
   # or parenthesis for exclusive bounds
   def __repr__(self):
      return '%s%d,%d%s' % (self.leftBound, self.lowerParameter, self.upperParameter, self.rightBound)


