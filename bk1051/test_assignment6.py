import unittest
from assignment6 import *
import mock

'''
Testing with input uses info provided by:
http://stackoverflow.com/questions/2617057/supply-inputs-to-python-unit-tests
'''

class Assignment6TestCase(unittest.TestCase):
    def test_quit(self):
        with self.assertRaises(SystemExit):
            parse_interval_input("quit")
        with self.assertRaises(SystemExit):
            parse_interval_input("please QUIT!!!")
        with self.assertRaises(SystemExit):
            parse_interval_list_input("please QUIT!!!")

    def test_invalid_interval_input(self):
        self.assertEqual(parse_interval_input("1111"), "Invalid interval")
        self.assertEqual(parse_interval_input("11,11"), "Invalid interval")
        self.assertEqual(parse_interval_input("[11,11)"), "Invalid interval")
        self.assertEqual(parse_interval_input("[4,-1]"), "Invalid interval")
        self.assertEqual(parse_interval_input("(3,4)"), "Invalid interval")
        self.assertEqual(parse_interval_input("foo"), "Invalid interval")
        self.assertEqual(parse_interval_input("[11,12,21)"), "Invalid interval")

    def test_invalid_interval_list_input(self):
        self.assertEqual(parse_interval_input("[-10,-7] (-4,1] [3,6) (8,12) [15,23]"),
                        "Invalid interval list. Must be valid intervals, separated by commas")
        self.assertEqual(parse_interval_input("[-10,-7], (-4,1], [13,6), (8,12), [15,23]"),
                        "Invalid interval list. Must be valid intervals, separated by commas")

    def test_parse_interval_list(self):
        self.assertEqual(
            intervals_to_strings(
                parse_interval_list_input("[-10,-7], (-4,1], [3,6), (8,12), [15,23]")
            ),
            ["[-10,-7]", "(-4,1]", "[3,6)", "(8,12)", "[15,23]"]
        )

    def test_insert_interval_from_input(self):
        interval_list = parse_interval_list_input("[-10,-7], (-4,1], [3,6), (8,12), [15,23]")
        newint = parse_interval_input("[4,8]")
        interval_list = insert(interval_list, newint)
        self.assertEqual(interval_list_to_string(interval_list),
            "[-10,7], (-4,1], [3,12), [15,23]")

        newint = parse_interval_input("[24,24]")
        interval_list = insert(interval_list, newint)
        self.assertEqual(interval_list_to_string(interval_list),
            "[-10,7], (-4,1], [3,12), [15,24]")

        newint = parse_interval_input("[12,13)")
        interval_list = insert(interval_list, newint)
        self.assertEqual(interval_list_to_string(interval_list),
            "[-10,7], (-4,1], [3,13), [15,24]")

        newint = parse_interval_input("(2,12)")
        interval_list = insert(interval_list, newint)
        self.assertEqual(interval_list_to_string(interval_list),
            "[-10,7], (-4,1], [3,13), [15,24]")

        newint = parse_interval_input("(-7,-2]")
        interval_list = insert(interval_list, newint)
        self.assertEqual(interval_list_to_string(interval_list),
            "[-10,1], [3,13), [15,24]")

        newint = parse_interval_input("[-2,5]")
        interval_list = insert(interval_list, newint)
        self.assertEqual(interval_list_to_string(interval_list),
            "[-10,13), [15,24]")
