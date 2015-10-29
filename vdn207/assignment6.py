'''The main program which interacts with the user'''

from interval_operations import mergeIntervals, mergeOverlapping, insert
import interval as inter
import re
import custom_exceptions as cexcep

def find_intervals(initial_input):
	'''Returns a list of intervals from a string'''
	
	return [str(interval) for interval in re.findall('[(\[]-?\d+,-?\d+[)\]]', initial_input)]

if __name__ == '__main__':

	print "WELCOME TO THE INTERVAL. ENTER VALID LIST OF INTERVALS TO BEGIN. IF NOT ONLY VALID INTERVALS WILL BE TAKEN \n"
	print "Enter 'quit' to exit\n"

	initial_input_fail = True
	while initial_input_fail:	# Reading the input list until valid intervals are given
		try:
			initial_input = raw_input("List of intervals? ")
			if initial_input == 'quit':	# If the user wants to quit
				exit()

			intervals = find_intervals(initial_input)	# Extracting intervals from a user input
			if len(intervals) == 0:
				print "Invalid Interval"
				continue
			try:
				list_of_intervals = [inter.interval(sample_interval) for sample_interval in intervals]
				initial_input_fail = False
			except cexcep.InvalidBoundsException:
				continue
		except KeyboardInterrupt:
			continue

	while True:		# Reading subsequent intervals from the user until he/she quits
		try:	
			user_input = raw_input("Interval? ")	
			if user_input == 'quit':	# If the user wants to quit
				break
			try:	# Creating an object of type 'interval'
				user_interval = inter.interval(user_input)	
			except (cexcep.InvalidBoundsException, cexcep.InvalidBoundTypeException):
				print "Invalid interval"
				continue
			else:	# Merging the valid interval with the existing list of intervals
				list_of_intervals = insert(list_of_intervals, user_interval)
				print [interval for interval in list_of_intervals]

		except KeyboardInterrupt:
			continue