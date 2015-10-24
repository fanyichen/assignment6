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
            interval.parse_interval("[-11,]")
            interval.parse_interval("{1,1]")
            interval.parse_interval("(-1.0,1]")

    def test_valid_interval_creation_and_representation(self):
        intvl1 = interval.interval("[0, 1]")
        self.assertEqual(str(intvl1), "[0, 1]")
        intvl2 = interval.interval("( -10 , +1)")
        self.assertEqual(intvl2.__str__(), "(-10, 1)")
        intvl3 = interval.interval("  [ -3, 3 )")
        self.assertEqual(intvl3.__str__(), "[-3, 3)")
        intvl4 = interval.interval("[1, 1]")
        self.assertEqual(intvl4.__str__(), "[1, 1]")
        intvl5 = interval.interval("[1, 2)")
        self.assertEqual(intvl5.__str__(), "[1, 2)")

    def test_invalid_intervals_do_not_validate(self):
        with self.assertRaises(interval.InvalidIntervalException):
            intvl1 = interval.interval("(1, 1)")
            intvl2 = interval.interval("(-1, -3)")
            intvl3 = interval.interval("[3, 1]")
            intvl4 = interval.interval("(1, 1]")

    def test_interval_contains(self):
        intvl1 = interval.interval("[1, 3]")
        for n in (1, 2, 3):
            self.assertTrue(intvl1.contains(n))
        self.assertFalse(intvl1.contains(0))
        self.assertFalse(intvl1.contains(4))

        intvl2 = interval.interval("(1, 3)")
        self.assertTrue(intvl2.contains(2))
        self.assertFalse(intvl2.contains(1))
        self.assertFalse(intvl2.contains(3))

        intvl3 = interval.interval("(-3, 1]")
        for n in (-2, -1, 0, 1):
            self.assertTrue(intvl3.contains(n))
        self.assertFalse(intvl3.contains(-3))
        self.assertFalse(intvl3.contains(2))
