"""Error handling classes"""

class MergeError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InvalidIntervalError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
