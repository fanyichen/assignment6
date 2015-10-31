__author__ = 'bulos87'

import re

__author__ = 'obr214'


class IntervalException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Interval:

    def __init__(self, interval_string):

        if isinstance(interval_string, basestring):
            #Deletes all heading, trailing and whitespaces in the string
            interval_string = interval_string.strip().replace(' ', '')

            interval_pattern ='^(\(|\[)(-?\d+),(-?\d+)(\)|\])$'
            m = re.match(interval_pattern, interval_string)
            if m:
                #Set the values of the bounds
                self.lower_bound = int(m.group(2))
                self.upper_bound = int(m.group(3))

                #Checks the parentesis/square brackets
                if m.group(1) == '[':
                    self.lower_bound_inclusive = True
                    self.lower_starting_number = self.lower_bound
                else:
                    self.lower_bound_inclusive = False
                    self.lower_starting_number = self.lower_bound + 1

                if m.group(4) == ']':
                    self.upper_bound_inclusive = True
                    self.upper_starting_number = self.upper_bound
                else:
                    self.upper_bound_inclusive = False
                    self.upper_starting_number = self.upper_bound - 1

                if self.lower_starting_number > self.upper_starting_number:
                    raise IntervalException("Lower Bound bigger than Upper Bound")
            else:
                raise IntervalException("Interval String with wrong format")

        else:  # The object is not a string. Return that the interval cannot be constructed.
            raise ValueError("The interval parameter is not a string")

    def __repr__(self):

        interval_string = ''
        if self.lower_bound_inclusive:
            interval_string += '['
        else:
            interval_string += '('

        interval_string += str(self.lower_bound) + ',' + str(self.upper_bound)

        if self.upper_bound_inclusive:
            interval_string += ']'
        else:
            interval_string += ')'

        return interval_string

    @staticmethod
    def sort_two_intervals(interval1, interval2):
        if interval1.lower_starting_number < interval2.lower_starting_number:
            return interval1, interval2
        elif interval1.lower_starting_number > interval2.lower_starting_number:
            return interval2, interval1
        else:
            if interval1.upper_starting_number > interval2.upper_starting_number:
                return interval1, interval2
            elif interval1.upper_starting_number < interval2.upper_starting_number:
                return interval2, interval1
            else:
                return interval1, interval2

    @staticmethod
    def sort_intervals(list_intervals):
        """
        Sort a list of intervals:
        Implementation of a bubble sort.

        Args:
            list_intervals: A list containing Interval objects

        Returns:
            A sorted list of Interval objects.
        """
        for max_limit in range(len(list_intervals)-1, 0, -1):
            for i in range(max_limit):
                interval_1st, interval_2nd = Interval.sort_two_intervals(list_intervals[i], list_intervals[i+1])
                list_intervals[i] = interval_1st
                list_intervals[i+1] = interval_2nd

        return list_intervals

    @staticmethod
    def merge_intervals(interval_1, interval_2):
        """
        Merges two intervals:
        The function merge two intervals if these are adjancent or overlaping.
        Otherwise, it throws an exception.

        Args:
            interval_1 and interval_2: Objects of the class Interval

        Returns:
            The resulting Interval object

        Raises:
            IntervalException: In case the parameters are not Interval objects. In case the merge cannot be done.
        """

        interval_1, interval_2 = Interval.sort_two_intervals(interval_1, interval_2)

        if isinstance(interval_1, Interval) and isinstance(interval_2, Interval):
            if interval_1.lower_starting_number <= interval_2.lower_starting_number \
                    and interval_1.upper_starting_number >= interval_2.upper_starting_number:
                return interval_1

            elif interval_1.upper_starting_number >= interval_2.lower_starting_number \
                    or interval_2.lower_starting_number == interval_1.upper_starting_number+1:

                #Creates the new interval string
                new_interval_string = ''

                if interval_1.lower_bound_inclusive:
                    new_interval_string += '['
                else:
                    new_interval_string += '('

                new_interval_string += str(interval_1.lower_bound) + ',' + str(interval_2.upper_bound)

                if interval_2.upper_bound_inclusive:
                    new_interval_string += ']'
                else:
                    new_interval_string += ')'

                new_interval = Interval(new_interval_string)
                return new_interval

            else:
                raise IntervalException("Merge Failed")
        else:
            raise IntervalException("The parameter given are not instances of the class Interval")

    @staticmethod
    def merge_overlapping(list_intervals):
        """
        Merges overlapping intervals:
        The function takes a list of intervals and merges all overlapping intervals.
        Example: Given the interval list [1,5], [2,6), (8,10], [8,18], the function would return [1,6), [8,18].

        Args:
            list_intervals: A list of Interval objects

        Returns:
            A list with the overlapping intervals merged.
        """

        final_intervals = []

        while len(list_intervals) > 1:

            try:
                merged_interval = Interval.merge_intervals(list_intervals[0], list_intervals[1])
                list_intervals.pop(0)
                list_intervals.pop(0)
                list_intervals.insert(0, merged_interval)
            except IntervalException:
                final_intervals.append(list_intervals.pop(0))

        final_intervals.append(list_intervals.pop())

        return final_intervals

    @staticmethod
    def insert(list_intervals, new_interval):
        """
        Inserts a new interval into a list of intervals:
        The function takes a new interval and inserts it at the end of the list. Then a sort function is
        called to have all the intervals in the right place.
        The merge_overlapping function is called to compress the intervals if required.

        Args:
            list_intervals: A list of Interval objects
            new_interval: An instance of Interval that will be inserted in list_intervals

        Returns:
            A list of Interval objects.
        """

        list_intervals.append(new_interval)
        ordered_list = Interval.sort_intervals(list_intervals)

        return Interval.merge_overlapping(ordered_list)
