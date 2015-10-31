from intervals import *



def add_input(interval_list,user_input):
	user_interval = intervalInt(user_input)
	interval_list_tmp = interval_list[:]
	if len(interval_list_tmp) != 0:
		interval_list_tmp = insert(interval_list_tmp,user_interval)
	else:
		interval_list_tmp.append(user_interval)
	return interval_list_tmp


if __name__ == '__main__':
	
	help_string = "\tInterval should be a of the form '[a,b]', '(a,b]', '[a,b)' \n\r\
	or '(a,b)' where a and be must be integer numbers \n\r \
	The bounds must always meet the requirement \n\r\
	that lower <= upper if both bounds are inclusive, \n\r\
	lower < upper if one bound is exclusive and one inclusive, \n\r\
	or lower < upper-1 if both are exclusive. "
	
	user_input = ' '
	interval_list = []
	try:
		user_input = raw_input('List of Intervals? ')
		user_intervals_str = user_input.split(', ')
		user_intervals_str = [interval.strip() for interval in user_intervals_str]
		for user_intervals in user_intervals_str:
			try:
				interval_list = add_input(interval_list,user_intervals)
			except MalformedInterval, InvalidInterval:
				#If the interval from the user is not valid, do nothing and continue
				pass
			
		while 1:
			
			try:
				user_input = raw_input('Interval? ')
			except EOFError:
				print '\n'
				continue			

			if user_input == 'help':
				print help_string
				continue
	
			elif user_input == 'quit':
				break
			try:
				interval_list = add_input(interval_list, user_input)
			except MalformedInterval:
				print 'Malformed interval syntax. Type help for more information.'
			except InvalidInterval:
				print 'Invalid interval. Type help for more information'
			else:
				print interval_list
		
	except KeyboardInterrupt:
		#Implementation decision: If KeyboardInterrupt finish the program
		pass
	except:
		print 'Exception raised, finishing program'
