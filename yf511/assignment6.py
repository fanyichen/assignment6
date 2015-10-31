
import re 
class interval:
	def __init__(self, string):
		lower, upper = map(int, string.strip(' ()[]').split(','))
		if string[0] == '[':
			self.lowerInclusive = True
			self.lower = lower
		else:
			self.lowerInclusive = False
			self.lower = lower + 1
		if string[-1] == ']':
			self.upperInclusive = True
			self.upper = upper
		else:
			self.upperInclusive = False
			self.upper = upper - 1

	def __repr__(self):
		left, right =['(','['], [')',']']
		return left[self.lowerInclusive] + str(self.lower-(1-self.lowerInclusive)) + ',' \
			   + str(self.upper+(1-self.upperInclusive)) + right[self.upperInclusive]

def mergeInterval(i1, i2):
	if i1.lower > i2.upper or i1.upper < i2.lower:
		print 'cannot merge'
	
	if i1.lower < i2.lower:
		lower = i1.lower
		lowerInclusive = i1.lowerInclusive
	else:
		lower = i2.lower
		lowerInclusive = i2.lowerInclusive
	if i1.upper > i2.upper:
		upper = i1.upper
		upperInclusive = i1.upperInclusive
	else:
		upper = i2.upper
		upperInclusive = i2.upperInclusive

	left, right =['(','['], [')',']']
	s = left[lowerInclusive] + str(lower-(1-lowerInclusive)) + ',' \
			   + str(upper+(1-upperInclusive)) + right[upperInclusive]
	return interval(s)



def mergeOverLap(interval_list):
	interval_list.sort(key=lambda x: x.lower)
	output = []
	output.append(interval_list[0])
	for i in range(len(interval_list)-1):
		if interval_list[i].upper < interval_list[i+1].lower:
			output.append(interval_list[i+1])
		else:
			output[-1] = mergeInterval(output[-1], interval_list[i+1])
	return output

def insert(interval_list, newInterval):
        interval_list.append(newInterval)
        return mergeOverLap(interval_list)
        #new_interval_list = interval_list + ','+newInterval
        #return mergeOverLap(new_interval_list)


def main():

	interval_list = []

	while True:
		
		if len(interval_list) == 0:

			initial_list_input = raw_input('List of intervals?')  
		
			if initial_list_input == 'quit':
				break

			interval_string = initial_list_input.replace(' ','')
			input_split = interval_string.split(',')
			for i in range(0, len(input_split), 2):
				

				try:
					intnew = interval(input_split[i] + ',' + input_split[i+1])
					interval_list.append(intnew)

				except:
					print ("Invalid input")
		else:
			interval_input = raw_input('Intervals?')
			if interval_input == 'quit':
				break
			try:
				new_int = interval(interval_input)
			except:
				print("Invalid interval")
			 	continue

			else:
				final_list = insert(interval_list, new_int)  # merge the input interval with the permanent list
				print final_list  # print out the final list

if __name__=='__main__':
    main()

