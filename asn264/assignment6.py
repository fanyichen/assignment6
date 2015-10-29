import sys
from interval import interval
from merge import *
from interact import *

def main():

	#First get a list of valid intervals
	ints = get_list()

	#Merge all overlapping and adjacent intervals
	if is_adjacent(ints) or is_overlapping(ints):
    		ints = mergeOverlapping(ints)

	#Repeat until user types "quit" or keyboard interrupt
	while True:
    		#Parse new interval to add to list
    		new_int = add_to_list()
    		#Insert the new interval into the list
    		ints = insert(ints, new_int[0])
    		#Print the result
        	print ints

#Run the program
if __name__ == "__main__":
	main()




