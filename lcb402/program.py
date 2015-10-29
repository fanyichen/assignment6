our_list = input('List of intervals?')

mergeOverlapping(our_list)

for i in (0, 100):
	int_prompt = input('Interval?')
	if int_prompt == 'quit' or 'Quit' or 'QUIT' or 'q':
		break
	else:
		try:
			our_list = insert(our_list, int_promt)
			print our_list
		except:
			print "Interval entered wrong format"

