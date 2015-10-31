class interval:
	'''creat a interval class object with needed attributes'''
	def __init__(self, interval):
		self.string = interval
		self.comma_index = self.string.find(",")
		self.left = int(self.string[1 : self.comma_index])
		if self.string[0] == "[":
			self.lower = self.left
		elif self.string[0] == "(":
			self.lower = self.left + 1
		self.right = int(self.string[self.comma_index+1 : -1])
		if self.string[-1] == "]":
			self.upper = self.right
		elif self.string[-1] == ")":
			self.upper = self.right - 1
		self.list = range(self.lower, self.upper+1)
	
	def __repr__(self):
		output_str = self.string + " represents the numbers %s, through %s" %(self.lower, self.upper)
		return output_str 
