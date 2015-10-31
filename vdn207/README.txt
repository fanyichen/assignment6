This is a README file which gives information about the program.

This program has 4 files:
	1) assignment6.py - Contains the main function and run the software. This has to be executed to use the software.
	2) interval.py - Definition of the class 'interval'
	3) custom_exceptions.py - Contains the exceptions defined for specific use cases of the software
	4) interval_operations.py - Contains the functions that work with intervals

There is folder called 'tests' which has the test file for testing the 3 functions operating on the interval objects.

The test file can be run from the parent directory of the software using the command below:
	python -m unittest discover -v tests

The output of the test cases I got:
	test_correctness_of_mergeIntervals (test_interval_operations.IntervalOperationTests) ... ok
	test_exception_when_intervals_cannot_be_merged (test_interval_operations.IntervalOperationTests) ... ok
	test_insert (test_interval_operations.IntervalOperationTests) ... ok
	test_mergeOverlapping (test_interval_operations.IntervalOperationTests) ... ok

	----------------------------------------------------------------------
	Ran 4 tests in 0.001s

	OK
