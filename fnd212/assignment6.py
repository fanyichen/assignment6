from intervals import *

def add_input(interval_list,user_input):
	user_interval = intervalInt(user_input)
	interval_list_tmp = interval_list
	if len(interval_list_tmp) != 0:
		interval_list_tmp = insert(interval_list_tmp,user_interval)
	else:
		interval_list_tmp.append(user_interval)
	return interval_list_tmp


if __name__ == '__main__':

	user_input = ' '
	interval_list = []

	while 1:
		user_input = raw_input('Interval? ')
		if user_input == 'help':
			print '''Interval should be a of the form '[a,b]', '(a,b]', '[a,b)'
					or '(a,b)' where a and be must be integer numbers 
					The bounds must always meet the requirement
					that lower <= upper if both bounds are inclusive,
					lower < upper if one bound is exclusive and one inclusive,
					or lower < upper-1 if both are exclusive. '''
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



		



		

