# This program is to manage the user-input intervals. First have a list of intervals entered,
# then by taking new input interval to merge intervals.
# input of valid intervals must start with [,(, and end with ),] in order for correct output

import re
import sys
from interval import interval
from interval_functions import *

def prompt():
	'''Start the program by prompting user input'''
	start = True
	print "Please enter a list of intervals, start with '[]()', and put ', ' in between intervals."
	user_list = raw_input("List of intervals? \n")
	if user_list in ["quit","Quit","q","Q"]:
		start = False
		return
	interval_list = user_list.split(", ")
	for element in interval_list:
		if not validInput(element):
			start = False
		else:
			start = True
	while start:
			user_interval = raw_input("Interval? (please enter only in the right format):\n")
			if user_interval in ["quit","Quit","q","Q"]:
				start = False
				return
			elif not validInput(user_interval):
				print "Invalid interval"
				pass
			else:	
				insert_interval = interval(user_interval)
				if len(insert_interval.list) == 0:
					print "Invalid interval"
				else:
					interval_list = insert(interval_list, user_interval)
					print interval_list

def validInput(input_interval):
	'''check is input interval is valid'''
	delimiters = ",", "[","]", "(",")"
	regexPattern = '|'.join(map(re.escape, delimiters))
	int_element = re.split(regexPattern, input_interval)
	if input_interval[0] in ["[","]","(",")"] or input_interval[-1] in ["[","]","(",")"]:
		try:
			lower = int(int_element[1])
			upper = int(int_element[-2])
			return True
		except:
			return False
	else:
		return False

class InvalidIntervalError(Exception):
	def __str__(self):
		return 'Invalid interval'

if __name__ == "__main__":
	try:
		prompt()

	except:
		pass
