# User defined error class
# Sida Ye

class disjoint_Error(Exception):
	# if intervals are disjoint
	def __str__(self):
		return "Disjoint Intervals!"

class invalid_Error(Exception):
	# if input interval is invalid
	def __str__(self):
		return "Invalid Interval!"