import sys
import interval
import dealWithInterval
import userExceptions
from interval import interval
from userExceptions import interval_bad_leftbound, interval_bad_rightbound, interval_bad_invalidbound, interval_bad_zero, interval_bad_nocomma, merge_bad

intervalList = []
print 'press the return button to stop enter new interval and go to next step.'
print 'list of intervals'

try:
	while True:		
		intervalInput = raw_input()			
		if intervalInput == '':
			break
		try: 
			interval(intervalInput)
			intervalList.append(intervalInput)
		except (interval_bad_leftbound, interval_bad_rightbound, interval_bad_invalidbound, interval_bad_zero, interval_bad_nocomma):
			print 'invalid interval'
	print intervalList	
	
	while True:
		intervalInsert = raw_input('interval?')
		if str.lower(intervalInsert) == 'quit' or str.lower(intervalInsert) == 'q':
			sys.exit()
		try:
			interval(intervalInsert)
		except (interval_bad_leftbound, interval_bad_rightbound, interval_bad_invalidbound, interval_bad_zero, interval_bad_nocomma):
			print 'invalid interval'
		else:
			intervalList = dealWithInterval.insert(intervalList, intervalInsert)
			print intervalList
except (KeyboardInterrupt, EOFError):
	print 'terminate abnormally'

