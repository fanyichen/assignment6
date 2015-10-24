import unittest
import interval

class IntervalTestCase(unittest.TestCase):

    def test_parse_interval_0_1_True_True(self):
        self.assertEqual(interval.parse_interval("[0,1]"), (0,1,True,True))

    def test_parse_interval_neg10_neg1_False_True(self):
        self.assertEqual(interval.parse_interval("( -10, -1 ]"), (-10,-1,False,True))

    def test_parse_interval_10_neg1_False_False(self):
        self.assertEqual(interval.parse_interval("(10, -1)"), (10,-1,False,False))

    def test_parse_well_formed_intervals(self):
        self.assertEqual(interval.parse_interval("[0, 1]"), (0,1,True,True))
        self.assertEqual(interval.parse_interval("[ 10, 1)"), (10,1,True,False))
        self.assertEqual(interval.parse_interval("[-70,+1]"), (-70,1,True,True))

    def test_parse_malformed_intervals_raise_exceptions(self):
        with self.assertRaises(interval.IntervalParseException):
            interval.parse_interval("-1 1")
            interval.parse_interval("[-1 1,1]")
            interval.parse_interval("{1,1]")
            interval.parse_interval("(-1.0,1]")

    def test_create_interval_0_1_True_True(self):
        intvl = interval.interval("[0,1]")
        self.assertEqual(intvl.bounds, (0, 1))
        self.assertEqual(intvl.inclusive, (True, True))
