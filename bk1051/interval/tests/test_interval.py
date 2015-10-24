import unittest
import interval

class IntervalTestCase(unittest.TestCase):

    def test_create_interval_0_1_True_True(self):
        intvl = interval.interval("[0,1]")
        self.assertEqual(intvl.bounds, (0, 1))
        self.assertEqual(intvl.)
