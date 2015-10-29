import re

#this was my first try

def interactwithuser():
	line = ''
	intevals = []
	while not endGame(line):  # Loop continuously
	    line = raw_input("List of Intervals? ")
	    if line:
	    	responseToUser(line)

def responseToUser(line):
	x = illegalCharactersfound(line)
	y = masterPopulated(line)
	if x == False and y == False:
		return "List of Intervals? "
	elif x == False and y == True:
		return """Invalid Intervals.
		Interval?
		"""
	elif x == True and y == False:
		return """Invalid Intervals.
		List of Intervals?
		"""
	elif x == True and y == True:
		return """Invalid Intervals.
		Interval?
		"""


def masterPopulated(line):
	k = inputParser(line)
	x = len(k)
	masterinterval = []
	if x > 1:
		masterinterval = inputParser(line)
		#print masterinterval
		return True
	if x == 1:
		return insert(masterinterval, line)

def inputParser(line):
    parenthesis = re.findall("\(([^\()]+)\)", line)
    parenthesisListSplit = [i.split(',') for i in parenthesis]
    parenthesisListIntegers = [map(int, i) for i in parenthesisListSplit]
    parenthesisListIntegersIncremented = [[x+1 if x>=0 else x-1 for x in innerlist] for innerlist in parenthesisListIntegers]
    return parenthesisListIntegersIncremented
	# brackets = re.findall("\[([^\][()]+)\]", line)
	# parenToBracket = re.findall("\(([^\][()]+)\]", line)
	# bracketToParen = re.findall("\[([^\][()]+)\)", line)
	
	# intevallist = []
	# parserlist = ['\(([^\][()]+)\)','\(([^\][()]+)\]','\[([^\][()]+)\]','\[([^\][()]+)\)']
	
	# # a = re.findall("\(([^\][()]+)\)|\(([^\][()]+)\]|\[([^\][()]+)\]|\[([^\][()]+)\)", line)
	# b = [x for t in a for x in t]
	# c = filter(None, b)
	# y = str_list = filter(None, x) # fastest

def intervalListempty(x):
	y = len(x)
	if y == 0:
		return True
	else:
		return False

def illegalCharactersfound(line):
	x = re.match('[\200-\377]|[\100-\132]|[\134]|[\136-\137]|[\140-\176]|[\072-\077]|[\055-\057]|[\052-\053]|[\052-\053]|[\041-\047]|\0|\v|\f|\a|\n|\r|\t',line)
	if x != None:
		return True
	else:
		return False

def endGame(line):
	if userWantsToQuit(line):
		return True
	# elif not moreThanOneIntervalLeft(userinput):
	# 	return True
	else:
		return False

def userWantsToQuit(x):
	x = re.match("quit", x)
	if x != None:
		return True
	else:
		return False

if __name__ == "__main__":
	try:
		interactwithuser()
	except EOFError:
		pass

import re

listofintervals = []
def interactwithuser():
	userinput = 'string'
	while not endGame(userinput):  # Loop continuously
	    userPrompt(userinput)
	    if endGame(userinput):       # If it is a blank line...
	        break           # ...break the loop

def userPrompt(userinput):
	x = illegalCharactersfound(userinput)
	y = moreThanOneIntervalLeft(listofintervals)
	initialUserInput = raw_input("List of Intervals? ")
	subsequentUserInput = raw_input("Interval? ")
	if x == True and y == True:
		print "Please provide valid input with no special characters. e.g., (3,4) or [4,-9)"
		return initialUserInput
	elif x == True and y == False:
		print "Please provide valid input with no special characters. e.g., (3,4) or [4,-9)"
		return subsequentUserInput
	elif x == False and y == True:
		return initialUserInput
	elif x == False and y == False:
		return subsequentUserInput

def illegalCharactersfound(userinput):
	x = re.match('[\200-\377]|[\100-\132]|[\134]|[\136-\137]|[\140-\176]|[\072-\077]|[\055-\057]|[\052-\053]|[\052-\053]|[\041-\047]|\0|\v|\f|\a|\n|\r|\t',userinput)
	if x != None:
		return True
	else:
		return False


# def insert(intervals, newint):

# def mergeOverlapping(intervals):

# def mergeIntervals(int1, int2):

# Reasons to Terminate Game

def endGame(userinput):
	if userWantsToQuit(userinput):
		return True
	# elif not moreThanOneIntervalLeft(userinput):
	# 	return True
	else:
		return False

def intervalListempty(x):
	y = len(x)
	if y == 0:
		return True
	else:
		return False

def moreThanOneIntervalLeft(x):
	y = len(x)
	if y > 1:
		return True
	elif y == 1:
		return False

def userWantsToQuit(x):
	x = re.match("quit", x)
	if x != None:
		return True
	else:
		return False

if __name__ == "__main__":
	try:
		interactwithuser()
	except EOFError:
		pass