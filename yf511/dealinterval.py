import re
import main6

"""Creat an interval class to Interpret the interval and form into correct representation. Raise Error when the string is incorrect."""
class dealinterval(object):
    def __init__(self, string):
        #get rid of "([and ])" in the interval and split string by comma
        self.string = string
        if len(self.string.strip("([])").split(",")) !=2:
            raise ValueError('Invalid Interval Input')
        try:
            lower = int(self.string.strip('()[]').split(',')[0])
            upper = int(self.string.strip('()[]').split(',')[1])

        except:
            raise ValueError('Invalid Intervals. Please print in correct format. i.e. [1,4],(2,5]')

         #Interpret parenthesis i.e. () and squre brackets i.e. [] for exclusive and inclusive bounds respectively
        if string[0] == '[':
            self.lowerInclusive = True
            self.lower = lower
        if string[0] == '(':
            self.lowerInclusive = False
            self.lower = lower
        if string[-1] == ']':
            self.upperInclusive = True
            self.upper = upper
        if string[-1] == ')':
            self.upperInclusive = False
            self.upper = upper
        if self.lower > self.upper:
            raise ValueError('Invalid Intervals! Incorrect: Lower and upper bound')
        if string [0] == '(' and string [-1] == ')':
            if lower +1 < upper:
                pass
            else :
                raise ValueError('Invalid Intervals! Incorrect: Lower and upper bound')

        """print out the result in correct form"""
    def __repr__(self):
        left, right =['(','['], [')',']']
        return left[self.lowerInclusive] + str(self.lower) + ',' + str(self.upper) + right[self.upperInclusive]

def mergeInterval(i1, i2):
    """merge two intervals by interval class to understand the real interval and judge whether two can merge,
     if it possible, returns a merged interval or raise ValueError when two intervals cant be merged
    """
    # i1 = dealinterval(i1)
    # i2 = dealinterval(i2)
    if (i1.lower - 1 > i2.upper) or (i1.upper < i2.lower -1):
        raise ValueError('Disjoint intervals')

    if i1.lower < i2.lower:
        lower = i1.lower
        lowerInclusive = i1.lowerInclusive
    elif i1.lower > i2.lower:
        lower = i2.lower
        lowerInclusive = i2.lowerInclusive
    else:
        if i1.lowerInclusive == i2.lowerInclusive:
            lower = i2.lower
            lowerInclusive = i2.lowerInclusive
        if i1.lowerInclusive != i2.lowerInclusive:
            lower = i2.lower
            lowerInclusive = True
    if i1.upper > i2.upper:
        upper = i1.upper
        upperInclusive = i1.upperInclusive
    elif i1.upper < i2.upper:
        upper = i2.upper
        upperInclusive = i2.upperInclusive
    else:
        if i1.upperInclusive == i2.upperInclusive:
            upper = i2.upper
            upperInclusive = i2.upperInclusive
        if i1.upperInclusive != i2.upperInclusive:
            upper = i2.upper
            upperInclusive = True
        

    left, right =['(','['], [')',']']
    s = left[lowerInclusive] + str(lower) + ',' + str(upper) + right[upperInclusive]
    # print dealinterval(s)
    return dealinterval(s)



def mergeOverLap(interval_list):
    """sort the interval"""
    interval_list.sort(key=lambda x: x.lower)
    output = []
    output.append(interval_list[0])

    for i in range(len(interval_list)-1):
        if interval_list[i].upper < interval_list[i+1].lower:
            if interval_list[i].upper +1 == interval_list[i+1].lower:
                if interval_list[i].upperInclusive == True and interval_list[i+1].lowerInclusive == True:
                    output[-1].upper += 1
                else:
                    output.append(interval_list[i+1])
            else:
                output.append(interval_list[i+1])

        else:
            output[-1] = mergeInterval(output[-1], interval_list[i+1])
    return output

def insert(interval_list, newInterval):
    """insert a interval to interval list and do the merge function by using mergeoverlap"""
    interval_list.append(newInterval)
    return mergeOverLap(interval_list)
      # '''inserts single interval (newint) into a list of non-overlapping intervals (intlist), and 
#     merges the overlapping intervals. Returns a single merged interval or a list of merged intervals
#     """

if __name__ == '__main__':
    main6.main()

#     