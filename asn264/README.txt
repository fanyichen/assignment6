NetID: asn264

This is my submission for Assignment 6. 



TO RUN PROGRAM:
To run the package from the command line, type:

	$ python assignment6.py

This will prompt you for a list of intervals separated by commas. 
The following is an example of valid input:

	[1,2), [6,10], [23,50)

Note, distinct intervals *MUST* be separated by commas. As a rule,
correctly-formatted, non-empty intervals followed by commas will be accepted
by the program. 
 
Moreover, the program will only accept non-empty intervals. 
The following are some examples of illegal empty intervals:

	[5,1], (1,1), [2,2), (3,1]

To quit the program, type "quit" or use a keyboard interrupt. 



NOTES ON TESTING:
Tests are provided in test_interval.py, test_interact.py, and test_merge.py. I have attempted to be comprehensive and the tests reflect issues or cases that I focused on during development. 

To run the tests provided in test_interval.py from the command line, type:

	$ python -m unittest -v test_interval

Other tests are run similarly. 



NOTES ON PACKAGE STRUCTURE:
	- interval.py contains the interval class.
	- merge.py is a module containing helper functions which enable interval merging.
	It contains the following required functions: mergeIntervals, mergeOverlapping, and insert.
	- interact.py is a module containing helper functions which are responsible for interacting with and interpreting user input. 
	- assignment6.py contains a main function which encapsulates the full
  	functionality of the program.




