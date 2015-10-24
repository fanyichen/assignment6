import unittest
import interval

class IntervalTestCase(unittest.TestCase):

    def test_parse_interval_0_1_True_True(self):
        self.assertEqual(interval.parse_interval("[0,1]"), (0,1,True,True))

    def test_create_interval_0_1_True_True(self):
        intvl = interval.interval("[0,1]")
        self.assertEqual(intvl.bounds, (0, 1))
        self.assertEqual(intvl.inclusive, (True, True))
