
class interval(object):

    def __init__(self, string):
        # record the 4 four elements of an interval
        self.left = string[0]
        self.right = string[-1]
        self.lowerbound = int(string.rpartition(",")[0][1])
        self.upperbound = int(string.rpartition(",")[2][:-1])

        # report error information for invalid input
        if self.left != "(" and self.left != "[":
            raise ValueError("Input must start with parentheses or brackets")
        if self.right != ")" and self.right != "]":
            raise ValueError("Input must end with parentheses or brackets")

        # report the true interval
        self.TrueLowerbound = self.lowerbound
        self.TrueUpperbound = self.upperbound
        if self.left == "(":
            self.TrueLowerbound = self.lowerbound + 1
            self.left = "["
        if self.right == ")":
            self.TrueUpperbound = self.upperbound - 1
            self.right = "]"

        # report error information for invalid input
        if self.lowerbound >= self.upperbound:
            raise ValueError("Lower bound is greater or equal than upper bound")

    def __repr__(self):
        return (self.left + str(self.TrueLowerbound) + ","  + str(self.TrueUpperbound) + self.right)


def mergeIntervals(int1, int2):
    # Sort intervals by lower bound
    SortedIntervals = sorted([int1, int2], key=lambda x:x.TrueLowerbound)
    if SortedIntervals[0].TrueUpperbound >= SortedIntervals[1].TrueLowerbound:
        return interval("[" + str(SortedIntervals[0].TrueLowerbound) + "," + str(SortedIntervals[1].TrueUpperbound) + "]")
    else:
        raise ValueError("Intervals do not overlap")

def mergeOverlapping(intervals):
    # Sort intervals by lower bound
    SortedIntervals = sorted(intervals, key=lambda x:x.TrueLowerbound)
    MergedIntervals = []  # start with empty interval

    for x in SortedIntervals:
        if not MergedIntervals:
            MergedIntervals.append(x)
        else:
            if x.TrueLowerbound <= MergedIntervals[-1].TrueUpperbound:
                MergedIntervals[-1].TrueUpperbound = max(x.TrueUpperbound,MergedIntervals[-1].TrueUpperbound)
            else:
                MergedIntervals.append(x)
    return MergedIntervals

def insert(intervals, newint):
    intervals.append(newint)
    return mergeOverlapping(intervals)


