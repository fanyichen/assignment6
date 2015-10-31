'''user defined exceptions to raise specific errors of invalid input and intervals'''

class interval_bad_leftbound(Exception):
	'''raise bad left bound error'''

	def __str__(self):
		return 'invalid interval: left bound!'

class interval_bad_rightbound(Exception):
	'''raise bad right bound error'''

	def __str__(self):
		return 'invalid interval: right bound!'

class interval_bad_invalidbound(Exception):
	'''raise bad lower or upper bound error'''

	def __str__(self):
		return 'invalid interval: invalid lower/upper bound!'

class interval_bad_zero(Exception):
	'''raise zero length interval error'''

	def __str__(self):
		return 'invalid interval: lower bound > upper bound!'

class interval_bad_nocomma(Exception):
	'''raise interval with no comma error'''

	def __str__(self):
		return 'invalid interval: comma not found!'

class merge_bad(Exception):
	'''raise error that two intervals cannot merge'''

	def __str__(self):
		return 'the two intervals can not be merged...'
